# Skills vs Hooks

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Workflow integration
- **Instructional Priority**: Foundational
- **Technical Application Practice**: No
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/hooks

---

## Content

Hooks fire on events. A hook might run a linter every time Claude saves a file, or validate input before certain tool calls. They're event-driven.

Skills are request-driven. They activate based on what you're asking.

**Use Hooks for:**

- Operations that should run on every file save
- Validation before specific tool calls
- Automated side effects of Claude's actions

**Use Skills for:**

- Knowledge that informs how Claude handles requests
- Guidelines that affect Claude's reasoning
