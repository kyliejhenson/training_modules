# Testing Resources with the Inspector

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Evaluation & testing
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

You can test resources using the MCP Inspector. Start your server with:

```bash
uv run mcp dev mcp_server.py
```

Then connect to the inspector in your browser. You'll see two sections:

- **Resources** — Lists your direct/static resources
- **Resource Templates** — Lists your templated resources

Click on any resource to test it. For templated resources, you'll need to provide values for the parameters. The inspector shows you the exact response structure your client will receive, including the MIME type and serialized data.
