# Skills and Subagents

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/sub-agents

---

## Content

Subagents don't automatically see your skills. When you delegate a task to a subagent, it starts with a fresh, clean context.

Important distinctions:

- Built-in agents (like Explorer, Plan, and Verify) can't access skills at all
- Custom subagents you define can use skills, but only when you explicitly list them
- Skills are loaded when the subagent starts, not on demand like in the main conversation

To create a custom subagent with skills, add an agent markdown file in `.claude/agents`. You can use the `/agents` command in Claude Code to create one interactively. The generated agent file includes a `skills` field that lists which skills to load:

```
---
name: frontend-security-accessibility-reviewer
description: "Use this agent when you need to review frontend code for accessibility..."
tools: Bash, Glob, Grep, Read, WebFetch, WebSearch, Skill...
model: sonnet
color: blue
skills: accessibility-audit, performance-check
---
```

When you delegate to this subagent, it has both skills loaded and applies them to every review. First make sure the skills exist in your `.claude/skills` directory, then either create a new subagent or add the `skills` field to an existing agent's markdown file.

This pattern works well when:

- You want isolated task delegation with specific expertise
- Different subagents need different skills (frontend reviewer vs. backend reviewer)
- You want to enforce standards in delegated work without relying on prompts
