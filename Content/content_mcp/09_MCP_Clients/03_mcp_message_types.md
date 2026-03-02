# MCP Message Types

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:

- **ListToolsRequest / ListToolsResult:** The client asks the server "what tools do you provide?" and gets back a list of available tools.
- **CallToolRequest / CallToolResult:** The client asks the server to run a specific tool with given arguments, then receives the results.
