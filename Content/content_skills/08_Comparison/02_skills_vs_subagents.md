# Skills vs Subagents

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/sub-agents

---

## Content

Skills add knowledge to your current conversation. When a skill activates, its instructions join the existing context.

Subagents run in a separate context. They receive a task, work on it independently, and return results. They're isolated from the main conversation.

**Use Subagents when:**

- You want to delegate a task to a separate execution context
- You need different tool access than the main conversation
- You want isolation between delegated work and your main context

**Use Skills when:**

- You want to enhance Claude's knowledge for the current task
- The expertise applies throughout a conversation
