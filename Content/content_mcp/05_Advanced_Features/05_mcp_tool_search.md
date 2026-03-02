# MCP Tool Search

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

When you have many MCP servers configured, tool definitions can consume a significant portion of your context window. MCP Tool Search solves this by dynamically loading tools on-demand instead of preloading all of them.

### How it works

Claude Code automatically enables Tool Search when your MCP tool descriptions would consume more than 10% of the context window. When triggered:

1. MCP tools are deferred rather than loaded into context upfront.
2. Claude uses a search tool to discover relevant MCP tools when needed.
3. Only the tools Claude actually needs are loaded into context.
4. MCP tools continue to work exactly as before from your perspective.

### Configuration

Control tool search behavior with the `ENABLE_TOOL_SEARCH` environment variable:

| Value        | Behavior                                                    |
|-------------|-------------------------------------------------------------|
| `auto`      | Activates when MCP tools exceed 10% of context (default)    |
| `auto:<N>`  | Activates at custom threshold (e.g., `auto:5` for 5%)       |
| `true`      | Always enabled                                              |
| `false`     | Disabled; all MCP tools loaded upfront                      |

```bash
# Use a custom 5% threshold
ENABLE_TOOL_SEARCH=auto:5 claude

# Disable tool search entirely
ENABLE_TOOL_SEARCH=false claude
```

You can also disable it via the `disallowedTools` setting:

```json
{
  "permissions": {
    "deny": ["MCPSearch"]
  }
}
```

### Model requirements

This feature requires models that support `tool_reference` blocks: Sonnet 4 and later, or Opus 4 and later. Haiku models do not support tool search.

### For MCP server authors

If you are building an MCP server, add clear, descriptive server instructions that explain what category of tasks your tools handle, when Claude should search for them, and the key capabilities your server provides.
