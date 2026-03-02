# The MCP Prompt Workflow

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

The complete prompt workflow:

1. Write and evaluate a prompt relevant to your server's functionality
2. Define the prompt in your MCP server using the `@mcp.prompt` decorator
3. Clients can request the prompt at any time
4. Arguments provided by the client become keyword arguments in your prompt function
5. The function returns formatted messages ready for the AI model

In the CLI, when you type a slash (`/`), available prompts appear as commands. Selecting a prompt like "format" will prompt you to choose from available documents. After selecting a document, the system sends the complete prompt to Claude. The AI receives both the formatting instructions and the document ID, then uses available tools to fetch and process the content.

This system creates reusable, parameterized prompts that maintain consistency while allowing customization through variables.
