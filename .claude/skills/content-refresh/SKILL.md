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

- **Source registry**: `.content-monitor/source-registry.json` — maps each source URL to the content files it feeds
- **Baseline snapshot**: `.content-monitor/baseline-snapshot.json` — last-known state of each source page
- **Deliverable registry**: `.content-monitor/deliverable-registry.json` — maps each deliverable PPTX to the content sections and slides that use them
- **Tag definitions**: `Tag_definitions/content-tag-definitions.md` — source of truth for all tag names and values

---

## Stage 1: Detect Drift & Present Diffs

### Step 1: Load registry and baseline

Read `source-registry.json` and `baseline-snapshot.json` from `.content-monitor/`. Parse them to understand which URLs to check, what the baseline state looked like, and which content files each source feeds.

### Step 2: Fetch each source page

For each page in the baseline snapshot, use WebFetch to retrieve the current content. Extract:

- All section headings (H2, H3 level)
- Key content markers (specific technical terms, config values, feature names)
- Feature/capability tables (for the platform overview page)
- Navigation cards (for the platform home page)
- Course listings (for the /learn page)

For the Claude Code docs index (llms.txt), fetch it and count total pages and check for new or removed page titles.

### Step 3: Compare against baseline

For each source page, compare current state against baseline:

- **Section headings**: New sections? Removed sections? Renamed sections?
- **Key content markers**: Same technical terms, config values, and feature names present?
- **Feature tables**: New features listed? Removed features?
- **Page count**: Has the docs index grown or shrunk?

If no changes are detected across all sources, report that clearly and stop. No further stages are needed.

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

For each accepted update:

1. Overwrite the content file with the updated version (preserving the file format: title, Tags block, separator, Content section)
2. If the section title changed, update the corresponding entry in `00_content_index.md`
3. If a brand-new section is needed (new upstream content), create the file following the content-chunking format and add it to `00_content_index.md`

### Step 8: Update baseline snapshot

Update `.content-monitor/baseline-snapshot.json` with the current state of all checked source pages. Do this regardless of whether the user accepted or skipped content updates — the baseline tracks the *source* state, not our content state. Update the `snapshot_date` field to today's date.

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

For each accepted slide update:

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
