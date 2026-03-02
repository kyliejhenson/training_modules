# What Is the Model Context Protocol

## Tags
- **Technical Skill Level**: Beginner
- **Use Case Types**: Workflow integration
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write tedious integration code. It shifts the burden of tool definitions and execution away from your server to specialized MCP servers.

The basic architecture consists of an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to some outside service.
