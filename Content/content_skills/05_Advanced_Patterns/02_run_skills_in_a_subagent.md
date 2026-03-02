# Run Skills in a Subagent

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/sub-agents

---

## Content

Add `context: fork` to your frontmatter when you want a skill to run in isolation. The skill content becomes the prompt that drives the subagent. It won't have access to your conversation history.

Important: `context: fork` only makes sense for skills with explicit instructions. If your skill contains guidelines like "use these API conventions" without a task, the subagent receives the guidelines but no actionable prompt, and returns without meaningful output.

Skills and subagents work together in two directions:

| Approach                     | System prompt                             | Task                        | Also loads                   |
| :--------------------------- | :---------------------------------------- | :-------------------------- | :--------------------------- |
| Skill with `context: fork`   | From agent type (`Explore`, `Plan`, etc.) | SKILL.md content            | CLAUDE.md                    |
| Subagent with `skills` field | Subagent's markdown body                  | Claude's delegation message | Preloaded skills + CLAUDE.md |

With `context: fork`, you write the task in your skill and pick an agent type to execute it. For the inverse (defining a custom subagent that uses skills as reference material), see the Subagents documentation.

### Example: Research skill using Explore agent

This skill runs research in a forked Explore agent. The skill content becomes the task, and the agent provides read-only tools optimized for codebase exploration:

```yaml
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:

1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file references
```

When this skill runs:

1. A new isolated context is created
2. The subagent receives the skill content as its prompt ("Research $ARGUMENTS thoroughly...")
3. The `agent` field determines the execution environment (model, tools, and permissions)
4. Results are summarized and returned to your main conversation

The `agent` field specifies which subagent configuration to use. Options include built-in agents (`Explore`, `Plan`, `general-purpose`) or any custom subagent from `.claude/agents/`. If omitted, uses `general-purpose`.
