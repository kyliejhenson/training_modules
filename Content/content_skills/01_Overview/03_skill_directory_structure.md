# Skill Directory Structure

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Each skill is a directory with `SKILL.md` as the entrypoint. The directory can contain additional supporting files:

```text
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md      # Example output showing expected format
└── scripts/
    └── validate.sh    # Script Claude can execute
```

The `SKILL.md` contains the main instructions and is required. Other files are optional and let you build more powerful skills: templates for Claude to fill in, example outputs showing the expected format, scripts Claude can execute, or detailed reference documentation. Reference these files from your `SKILL.md` so Claude knows what they contain and when to load them.
