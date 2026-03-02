# Skill Doesn't Load

## Tags
- **Technical Skill Level**: Intermediate
- **Use Case Types**: Technical implementation, Evaluation & testing
- **Instructional Priority**: Supplemental
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://code.claude.com/docs/en/skills

---

## Content

If your skill doesn't appear when you ask Claude "what skills are available," check these structural requirements:

- The `SKILL.md` file must be inside a named directory, not at the skills root
- The file name must be exactly `SKILL.md` — all caps on "SKILL", lowercase "md"

Run `claude --debug` to see loading errors. Look for messages mentioning your skill name. Sometimes this alone will point you straight to the problem.
