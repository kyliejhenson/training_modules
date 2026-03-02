# Anthropic Training Content Pipeline

An automated pipeline that turns Anthropic documentation into branded, audience-tailored training decks — and keeps them current as upstream docs change.

## The Problem

Training content goes stale because upstream documentation changes. Manual updates don't scale across multiple audiences and features. Rewriting decks from scratch wastes effort that could be spent on delivery.

## How It Works

```
Source Docs ──► Content Chunking ──► Generate Training ──► Add Media
                  (tagged,              (audience-          (images,
                   modular)              filtered)           video links)
                                             │
                                    ┌────────┴────────┐
                                    ▼                  ▼
                              Exercises         Facilitator Guide
                               (.docx)              (.docx)

                        Content Refresh ◄── Upstream drift detection
                        (auto-detects changes, traces impact to slides)
```

The pipeline is driven by six Claude Code skills that run independently but compose into a full workflow.

## Key Design Decisions

**Modular content, not monolithic decks.** Source docs are chunked into single-concept markdown sections (108 across two features), each tagged on five dimensions: skill level, use case type, instructional priority, practice applicability, and selling relevance. This means the same source content can generate different decks for different audiences without duplication.

**Profile-based filtering.** Four audience profiles (Developers, Enterprise Champions, Solutions Engineers, Solutions Partners) define which content sections match based on tag criteria. A section only appears in a deck if its tags satisfy all of the profile's requirements.

**Drift detection with traceability.** A deliverable registry maps every slide back to its source content sections. When upstream docs change, the pipeline detects the drift, identifies affected sections, and traces impact to specific slides — presenting changes for human review before any updates are applied.

## What's In the Repo

| Directory | Purpose |
|-----------|---------|
| `Content/` | 108 tagged content sections across MCP and Skills features |
| `Profiles/` | 4 audience profile definitions with tag criteria |
| `Deliverables/` | Generated training decks, exercises, and guides |
| `Imagery/` | ~600 screenshots and illustrations for slide media |
| `.claude/skills/` | The 6 pipeline skills (chunking, generation, media, exercises, facilitation, refresh) |
| `.content-monitor/` | Drift detection infrastructure (registries, baselines, scripts) |

## Generating a Training Package

```
1. content-chunking         → Chunk source docs into tagged sections
2. generate-training        → Build text-complete PPTX for target audience
3. add-training-media       → Insert screenshots and video links
4. generate-exercises       → Create hands-on exercise document (optional)
5. generate-facilitator-guide → Create facilitator guide (optional)
```

## Maintaining Content

```
content-refresh             → Detect upstream drift, update content + slides
```

Three refresh modes: quick (critical pages only), standard (critical + normal), full (all pages). Each run creates git checkpoint commits for easy rollback.

## Built With

Claude Code skills, Python (XML manipulation, web scraping, diff generation), branded PPTX template with 25 slide layouts.
