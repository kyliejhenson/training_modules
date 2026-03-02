# What Are Skills

## Tags
- **Technical Skill Level**: Beginner
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Skills extend what Claude can do in Claude Code. A skill is created by writing a `SKILL.md` file with instructions, which Claude then adds to its toolkit. Claude uses skills when they are relevant to the current task, or users can invoke one directly with `/skill-name`.

Skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control, subagent execution, and dynamic context injection.

Custom slash commands have been merged into skills. A file at `.claude/commands/review.md` and a skill at `.claude/skills/review/SKILL.md` both create `/review` and work the same way. Existing `.claude/commands/` files continue to work. Skills add optional features: a directory for supporting files, frontmatter to control whether the user or Claude invokes them, and the ability for Claude to load them automatically when relevant.
