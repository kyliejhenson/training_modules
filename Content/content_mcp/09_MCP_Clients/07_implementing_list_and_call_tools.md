# Implementing list_tools and call_tool

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

The two essential client functions are `list_tools()` and `call_tool()`.

**List Tools Function**

Gets all available tools from the MCP server:

```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

Access your session (the connection to the server), call the built-in `list_tools()` method, and return the tools from the result.

**Call Tool Function**

Executes a specific tool on the server:

```python
async def call_tool(
    self,
    tool_name: str,
    tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

Pass the tool name and input parameters (provided by Claude) to the server and return the result.

**Testing the Client**

Run the client file directly to verify everything works:

```bash
uv run mcp_client.py
```

This will connect to your MCP server and print out the available tools, including descriptions and input schemas.
