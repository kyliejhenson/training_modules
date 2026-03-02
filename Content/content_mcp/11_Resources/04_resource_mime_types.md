# Resource MIME Types and Serialization

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Resources can return any type of data — strings, JSON, binary data, etc. Use the `mime_type` parameter to give clients a hint about what kind of data you're returning:

- `"application/json"` for structured data
- `"text/plain"` for plain text
- `"application/pdf"` for binary files

The MCP Python SDK automatically serializes your return values. You don't need to manually convert objects to JSON strings — just return the data structure and let the SDK handle serialization.
