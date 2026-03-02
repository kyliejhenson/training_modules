#!/usr/bin/env python3
"""
Insert images and video hyperlinks into an unpacked PowerPoint presentation.

Takes a JSON manifest mapping slide filenames to image and video operations,
then performs the corresponding XML-level changes.

Usage:
    python insert_media.py <unpacked_dir> <manifest.json>

Manifest format:
{
    "slide6.xml": {
        "images": [
            {
                "src": "/path/to/screenshot.png",
                "position": "full-bleed",
                "caption": "Optional caption text",
                "source": "Optional source text"
            }
        ]
    },
    "slide9.xml": {
        "images": [
            {
                "src": "/path/to/icon.png",
                "position": "content",
                "x": 640080,
                "y": 274320,
                "cx": 4572000,
                "cy": 2571750
            }
        ]
    },
    "slide8.xml": {
        "videos": [
            {
                "url": "https://www.youtube.com/watch?v=example",
                "target_shapes": ["VideoArea", "URLPlaceholder"]
            }
        ]
    }
}

Image position types:
  - "full-bleed": Image fills the entire slide (9144000 x 5143500 EMU = 10" x 5.625")
  - "content": Image placed at specific coordinates (provide x, y, cx, cy in EMU)
  - "replace": Replace an existing placeholder image by matching rId

Video entries:
  - "url": The hyperlink URL to embed
  - "target_shapes": List of shape names to make clickable

EMU reference: 914400 EMU = 1 inch
Full slide: 9144000 x 5143500 EMU (10" x 5.625" for 16:9)
"""

import json
import os
import re
import shutil
import sys
from pathlib import Path

try:
    from defusedxml.minidom import parseString
except ImportError:
    from xml.dom.minidom import parseString


# Slide dimensions in EMU (16:9 aspect ratio)
SLIDE_WIDTH = 9144000   # 10 inches
SLIDE_HEIGHT = 5143500  # 5.625 inches


def get_next_rid(rels_content):
    """Find the next available rId number in a .rels file."""
    ids = re.findall(r'Id="rId(\d+)"', rels_content)
    if not ids:
        return 1
    return max(int(i) for i in ids) + 1


def get_max_element_id(slide_content):
    """Find the highest id attribute in slide XML to avoid collisions."""
    ids = re.findall(r'<p:cNvPr\s+id="(\d+)"', slide_content)
    if not ids:
        return 1
    return max(int(i) for i in ids)


def add_image_relationship(rels_path, rid, media_filename):
    """Add an image relationship entry to a slide's .rels file."""
    with open(rels_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_rel = (
        f'  <Relationship Id="rId{rid}" '
        f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
        f'Target="../media/{media_filename}"/>'
    )

    content = content.replace(
        '</Relationships>',
        f'{new_rel}\n</Relationships>'
    )

    with open(rels_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return rid


def add_hyperlink_relationship(rels_path, rid, url):
    """Add a hyperlink relationship entry to a slide's .rels file."""
    with open(rels_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_rel = (
        f'  <Relationship Id="rId{rid}" '
        f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
        f'Target="{url}" TargetMode="External"/>'
    )

    content = content.replace(
        '</Relationships>',
        f'{new_rel}\n</Relationships>'
    )

    with open(rels_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return rid


def build_pic_element(rid, element_id, x, y, cx, cy, image_name, descr=""):
    """Build a <p:pic> XML element string."""
    if not descr:
        descr = image_name

    return (
        f'<p:pic>\n'
        f'  <p:nvPicPr>\n'
        f'    <p:cNvPr id="{element_id}" name="{image_name}" descr="{descr}"/>\n'
        f'    <p:cNvPicPr>\n'
        f'      <a:picLocks noChangeAspect="1"/>\n'
        f'    </p:cNvPicPr>\n'
        f'    <p:nvPr/>\n'
        f'  </p:nvPicPr>\n'
        f'  <p:blipFill>\n'
        f'    <a:blip r:embed="rId{rid}"/>\n'
        f'    <a:stretch>\n'
        f'      <a:fillRect/>\n'
        f'    </a:stretch>\n'
        f'  </p:blipFill>\n'
        f'  <p:spPr>\n'
        f'    <a:xfrm>\n'
        f'      <a:off x="{x}" y="{y}"/>\n'
        f'      <a:ext cx="{cx}" cy="{cy}"/>\n'
        f'    </a:xfrm>\n'
        f'    <a:prstGeom prst="rect">\n'
        f'      <a:avLst/>\n'
        f'    </a:prstGeom>\n'
        f'  </p:spPr>\n'
        f'</p:pic>'
    )


def replace_placeholder_image(slide_path, rels_path, unpacked_dir, image_entry, slide_name):
    """Replace an existing placeholder image with a new one.

    Finds existing p:pic elements in the slide, identifies which media file
    they reference, and swaps the media file on disk.
    """
    with open(slide_path, 'r', encoding='utf-8') as f:
        slide_content = f.read()
    with open(rels_path, 'r', encoding='utf-8') as f:
        rels_content = f.read()

    src = image_entry['src']
    target_index = image_entry.get('replace_index', 0)

    # Find all image relationship IDs in the slide
    blip_rids = re.findall(r'r:embed="(rId\d+)"', slide_content)

    # Find which ones point to images in the rels file
    image_rids = []
    for rid in blip_rids:
        pattern = rf'Id="{rid}"[^>]*Type="[^"]*relationships/image"[^>]*Target="([^"]*)"'
        match = re.search(pattern, rels_content)
        if match:
            image_rids.append((rid, match.group(1)))

    if target_index >= len(image_rids):
        print(f"  WARNING: replace_index {target_index} out of range for {slide_name} (has {len(image_rids)} images)")
        return False

    rid, old_target = image_rids[target_index]
    old_media_path = os.path.normpath(os.path.join(unpacked_dir, 'ppt', 'media', os.path.basename(old_target)))

    # Copy new image over the old one
    shutil.copy2(src, old_media_path)
    print(f"  Replaced {os.path.basename(old_target)} with {os.path.basename(src)}")
    return True


def insert_image_into_slide(slide_path, rels_path, unpacked_dir, image_entry, slide_name):
    """Insert a new image into a slide.

    Handles full-bleed and content positioning.
    Returns True on success.
    """
    position = image_entry.get('position', 'content')
    src = image_entry['src']

    if not os.path.exists(src):
        print(f"  ERROR: Image not found: {src}")
        return False

    # Determine media filename
    slide_num = re.search(r'slide(\d+)', slide_name)
    slide_num = slide_num.group(1) if slide_num else '0'

    with open(rels_path, 'r', encoding='utf-8') as f:
        rels_content = f.read()
    with open(slide_path, 'r', encoding='utf-8') as f:
        slide_content = f.read()

    # Count existing images for this slide to make unique filename
    existing_images = len(re.findall(rf'image-{slide_num}-\d+', rels_content))
    img_index = existing_images + 1

    # Determine file extension
    ext = os.path.splitext(src)[1].lower()
    if ext not in ('.png', '.jpg', '.jpeg', '.gif', '.svg'):
        ext = '.png'

    media_filename = f"image-{slide_num}-{img_index}{ext}"
    media_dest = os.path.join(unpacked_dir, 'ppt', 'media', media_filename)

    # Copy image to media directory
    os.makedirs(os.path.dirname(media_dest), exist_ok=True)
    shutil.copy2(src, media_dest)
    print(f"  Copied {os.path.basename(src)} -> ppt/media/{media_filename}")

    # Add relationship
    rid = get_next_rid(rels_content)
    add_image_relationship(rels_path, rid, media_filename)
    print(f"  Added relationship rId{rid} -> {media_filename}")

    # Determine position
    if position == 'full-bleed':
        x, y, cx, cy = 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT
    else:
        x = image_entry.get('x', 640080)
        y = image_entry.get('y', 274320)
        cx = image_entry.get('cx', 4572000)
        cy = image_entry.get('cy', 2571750)

    # Build pic element
    max_id = get_max_element_id(slide_content)
    element_id = max_id + 1
    image_name = f"Image {img_index}"

    pic_xml = build_pic_element(rid, element_id, x, y, cx, cy, image_name,
                                 descr=os.path.basename(src))

    # Insert pic element into the slide's shape tree
    # For full-bleed: insert as FIRST child of spTree (behind other elements)
    # For content: insert as LAST child of spTree (in front)
    if position == 'full-bleed':
        grp_sp_pr_end = slide_content.find('</p:grpSpPr>')
        if grp_sp_pr_end != -1:
            insert_pos = grp_sp_pr_end + len('</p:grpSpPr>')
            slide_content = (
                slide_content[:insert_pos] +
                '\n' + pic_xml + '\n' +
                slide_content[insert_pos:]
            )
        else:
            print(f"  WARNING: Could not find </p:grpSpPr> in {slide_name}")
            return False
    else:
        slide_content = slide_content.replace(
            '</p:spTree>',
            pic_xml + '\n</p:spTree>'
        )

    with open(slide_path, 'w', encoding='utf-8') as f:
        f.write(slide_content)

    print(f"  Inserted {image_name} at ({x}, {y}) size ({cx}, {cy})")
    return True


def add_hyperlink_to_shape(slide_path, rels_path, video_entry, slide_name):
    """Add a clickable hyperlink to named shapes in a slide.

    Finds shapes by name, adds a hyperlink relationship to the .rels file,
    and inserts an <a:hlinkClick> element into the shape's <p:cNvPr>.

    Returns the number of shapes successfully linked.
    """
    url = video_entry.get('url', '')
    target_shapes = video_entry.get('target_shapes', [])

    if not url:
        print(f"  ERROR: No URL provided for video entry in {slide_name}")
        return 0

    if not target_shapes:
        print(f"  WARNING: No target shapes specified for video in {slide_name}")
        return 0

    with open(rels_path, 'r', encoding='utf-8') as f:
        rels_content = f.read()
    with open(slide_path, 'r', encoding='utf-8') as f:
        slide_content = f.read()

    # Add one hyperlink relationship for this URL
    rid = get_next_rid(rels_content)
    add_hyperlink_relationship(rels_path, rid, url)
    print(f"  Added hyperlink relationship rId{rid} -> {url}")

    # Re-read rels since we just modified it
    # (in case we need get_next_rid again, though for video we share one rId)

    linked_count = 0
    for shape_name in target_shapes:
        # Find the shape's <p:cNvPr> by name attribute
        # Pattern: <p:cNvPr id="N" name="ShapeName"/>
        # We need to add <a:hlinkClick r:id="rIdN"/> inside it
        #
        # The cNvPr can be self-closing: <p:cNvPr id="4" name="VideoArea"/>
        # Or it can have children: <p:cNvPr id="4" name="VideoArea">...</p:cNvPr>

        # Match self-closing cNvPr with this shape name
        self_closing_pattern = rf'(<p:cNvPr\s+id="\d+"\s+name="{re.escape(shape_name)}")\s*/>'
        match = re.search(self_closing_pattern, slide_content)

        if match:
            # Convert self-closing to open/close with hlinkClick inside
            old = match.group(0)
            new = f'{match.group(1)}>\n      <a:hlinkClick r:id="rId{rid}"/>\n    </p:cNvPr>'
            slide_content = slide_content.replace(old, new, 1)
            print(f"  Linked shape '{shape_name}' to {url}")
            linked_count += 1
            continue

        # Match open tag cNvPr with this shape name (already has children)
        open_pattern = rf'(<p:cNvPr\s+id="\d+"\s+name="{re.escape(shape_name)}")>'
        match = re.search(open_pattern, slide_content)

        if match:
            # Check if it already has an hlinkClick
            # Find the closing </p:cNvPr> after this match
            start = match.end()
            close_idx = slide_content.find('</p:cNvPr>', start)
            if close_idx != -1:
                between = slide_content[start:close_idx]
                if 'hlinkClick' in between:
                    print(f"  Shape '{shape_name}' already has a hyperlink, skipping")
                    linked_count += 1
                    continue

            # Insert hlinkClick right after the opening tag
            old = match.group(0) + '>'
            new = old + f'\n      <a:hlinkClick r:id="rId{rid}"/>'
            slide_content = slide_content.replace(old, new, 1)
            print(f"  Linked shape '{shape_name}' to {url}")
            linked_count += 1
            continue

        print(f"  WARNING: Shape '{shape_name}' not found in {slide_name}")

    with open(slide_path, 'w', encoding='utf-8') as f:
        f.write(slide_content)

    return linked_count


def ensure_content_type(unpacked_dir, extension):
    """Ensure the Content_Types.xml has an entry for the given extension."""
    ct_path = os.path.join(unpacked_dir, '[Content_Types].xml')
    if not os.path.exists(ct_path):
        return

    with open(ct_path, 'r', encoding='utf-8') as f:
        content = f.read()

    ext = extension.lstrip('.')
    content_type_map = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'svg': 'image/svg+xml',
    }

    if ext in content_type_map and f'Extension="{ext}"' not in content:
        new_entry = f'  <Default Extension="{ext}" ContentType="{content_type_map[ext]}"/>'
        content = content.replace(
            '</Types>',
            f'{new_entry}\n</Types>'
        )
        with open(ct_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Added Content_Type for .{ext}")


def process_manifest(unpacked_dir, manifest):
    """Process the entire media manifest (images and videos)."""
    slides_dir = os.path.join(unpacked_dir, 'ppt', 'slides')
    rels_dir = os.path.join(slides_dir, '_rels')

    image_success = 0
    video_success = 0
    error_count = 0

    # Track which extensions we need
    extensions_used = set()

    for slide_name, slide_data in manifest.items():
        slide_path = os.path.join(slides_dir, slide_name)
        rels_path = os.path.join(rels_dir, f'{slide_name}.rels')

        if not os.path.exists(slide_path):
            print(f"SKIP: {slide_name} not found in unpacked directory")
            error_count += 1
            continue

        if not os.path.exists(rels_path):
            print(f"SKIP: {slide_name}.rels not found")
            error_count += 1
            continue

        has_images = 'images' in slide_data and slide_data['images']
        has_videos = 'videos' in slide_data and slide_data['videos']

        if has_images or has_videos:
            print(f"\nProcessing {slide_name}:")

        # Process images
        for image_entry in slide_data.get('images', []):
            src = image_entry.get('src', '')
            ext = os.path.splitext(src)[1].lower().lstrip('.')
            if ext:
                extensions_used.add(ext)

            position = image_entry.get('position', 'content')

            if position == 'replace':
                ok = replace_placeholder_image(slide_path, rels_path, unpacked_dir, image_entry, slide_name)
            else:
                ok = insert_image_into_slide(slide_path, rels_path, unpacked_dir, image_entry, slide_name)

            if ok:
                image_success += 1
            else:
                error_count += 1

        # Process videos
        for video_entry in slide_data.get('videos', []):
            linked = add_hyperlink_to_shape(slide_path, rels_path, video_entry, slide_name)
            if linked > 0:
                video_success += linked
            else:
                error_count += 1

    # Ensure content types are registered
    for ext in extensions_used:
        ensure_content_type(unpacked_dir, ext)

    print(f"\n{'='*50}")
    print(f"Done: {image_success} images inserted, {video_success} video links added, {error_count} errors")
    return error_count == 0


def main():
    if len(sys.argv) < 3:
        print("Usage: python insert_media.py <unpacked_dir> <manifest.json>")
        sys.exit(1)

    unpacked_dir = sys.argv[1]
    manifest_path = sys.argv[2]

    if not os.path.isdir(unpacked_dir):
        print(f"Error: {unpacked_dir} is not a directory")
        sys.exit(1)

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    success = process_manifest(unpacked_dir, manifest)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
