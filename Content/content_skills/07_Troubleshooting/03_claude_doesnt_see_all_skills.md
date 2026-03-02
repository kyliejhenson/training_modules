# Claude Doesn't See All Skills

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Skill descriptions are loaded into context so Claude knows what's available. If you have many skills, they may exceed the character budget. The budget scales dynamically at 2% of the context window, with a fallback of 16,000 characters.

Run `/context` to check for a warning about excluded skills.

To override the limit, set the `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable to a higher value.
