# Using MCP Servers from Claude.ai

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

If you have logged into Claude Code with a Claude.ai account, MCP servers you have added in Claude.ai are automatically available in Claude Code.

### Steps

1. Configure MCP servers in Claude.ai at `claude.ai/settings/connectors`. On Team and Enterprise plans, only admins can add servers.
2. Complete any required authentication steps in Claude.ai.
3. View and manage servers in Claude Code:
   ```
   # Within Claude Code, see all MCP servers including Claude.ai ones
   > /mcp
   ```
   Claude.ai servers appear in the list with indicators showing they come from Claude.ai.

### Disabling Claude.ai MCP servers

To disable Claude.ai MCP servers in Claude Code, set the `ENABLE_CLAUDEAI_MCP_SERVERS` environment variable to `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```
