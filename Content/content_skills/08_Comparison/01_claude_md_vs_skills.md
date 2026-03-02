# CLAUDE.md vs Skills

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/memory

---

## Content

CLAUDE.md loads into every conversation, always. Skills load on demand when Claude matches a request to a skill.

**Use CLAUDE.md for:**

- Project-wide standards that always apply
- Constraints like "never modify the database schema"
- Framework preferences and coding style

**Use Skills for:**

- Task-specific expertise
- Knowledge that's only relevant sometimes
- Detailed procedures that would clutter every conversation

Example: If you want Claude to always use TypeScript strict mode in your project, put it in CLAUDE.md. Your PR review checklist doesn't need to be in context when you're writing new code — it loads when you actually ask for a review, so make it a skill.
