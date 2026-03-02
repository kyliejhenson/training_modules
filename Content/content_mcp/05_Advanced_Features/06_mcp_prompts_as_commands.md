# Using MCP Prompts as Commands

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

MCP servers can expose prompts that become available as slash commands in Claude Code.

### Discovering and executing prompts

1. **Discover available prompts**: Type `/` to see all available commands, including those from MCP servers. MCP prompts appear with the format `/mcp__servername__promptname`.

2. **Execute a prompt without arguments**:
   ```
   > /mcp__github__list_prs
   ```

3. **Execute a prompt with arguments** (space-separated after the command):
   ```
   > /mcp__github__pr_review 456
   ```
   ```
   > /mcp__jira__create_issue "Bug in login flow" high
   ```

### Key points

- MCP prompts are dynamically discovered from connected servers.
- Arguments are parsed based on the prompt's defined parameters.
- Prompt results are injected directly into the conversation.
- Server and prompt names are normalized (spaces become underscores).
