# Restrict Claude's Skill Access

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation, Security & compliance
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

By default, Claude can invoke any skill that doesn't have `disable-model-invocation: true` set. Skills that define `allowed-tools` grant Claude access to those tools without per-use approval when the skill is active. Your permission settings still govern baseline approval behavior for all other tools. Built-in commands like `/compact` and `/init` are not available through the Skill tool.

There are three ways to control which skills Claude can invoke:

**Disable all skills** by denying the Skill tool in `/permissions`:

```text
# Add to deny rules:
Skill
```

**Allow or deny specific skills** using permission rules:

```text
# Allow only specific skills
Skill(commit)
Skill(review-pr *)

# Deny specific skills
Skill(deploy *)
```

Permission syntax: `Skill(name)` for exact match, `Skill(name *)` for prefix match with any arguments.

**Hide individual skills** by adding `disable-model-invocation: true` to their frontmatter. This removes the skill from Claude's context entirely.

Note: The `user-invocable` field only controls menu visibility, not Skill tool access. Use `disable-model-invocation: true` to block programmatic invocation.
