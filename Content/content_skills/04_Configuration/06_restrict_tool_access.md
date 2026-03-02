# Restrict Tool Access

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation, Security & compliance
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Use the `allowed-tools` field in frontmatter to limit which tools Claude can use when a skill is active. This lets you create constrained environments, such as a read-only mode where Claude can explore files but not modify them:

```yaml
---
name: safe-reader
description: Read files without making changes
allowed-tools: Read, Grep, Glob
---
```

When `allowed-tools` is set, Claude can only use the listed tools without asking for additional permission while that skill is active.
