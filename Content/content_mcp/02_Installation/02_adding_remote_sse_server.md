# Adding a Remote SSE Server

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

SSE (Server-Sent Events) is a legacy transport type that some MCP servers still use. Where available, HTTP servers should be used instead, as SSE is deprecated.

### Syntax

```bash
# Basic syntax
claude mcp add --transport sse <name> <url>

# Real example: Connect to Asana
claude mcp add --transport sse asana https://mcp.asana.com/sse

# Example with authentication header
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key-here"
```

### Key points

- SSE transport is deprecated. Use HTTP servers instead where available.
- Authentication headers can be passed with the `--header` flag, the same as HTTP servers.
