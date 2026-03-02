# Windows-Specific MCP Setup

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

On native Windows (not WSL), local MCP servers that use `npx` require the `cmd /c` wrapper to ensure proper execution.

### Example

```bash
# This creates command="cmd" which Windows can execute
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

Without the `cmd /c` wrapper, you will encounter "Connection closed" errors because Windows cannot directly execute `npx`.

This does not apply when using Windows Subsystem for Linux (WSL), where standard Unix-style commands work as expected.
