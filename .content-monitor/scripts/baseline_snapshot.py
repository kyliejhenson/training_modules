#!/usr/bin/env python3
"""
baseline_snapshot.py — Generate or update the baseline snapshot.

Fetches each source page from source-registry.json, extracts structured
data (headings, key content markers, feature tables, navigation cards),
and writes a new baseline-snapshot.json.

Usage:
    python baseline_snapshot.py                     # update all pages
    python baseline_snapshot.py --pages cc_skills cc_mcp  # update specific pages only
    python baseline_snapshot.py --priority critical  # only critical-priority pages
    python baseline_snapshot.py --priority normal    # critical + normal pages
    python baseline_snapshot.py --dry-run           # print what would be fetched, don't write

Requires: requests, beautifulsoup4
    pip install requests beautifulsoup4 --break-system-packages
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install requests beautifulsoup4 --break-system-packages")
    sys.exit(1)

MONITOR_DIR = Path(__file__).resolve().parent.parent
REGISTRY_PATH = MONITOR_DIR / "source-registry.json"
SNAPSHOT_PATH = MONITOR_DIR / "baseline-snapshot.json"

# ─── Section hashing ─────────────────────────────────────────────────

def normalize_text(text: str) -> str:
    """Collapse whitespace so minor formatting changes don't trigger false diffs."""
    return " ".join(text.split()).strip()


def extract_section_hashes(soup: BeautifulSoup) -> dict[str, str]:
    """Split page into heading-delimited sections and SHA-256 hash each one.

    Returns {"Section Title": "<hex digest>", ...}
    This catches changes to code examples, parameter lists, configuration values,
    and any other content within a section — not just structural signals.
    """
    sections: dict[str, list[str]] = {}
    current_heading = "_preamble"
    sections[current_heading] = []

    for element in soup.find_all(["h1", "h2", "h3", "p", "pre", "code",
                                   "ul", "ol", "table", "div", "dl"]):
        if element.name in ("h1", "h2", "h3"):
            heading_text = element.get_text(strip=True)
            if heading_text:
                current_heading = heading_text
                if current_heading not in sections:
                    sections[current_heading] = []
        else:
            # Skip nested elements already captured by a parent
            if element.find_parent(["pre", "ul", "ol", "table", "dl"]) and element.name != "pre":
                continue
            text = element.get_text(strip=True)
            if text:
                sections[current_heading].append(text)

    # Hash each section
    hashes = {}
    for heading, content_parts in sections.items():
        if not content_parts:
            continue
        combined = normalize_text("\n".join(content_parts))
        hashes[heading] = hashlib.sha256(combined.encode("utf-8")).hexdigest()

    return hashes


# ─── Extraction helpers ──────────────────────────────────────────────

def fetch_page(url: str, timeout: int = 30) -> str | None:
    """Fetch a URL and return its HTML text, or None on failure."""
    try:
        resp = requests.get(url, timeout=timeout, headers={
            "User-Agent": "Anthropic-Training-Monitor/1.0"
        })
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"  WARNING: Failed to fetch {url}: {e}", file=sys.stderr)
        return None


def extract_headings(soup: BeautifulSoup) -> list[str]:
    """Extract H1–H3 heading text."""
    return [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]


def extract_key_markers(text: str, existing_markers: list[str]) -> list[str]:
    """
    Check which of the known markers still appear in the page text.
    Also detect potential new markers (config-like patterns).
    """
    found = [m for m in existing_markers if m in text]

    # Detect new config-like patterns not in existing list
    config_patterns = re.findall(r'[A-Z][A-Z_]{3,}[A-Z]', text)  # e.g. MAX_MCP_OUTPUT_TOKENS
    cli_patterns = re.findall(r'claude\s+\w+[\w\s-]*(?=\n|\.|,)', text)  # e.g. claude mcp add
    code_patterns = re.findall(r'(?:context|agent|model|hooks):\s*\w+', text)  # frontmatter-style

    # Deduplicate and add any truly new ones
    all_new = set(config_patterns + cli_patterns + code_patterns) - set(existing_markers)
    # Only include items that look meaningful (>4 chars, not all-caps noise)
    new_meaningful = [m.strip() for m in all_new if len(m.strip()) > 4]

    return {"found": found, "new_candidates": sorted(new_meaningful)[:20]}


def extract_tables(soup: BeautifulSoup) -> dict:
    """Extract text content from HTML tables, returning header→rows mapping."""
    tables = {}
    for i, table in enumerate(soup.find_all("table")):
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        rows = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            if cells:
                rows.append(cells)
        key = f"table_{i}" if not headers else "_".join(headers[:2]).lower().replace(" ", "_")
        tables[key] = {"headers": headers, "row_count": len(rows), "first_column": [r[0] for r in rows if r]}
    return tables


def extract_nav_cards(soup: BeautifulSoup) -> list[str]:
    """Extract navigation card titles from card-like structures."""
    cards = []
    # Look for common card patterns
    for el in soup.find_all(["a", "div"], class_=lambda c: c and ("card" in str(c).lower())):
        title = el.find(["h2", "h3", "h4", "strong", "span"])
        if title:
            text = title.get_text(strip=True)
            if text and len(text) < 100:
                cards.append(text)
    return list(dict.fromkeys(cards))  # dedupe preserving order


def extract_code_blocks(soup: BeautifulSoup) -> list[str]:
    """Extract first line of each code block (useful for tracking CLI examples)."""
    blocks = []
    for code in soup.find_all("code"):
        text = code.get_text(strip=True)
        first_line = text.split("\n")[0].strip()
        if first_line and len(first_line) > 5:
            blocks.append(first_line)
    return blocks[:30]  # cap at 30


# ─── Page-specific extractors ────────────────────────────────────────

def extract_docs_page(html: str, page_id: str, existing_baseline: dict) -> dict:
    """Extract structured data from a Claude Code docs page."""
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    result = {
        "section_headings": extract_headings(soup),
        "section_hashes": extract_section_hashes(soup),
    }

    # Carry forward and check existing markers
    old = existing_baseline.get(page_id, {})
    old_markers = old.get("key_content_markers", [])
    if old_markers:
        marker_check = extract_key_markers(text, old_markers)
        result["key_content_markers"] = marker_check["found"]
        if marker_check["new_candidates"]:
            result["new_marker_candidates"] = marker_check["new_candidates"]
    else:
        # First run — seed with config-like patterns
        config = re.findall(r'[A-Z][A-Z_]{3,}[A-Z]', text)
        result["key_content_markers"] = sorted(set(config))[:20]

    # Check for bundled skills list (skills page)
    if page_id == "cc_skills":
        slash_commands = re.findall(r'/(\w+)', text)
        bundled = [f"/{cmd}" for cmd in slash_commands if cmd in ("simplify", "batch", "debug", "init")]
        if bundled:
            result["bundled_skills"] = sorted(set(bundled))

        # Frontmatter fields
        fm_matches = re.findall(r'(?:^|\n)\s*(\w[\w-]+):', text)
        known_fm = {"name", "description", "argument-hint", "disable-model-invocation",
                     "user-invocable", "allowed-tools", "model", "context", "agent", "hooks"}
        found_fm = [f for f in fm_matches if f in known_fm]
        if found_fm:
            result["frontmatter_fields"] = sorted(set(found_fm))

    # Check for sub-agent specific markers
    if page_id == "cc_sub_agents":
        sub_markers = ["context: fork", "skills field", "permissionMode",
                       "agent teams", "background: true", "isolation: worktree"]
        result["key_content_markers"] = [m for m in sub_markers if m in text]

    # Tables
    tables = extract_tables(soup)
    if tables:
        result["tables"] = tables

    return result


def extract_platform_home(html: str) -> dict:
    """Extract navigation cards from the platform home page."""
    soup = BeautifulSoup(html, "html.parser")
    return {
        "navigation_cards": extract_nav_cards(soup),
        "section_headings": extract_headings(soup),
        "section_hashes": extract_section_hashes(soup),
    }


def extract_platform_overview(html: str) -> dict:
    """Extract feature tables from the platform overview page."""
    soup = BeautifulSoup(html, "html.parser")
    tables = extract_tables(soup)

    # Also extract headings for structural changes
    return {
        "section_headings": extract_headings(soup),
        "feature_tables": tables,
        "section_hashes": extract_section_hashes(soup),
    }


def extract_learn_page(html: str) -> dict:
    """Extract course structure from the /learn landing page."""
    soup = BeautifulSoup(html, "html.parser")
    headings = extract_headings(soup)
    cards = extract_nav_cards(soup)

    # Look for course titles
    courses = []
    for el in soup.find_all(["h2", "h3", "h4", "a"]):
        text = el.get_text(strip=True)
        if any(kw in text.lower() for kw in ("course", "101", "action", "introduction", "mcp")):
            courses.append(text)

    return {
        "section_headings": headings,
        "featured_courses": list(dict.fromkeys(courses))[:10],
        "navigation_cards": cards,
        "section_hashes": extract_section_hashes(soup),
        "note": "Academy content behind Skilljar LMS — monitor landing page for course changes"
    }


def extract_llms_txt(html: str) -> dict:
    """Extract page titles from the llms.txt index."""
    lines = html.strip().split("\n")
    titles = []
    for line in lines:
        # llms.txt format: typically "- [Title](url)" or just lines
        match = re.search(r'\[([^\]]+)\]', line)
        if match:
            titles.append(match.group(1))
        elif line.strip() and not line.startswith("#") and not line.startswith("---"):
            titles.append(line.strip())

    return {
        "page_count": len(titles),
        "page_titles_sample": titles[:15],
    }


# ─── Main logic ──────────────────────────────────────────────────────

EXTRACTORS = {
    "cc_skills": lambda html, old: extract_docs_page(html, "cc_skills", old),
    "cc_mcp": lambda html, old: extract_docs_page(html, "cc_mcp", old),
    "cc_sub_agents": lambda html, old: extract_docs_page(html, "cc_sub_agents", old),
    "cc_hooks": lambda html, old: extract_docs_page(html, "cc_hooks", old),
    "cc_memory": lambda html, old: extract_docs_page(html, "cc_memory", old),
    "cc_plugins": lambda html, old: extract_docs_page(html, "cc_plugins", old),
    "platform_home": lambda html, old: extract_platform_home(html),
    "platform_overview": lambda html, old: extract_platform_overview(html),
    "academy_mcp": lambda html, old: extract_learn_page(html),
    "cc_docs_index": lambda html, old: extract_llms_txt(html),
}


def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Written: {path}")


def build_url_map(registry: dict) -> dict[str, str]:
    """Map page IDs to URLs from the source registry."""
    url_map = {}
    for page in registry.get("source_pages", []):
        url_map[page["id"]] = page["url"]
    # Also include llms.txt if present in baseline
    if "cc_docs_index" not in url_map:
        url_map["cc_docs_index"] = "https://code.claude.com/docs/llms.txt"
    return url_map


# Priority levels in ascending order. Filtering by a level includes all
# levels at or above that level (e.g., --priority normal includes critical + normal).
PRIORITY_LEVELS = {"critical": 0, "normal": 1, "low": 2}


def filter_pages_by_priority(registry: dict, max_priority: str) -> list[str]:
    """Return page IDs whose refresh_priority is at or above the given threshold.

    Priority is cumulative:
      --priority critical  → only critical pages
      --priority normal    → critical + normal pages
      --priority low       → all pages (same as no filter)

    Pages without a refresh_priority field default to 'normal'.
    """
    threshold = PRIORITY_LEVELS.get(max_priority, 1)
    ids = []
    for page in registry.get("source_pages", []):
        page_priority = page.get("refresh_priority", "normal")
        if PRIORITY_LEVELS.get(page_priority, 1) <= threshold:
            ids.append(page["id"])
    return ids


def main():
    parser = argparse.ArgumentParser(description="Generate or update baseline snapshot")
    parser.add_argument("--pages", nargs="+", help="Only update these page IDs")
    parser.add_argument("--priority", choices=["critical", "normal", "low"],
                        help="Only process pages at or above this priority level "
                             "(critical = only critical; normal = critical + normal; low = all)")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be fetched")
    parser.add_argument("--output", type=str, help="Write to alternate output path")
    args = parser.parse_args()

    # Load existing data
    registry = load_json(REGISTRY_PATH)
    url_map = build_url_map(registry)

    existing_snapshot = {}
    if SNAPSHOT_PATH.exists():
        existing_snapshot = load_json(SNAPSHOT_PATH).get("pages", {})

    # Determine which pages to process
    if args.pages:
        page_ids = args.pages
    elif args.priority:
        page_ids = filter_pages_by_priority(registry, args.priority)
        print(f"Priority filter '{args.priority}': selected {len(page_ids)} page(s)")
    else:
        page_ids = list(url_map.keys())
    invalid = [p for p in page_ids if p not in url_map]
    if invalid:
        print(f"ERROR: Unknown page IDs: {invalid}", file=sys.stderr)
        print(f"  Valid IDs: {list(url_map.keys())}", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        print("Dry run — would fetch these pages:")
        for pid in page_ids:
            print(f"  {pid}: {url_map[pid]}")
        return

    # Fetch and extract
    new_pages = dict(existing_snapshot)  # start from existing, overwrite fetched ones
    success_count = 0
    fail_count = 0

    for pid in page_ids:
        url = url_map[pid]
        print(f"Fetching {pid}: {url}")
        html = fetch_page(url)
        if html is None:
            fail_count += 1
            continue

        extractor = EXTRACTORS.get(pid, lambda h, o: extract_docs_page(h, pid, o))
        try:
            data = extractor(html, existing_snapshot)
            data["url"] = url
            new_pages[pid] = data
            heading_count = len(data.get("section_headings", []))
            hash_count = len(data.get("section_hashes", {}))
            print(f"  OK — {heading_count} headings, {hash_count} section hashes extracted")
            success_count += 1
        except Exception as e:
            print(f"  ERROR extracting {pid}: {e}", file=sys.stderr)
            fail_count += 1

    # Build output
    snapshot = {
        "snapshot_date": date.today().isoformat(),
        "pages": new_pages,
    }

    output_path = Path(args.output) if args.output else SNAPSHOT_PATH
    save_json(output_path, snapshot)

    print(f"\nDone: {success_count} pages updated, {fail_count} failures")
    if fail_count:
        print("  Re-run with --pages <id> to retry failed pages")


if __name__ == "__main__":
    main()
