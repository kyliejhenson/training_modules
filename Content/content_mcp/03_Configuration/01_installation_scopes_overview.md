# MCP Installation Scopes Overview

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

MCP servers can be configured at three different scope levels, each serving distinct purposes for managing server accessibility and sharing:

- **Local scope**: Servers are private to you and only accessible in the current project. This is the default.
- **Project scope**: Servers are shared with everyone in the project via a `.mcp.json` file checked into version control.
- **User scope**: Servers are available to you across all projects on your machine, but remain private to your account.

Understanding these scopes helps you determine the best way to configure servers depending on whether you need personal, team-shared, or cross-project access.

### Where are MCP servers stored?

- **User and local scope**: `~/.claude.json` (in the `mcpServers` field or under project paths)
- **Project scope**: `.mcp.json` in your project root (checked into source control)
- **Managed**: `managed-mcp.json` in system directories (see Managed MCP Configuration section)
