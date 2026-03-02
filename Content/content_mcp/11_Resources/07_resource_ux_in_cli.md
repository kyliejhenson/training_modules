# Resource User Experience in the CLI

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

Once resource reading is implemented, you can test the resource functionality through your CLI application. When you type "@" followed by a resource name, the system will:

1. Show available resources in an autocomplete list
2. Let you select a resource using arrow keys and space
3. Include the resource content directly in your prompt
4. Send everything to the AI model without requiring additional tool calls

This creates a smoother user experience compared to having the AI model make separate tool calls to access document contents. The resource content becomes part of the initial context, allowing for immediate responses about the data.
