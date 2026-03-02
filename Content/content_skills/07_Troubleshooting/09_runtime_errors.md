# Runtime Errors

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation, Evaluation & testing
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

The skill loads but fails during execution. A few common causes:

- **Missing dependencies**: If your skill uses external packages, they must be installed. Add dependency info to your skill description so Claude knows what's needed.
- **Permission issues**: Scripts need execute permission. Run `chmod +x` on any scripts your skill references.
- **Path separators**: Use forward slashes everywhere, even on Windows.
