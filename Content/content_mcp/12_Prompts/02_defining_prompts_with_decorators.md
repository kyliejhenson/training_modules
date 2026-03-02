# Defining Prompts with Decorators

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Prompts use a similar decorator pattern to tools and resources:

```python
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.
The id of the document you need to reformat is:
<document_id>
{doc_id}
</document_id>
Add in headers, bullet points, tables, etc as necessary.
Feel free to add in structure.
Use the 'edit_document' tool to edit the document.
After the document has been reformatted...
"""
    return [
        base.UserMessage(prompt)
    ]
```

The function returns a list of messages that get sent directly to Claude. You can include multiple user and assistant messages to create more complex conversation flows.

Use the MCP Inspector to test your prompts before deploying them. The inspector shows you exactly what messages will be sent to Claude, including how variables get interpolated into your prompt template.
