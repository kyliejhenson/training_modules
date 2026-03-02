# MCP Client Architecture

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

In most real-world projects, you'll either implement an MCP client or an MCP server — not both.

The MCP client consists of two main components:

- **MCP Client** — A custom class you create to make using the session easier
- **Client Session** — The actual connection to the server (part of the MCP Python SDK)

The client session requires careful resource management — you need to properly clean up connections when done. That's why you wrap it in your own class that handles all the cleanup automatically.

The client enables your code to interact with the MCP server at two key points:
- Get a list of available tools to send to Claude
- Execute tools when Claude requests them
