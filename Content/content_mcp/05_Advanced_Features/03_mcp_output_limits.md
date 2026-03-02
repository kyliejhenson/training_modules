# MCP Output Limits and Warnings

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

When MCP tools produce large outputs, Claude Code helps manage token usage to prevent overwhelming your conversation context.

### Default behavior

- **Output warning threshold**: Claude Code displays a warning when any MCP tool output exceeds 10,000 tokens.
- **Default limit**: The default maximum is 25,000 tokens.

### Adjusting the limit

Use the `MAX_MCP_OUTPUT_TOKENS` environment variable:

```bash
export MAX_MCP_OUTPUT_TOKENS=50000
claude
```

### When to increase the limit

This is particularly useful when working with MCP servers that:

- Query large datasets or databases
- Generate detailed reports or documentation
- Process extensive log files or debugging information

If you frequently encounter output warnings with specific MCP servers, consider increasing the limit or configuring the server to paginate or filter its responses.
