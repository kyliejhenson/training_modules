# Testing the Complete Client-Server Flow

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Once the client functions are implemented, test the complete flow by running the main application:

```bash
uv run main.py
```

Try asking: "What is the contents of the report.pdf document?" Here's what happens behind the scenes:

1. Your application uses the client to get available tools
2. These tools are sent to Claude along with your question
3. Claude decides to use the `read_doc_contents` tool
4. Your application uses the client to execute that tool
5. The result is returned to Claude, who then responds to you

The client acts as the bridge between your application logic and the MCP server's functionality, making it easy to integrate powerful tools into your AI workflows.
