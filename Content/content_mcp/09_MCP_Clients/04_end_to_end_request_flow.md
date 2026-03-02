# End-to-End MCP Request Flow

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Here's how a user query flows through the entire system when a user asks "What repositories do I have?":

1. **User Query:** The user submits their question to your server
2. **Tool Discovery:** Your server needs to know what tools are available to send to Claude
3. **List Tools Exchange:** Your server asks the MCP client for available tools
4. **MCP Communication:** The MCP client sends a `ListToolsRequest` to the MCP server and receives a `ListToolsResult`
5. **Claude Request:** Your server sends the user's query plus the available tools to Claude
6. **Tool Use Decision:** Claude decides it needs to call a tool to answer the question
7. **Tool Execution Request:** Your server asks the MCP client to run the tool Claude specified
8. **External API Call:** The MCP client sends a `CallToolRequest` to the MCP server, which makes the actual API call
9. **Results Flow Back:** The external service responds with data, which flows back through the MCP server as a `CallToolResult`
10. **Tool Result to Claude:** Your server sends the tool results back to Claude
11. **Final Response:** Claude formulates a final answer using the data
12. **User Gets Answer:** Your server delivers Claude's response back to the user

Each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on your application logic.
