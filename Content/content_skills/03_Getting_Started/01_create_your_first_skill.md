# Create Your First Skill

## Tags
- **Technical Skill Level**: Beginner
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

This walkthrough creates a skill that teaches Claude to explain code using visual diagrams and analogies. Since it uses default frontmatter, Claude can load it automatically when you ask how something works, or you can invoke it directly with `/explain-code`.

### Step 1: Create the skill directory

Create a directory for the skill in your personal skills folder. Personal skills are available across all your projects.

```bash
mkdir -p ~/.claude/skills/explain-code
```

### Step 2: Write SKILL.md

Every skill needs a `SKILL.md` file with two parts: YAML frontmatter (between `---` markers) that tells Claude when to use the skill, and markdown content with instructions Claude follows when the skill is invoked. The `name` field becomes the `/slash-command`, and the `description` helps Claude decide when to load it automatically.

Create `~/.claude/skills/explain-code/SKILL.md`:

```yaml
---
name: explain-code
description: Explains code with visual diagrams and analogies. Use when explaining how code works, teaching about a codebase, or when the user asks "how does this work?"
---

When explaining code, always include:

1. **Start with an analogy**: Compare the code to something from everyday life
2. **Draw a diagram**: Use ASCII art to show the flow, structure, or relationships
3. **Walk through the code**: Explain step-by-step what happens
4. **Highlight a gotcha**: What's a common mistake or misconception?

Keep explanations conversational. For complex concepts, use multiple analogies.
```

### Step 3: Test the skill

You can test it two ways:

**Let Claude invoke it automatically** by asking something that matches the description:

```text
How does this code work?
```

**Or invoke it directly** with the skill name:

```text
/explain-code src/auth/login.ts
```

Either way, Claude should include an analogy and ASCII diagram in its explanation.
