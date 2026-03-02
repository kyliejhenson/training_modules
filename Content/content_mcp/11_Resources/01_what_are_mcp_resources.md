# What Are MCP Resources

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

Resources follow a request-response pattern. When your client needs data, it sends a `ReadResourceRequest` with a URI to identify which resource it wants. The MCP server processes this request and returns the data in a `ReadResourceResult`.

For example, a document mention feature where users type `@document_name` to reference files requires:

1. Getting a list of all available documents (for autocomplete)
2. Fetching the contents of a specific document (when mentioned)

When a user mentions a document, your system automatically injects the document's contents into the prompt sent to Claude, eliminating the need for Claude to use tools to fetch the information.
