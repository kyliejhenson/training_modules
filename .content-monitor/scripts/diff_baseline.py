#!/usr/bin/env python3
"""
diff_baseline.py — Structured comparison between current page state and baseline.

Fetches each source page (or reads from a pre-fetched snapshot), compares
against baseline-snapshot.json, and outputs a structured JSON diff report.

Usage:
    python diff_baseline.py                         # fetch live pages and diff against baseline
    python diff_baseline.py --current snapshot.json  # compare two local snapshots (no fetching)
    python diff_baseline.py --pages cc_skills cc_mcp # only diff specific pages
    python diff_baseline.py --priority critical      # only critical-priority pages
    python diff_baseline.py --priority normal        # critical + normal pages
    python diff_baseline.py --output diff-report.json # write report to file

Output format (JSON):
    {
      "diff_date": "2026-03-02",
      "pages_checked": 10,
      "pages_changed": 2,
      "pages_unchanged": 8,
      "diffs": {
        "cc_skills": {
          "status": "changed",
          "changes": [
            {"type": "heading_added", "value": "New section title"},
            {"type": "heading_removed", "value": "Old section title"},
            {"type": "marker_missing", "value": "some_config_var"},
            {"type": "marker_new", "value": "new_config_var"},
            {"type": "section_content_changed", "value": "Configuration", "detail": "Content hash changed ..."},
            ...
          ],
          "affected_files": ["01_Overview/01_what_are_skills.md", ...],
          "severity": "moderate"
        }
      }
    }

Requires: requests, beautifulsoup4 (only if fetching live — not needed with --current)
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

MONITOR_DIR = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = MONITOR_DIR / "baseline-snapshot.json"
REGISTRY_PATH = MONITOR_DIR / "source-registry.json"


def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


# ─── Diff helpers ────────────────────────────────────────────────────

def diff_lists(old: list, new: list, added_type: str, removed_type: str) -> list[dict]:
    """Compare two lists and return add/remove change entries."""
    changes = []
    old_set = set(old)
    new_set = set(new)

    for item in sorted(new_set - old_set):
        changes.append({"type": added_type, "value": item})
    for item in sorted(old_set - new_set):
        changes.append({"type": removed_type, "value": item})

    return changes


def normalize_table_value(val) -> list[str]:
    """Normalize a table value to a flat list of strings for comparison.
    Handles both formats:
      - Old baseline format: {"key": ["item1", "item2"]}  (values are lists)
      - New script format: {"key": {"first_column": [...], "row_count": N}}
    """
    if isinstance(val, list):
        return val
    if isinstance(val, dict):
        return val.get("first_column", [])
    return []


def diff_tables(old_tables: dict, new_tables: dict) -> list[dict]:
    """Compare feature table structures."""
    changes = []

    all_keys = set(list(old_tables.keys()) + list(new_tables.keys()))
    for key in sorted(all_keys):
        old_t = old_tables.get(key)
        new_t = new_tables.get(key)

        if old_t is None:
            changes.append({"type": "table_added", "value": key})
            continue
        if new_t is None:
            changes.append({"type": "table_removed", "value": key})
            continue

        # Normalize to lists for comparison
        old_items = normalize_table_value(old_t)
        new_items = normalize_table_value(new_t)
        changes.extend(diff_lists(old_items, new_items,
                                  f"table_row_added:{key}", f"table_row_removed:{key}"))

        # Compare row count if available (new format only)
        if isinstance(old_t, dict) and isinstance(new_t, dict):
            old_count = old_t.get("row_count", 0)
            new_count = new_t.get("row_count", 0)
            if old_count != new_count:
                changes.append({
                    "type": "table_size_changed",
                    "value": key,
                    "detail": f"{old_count} → {new_count} rows"
                })

    return changes


def diff_page(page_id: str, old_data: dict, new_data: dict) -> dict:
    """
    Compare old and new page data, returning a structured diff.
    Works with whatever keys are present — headings, markers, tables, cards, etc.
    """
    changes = []

    # Section headings
    old_headings = old_data.get("section_headings", old_data.get("section_headings_sample", []))
    new_headings = new_data.get("section_headings", new_data.get("section_headings_sample", []))
    changes.extend(diff_lists(old_headings, new_headings, "heading_added", "heading_removed"))

    # Key content markers
    old_markers = old_data.get("key_content_markers", [])
    new_markers = new_data.get("key_content_markers", [])
    changes.extend(diff_lists(old_markers, new_markers, "marker_new", "marker_missing"))

    # New marker candidates (from baseline_snapshot.py)
    new_candidates = new_data.get("new_marker_candidates", [])
    for c in new_candidates:
        changes.append({"type": "marker_candidate", "value": c})

    # Bundled skills (skills page)
    old_skills = old_data.get("bundled_skills", [])
    new_skills = new_data.get("bundled_skills", [])
    if old_skills or new_skills:
        changes.extend(diff_lists(old_skills, new_skills, "bundled_skill_added", "bundled_skill_removed"))

    # Frontmatter fields
    old_fm = old_data.get("frontmatter_fields", [])
    new_fm = new_data.get("frontmatter_fields", [])
    if old_fm or new_fm:
        changes.extend(diff_lists(old_fm, new_fm, "frontmatter_added", "frontmatter_removed"))

    # Navigation cards
    old_cards = old_data.get("navigation_cards", [])
    new_cards = new_data.get("navigation_cards", [])
    if old_cards or new_cards:
        changes.extend(diff_lists(old_cards, new_cards, "card_added", "card_removed"))

    # Featured courses
    old_courses = old_data.get("featured_courses", [])
    new_courses = new_data.get("featured_courses", [])
    if old_courses or new_courses:
        changes.extend(diff_lists(old_courses, new_courses, "course_added", "course_removed"))

    # Learning sections
    old_sections = old_data.get("learning_sections", [])
    new_sections = new_data.get("learning_sections", [])
    if old_sections or new_sections:
        changes.extend(diff_lists(old_sections, new_sections, "learning_section_added", "learning_section_removed"))

    # Feature tables (platform overview)
    old_ft = old_data.get("feature_tables", {})
    new_ft = new_data.get("feature_tables", {})
    if old_ft or new_ft:
        changes.extend(diff_tables(old_ft, new_ft))

    # Page count (llms.txt)
    old_count = old_data.get("page_count")
    new_count = new_data.get("page_count")
    if old_count is not None and new_count is not None and old_count != new_count:
        changes.append({
            "type": "page_count_changed",
            "value": f"{old_count} → {new_count}",
            "detail": f"{'Grew' if new_count > old_count else 'Shrunk'} by {abs(new_count - old_count)} pages"
        })

    # Page titles sample
    old_titles = old_data.get("page_titles_sample", [])
    new_titles = new_data.get("page_titles_sample", [])
    if old_titles or new_titles:
        changes.extend(diff_lists(old_titles, new_titles, "doc_page_added", "doc_page_removed"))

    # Section content hashes — catches changes to code examples, parameter lists,
    # configuration values, and any other within-section content that structural
    # signals (headings, markers) would miss.
    old_hashes = old_data.get("section_hashes", {})
    new_hashes = new_data.get("section_hashes", {})
    if old_hashes or new_hashes:
        for section in sorted(set(old_hashes) | set(new_hashes)):
            old_h = old_hashes.get(section)
            new_h = new_hashes.get(section)

            if old_h and not new_h:
                # Section removed — already caught by heading_removed, skip
                continue
            if new_h and not old_h:
                # Section added — already caught by heading_added, skip
                continue
            if old_h != new_h:
                changes.append({
                    "type": "section_content_changed",
                    "value": section,
                    "detail": "Content hash changed (code examples, params, or text updated)"
                })

    # Determine severity
    severity = classify_severity(changes)

    return {
        "status": "changed" if changes else "unchanged",
        "changes": changes,
        "severity": severity,
    }


def classify_severity(changes: list[dict]) -> str:
    """
    Classify overall severity of changes.
    - critical: structural changes (headings added/removed, tables changed)
    - moderate: content changes (markers missing, new features)
    - minor: cosmetic or candidate-only changes
    """
    if not changes:
        return "none"

    critical_types = {"heading_added", "heading_removed", "table_added", "table_removed",
                      "page_count_changed", "doc_page_added", "doc_page_removed",
                      "bundled_skill_added", "bundled_skill_removed",
                      "frontmatter_added", "frontmatter_removed"}
    moderate_types = {"marker_missing", "marker_new", "card_added", "card_removed",
                      "course_added", "course_removed", "table_size_changed",
                      "learning_section_added", "learning_section_removed",
                      "section_content_changed"}

    types_present = {c["type"].split(":")[0] for c in changes}

    if types_present & critical_types:
        return "critical"
    if types_present & moderate_types:
        return "moderate"
    return "minor"


# ─── Affected files lookup ───────────────────────────────────────────

def get_affected_files(page_id: str, registry: dict) -> list[str]:
    """Look up which content files a source page feeds."""
    for page in registry.get("source_pages", []):
        if page["id"] == page_id:
            return page.get("affected_files", [])
    return []


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


# ─── Main ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Diff current state against baseline snapshot")
    parser.add_argument("--current", type=str,
                        help="Path to current snapshot JSON (skip live fetching)")
    parser.add_argument("--pages", nargs="+",
                        help="Only diff these page IDs")
    parser.add_argument("--priority", choices=["critical", "normal", "low"],
                        help="Only diff pages at or above this priority level "
                             "(critical = only critical; normal = critical + normal; low = all)")
    parser.add_argument("--output", type=str,
                        help="Write diff report to file (default: stdout)")
    parser.add_argument("--summary", action="store_true",
                        help="Print human-readable summary instead of JSON")
    args = parser.parse_args()

    # Load baseline
    if not SNAPSHOT_PATH.exists():
        print("ERROR: No baseline snapshot found. Run baseline_snapshot.py first.", file=sys.stderr)
        sys.exit(1)

    baseline = load_json(SNAPSHOT_PATH)
    baseline_pages = baseline.get("pages", {})

    # Load or generate current state
    if args.current:
        current = load_json(Path(args.current))
        current_pages = current.get("pages", {})
    else:
        # Generate fresh snapshot by running baseline_snapshot.py
        print("Generating fresh snapshot...", file=sys.stderr)
        try:
            from baseline_snapshot import main as snapshot_main
            import tempfile
            with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as tmp:
                tmp_path = tmp.name
            # Run snapshot to temp file
            sys.argv = ["baseline_snapshot.py", "--output", tmp_path]
            if args.pages:
                sys.argv.extend(["--pages"] + args.pages)
            elif args.priority:
                sys.argv.extend(["--priority", args.priority])
            snapshot_main()
            current = load_json(Path(tmp_path))
            current_pages = current.get("pages", {})
            Path(tmp_path).unlink()
        except ImportError:
            print("ERROR: Cannot import baseline_snapshot. Use --current <file> to provide a snapshot.",
                  file=sys.stderr)
            sys.exit(1)

    # Load registry for affected files lookup
    registry = load_json(REGISTRY_PATH) if REGISTRY_PATH.exists() else {"source_pages": []}

    # Determine pages to diff
    if args.pages:
        page_ids = args.pages
    elif args.priority:
        page_ids = filter_pages_by_priority(registry, args.priority)
        print(f"Priority filter '{args.priority}': selected {len(page_ids)} page(s)", file=sys.stderr)
    else:
        page_ids = list(set(list(baseline_pages.keys()) + list(current_pages.keys())))

    # Run diffs
    diffs = {}
    pages_changed = 0
    pages_unchanged = 0

    for pid in sorted(page_ids):
        old = baseline_pages.get(pid, {})
        new = current_pages.get(pid, {})

        if not old and not new:
            continue

        if not old:
            diffs[pid] = {
                "status": "new_page",
                "changes": [{"type": "new_page", "value": f"Page {pid} not in baseline"}],
                "affected_files": get_affected_files(pid, registry),
                "severity": "critical",
            }
            pages_changed += 1
            continue

        if not new:
            diffs[pid] = {
                "status": "page_missing",
                "changes": [{"type": "page_missing", "value": f"Page {pid} not in current snapshot"}],
                "affected_files": get_affected_files(pid, registry),
                "severity": "critical",
            }
            pages_changed += 1
            continue

        result = diff_page(pid, old, new)
        result["affected_files"] = get_affected_files(pid, registry)

        if result["status"] == "changed":
            pages_changed += 1
            diffs[pid] = result
        else:
            pages_unchanged += 1

    # Annotate diffs with refresh_priority from registry
    priority_map = {p["id"]: p.get("refresh_priority", "normal")
                    for p in registry.get("source_pages", [])}
    for pid, diff in diffs.items():
        diff["refresh_priority"] = priority_map.get(pid, "normal")

    # Build report
    report = {
        "diff_date": date.today().isoformat(),
        "baseline_date": baseline.get("snapshot_date", "unknown"),
        "pages_checked": len(page_ids),
        "pages_changed": pages_changed,
        "pages_unchanged": pages_unchanged,
        "priority_filter": args.priority or "all",
        "diffs": diffs,
    }

    # Output
    if args.summary:
        print_summary(report)
    elif args.output:
        with open(args.output, "w") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Diff report written to {args.output}", file=sys.stderr)
    else:
        print(json.dumps(report, indent=2))

    # Exit code: 0 if no changes, 1 if changes detected
    sys.exit(1 if pages_changed > 0 else 0)


def print_summary(report: dict):
    """Print a human-readable summary of the diff report."""
    priority_filter = report.get("priority_filter", "all")
    print(f"Content Drift Report — {report['diff_date']}")
    print(f"Baseline from: {report['baseline_date']}")
    print(f"Pages checked: {report['pages_checked']} (priority filter: {priority_filter})")
    print(f"Changed: {report['pages_changed']} | Unchanged: {report['pages_unchanged']}")
    print()

    if not report["diffs"]:
        print("No drift detected. All pages match baseline.")
        return

    for pid, diff in report["diffs"].items():
        severity = diff.get("severity", "unknown")
        priority = diff.get("refresh_priority", "normal")
        icon = {"critical": "!!!", "moderate": "!!", "minor": "!", "none": " "}.get(severity, "?")
        print(f"[{icon}] {pid} — severity: {severity} | priority: {priority}")

        for change in diff.get("changes", []):
            ctype = change["type"]
            value = change["value"]
            detail = change.get("detail", "")
            prefix = "+" if "added" in ctype or "new" in ctype else "-" if "removed" in ctype or "missing" in ctype else "~"
            line = f"    {prefix} {ctype}: {value}"
            if detail:
                line += f" ({detail})"
            print(line)

        affected = diff.get("affected_files", [])
        if affected:
            print(f"    → Affects {len(affected)} content file(s)")
        print()


if __name__ == "__main__":
    main()
