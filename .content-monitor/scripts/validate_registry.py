#!/usr/bin/env python3
"""
validate_registry.py — Validate that all files referenced in the registries actually exist.

Checks:
  1. source-registry.json: every affected_file path resolves to a real file
  2. deliverable-registry.json: every deliverable PPTX exists, every content_map
     section resolves, and sources_manifest exists
  3. baseline-snapshot.json: every page ID matches a source-registry entry

Usage:
    python validate_registry.py             # full validation, exit code = number of errors
    python validate_registry.py --json      # output results as JSON
    python validate_registry.py --fix       # remove dangling references (writes corrected files)

No external dependencies required.
"""

import argparse
import json
import sys
from pathlib import Path

MONITOR_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = MONITOR_DIR.parent  # Training_modules/
CONTENT_DIR = REPO_ROOT / "Content"

REGISTRY_PATH = MONITOR_DIR / "source-registry.json"
DELIVERABLE_PATH = MONITOR_DIR / "deliverable-registry.json"
SNAPSHOT_PATH = MONITOR_DIR / "baseline-snapshot.json"


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ─── Validators ──────────────────────────────────────────────────────

def validate_source_registry(registry: dict) -> list[dict]:
    """Check that every affected_file in source-registry.json exists on disk."""
    errors = []
    warnings = []

    for page in registry.get("source_pages", []):
        page_id = page["id"]
        feature = page.get("content_feature")

        if not feature:
            # Pages like platform_home have no content_feature — that's expected
            if page.get("affected_files"):
                errors.append({
                    "type": "error",
                    "registry": "source",
                    "page_id": page_id,
                    "message": f"Page has affected_files but no content_feature"
                })
            continue

        content_dir = CONTENT_DIR / feature

        if not content_dir.exists():
            errors.append({
                "type": "error",
                "registry": "source",
                "page_id": page_id,
                "message": f"Content directory does not exist: Content/{feature}/"
            })
            continue

        for filepath in page.get("affected_files", []):
            full_path = content_dir / filepath
            if not full_path.exists():
                errors.append({
                    "type": "error",
                    "registry": "source",
                    "page_id": page_id,
                    "file": filepath,
                    "message": f"File not found: Content/{feature}/{filepath}"
                })

        # Check URL is valid-looking
        url = page.get("url", "")
        if not url.startswith("http"):
            warnings.append({
                "type": "warning",
                "registry": "source",
                "page_id": page_id,
                "message": f"URL looks invalid: {url}"
            })

    return errors + warnings


def validate_deliverable_registry(deliverables: dict) -> list[dict]:
    """Check that deliverable files and their content_map references exist."""
    errors = []

    for entry in deliverables.get("deliverables", []):
        deliverable_file = REPO_ROOT / entry["file"]
        feature = entry.get("feature")

        # Check the PPTX exists
        if not deliverable_file.exists():
            errors.append({
                "type": "error",
                "registry": "deliverable",
                "deliverable": entry["file"],
                "message": f"Deliverable file not found: {entry['file']}"
            })

        # Check sources manifest exists
        manifest = entry.get("sources_manifest")
        if manifest:
            manifest_path = REPO_ROOT / manifest
            if not manifest_path.exists():
                errors.append({
                    "type": "error",
                    "registry": "deliverable",
                    "deliverable": entry["file"],
                    "message": f"Sources manifest not found: {manifest}"
                })

        # Check content_map references
        content_dir = CONTENT_DIR / feature if feature else None
        for mapping in entry.get("content_map", []):
            section = mapping["section"]
            if content_dir:
                section_path = content_dir / section
                if not section_path.exists():
                    errors.append({
                        "type": "error",
                        "registry": "deliverable",
                        "deliverable": entry["file"],
                        "section": section,
                        "message": f"Content section not found: Content/{feature}/{section}"
                    })

            # Validate slide numbers are positive integers
            for slide_num in mapping.get("slides", []):
                if not isinstance(slide_num, int) or slide_num < 1:
                    errors.append({
                        "type": "error",
                        "registry": "deliverable",
                        "deliverable": entry["file"],
                        "section": section,
                        "message": f"Invalid slide number: {slide_num}"
                    })

    return errors


def validate_baseline_snapshot(snapshot: dict, registry: dict) -> list[dict]:
    """Check that baseline page IDs match source-registry entries."""
    errors = []

    registry_ids = {p["id"] for p in registry.get("source_pages", [])}
    # cc_docs_index is tracked in baseline but not always in source_pages
    registry_ids.add("cc_docs_index")

    snapshot_ids = set(snapshot.get("pages", {}).keys())

    # Pages in baseline but not in registry
    orphaned = snapshot_ids - registry_ids
    for pid in orphaned:
        errors.append({
            "type": "warning",
            "registry": "baseline",
            "page_id": pid,
            "message": f"Page in baseline but not in source registry"
        })

    # Pages in registry but not in baseline
    missing = registry_ids - snapshot_ids
    for pid in missing:
        errors.append({
            "type": "warning",
            "registry": "baseline",
            "page_id": pid,
            "message": f"Page in source registry but no baseline snapshot"
        })

    return errors


def cross_validate(registry: dict, deliverables: dict) -> list[dict]:
    """Cross-check: content sections in deliverables should appear in source registry."""
    errors = []

    # Build set of all known content files from source registry
    known_files = set()
    for page in registry.get("source_pages", []):
        feature = page.get("content_feature")
        if feature:
            for f in page.get("affected_files", []):
                known_files.add(f"{feature}/{f}")

    # Check deliverable content_map against known files
    for entry in deliverables.get("deliverables", []):
        feature = entry.get("feature")
        for mapping in entry.get("content_map", []):
            key = f"{feature}/{mapping['section']}"
            if key not in known_files:
                errors.append({
                    "type": "warning",
                    "registry": "cross-validation",
                    "deliverable": entry["file"],
                    "section": mapping["section"],
                    "message": f"Content section in deliverable but not tracked in source registry: {key}"
                })

    return errors


# ─── Fix mode ────────────────────────────────────────────────────────

def fix_source_registry(registry: dict, errors: list[dict]) -> int:
    """Remove dangling file references from source registry."""
    dangling = {(e["page_id"], e.get("file")) for e in errors
                if e["registry"] == "source" and e["type"] == "error" and "file" in e}
    if not dangling:
        return 0

    removed = 0
    for page in registry.get("source_pages", []):
        pid = page["id"]
        original = page.get("affected_files", [])
        filtered = [f for f in original if (pid, f) not in dangling]
        if len(filtered) < len(original):
            removed += len(original) - len(filtered)
            page["affected_files"] = filtered

    save_json(REGISTRY_PATH, registry)
    return removed


def fix_deliverable_registry(deliverables: dict, errors: list[dict]) -> int:
    """Remove dangling section references from deliverable registry."""
    dangling = {(e["deliverable"], e.get("section")) for e in errors
                if e["registry"] == "deliverable" and e["type"] == "error" and "section" in e}
    if not dangling:
        return 0

    removed = 0
    for entry in deliverables.get("deliverables", []):
        dfile = entry["file"]
        original = entry.get("content_map", [])
        filtered = [m for m in original if (dfile, m["section"]) not in dangling]
        if len(filtered) < len(original):
            removed += len(original) - len(filtered)
            entry["content_map"] = filtered

    save_json(DELIVERABLE_PATH, deliverables)
    return removed


# ─── Main ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Validate registry file references")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--fix", action="store_true", help="Remove dangling references")
    args = parser.parse_args()

    all_errors = []

    # Load files
    registry = load_json(REGISTRY_PATH)
    deliverables = load_json(DELIVERABLE_PATH)
    snapshot = load_json(SNAPSHOT_PATH)

    if not registry:
        print("ERROR: source-registry.json not found", file=sys.stderr)
        sys.exit(1)

    # Run validators
    all_errors.extend(validate_source_registry(registry))

    if deliverables:
        all_errors.extend(validate_deliverable_registry(deliverables))
        all_errors.extend(cross_validate(registry, deliverables))
    else:
        all_errors.append({
            "type": "warning",
            "registry": "deliverable",
            "message": "deliverable-registry.json not found — skipping deliverable checks"
        })

    if snapshot:
        all_errors.extend(validate_baseline_snapshot(snapshot, registry))
    else:
        all_errors.append({
            "type": "warning",
            "registry": "baseline",
            "message": "baseline-snapshot.json not found — skipping baseline checks"
        })

    # Output
    errors_only = [e for e in all_errors if e["type"] == "error"]
    warnings_only = [e for e in all_errors if e["type"] == "warning"]

    if args.json:
        result = {
            "valid": len(errors_only) == 0,
            "error_count": len(errors_only),
            "warning_count": len(warnings_only),
            "issues": all_errors,
        }
        print(json.dumps(result, indent=2))
    else:
        if not all_errors:
            print("All registries valid — no issues found.")
        else:
            if errors_only:
                print(f"\n ERRORS ({len(errors_only)}):")
                for e in errors_only:
                    print(f"  [{e['registry']}] {e['message']}")
            if warnings_only:
                print(f"\n WARNINGS ({len(warnings_only)}):")
                for w in warnings_only:
                    print(f"  [{w['registry']}] {w['message']}")

    # Fix mode
    if args.fix and errors_only:
        print("\n--- Fix mode ---")
        removed_src = fix_source_registry(registry, errors_only)
        removed_del = fix_deliverable_registry(deliverables, errors_only) if deliverables else 0
        print(f"  Removed {removed_src} dangling source references")
        print(f"  Removed {removed_del} dangling deliverable references")
        print("  Re-run without --fix to verify")

    sys.exit(len(errors_only))


if __name__ == "__main__":
    main()
