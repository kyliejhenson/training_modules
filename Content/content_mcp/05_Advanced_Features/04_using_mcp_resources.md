# Using MCP Resources

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

MCP servers can expose resources that you can reference using `@` mentions, similar to how you reference files in Claude Code.

### Referencing resources

1. **List available resources**: Type `@` in your prompt to see available resources from all connected MCP servers. Resources appear alongside files in the autocomplete menu.

2. **Reference a specific resource** using the format `@server:protocol://resource/path`:
   ```
   > Can you analyze @github:issue://123 and suggest a fix?
   ```
   ```
   > Please review the API documentation at @docs:file://api/authentication
   ```

3. **Reference multiple resources** in a single prompt:
   ```
   > Compare @postgres:schema://users with @docs:file://database/user-model
   ```

### Key points

- Resources are automatically fetched and included as attachments when referenced.
- Resource paths are fuzzy-searchable in the `@` mention autocomplete.
- Claude Code automatically provides tools to list and read MCP resources when servers support them.
- Resources can contain any type of content the MCP server provides (text, JSON, structured data, etc.).
