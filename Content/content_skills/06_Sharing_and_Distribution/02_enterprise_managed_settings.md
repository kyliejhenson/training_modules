# Enterprise Deployment Through Managed Settings

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Security & compliance, Adoption & change management
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: Yes
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Administrators can deploy skills organization-wide through managed settings. Enterprise skills take the highest priority — they override personal, project, and plugin skills with the same name.

The managed settings file supports features like `strictKnownMarketplaces` to control where plugins can be installed from:

```
"strictKnownMarketplaces": [
  {
    "source": "github",
    "repo": "acme-corp/approved-plugins"
  },
  {
    "source": "npm",
    "package": "@acme-corp/compliance-plugins"
  }
]
```

This is the right choice for mandatory standards, security requirements, compliance workflows, and coding practices that must be consistent across the organization.
