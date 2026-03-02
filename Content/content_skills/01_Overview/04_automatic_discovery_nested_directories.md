# Automatic Discovery from Nested Directories

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

When you work with files in subdirectories, Claude Code automatically discovers skills from nested `.claude/skills/` directories. For example, if you're editing a file in `packages/frontend/`, Claude Code also looks for skills in `packages/frontend/.claude/skills/`. This supports monorepo setups where packages have their own skills.

Skills defined in `.claude/skills/` within directories added via `--add-dir` are loaded automatically and picked up by live change detection, so you can edit them during a session without restarting.

Note: CLAUDE.md files from `--add-dir` directories are not loaded by default. To load them, set `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`.
