# Managing MCP Servers

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Once MCP servers are configured, you can manage them using built-in CLI commands.

### Commands

```bash
# List all configured servers
claude mcp list

# Get details for a specific server
claude mcp get github

# Remove a server
claude mcp remove github

# (within Claude Code) Check server status
/mcp
```

### Tips

- Use the `--scope` flag to specify where the configuration is stored:
  - `local` (default): Available only to you in the current project.
  - `project`: Shared with everyone in the project via `.mcp.json`.
  - `user`: Available to you across all projects.
- Set environment variables with `--env` flags (e.g., `--env KEY=value`).
- Configure MCP server startup timeout using the `MCP_TIMEOUT` environment variable (e.g., `MCP_TIMEOUT=10000 claude` sets a 10-second timeout).
- Claude Code will display a warning when MCP tool output exceeds 10,000 tokens. To increase this limit, set `MAX_MCP_OUTPUT_TOKENS` (e.g., `MAX_MCP_OUTPUT_TOKENS=50000`).
- Use `/mcp` to authenticate with remote servers that require OAuth 2.0 authentication.
