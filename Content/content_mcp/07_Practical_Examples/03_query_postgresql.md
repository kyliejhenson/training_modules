# Practical Example: Query Your PostgreSQL Database

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration, Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

This example walks through connecting Claude Code to a PostgreSQL database for natural-language querying.

### Setup

```bash
# 1. Add the database server with your connection string
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub \
  --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"
```

### Example prompts

Once connected, you can ask Claude Code:

- "What's our total revenue this month?"
- "Show me the schema for the orders table"
- "Find customers who haven't made a purchase in 90 days"
