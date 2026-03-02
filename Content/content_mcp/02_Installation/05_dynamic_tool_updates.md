# Dynamic Tool Updates

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Claude Code supports MCP `list_changed` notifications, which allow MCP servers to dynamically update their available tools, prompts, and resources without requiring you to disconnect and reconnect.

When an MCP server sends a `list_changed` notification, Claude Code automatically refreshes the available capabilities from that server. This means that if a server adds, removes, or modifies its tools while you are connected, the changes will appear in Claude Code without any manual intervention.
