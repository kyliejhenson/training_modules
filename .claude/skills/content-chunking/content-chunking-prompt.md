# Content Chunking & Tagging Prompt

Use this prompt to break source content into tagged, modular sections for the training generation pipeline. Replace the placeholder values in `[brackets]` before running.

---

## Prompt

```
You are a training content architect. Your job is to break a single source document into small, modular content sections — one concept per section — and tag each section so it can be matched to the right audience when auto-generating training materials.

## Source content

[INSERT SOURCE — a URL, pasted text, or file path]

## Tag definitions

Read the tag definitions from: [PATH TO content-tag-definitions.md]

Apply ALL tag dimensions from that file to every section you create. Place tags in a consistent "## Tags" block at the top of each file using this format:

## Tags
- **[Tag Dimension Name]**: [Value(s)]

If a section fits multiple values within a single dimension (e.g., two Use Case Types), list them comma-separated on the same line.

## How to chunk

1. Read the full source content end to end before splitting anything.
2. Identify every distinct concept. A "concept" is the smallest idea that can stand alone and still be useful to a reader. Examples:
   - A definition or overview of a feature → one section
   - A single installation method → one section
   - A configuration option with its own syntax → one section
   - A practical walkthrough or example → one section
   - A security/compliance consideration → one section
3. Do NOT merge multiple concepts into one section for brevity. Err on the side of smaller sections. A section should cover exactly one thing a reader might need.
4. Do NOT pad sections with filler. If a concept is short, the section should be short.
5. Preserve code examples, commands, and syntax exactly as they appear in the source. These are critical for technical audiences.

## Output structure

Save all output to: [OUTPUT PATH, e.g., /path/to/Content/]

### Folder organization

Group sections into subfolders by theme. Use numbered prefixes for ordering:

```
Content/
├── 00_content_index.md
├── 01_[Theme]/
│   ├── 01_[concept].md
│   ├── 02_[concept].md
├── 02_[Theme]/
│   ├── 01_[concept].md
...
```

Choose subfolder themes that reflect the natural structure of the source material (e.g., Overview, Installation, Configuration, Security, Examples). Aim for 3–8 subfolders. Avoid single-file subfolders unless the concept is truly standalone.

### File format

Every section file must follow this template:

```markdown
# [Descriptive Title]

## Tags
- **[Dimension 1]**: [Value]
- **[Dimension 2]**: [Value(s)]
- **[Dimension 3]**: [Value]
- **[Dimension 4]**: [Value]

---

## Content

[Section body — explanation, code examples, steps, tips, etc.]
```

### Content index

Create a `00_content_index.md` at the root of the output folder. It should contain:

- A table for each subfolder listing: file number, filename, concept summary, and key tag values (at minimum the skill level and use case types).
- A summary of all tag dimensions and their possible values at the bottom for quick reference.

## Quality checklist

Before finishing, verify:
- [ ] Every concept from the source is represented in exactly one section (no gaps, no duplicates).
- [ ] Every section file has ALL tag dimensions from the definitions file.
- [ ] All tag values are spelled exactly as defined (no paraphrasing or inventing new values).
- [ ] Code examples and commands are preserved verbatim from the source.
- [ ] The content index accurately reflects the final file structure.
```

---

## Usage notes

- **Swap the source**: Replace the source content placeholder with a URL, a file path, or pasted text. The prompt works with any format.
- **Swap the tag definitions**: Point to your current `content-tag-definitions.md`. If the tag dimensions change over time, the prompt adapts automatically since it reads from the file rather than hardcoding values.
- **Swap the output path**: Direct output wherever it belongs in your pipeline.
- **Multiple sources**: Run the prompt once per source document. Each run produces its own `Content/` folder. To distinguish them, use unique output paths (e.g., `Content_MCP/`, `Content_Hooks/`).
