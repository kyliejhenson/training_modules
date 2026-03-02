# Using Claude Code as an MCP Server

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

You can use Claude Code itself as an MCP server that other applications can connect to. This lets applications like Claude Desktop access Claude Code's tools (View, Edit, LS, etc.).

### Starting the server

```bash
claude mcp serve
```

### Connecting from Claude Desktop

Add this configuration to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

### Configuring the executable path

The `command` field must reference the Claude Code executable. If `claude` is not in your system's PATH, specify the full path:

```bash
which claude
```

Then use the full path:

```json
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "/full/path/to/claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

Without the correct path, you will encounter `spawn claude ENOENT` errors.

### Key points

- The server provides access to Claude's tools like View, Edit, LS, etc.
- In Claude Desktop, you can ask Claude to read files, make edits, and more.
- This MCP server only exposes Claude Code's tools to the MCP client. Your client is responsible for implementing user confirmation for individual tool calls.
