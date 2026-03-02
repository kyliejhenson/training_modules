# Using Scripts Efficiently

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

Scripts in your skill directory can run without loading their contents into context. The script executes and only the output consumes tokens. The key instruction to include in your `SKILL.md` is to tell Claude to _run_ the script, not _read_ it.

This is particularly useful for:

- Environment validation
- Data transformations that need to be consistent
- Operations that are more reliable as tested code than generated code
