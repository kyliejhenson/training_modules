# Where Skills Live

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Where a skill is stored determines who can use it. Skills can be placed at four levels:

| Location   | Path                                                | Applies to                     |
| :--------- | :-------------------------------------------------- | :----------------------------- |
| Enterprise | See managed settings documentation                  | All users in your organization |
| Personal   | `~/.claude/skills/<skill-name>/SKILL.md`            | All your projects              |
| Project    | `.claude/skills/<skill-name>/SKILL.md`              | This project only              |
| Plugin     | `<plugin>/skills/<skill-name>/SKILL.md`             | Where plugin is enabled        |

When skills share the same name across levels, higher-priority locations win: enterprise > personal > project. Plugin skills use a `plugin-name:skill-name` namespace, so they cannot conflict with other levels. If you have files in `.claude/commands/`, those work the same way, but if a skill and a command share the same name, the skill takes precedence.
