# Adding MCP Servers from JSON Configuration

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

If you have a JSON configuration for an MCP server, you can add it directly using the `claude mcp add-json` command.

### Syntax and examples

```bash
# Basic syntax
claude mcp add-json <name> '<json>'

# HTTP server with JSON configuration
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'

# Stdio server with JSON configuration
claude mcp add-json local-weather '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'

# HTTP server with pre-configured OAuth credentials
claude mcp add-json my-server '{"type":"http","url":"https://mcp.example.com/mcp","oauth":{"clientId":"your-client-id","callbackPort":8080}}' --client-secret
```

### Verifying

```bash
claude mcp get weather-api
```

### Tips

- Make sure the JSON is properly escaped in your shell.
- The JSON must conform to the MCP server configuration schema.
- You can use `--scope user` to add the server to your user configuration instead of a project-specific one.
