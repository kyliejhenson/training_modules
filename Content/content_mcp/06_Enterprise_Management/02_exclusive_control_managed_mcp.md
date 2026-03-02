# Exclusive Control with managed-mcp.json

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Security & compliance, Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

When you deploy a `managed-mcp.json` file, it takes exclusive control over all MCP servers. Users cannot add, modify, or use any MCP servers other than those defined in this file. This is the simplest approach for organizations that want complete control.

### File locations

System administrators deploy the configuration file to a system-wide directory:

- **macOS**: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- **Linux and WSL**: `/etc/claude-code/managed-mcp.json`
- **Windows**: `C:\Program Files\ClaudeCode\managed-mcp.json`

These are system-wide paths (not user home directories) that require administrator privileges. They are designed to be deployed by IT administrators.

### Example configuration

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.dev/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"],
      "env": {
        "COMPANY_API_URL": "https://internal.company.com"
      }
    }
  }
}
```

### Key points

- Users cannot add MCP servers through `claude mcp add` or configuration files when this file is present.
- The `allowedMcpServers` and `deniedMcpServers` settings still apply to filter which managed servers are actually loaded.
