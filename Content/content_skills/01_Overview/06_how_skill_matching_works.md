# How Skill Matching Works

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

When Claude Code starts, it scans four locations for skills but only loads the **name and description** — not the full content. This keeps context efficient.

When you send a request, Claude compares your message against the descriptions of all available skills. Claude uses semantic matching — your request needs to overlap with the description's meaning. For example, "explain what this function does" would match a skill described as "explain code with visual diagrams" because the intent overlaps.

Once a match is found, Claude asks you to confirm loading the skill. This confirmation step keeps you aware of what context Claude is pulling in. After you confirm, Claude reads the complete `SKILL.md` file and follows its instructions.
