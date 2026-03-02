# The MCP Server Inspector

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Evaluation & testing
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time, without connecting to a full application.

### Starting the Inspector

```bash
mcp dev mcp_server.py
```

This starts a development server and gives you a local URL (typically `http://127.0.0.1:6274`). Open this URL in your browser to access the MCP Inspector.

### Using the Inspector

Key elements in the interface:

- A **Connect** button to start your MCP server
- Navigation tabs for Resources, Tools, Prompts, and other features
- A tools listing and testing panel

Click **Connect** first to initialize your server.

### Testing Tools

Navigate to the **Tools** section and click "List Tools" to see all available tools. When you select a tool, the right panel shows its details and input fields.

For example, to test a document reading tool:
1. Select the `read_doc_contents` tool
2. Enter a document ID (like "deposition.md")
3. Click "Run Tool"
4. Check the results for success and expected output

You can test multiple tools in sequence to verify complex workflows. The inspector maintains your server state between tool calls, so edits persist.
