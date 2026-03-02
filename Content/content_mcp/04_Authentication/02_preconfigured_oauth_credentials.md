# Pre-Configured OAuth Credentials

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation, Security & compliance
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Some MCP servers do not support automatic OAuth setup. If you see an error like "Incompatible auth server: does not support dynamic client registration," the server requires pre-configured credentials. You must register an OAuth app through the server's developer portal first, then provide the credentials when adding the server.

### Steps

1. **Register an OAuth app** with the server through its developer portal. Note your client ID and client secret. If required, register a redirect URI in the format `http://localhost:PORT/callback`.

2. **Add the server with your credentials** using one of these methods:

   **Using `claude mcp add`:**
   ```bash
   claude mcp add --transport http \
     --client-id your-client-id --client-secret --callback-port 8080 \
     my-server https://mcp.example.com/mcp
   ```

   **Using `claude mcp add-json`:**
   ```bash
   claude mcp add-json my-server \
     '{"type":"http","url":"https://mcp.example.com/mcp","oauth":{"clientId":"your-client-id","callbackPort":8080}}' \
     --client-secret
   ```

   **In CI / via environment variable:**
   ```bash
   MCP_CLIENT_SECRET=your-secret claude mcp add --transport http \
     --client-id your-client-id --client-secret --callback-port 8080 \
     my-server https://mcp.example.com/mcp
   ```

3. **Authenticate in Claude Code** by running `/mcp` and following the browser login flow.

### Key points

- The client secret is stored securely in your system keychain (macOS) or a credentials file, not in your config.
- If the server uses a public OAuth client with no secret, use only `--client-id` without `--client-secret`.
- These flags only apply to HTTP and SSE transports; they have no effect on stdio servers.
- Use `claude mcp get <name>` to verify that OAuth credentials are configured.
