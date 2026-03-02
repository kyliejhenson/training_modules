# Choosing the Right Scope

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Adoption & change management
- **Instructional Priority**: Applied
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

Select your scope based on how broadly the server needs to be available and whether it should be shared:

- **Local scope**: Personal servers, experimental configurations, or sensitive credentials specific to one project.
- **Project scope**: Team-shared servers, project-specific tools, or services required for collaboration.
- **User scope**: Personal utilities needed across multiple projects, development tools, or frequently used services.

### Scope hierarchy and precedence

When servers with the same name exist at multiple scopes, the system resolves conflicts by prioritizing:

1. Local-scoped servers (highest priority)
2. Project-scoped servers
3. User-scoped servers (lowest priority)

This design ensures that personal configurations can override shared ones when needed.
