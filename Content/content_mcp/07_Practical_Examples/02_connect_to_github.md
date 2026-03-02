# Practical Example: Connect to GitHub for Code Reviews

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration, Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

This example walks through connecting Claude Code to GitHub for pull request management and code reviews.

### Setup

```bash
# 1. Add the GitHub MCP server
claude mcp add --transport http github https://api.githubcopilot.com/mcp/

# 2. In Claude Code, authenticate if needed
> /mcp
# Select "Authenticate" for GitHub
```

### Example prompts

Once connected, you can ask Claude Code:

- "Review PR #456 and suggest improvements"
- "Create a new issue for the bug we just found"
- "Show me all open PRs assigned to me"
