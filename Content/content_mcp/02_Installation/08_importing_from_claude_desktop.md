# Importing MCP Servers from Claude Desktop

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

If you have already configured MCP servers in Claude Desktop, you can import them into Claude Code rather than reconfiguring each one manually.

### Steps

1. Run the import command:
   ```bash
   claude mcp add-from-claude-desktop
   ```
2. An interactive dialog will appear allowing you to select which servers to import.
3. Verify the imports:
   ```bash
   claude mcp list
   ```

### Key points

- This feature works only on macOS and Windows Subsystem for Linux (WSL).
- It reads the Claude Desktop configuration file from its standard location.
- Use the `--scope user` flag to add servers to your user configuration.
- Imported servers retain the same names as in Claude Desktop.
- If servers with the same name already exist, they receive a numerical suffix (e.g., `server_1`).
