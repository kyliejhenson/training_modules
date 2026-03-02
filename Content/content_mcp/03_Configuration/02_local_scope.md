# Local Scope

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Local-scoped servers are the default configuration level. They are stored in `~/.claude.json` under your project's path. These servers remain private to you and are only accessible when working within the current project directory.

Local scope is ideal for personal development servers, experimental configurations, or servers containing sensitive credentials that should not be shared with teammates.

### Example

```bash
# Add a local-scoped server (default)
claude mcp add --transport http stripe https://mcp.stripe.com

# Explicitly specify local scope
claude mcp add --transport http stripe --scope local https://mcp.stripe.com
```

### Note

The term "local scope" for MCP servers differs from general local settings. MCP local-scoped servers are stored in `~/.claude.json` (your home directory), while general local settings use `.claude/settings.local.json` (in the project directory).
