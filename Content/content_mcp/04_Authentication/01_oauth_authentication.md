# Authenticating with Remote MCP Servers (OAuth 2.0)

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Security & compliance
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections.

### Steps

1. **Add the server** that requires authentication:
   ```bash
   claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
   ```

2. **Authenticate using the `/mcp` command** within Claude Code:
   ```
   > /mcp
   ```
   Follow the steps in your browser to log in.

### Tips

- Authentication tokens are stored securely and refreshed automatically.
- Use "Clear authentication" in the `/mcp` menu to revoke access.
- If your browser doesn't open automatically, copy the provided URL and open it manually.
- If the browser redirect fails with a connection error after authenticating, paste the full callback URL from your browser's address bar into the URL prompt that appears in Claude Code.
- OAuth authentication works with HTTP servers.
