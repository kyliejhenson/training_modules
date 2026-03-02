# Managed MCP Configuration Overview

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Security & compliance, Adoption & change management
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: Yes
- **Source**: https://code.claude.com/docs/en/mcp

---

## Content

For organizations that need centralized control over MCP servers, Claude Code supports two configuration options:

1. **Exclusive control with `managed-mcp.json`**: Deploy a fixed set of MCP servers that users cannot modify or extend.
2. **Policy-based control with allowlists/denylists**: Allow users to add their own servers, but restrict which ones are permitted.

### What IT administrators can do

- **Control which MCP servers employees can access**: Deploy a standardized set of approved MCP servers across the organization.
- **Prevent unauthorized MCP servers**: Restrict users from adding unapproved MCP servers.
- **Disable MCP entirely**: Remove MCP functionality completely if needed.

These options can be combined: if `managed-mcp.json` exists, it has exclusive control and users cannot add servers. Allowlists and denylists still apply to filter which managed servers are actually loaded.
