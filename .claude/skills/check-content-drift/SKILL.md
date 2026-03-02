---
name: check-content-drift
description: >
  DEPRECATED — This skill has been merged into content-refresh.
  Use the content-refresh skill instead, which includes drift detection
  as its Stage 1 and exits early if no changes are found.
  Kept as a redirect to avoid breaking existing references.
---

# Content Drift Monitor — MERGED INTO content-refresh

This skill's functionality has been fully merged into the **content-refresh** skill. The content-refresh skill includes drift detection as its Stage 1, and exits early if no changes are detected — making this standalone skill redundant.

## What to do instead

Run the **content-refresh** skill. It will:

1. **Detect drift** (Stage 1) — fetches all source pages, compares against baseline, maps changes to content files
2. **Update content** (Stage 2) — if changes are found, presents diffs for your review and applies accepted updates
3. **Update deliverables** (Stage 3) — traces content changes to affected training decks and suggests slide-level updates

If no drift is detected in Stage 1, the skill reports that clearly and stops — giving you the same "quick check" behavior this skill used to provide, but without maintaining a separate skill.
