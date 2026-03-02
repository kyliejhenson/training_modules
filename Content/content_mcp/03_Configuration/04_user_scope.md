# User Scope

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

User-scoped servers are stored in `~/.claude.json` and provide cross-project accessibility. They are available across all projects on your machine while remaining private to your user account.

This scope works well for personal utility servers, development tools, or services you frequently use across different projects.

### Example

```bash
# Add a user-scoped server
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```
