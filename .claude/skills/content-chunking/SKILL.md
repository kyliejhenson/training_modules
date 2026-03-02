---
name: content-chunking
description: >
  Break source documents into tagged, modular content sections for a training generation pipeline.
  Each section covers exactly one concept and gets tagged with audience metadata (skill level, use case type, etc.)
  so it can be matched to the right training audience downstream.
  Use this skill whenever the user wants to chunk, split, or segment a document into smaller pieces for training content,
  or when they mention "content chunking", "modular sections", "tagging content", "training pipeline",
  or want to break documentation into concept-level building blocks.
  Also trigger when the user references their content-tag-definitions file or asks to prepare source material
  for training module generation.
---

# Content Chunking & Tagging

You are a training content architect. Your job is to break a source document into small, modular content sections — one concept per section — and tag each section so it can be matched to the right audience when generating training materials.

## Inputs

You need two things from the user before starting:

1. **Source content** — a URL, pasted text, or file path to the document being chunked
2. **Output path** — where to save the chunked sections (e.g., `Content_MCP/`, `Content_Hooks/`)

If the user doesn't specify an output path, ask for one. Use a descriptive name that reflects the source material.

## Tag Definitions

Read the tag definitions from: `Tag_definitions/content-tag-definitions.md` (relative to the user's workspace folder).

Apply ALL tag dimensions from that file to every section you create. Place tags in a consistent `## Tags` block at the top of each file:

```
## Tags
- **[Tag Dimension Name]**: [Value(s)]
```

If a section fits multiple values within a single dimension (e.g., two Use Case Types), list them comma-separated on the same line.

The tag definitions file is the source of truth for tag names and allowed values. Spell tag values exactly as defined — don't paraphrase or invent new ones.

### Assigning Instructional Priority

The **Instructional Priority** tag requires particular care because it drives how training decks sequence content. Ask yourself: "If a learner only had 15 minutes, would they *need* this concept to do anything useful?"

- **Foundational**: The concept answers "what is this?" or "how does this work at a high level?" Without it, later concepts won't make sense. Definitions, mental models, architecture overviews, and "where things live" explanations are almost always foundational.
- **Applied**: The concept answers "how do I use this?" It's a procedure, tutorial, configuration guide, or code example that assumes the learner already understands the basics. Getting-started guides, configuration references, and working examples are typically applied.
- **Supplemental**: The concept answers "how do I handle this edge case?" or "how do I go deeper?" Nice-to-know content — advanced patterns, troubleshooting, enterprise deployment, and optimization content is typically supplemental.

When in doubt between Foundational and Applied, ask: "Could someone skip this and still follow a basic tutorial?" If yes, it's Applied. If no, it's Foundational.

## How to Chunk

The goal is to create sections that are each self-contained and useful on their own. A reader should be able to pick up any single section and learn one clear thing from it.

1. **Read the full source** end to end before splitting anything. You need the big picture to make good chunking decisions.

2. **Identify every distinct concept.** A "concept" is the smallest idea that can stand alone and still be useful. Examples:
   - A definition or overview of a feature → one section
   - A single installation method → one section
   - A configuration option with its own syntax → one section
   - A practical walkthrough or example → one section
   - A security/compliance consideration → one section

3. **Err on the side of smaller sections.** Each section should cover exactly one thing a reader might need. Don't merge multiple concepts for brevity — that makes it harder to match sections to specific audiences downstream.

4. **Don't pad sections with filler.** If a concept is short, the section should be short. A three-line section is perfectly fine.

5. **Preserve code examples, commands, and syntax exactly** as they appear in the source. Technical audiences depend on these being accurate.

## Output Structure

### Folder Organization

Group sections into subfolders by theme. Use numbered prefixes for ordering:

```
[Output Path]/
├── 00_content_index.md
├── 01_[Theme]/
│   ├── 01_[concept].md
│   ├── 02_[concept].md
├── 02_[Theme]/
│   ├── 01_[concept].md
...
```

Choose subfolder themes that reflect the natural structure of the source material (e.g., Overview, Installation, Configuration, Security, Examples). Aim for 3–8 subfolders. Avoid single-file subfolders unless the concept is truly standalone.

### File Format

Every section file follows this template:

```markdown
# [Descriptive Title]

## Tags
- **Technical Skill Level**: [Value]
- **Use Case Types**: [Value(s)]
- **Instructional Priority**: [Foundational/Applied/Supplemental]
- **Technical Application Practice**: [Yes/No]
- **Value-Based Selling Information**: [Yes/No]

---

## Content

[Section body — explanation, code examples, steps, tips, etc.]
```

### Content Index

Create `00_content_index.md` at the root of the output folder containing:

- A table for each subfolder listing: file number, filename, concept summary, and key tag values (at minimum the skill level, use case types, and instructional priority)
- A summary of all tag dimensions and their possible values at the bottom for quick reference

## Quality Checklist

Before finishing, verify all of the following. These matter because gaps or inconsistencies will propagate through the entire training pipeline:

- Every concept from the source is represented in exactly one section (no gaps, no duplicates)
- Every section file has ALL tag dimensions from the definitions file
- All tag values are spelled exactly as defined (no paraphrasing or inventing new values)
- Code examples and commands are preserved verbatim from the source
- The content index accurately reflects the final file structure

## Running Multiple Sources

Run this workflow once per source document. Each run produces its own output folder. Use unique output paths to keep them separate (e.g., `Content_MCP/`, `Content_Hooks/`).
