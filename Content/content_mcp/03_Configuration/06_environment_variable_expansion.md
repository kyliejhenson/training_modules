# Environment Variable Expansion in .mcp.json

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation, Security & compliance
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Claude Code supports environment variable expansion in `.mcp.json` files, allowing teams to share configurations while keeping machine-specific paths and sensitive values like API keys out of version control.

### Supported syntax

- `${VAR}` — Expands to the value of environment variable `VAR`.
- `${VAR:-default}` — Expands to `VAR` if set; otherwise uses `default`.

### Where expansion works

Environment variables can be expanded in:

- `command` — The server executable path
- `args` — Command-line arguments
- `env` — Environment variables passed to the server
- `url` — For HTTP server types
- `headers` — For HTTP server authentication

### Example

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

If a required environment variable is not set and has no default value, Claude Code will fail to parse the configuration.
