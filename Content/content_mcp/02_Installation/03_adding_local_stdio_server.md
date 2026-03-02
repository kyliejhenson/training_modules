# Adding a Local Stdio Server

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Stdio servers run as local processes on your machine. They are ideal for tools that need direct system access or custom scripts.

### Syntax

```bash
# Basic syntax
claude mcp add [options] <name> -- <command> [args...]

# Real example: Add Airtable server
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable \
  -- npx -y airtable-mcp-server
```

### Option ordering

All options (`--transport`, `--env`, `--scope`, `--header`) must come **before** the server name. The `--` (double dash) separates the server name from the command and arguments that get passed to the MCP server.

- `claude mcp add --transport stdio myserver -- npx server` runs `npx server`
- `claude mcp add --transport stdio --env KEY=value myserver -- python server.py --port 8080` runs `python server.py --port 8080` with `KEY=value` in the environment

This syntax prevents conflicts between Claude's flags and the server's flags.
