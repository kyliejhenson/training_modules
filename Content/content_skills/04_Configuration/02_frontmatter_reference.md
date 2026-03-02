# Frontmatter Reference

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Skill behavior is configured using YAML frontmatter fields between `---` markers at the top of the `SKILL.md` file:

```yaml
---
name: my-skill
description: What this skill does
disable-model-invocation: true
allowed-tools: Read, Grep
---

Your skill instructions here...
```

All fields are optional. Only `description` is recommended so Claude knows when to use the skill.

| Field                      | Required    | Description                                                                                                                                           |
| :------------------------- | :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                     | No          | Display name for the skill. If omitted, uses the directory name. Lowercase letters, numbers, and hyphens only (max 64 characters).                    |
| `description`              | Recommended | What the skill does and when to use it. Claude uses this to decide when to apply the skill. If omitted, uses the first paragraph of markdown content. |
| `argument-hint`            | No          | Hint shown during autocomplete to indicate expected arguments. Example: `[issue-number]` or `[filename] [format]`.                                    |
| `disable-model-invocation` | No          | Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`. Default: `false`. |
| `user-invocable`           | No          | Set to `false` to hide from the `/` menu. Use for background knowledge users shouldn't invoke directly. Default: `true`.                              |
| `allowed-tools`            | No          | Tools Claude can use without asking permission when this skill is active.                                                                             |
| `model`                    | No          | Model to use when this skill is active.                                                                                                               |
| `context`                  | No          | Set to `fork` to run in a forked subagent context.                                                                                                    |
| `agent`                    | No          | Which subagent type to use when `context: fork` is set.                                                                                               |
| `hooks`                    | No          | Hooks scoped to this skill's lifecycle.                                                                                                               |
