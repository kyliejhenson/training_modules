# The /simplify Built-in Skill

## Tags
- **Technical Skill Level**: Beginner
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Claude Code ships with `/simplify`, a built-in skill available in every session. It reviews recently changed files for code reuse, quality, and efficiency issues, then fixes them.

Run it after implementing a feature or bug fix to clean up your work. It spawns three review agents in parallel (code reuse, code quality, efficiency), aggregates their findings, and applies fixes.

Pass optional text to focus on specific concerns:

```text
/simplify focus on memory efficiency
```
