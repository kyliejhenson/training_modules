# The /batch Built-in Skill

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Claude Code ships with `/batch`, a built-in skill available in every session that orchestrates large-scale changes across a codebase in parallel.

Provide a description of the change and `/batch` researches the codebase, decomposes the work into 5 to 30 independent units, and presents a plan for your approval. Once approved, it spawns one background agent per unit, each in an isolated git worktree. Each agent implements its unit, runs tests, and opens a pull request.

Requirements: a git repository.

Example usage:

```text
/batch migrate src/ from Solid to React
```
