# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A training content pipeline that turns Anthropic documentation into branded PowerPoint training decks, tailored to specific audience profiles. The pipeline has five stages: chunk source docs into tagged sections, generate a text-complete PPTX from a template, add media (images + video links), monitor upstream docs for drift, and refresh content and deliverables when drift is detected.

## Pipeline Stages (Skills)

The pipeline is driven by six Claude Code skills in `.claude/skills/`:

### Content Preparation
1. **content-chunking** — Breaks a source document (URL, file, or pasted text) into one-concept-per-file markdown sections, each tagged with audience metadata. Outputs go to `Content/content_<feature>/` with a `00_content_index.md` summarizing all sections.

### Training Generation
2. **generate-training** — Builds a branded PPTX from `Anthropic_Training_Template.pptx`. Asks the user for an audience profile and feature topic, filters content sections by profile tags, plans a slide deck, populates all text and presenter notes. Outputs text-complete decks (no images or clickable videos yet). Output naming: `Training_[Feature]_[Profile].pptx`.

3. **add-training-media** — Inserts images and makes video links clickable in a deck produced by generate-training. Matches images from `Imagery/` to slides, searches for videos on claude.com and YouTube, builds a `media_manifest.json`, and runs `insert_media.py` for XML-level media insertion.

### Supporting Deliverables
4. **generate-exercises** — Creates a branded `.docx` exercise document from a training deck's Sources manifest. Produces audience-appropriate hands-on activities grounded in the same content the training covered. Output naming: `Exercises_[Feature]_[Profile].docx`.

5. **generate-facilitator-guide** — Creates a comprehensive `.docx` facilitator guide from a training PPTX. Includes per-slide facilitation guidance with embedded slide images, presenter notes, engagement techniques, and timing. Output naming: `Facilitator_Guide_[Feature]_[Profile].docx`.

### Content Maintenance
6. **content-refresh** — The single skill for all drift detection and content updating. Fetches upstream doc pages, compares against baselines, generates side-by-side diffs for affected content sections, and presents them for user review (accept/skip/edit per section). Then traces accepted changes through the deliverable registry to identify which training decks and slides are affected, and suggests PPTX text updates for review. Every change requires explicit user approval. If no drift is detected, it exits early.

> **Note**: The former `check-content-drift` skill has been merged into `content-refresh`. Its SKILL.md remains as a redirect.

## Key Directory Layout

```
Content/
  content_mcp/          # MCP feature content (67 sections across 13 subfolders)
  content_skills/       # Skills feature content (across 8 subfolders)
  Each has 00_content_index.md with full section inventory and tags

Profiles/               # Audience profiles (developers, enterprise-champions, solutions-engineers, solutions-partners)
Tag_definitions/        # content-tag-definitions.md — source of truth for all tag names and values
Imagery/
  images_mcp/           # MCP screenshots
  images_skills/        # Skills screenshots
  illustrations/        # Themed SVG/PNG illustrations (4 subdirs by theme)
  logos/                # Anthropic logos

fonts/                  # Anthropic brand fonts (Styrene A, Test Tiempos, Lora)
TEMPLATE_GUIDE.md       # Complete guide to the 25-slide template (brand specs, slide inventory, population rules)
Anthropic_Training_Template.pptx  # The source template
```

## Content Tagging System

Every content section is tagged on five dimensions defined in `Tag_definitions/content-tag-definitions.md`:

- **Technical Skill Level**: Beginner / Intermediate / Advanced
- **Use Case Types**: Technical implementation, Security & compliance, Workflow integration, Business value & ROI, Adoption & change management, Evaluation & testing
- **Instructional Priority**: Foundational / Applied / Supplemental (drives slide sequencing)
- **Technical Application Practice**: Yes / No
- **Value-Based Selling Information**: Yes / No

Content-to-profile matching requires ALL of: skill level at or below profile level, AND at least one use case type overlap.

## Profile Tag Quick Reference

| Profile | Skill Level | Key Use Cases | Practice | Selling |
|---------|------------|---------------|----------|---------|
| Developers | Advanced | Technical impl, Security, Eval & testing | Yes | No |
| Enterprise Champions | Intermediate | Security, Workflow, Business value, Adoption | No | Yes |
| Solutions Engineers | Advanced | Technical impl, Security, Workflow, Business value, Eval | Yes | Yes |
| Solutions Partners | Intermediate | All six types | Yes | Yes |

## Template Brand Specs

- Colors: Dark `141413`, Light `FAF9F5`, Orange `D97757`, Blue `6A9BCC`, Green `788C5D`, Mid Gray `B0AEA5`, Light Gray `E8E6DC`, Dusty Rose `B5758A`, Lavender `9D8FBF`, Cornflower Blue `7EA5CB`, Sage Mint `ADBEB0`, Warm Sand `CCC0AB`
- Fonts: Test Tiempos Headline Light (PPTX slide titles), Styrene A (labels/UI), Lora (body text in PPTX and docx deliverables), Courier New (code)
- Font fallbacks: Test Tiempos Headline Light → Georgia, Styrene A → Arial, Lora → Georgia, Courier New → Consolas
- Hex values in PPTX XML use NO `#` prefix
- EMU conversions: 1 inch = 914,400 EMU; full slide = 9,144,000 x 5,143,500

## PPTX Editing Workflow

Template editing follows unpack → edit XML → clean → repack:
1. Unpack: `python scripts/office/unpack.py <file.pptx> <output_dir>/`
2. Duplicate slides: `python scripts/add_slide.py`
3. Edit slide XML with the Edit tool (never sed/awk)
4. Clean: `python scripts/clean.py <unpacked_dir>`
5. Repack: `python scripts/office/pack.py <unpacked_dir> <output.pptx> --original <original.pptx>`

Media insertion uses `insert_media.py` from the add-training-media skill with a JSON manifest.

## Content Drift Monitoring & Refresh

Source URLs are registered in `.content-monitor/source-registry.json`, mapping each upstream page to the content files it feeds. Each source page has a `refresh_priority` (critical/normal/low) that controls which pages are checked during different refresh modes. Baselines are stored in `.content-monitor/baseline-snapshot.json`.

### Refresh Priority

Each source page is assigned a priority based on its impact on the learning experience:

- **critical** — Impacts how the learner will actually understand the content and if the content still makes sense (e.g., core feature docs like skills and MCP)
- **normal** — Updates that will not impact complete understanding but may impact breadth or accuracy (e.g., sub-agents, hooks, memory, plugins)
- **low** — Light changes that don't impact learning experience (e.g., landing pages, navigation-only pages)

The scripts support a `--priority` flag that is cumulative: `--priority critical` checks only critical pages, `--priority normal` checks critical + normal, and omitting the flag checks everything. The content-refresh skill asks which refresh mode to use at the start of each run: quick (critical only), standard (critical + normal), or full (all pages).

### Refresh Workflow

The deliverable registry (`.content-monitor/deliverable-registry.json`) maps each training PPTX to the content sections and slides that use them. It is auto-populated by generate-training (Step 7c) whenever a new deck is built. The content-refresh skill reads this registry to trace content changes through to affected deliverables and suggest slide-level updates.

The typical refresh workflow is: run **content-refresh** → select refresh mode → review and accept content diffs → review and accept deliverable slide updates. If no drift is detected, content-refresh exits early. After substantial text updates to deliverables, consider re-running **add-training-media** on affected decks to verify image-to-slide matching is still accurate.

### Rollback

The content-refresh skill creates git checkpoint commits before and after each stage, so any update can be reverted without regenerating from scratch. Commits use the prefix `content-refresh:` and follow a structured naming convention (e.g., `content-refresh: pre-stage-1 snapshot`, `content-refresh: stage-1 complete — updated N content sections`). Baseline snapshot updates are committed separately from content changes, so reverting content doesn't also revert the baseline (avoiding re-detection of the same drift). To find checkpoints: `git log --oneline --grep="content-refresh:" -10`. To revert a stage: `git revert <commit-hash>`. See the Rollback section in the content-refresh SKILL.md for detailed procedures.

## End-to-End Orchestration Guide

The skills are designed to run independently, but here's the recommended order for generating a complete training package from scratch, and for maintaining it over time.

### New Training Package (full flow)

```
1. content-chunking          Chunk source docs into tagged sections
       ↓                     (one-time per feature topic)
2. generate-training         Build text-complete PPTX from template
       ↓                     User reviews text content
3. add-training-media        Insert images + clickable video links
       ↓                     User reviews final deck
4. generate-exercises        Create hands-on exercise .docx
       ↓                     (optional — skip if no practice needed)
5. generate-facilitator-guide  Create facilitator guide .docx
                              (optional — skip if self-guided)
```

Each step produces output the next step consumes. The key handoff points are: generate-training produces a `_Sources.md` manifest that generate-exercises reads, and the training PPTX itself is the input for both add-training-media and generate-facilitator-guide.

All final deliverables go to `Deliverables/`.

### Content Maintenance (ongoing)

```
content-refresh              Select refresh mode (quick/standard/full),
                             detect drift, update content sections,
                             propagate changes to deliverables
       ↓ (if slides changed substantially)
add-training-media           Re-verify image matching on updated decks
```

Recommended cadence: quick refresh (critical only) mid-week, standard refresh (critical + normal) weekly, full refresh monthly or when structural changes are suspected.

Run content-refresh periodically (weekly recommended) or whenever upstream docs are known to have changed. If content-refresh updates slide text on a deck, consider re-running add-training-media to check whether images still match the new content.

### Quick Reference: What each skill needs

| Skill | Requires | Produces |
|-------|----------|----------|
| content-chunking | Source doc (URL/file/text) | `Content/content_<feature>/` sections + index |
| generate-training | Content sections + Profile + Template | `Training_[Feature]_[Profile].pptx` + `_Sources.md` |
| add-training-media | Training PPTX + `Imagery/` folder | Updated PPTX with media |
| generate-exercises | `_Sources.md` + Profile + Content sections | `Exercises_[Feature]_[Profile].docx` |
| generate-facilitator-guide | Training PPTX + Profile | `Facilitator_Guide_[Feature]_[Profile].docx` |
| content-refresh | Source registry + Baseline + Content sections | Updated content + updated deliverables |

## Keeping Documentation Up to Date

When you make changes to the pipeline — adding new skills, content folders, profiles, tag dimensions, imagery directories, or modifying the PPTX workflow — update the relevant documentation to match:

- **This file (CLAUDE.md)**: Update whenever the repo structure, pipeline stages, tagging system, profile list, brand specs, or editing workflow changes. This is the primary onboarding document for future Claude Code sessions, so stale information here compounds across every subsequent interaction.
- **`00_content_index.md` files**: Update when content sections are added, removed, renamed, or re-tagged within a feature folder.
- **`.content-monitor/source-registry.json`**: Update when new source URLs are chunked or existing mappings change.
- **`.content-monitor/deliverable-registry.json`**: Auto-populated by generate-training. Manually update if deliverables are renamed, moved, or deleted outside the pipeline.
- **`Tag_definitions/content-tag-definitions.md`**: Update if new tag dimensions or values are introduced.
- **TEMPLATE_GUIDE.md**: Update if the template slides, brand specs, or population rules change.

Do not let documentation drift behind the actual state of the repo. If you change something and the docs don't reflect it, fix the docs in the same session.
