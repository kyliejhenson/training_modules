# MCP Servers Explained

## Tags
- **Technical Skill Level**: Beginner
- **Use Case Types**: Technical implementation, Workflow integration
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

MCP Servers provide access to data or functionality implemented by outside services. They act as specialized interfaces that expose tools, prompts, and resources in a standardized way.

For example, an MCP Server for GitHub contains tools like `get_repos()` and connects directly to GitHub's API. Your server communicates with the MCP server, which handles all the service-specific implementation details.

Anyone can create an MCP server implementation. Often, service providers themselves release official MCP implementations — for example, AWS might release an official MCP server with tools for their various services.
