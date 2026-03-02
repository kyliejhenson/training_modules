---
name: content-refresh
description: >
  Detect upstream documentation changes, update affected content sections
  (with diff review), and propagate changes to training deliverables.
  This is the single skill for all drift detection and content updating —
  it combines drift detection, content updating, and deliverable impact
  analysis in one workflow with human review at every step. Use this skill
  whenever the user mentions 'content refresh', 'update content from source',
  'propagate changes', 'sync content', 'refresh training content',
  'update training from docs', 'check for drift', 'check content drift',
  'content drift', 'has the documentation changed', or wants to detect
  upstream changes or act on drift detection results. Also trigger for
  weekly or on-demand documentation change checks.
---

# Content Refresh Pipeline

You are running a three-stage content refresh pipeline that detects upstream documentation changes, updates affected content sections with user approval, and traces those changes through to training deliverables. Every change requires explicit user review — nothing is auto-applied.

## Source Files

Load these files before starting:

- **Source registry**: `.content-monitor/source-registry.json` — maps each source URL to the content files it feeds (includes `refresh_priority` per page)
- **Baseline snapshot**: `.content-monitor/baseline-snapshot.json` — last-known state of each source page
- **Deliverable registry**: `.content-monitor/deliverable-registry.json` — maps each deliverable PPTX to the content sections and slides that use them
- **Tag definitions**: `Tag_definitions/content-tag-definitions.md` — source of truth for all tag names and values

## Refresh Priority

Each source page in the registry has a `refresh_priority` field that controls which pages are checked during different refresh modes:

- **critical** — Impacts how the learner will actually understand the content and if the content still makes sense. These pages feed the most content sections and are checked in every refresh.
- **normal** — Updates that will not impact complete understanding but may impact breadth or accuracy. Checked in standard and full refreshes.
- **low** — Light changes that don't impact learning experience (e.g., landing pages, navigation-only pages). Only checked in full refreshes.

The `--priority` flag on the scripts is **cumulative**: `--priority critical` checks only critical pages, `--priority normal` checks critical + normal, and `--priority low` (or no flag) checks everything.

## Automation Scripts

Three Python helpers in `.content-monitor/scripts/` make the pipeline more deterministic and repeatable. Use them as building blocks within the stages below — they handle the mechanical work while Claude handles interpretation and user interaction.

### Install dependencies (one-time)

```bash
pip install requests beautifulsoup4 --break-system-packages
```

### baseline_snapshot.py — Generate/update baseline

Fetches each source page and extracts structured data (headings, markers, tables, cards) into `baseline-snapshot.json`. Use this instead of ad-hoc WebFetch interpretation.

```bash
# Update all pages
python .content-monitor/scripts/baseline_snapshot.py

# Update specific pages only
python .content-monitor/scripts/baseline_snapshot.py --pages cc_skills cc_mcp

# Update only critical-priority pages (quick refresh)
python .content-monitor/scripts/baseline_snapshot.py --priority critical

# Update critical + normal pages (standard refresh)
python .content-monitor/scripts/baseline_snapshot.py --priority normal

# Preview what would be fetched
python .content-monitor/scripts/baseline_snapshot.py --dry-run
```

### validate_registry.py — Check registry integrity

Validates that every file referenced in source-registry.json and deliverable-registry.json actually exists on disk. Run before any refresh to catch stale references.

```bash
# Check for errors (exit code = number of errors)
python .content-monitor/scripts/validate_registry.py

# JSON output for programmatic use
python .content-monitor/scripts/validate_registry.py --json

# Auto-remove dangling references
python .content-monitor/scripts/validate_registry.py --fix
```

### diff_baseline.py — Structured diff against baseline

Compares current page state against baseline and produces a structured JSON diff report with severity classification (critical/moderate/minor), refresh priority annotation, and affected file mapping.

```bash
# Fetch live pages and diff against baseline
python .content-monitor/scripts/diff_baseline.py

# Human-readable summary
python .content-monitor/scripts/diff_baseline.py --summary

# Only diff critical-priority pages (quick refresh)
python .content-monitor/scripts/diff_baseline.py --priority critical --summary

# Diff critical + normal pages (standard refresh)
python .content-monitor/scripts/diff_baseline.py --priority normal --summary

# Compare two local snapshots (no network)
python .content-monitor/scripts/diff_baseline.py --current new-snapshot.json

# Write report to file
python .content-monitor/scripts/diff_baseline.py --output diff-report.json
```

---

## Version Control & Rollback

This pipeline uses git commits as rollback checkpoints. Before each stage applies changes, a snapshot commit is created so the user can revert if an update introduces problems.

### Commit convention

All checkpoint commits use a structured prefix so they're easy to find in the log:

- `content-refresh: pre-stage-1 snapshot` — before any content files are modified
- `content-refresh: stage-1 complete — updated N content sections` — after Stage 1 changes are applied
- `content-refresh: pre-stage-3 snapshot` — before any deliverable PPTX files are modified
- `content-refresh: stage-3 complete — updated slides in N deliverables` — after Stage 3 changes are applied

### Checkpoint rules

1. **Always commit before modifying files.** Run `git add -A && git commit` with the appropriate pre-stage message before writing any changes. This ensures a clean restore point exists.
2. **Commit after each stage completes.** This captures the post-change state with a descriptive message summarizing what was updated.
3. **Never amend checkpoint commits.** Each commit is an independent restore point. If something goes wrong mid-stage, the pre-stage snapshot is the rollback target.
4. **Baseline snapshot updates get their own commit.** The baseline tracks source state (not our content state), so it's committed separately from content changes: `content-refresh: baseline snapshot updated YYYY-MM-DD`.
5. **Skip commits when nothing changed.** If a stage has no accepted changes (user skipped everything), don't create empty checkpoint commits.

### How to roll back

See the **Rollback** section at the end of this document for step-by-step restore instructions.

---

## Stage 1: Detect Drift & Present Diffs

### Step 0a: Select refresh mode

Before fetching, ask the user which refresh mode to use (via AskUserQuestion):

- **Quick refresh** — Critical-priority pages only (fastest; use for routine mid-week checks). Passes `--priority critical` to scripts.
- **Standard refresh** — Critical + normal priority pages (recommended weekly cadence). Passes `--priority normal` to scripts.
- **Full refresh** — All pages including low priority (monthly or when structural changes are suspected). No `--priority` flag (default behavior).

Store the selected mode — it will be passed to both `baseline_snapshot.py` and `diff_baseline.py` in Steps 2 and 3.

### Step 0b: Validate registries

Before doing any fetching, run the registry validator to catch stale references:

```bash
python .content-monitor/scripts/validate_registry.py
```

If errors are found, fix them first (`--fix` flag or manually) before proceeding. Warnings can be noted but don't block the refresh.

### Step 1: Load registry and baseline

Read `source-registry.json` and `baseline-snapshot.json` from `.content-monitor/`. Parse them to understand which URLs to check, what the baseline state looked like, and which content files each source feeds.

### Step 2: Fetch and snapshot current state

Use the baseline_snapshot script to fetch source pages and extract structured data. Pass the `--priority` flag based on the refresh mode selected in Step 0a:

```bash
# Quick refresh (critical only)
python .content-monitor/scripts/baseline_snapshot.py --priority critical --output .content-monitor/current-snapshot.json

# Standard refresh (critical + normal)
python .content-monitor/scripts/baseline_snapshot.py --priority normal --output .content-monitor/current-snapshot.json

# Full refresh (all pages — omit --priority)
python .content-monitor/scripts/baseline_snapshot.py --output .content-monitor/current-snapshot.json
```

This produces a current-state snapshot in the same format as the baseline, using consistent extraction logic (headings, markers, tables, cards, page counts). The `--output` flag writes to a separate file so the baseline isn't overwritten yet.

For individual pages or retries:
```bash
python .content-monitor/scripts/baseline_snapshot.py --pages cc_skills cc_mcp --output .content-monitor/current-snapshot.json
```

### Step 3: Diff against baseline

Use the diff script for a structured comparison. If a `--priority` filter was used in Step 2, pass the same filter here so only the fetched pages are diffed:

```bash
# With priority filter (match Step 2)
python .content-monitor/scripts/diff_baseline.py --current .content-monitor/current-snapshot.json --priority critical --summary

# Or without filter for full refresh
python .content-monitor/scripts/diff_baseline.py --current .content-monitor/current-snapshot.json --summary
```

This produces a severity-classified diff report showing exactly what changed: new/removed headings, missing/new markers, table changes, page count deltas, and section content hash changes (which catch edits to code examples, parameter lists, and configuration values that structural signals would miss). Each change is tagged with a type, severity (critical/moderate/minor), and the page's `refresh_priority`.

For the full JSON report (used in later steps):
```bash
python .content-monitor/scripts/diff_baseline.py --current .content-monitor/current-snapshot.json --output .content-monitor/diff-report.json
```

If no changes are detected across all sources, report that clearly and stop. No further stages are needed. Clean up the temporary `current-snapshot.json` file.

### Step 4: Identify affected content files

For each source page with changes, use the source registry to identify which content files in `Content/` are potentially affected. Read each affected content file to understand its current state.

### Step 5: Generate diffs for each affected section

For each affected content file:

1. Read the current content section file (including its Tags block)
2. Extract the relevant portion of the updated source page that maps to this section
3. Determine what changed:
   - **Text changes**: Updated explanations, new details, removed content
   - **Code changes**: Modified commands, syntax, examples
   - **Structural changes**: Section was split, merged, or reorganized upstream
   - **New content**: Upstream added a section that doesn't have a corresponding content file yet
   - **Section content hash changed**: The diff report includes `section_content_changed` entries when a section's content hash differs from baseline — this catches changes to code examples, parameter lists, configuration values, and other within-section edits that the structural signals (headings, markers) would miss. Treat these as moderate-severity changes and always fetch the live section text to generate a proper diff for user review.

4. Generate a proposed update that:
   - **Preserves existing tags** (skill level, use cases, priority, practice, selling) unless the nature of the content fundamentally changed. If tags should change, flag this explicitly.
   - **Preserves the Source URL** in the tags block
   - **Follows the exact content file format** from the content-chunking skill (title, Tags block, separator, Content section)
   - **Preserves code examples and commands verbatim** from the updated source

### Step 6: Present diffs for user review

Present all changes to the user as a numbered review list. For each affected section, show:

```
### [N]. [Section Title] — [file path]

**What changed upstream**: [1-2 sentence summary of what's different in the source]

**Current content** (first ~5 lines):
> [excerpt of current section body]

**Proposed update** (first ~5 lines):
> [excerpt of proposed new section body]

**Tag changes**: None / [describe any tag changes]

**Action**: Accept / Skip / Edit
```

Use AskUserQuestion to let the user choose an action for each section. Group sections by source page for easier review. Offer these options:

- **Accept all** — apply all proposed updates
- **Review individually** — go through each section one at a time
- **Skip all** — don't update any content (still update baseline)

If the user chooses "Review individually," present each section and ask:
- **Accept** — apply this update as proposed
- **Skip** — leave this section unchanged
- **Edit** — user provides custom text (keep tags, replace content body)

### Step 7: Apply accepted changes

**7a. Create pre-stage-1 checkpoint.** Before modifying any files, commit the current state:

```bash
git add -A && git commit -m "content-refresh: pre-stage-1 snapshot"
```

If there are no staged changes (working tree is clean), skip the commit — the current HEAD is already a valid restore point.

**7b. Apply updates.** For each accepted update:

1. Overwrite the content file with the updated version (preserving the file format: title, Tags block, separator, Content section)
2. If the section title changed, update the corresponding entry in `00_content_index.md`
3. If a brand-new section is needed (new upstream content), create the file following the content-chunking format and add it to `00_content_index.md`

**7c. Create post-stage-1 checkpoint.** After all content changes are written:

```bash
git add -A && git commit -m "content-refresh: stage-1 complete — updated N content sections"
```

Replace `N` with the actual count. Include the list of updated file paths in the commit body for traceability.

### Step 8: Update baseline snapshot

Replace the baseline with the current snapshot generated in Step 2:

```bash
cp .content-monitor/current-snapshot.json .content-monitor/baseline-snapshot.json
```

Or regenerate a fresh baseline directly:

```bash
python .content-monitor/scripts/baseline_snapshot.py
```

Do this regardless of whether the user accepted or skipped content updates — the baseline tracks the *source* state, not our content state. The snapshot_date is set automatically to today.

Commit the baseline update separately from content changes:

```bash
git add .content-monitor/baseline-snapshot.json && git commit -m "content-refresh: baseline snapshot updated YYYY-MM-DD"
```

This keeps baseline commits distinct from content commits, so rolling back content changes doesn't also revert the baseline (you don't want to re-detect the same drift next run).

Present a summary of Stage 1:
- How many source pages were checked
- How many had changes
- How many content sections were updated / skipped / newly created

---

## Stage 2: Trace Changes to Deliverables

### Step 9: Load deliverable registry

Read `.content-monitor/deliverable-registry.json`. If the file doesn't exist or has no deliverables listed, inform the user:

> "No deliverables are registered yet. The deliverable registry gets populated automatically when you generate training decks using the generate-training skill. To trace content changes to existing deliverables, you'll need to regenerate the deck or manually add a registry entry."

Skip to the Stage 1 summary and stop.

### Step 10: Find affected deliverables

For each content section that was updated (accepted) in Stage 1:

1. Search the deliverable registry for any deliverable whose `content_map` references that section
2. Record the deliverable file path, the slide number(s), and the usage description

### Step 11: Report deliverable impact

Present the findings to the user:

```
## Deliverable Impact

### [Deliverable filename]
- **Slide [N]**: Uses [section file] — [usage description]
- **Slide [M]**: Uses [section file] — [usage description]

### [Another deliverable filename]
- ...
```

If no deliverables are affected (the updated content sections aren't used in any registered deliverable), report that and stop.

Ask the user: "Would you like me to suggest updates to these slides based on the new content?"

If no, stop and present the final summary. If yes, proceed to Stage 3.

---

## Stage 3: Suggest Deliverable Updates

### Important: Read the PPTX Skill First

Before doing any PPTX editing, read the pptx SKILL.md file (check available skills). It contains the template editing workflow, scripts, QA process, and formatting rules. Also read `TEMPLATE_GUIDE.md` for brand specs and slide population rules.

### Step 12: Unpack and analyze affected slides

For each affected deliverable:

1. Copy the PPTX from `Deliverables/` to the working directory
2. Unpack using `unpack.py`
3. For each affected slide number, read the slide XML to extract:
   - Current slide title text
   - Current body/content text
   - Current presenter notes
   - Slide type (Key Concepts, Step-by-Step, Code/Demo, etc.)

### Step 13: Generate proposed slide updates

For each affected slide:

1. Read the updated content section that feeds this slide
2. Based on the slide type, generate proposed new text:
   - **Title**: Update if the concept name changed
   - **Body text**: Rewrite to reflect the updated content, following the slide type's formatting rules (e.g., 2x2 grid for Key Concepts, numbered steps for Step-by-Step)
   - **Presenter notes**: Update the Say/Do sections with the new content, preserving timing, engagement prompts, and transition language
3. Preserve all formatting, colors, fonts, and layout — only change the text content

### Step 14: Present slide changes for review

For each affected slide, show:

```
### Slide [N] in [Deliverable filename] — [Slide type]

**Current title**: [current]
**Proposed title**: [new] (or "No change")

**Current body** (excerpt):
> [current text excerpt]

**Proposed body** (excerpt):
> [proposed text excerpt]

**Notes updated**: Yes / No

**Action**: Accept / Skip / Edit
```

Use AskUserQuestion for each slide or offer "Accept all" / "Review individually" / "Skip all" as in Stage 1.

### Step 15: Apply accepted slide changes

**15a. Create pre-stage-3 checkpoint.** Before modifying any deliverable files, commit the current state:

```bash
git add -A && git commit -m "content-refresh: pre-stage-3 snapshot"
```

This is separate from the Stage 1 checkpoint. If Stage 3 goes wrong, you can revert to this commit without losing the content section updates from Stage 1.

**15b. Apply slide updates.** For each accepted slide update:

1. Edit the slide XML using the Edit tool (never sed/awk) to replace the text content
2. If presenter notes were updated, edit the notes XML as well
3. Follow the PPTX editing rules from the pptx skill:
   - Hex color values without `#` prefix
   - EMU coordinates for any positioning
   - Proper XML escaping for special characters (`&amp;`, `&lt;`, `&gt;`, `&apos;`, `&quot;`)

### Step 16: Repack and finalize

1. Run `clean.py` on the unpacked directory
2. Run `pack.py` to produce the updated PPTX, using the original as reference
3. Copy the updated PPTX back to `Deliverables/`, replacing the old version
4. Update the deliverable registry entry if any slide mappings changed

**16a. Create post-stage-3 checkpoint:**

```bash
git add -A && git commit -m "content-refresh: stage-3 complete — updated slides in N deliverables"
```

Replace `N` with the actual count. Include the deliverable filenames and affected slide numbers in the commit body.

### Step 17: Final summary

Present a complete summary of everything that happened across all three stages:

```
## Content Refresh Summary

### Source Pages Checked: [N]
- Changes detected: [list pages with changes]
- No changes: [list pages without changes]

### Content Sections Updated: [N] of [M] affected
- Accepted: [list]
- Skipped: [list]
- New sections created: [list, if any]

### Deliverables Updated: [N]
- [Deliverable filename]: Slides [X, Y, Z] updated
- ...

### Baseline snapshot updated: Yes (date: [today])
```

---

## Important Notes

- **Anthropic Academy content** (sections 08-13 of MCP) is behind Skilljar LMS and cannot be fully fetched. Monitor the /learn landing page for structural changes and flag if courses are added/removed/renamed. Content sections sourced from Academy material can only be manually updated.
- **Platform docs** (platform_home, platform_overview) don't feed specific content files — they're monitored for signals that new features exist. If changes are detected there, suggest the user run the content-chunking skill on any new documentation pages.
- **New source pages**: If the docs index shows new pages that aren't in the source registry, flag them to the user and suggest adding them to `source-registry.json` and chunking them.
- **Tag preservation**: When updating a content section, keep existing tags unless the update fundamentally changes the nature of the content (e.g., a conceptual overview becomes a code tutorial → skill level and use case type should change). Always flag tag changes explicitly for user review.
- **One section at a time**: Each content section is updated independently. A failure or skip on one section doesn't block others.
- **Media staleness**: When deliverable slide text is updated, the images on those slides may no longer match the new content. After completing Stage 3, if any substantial content changes were applied, inform the user: "Some slide content has changed significantly. You may want to re-run the add-training-media skill on the updated deck to verify that images still match the new text." Do not automatically re-run media insertion — just flag it for the user's consideration.

---

## Rollback

If an update introduces problems, use these procedures to restore to a previous state. All rollback operations use the git checkpoint commits created during the refresh pipeline.

### Find available checkpoints

List recent content-refresh commits:

```bash
git log --oneline --grep="content-refresh:" -10
```

This shows something like:

```
a1b2c3d content-refresh: stage-3 complete — updated slides in 2 deliverables
e4f5g6h content-refresh: pre-stage-3 snapshot
i7j8k9l content-refresh: baseline snapshot updated 2026-03-02
m0n1o2p content-refresh: stage-1 complete — updated 5 content sections
q3r4s5t content-refresh: pre-stage-1 snapshot
```

### Roll back Stage 3 only (undo deliverable changes, keep content updates)

This is the most common rollback — the slide updates didn't work out but the content section updates are fine.

```bash
git revert HEAD --no-edit
```

Or if multiple commits need reverting (e.g., both the stage-3-complete and baseline commits are after the target):

```bash
git revert --no-commit <stage-3-complete-hash>
git commit -m "content-refresh: reverted stage-3 deliverable updates"
```

### Roll back Stage 1 only (undo content changes, keep baseline update)

The content updates were wrong but you still want the baseline updated so the same drift isn't re-detected.

```bash
git revert --no-commit <stage-1-complete-hash>
git commit -m "content-refresh: reverted stage-1 content updates"
```

### Roll back everything (full revert to pre-refresh state)

Undo all changes from a refresh run. Use the pre-stage-1 snapshot as the target:

```bash
git revert --no-commit HEAD~N..HEAD
git commit -m "content-refresh: full rollback to pre-refresh state"
```

Where `N` is the number of commits to revert (count from the pre-stage-1 snapshot to HEAD). Alternatively, revert each checkpoint commit individually in reverse order.

**Important**: Reverting the baseline snapshot commit means the next refresh run will re-detect the same drift. This is intentional — it gives you a clean slate to re-run the refresh with different decisions.

### Roll back a single content section

If only one file needs reverting (not the entire stage):

```bash
git checkout <pre-stage-1-hash> -- Content/content_skills/01_Overview/01_what_are_skills.md
git add Content/content_skills/01_Overview/01_what_are_skills.md
git commit -m "content-refresh: reverted 01_what_are_skills.md to pre-refresh state"
```

### View what a checkpoint changed

To see exactly what a stage changed before deciding whether to revert:

```bash
git diff <pre-stage-hash> <post-stage-hash>
```

Or for a summary of affected files:

```bash
git diff --stat <pre-stage-hash> <post-stage-hash>
```
