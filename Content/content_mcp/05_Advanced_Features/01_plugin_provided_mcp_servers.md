# Plugin-Provided MCP Servers

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Plugins can bundle MCP servers, automatically providing tools and integrations when the plugin is enabled. Plugin MCP servers work identically to user-configured servers.

### How plugin MCP servers work

- Plugins define MCP servers in `.mcp.json` at the plugin root or inline in `plugin.json`.
- When a plugin is enabled, its MCP servers start automatically.
- Plugin MCP tools appear alongside manually configured MCP tools.
- Plugin servers are managed through plugin installation, not `/mcp` commands.

### Example configurations

In `.mcp.json` at plugin root:

```json
{
  "database-tools": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "DB_URL": "${DB_URL}"
    }
  }
}
```

Or inline in `plugin.json`:

```json
{
  "name": "my-plugin",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
      "args": ["--port", "8080"]
    }
  }
}
```

### Key features

- **Automatic lifecycle**: Servers start when the plugin is enabled, but you must restart Claude Code to apply MCP server changes.
- **Environment variables**: Use `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths.
- **Multiple transport types**: Supports stdio, SSE, and HTTP transports.
- **Bundled distribution**: Tools and servers packaged together for consistent team setups.
