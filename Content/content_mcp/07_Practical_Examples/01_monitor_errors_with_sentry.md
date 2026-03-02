# Practical Example: Monitor Errors with Sentry

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration, Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

This example walks through connecting Claude Code to Sentry for production error monitoring.

### Setup

```bash
# 1. Add the Sentry MCP server
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# 2. Use /mcp to authenticate with your Sentry account
> /mcp
```

### Example prompts

Once connected, you can ask Claude Code:

- "What are the most common errors in the last 24 hours?"
- "Show me the stack trace for error ID abc123"
- "Which deployment introduced these new errors?"
