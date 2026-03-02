# Policy-Based Control with Allowlists and Denylists

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Security & compliance, Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Instead of taking exclusive control, administrators can allow users to configure their own MCP servers while enforcing restrictions on which servers are permitted. This approach uses `allowedMcpServers` and `deniedMcpServers` in the managed settings file.

### Restriction types

Each entry in the allowlist or denylist can restrict servers in three ways:

1. **By server name** (`serverName`): Matches the configured name of the server.
2. **By command** (`serverCommand`): Matches the exact command and arguments used to start stdio servers.
3. **By URL pattern** (`serverUrl`): Matches remote server URLs with wildcard support.

Each entry must have exactly one of these fields.

### Example configuration

```json
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverName": "sentry" },
    { "serverCommand": ["npx", "-y", "@modelcontextprotocol/server-filesystem"] },
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://*.internal.corp/*" }
  ],
  "deniedMcpServers": [
    { "serverName": "dangerous-server" },
    { "serverCommand": ["npx", "-y", "unapproved-package"] },
    { "serverUrl": "https://*.untrusted.com/*" }
  ]
}
```

### How matching works

- **Command matching** is exact: the command array must match both the command and all arguments in the correct order.
- **URL matching** supports wildcards (`*`) for matching paths and subdomains.
- **Denylist takes absolute precedence**: if a server matches a denylist entry, it is blocked even if it is also on the allowlist.

### Allowlist behavior

- `undefined` (default): No restrictions — users can configure any MCP server.
- Empty array `[]`: Complete lockdown — users cannot configure any MCP servers.
- List of entries: Users can only configure servers that match.

### Denylist behavior

- `undefined` (default): No servers are blocked.
- Empty array `[]`: No servers are blocked.
- List of entries: Specified servers are explicitly blocked across all scopes.
