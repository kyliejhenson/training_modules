# String Substitutions in Skills

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Skills support string substitution for dynamic values in the skill content:

| Variable               | Description                                                                                                                                  |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| `$ARGUMENTS`           | All arguments passed when invoking the skill. If `$ARGUMENTS` is not present in the content, arguments are appended as `ARGUMENTS: <value>`. |
| `$ARGUMENTS[N]`        | Access a specific argument by 0-based index, such as `$ARGUMENTS[0]` for the first argument.                                                 |
| `$N`                   | Shorthand for `$ARGUMENTS[N]`, such as `$0` for the first argument or `$1` for the second.                                                   |
| `${CLAUDE_SESSION_ID}` | The current session ID. Useful for logging, creating session-specific files, or correlating skill output with sessions.                      |

Example using substitutions:

```yaml
---
name: session-logger
description: Log activity for this session
---

Log the following to logs/${CLAUDE_SESSION_ID}.log:

$ARGUMENTS
```
