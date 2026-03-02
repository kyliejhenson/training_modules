---
name: generate-facilitator-guide
description: "Generate a comprehensive Facilitator Guide (.docx) from an Anthropic training PowerPoint (.pptx). Use this skill whenever the user wants to create a facilitator guide, trainer guide, session leader guide, or instructor manual from a training presentation. Also trigger when the user mentions 'facilitator guide', 'trainer guide', 'facilitation notes', 'session guide', 'run sheet', 'facilitator manual', or asks how to prepare a facilitator to deliver a training deck. This skill extracts slide content and presenter notes from the .pptx, then produces a branded Word document with per-slide facilitation guidance including key concepts to emphasize, audience engagement techniques, activity instructions, timing, and adult learning best practices."
---

# Facilitator Guide Generator

Produces a branded Facilitator Guide (.docx) from an Anthropic training PowerPoint. The guide gives a facilitator everything they need to deliver the training: slide-by-slide guidance, engagement strategies, timing, and adult learning best practices.

---

## Step 1: Extract Content from the .pptx and Exercise Document

### Training Deck

```bash
python -m markitdown input_training.pptx
```

Parse the output into a slide map. **Every slide must be accounted for.** For each slide, capture:

- **Slide number** (1 through N)
- **Slide type** (Title, Agenda, Learning Objectives, Section Divider, Key Concepts, Full-Screen Image, Step-by-Step Process, Video Tutorial, Code/Demo, Comparison, Knowledge Check [MC/TF/Discussion/Hands-On], Reflection, Key Takeaways, Resources & Next Steps, Closing)
- **Presenter notes** — verbatim, not paraphrased

Verify: entry count must equal slide count. If they don't match, go back and find the missing slides.

### Exercise Document

Check the `Deliverables/` folder for a matching exercise document (pattern: `Exercises_[Feature]_[Profile].docx`). If one exists, extract its content:

```bash
python -m markitdown Deliverables/Exercises_[Feature]_[Profile].docx
```

Map each exercise back to the slide(s) it relates to. When generating per-slide facilitation content in Step 3, reference the corresponding exercise where relevant — for example, noting setup instructions the facilitator should give, how long the exercise takes, what the expected outcome looks like, or common mistakes participants make. This gives the facilitator a complete picture of what happens at each point in the session, not just the slides.

### Additional References

Also read **TEMPLATE_GUIDE.md** in the workspace root if it exists — it has slide type inventory and audience customization guidance.

---

## Step 2: Identify the Audience Profile

Check the title slide and filename (pattern: `Training_[Feature]_[Profile].pptx`) for the audience. If you can identify the profile, read the corresponding file from `Profiles/` to understand skill level, use cases, and learning style.

Audience shapes facilitation tone:

| Profile | Facilitation Focus |
|---------|-------------------|
| Developers | Let code speak, encourage edge-case questions, give hands-on time |
| Enterprise Champions | Storytelling, connect features to business outcomes, plan advocacy |
| Solutions Engineers | Balance technical depth with customer scenario framing |
| Solutions Partners | Connect everything to client conversations and implementation |

If you can't identify the profile, ask the user.

---

## Step 3: Generate Per-Slide Content

For **every slide** in the deck, write a facilitation section with these **3 parts**:

### Part 1: Presenter Notes (from the deck)

Include **complete, verbatim** presenter notes. Present them in a visually distinct block (gray background `#E8E6DC` table cell) so the facilitator can distinguish original notes from added guidance. If empty, state "No presenter notes in the deck for this slide."

### Part 2: Facilitation Guidance

Combine into one cohesive section:

- **Key concepts** (2-4 per slide): what matters most and *why* it matters for this audience
- **Delivery approach**: lecture, demo, discussion, or Q&A? What tone/energy?
- **Pacing**: specific time estimate (e.g., "3-5 minutes")
- **Common pitfalls**: what goes wrong and how to preempt it
- **Additional context** the deck author didn't include — audience-specific adjustments, deeper explanation

Frame additions as building on the presenter notes, not replacing them.

### Part 3: Engagement & Transition (only when needed)

**Only include this section if the presenter notes don't already cover engagement and transitions adequately.** Many slides will have thorough presenter notes that already provide questions to ask and natural segues — adding more would just be noise. Use your judgment: if the presenter notes already give the facilitator what they need for engagement and flow, skip Part 3 for that slide entirely.

When the presenter notes are thin or missing engagement/transition guidance, add:

- **Engagement prompts**: Write exact questions to ask (not "ask a question" — write the actual question). Include think-pair-share opportunities, polls, or real-world connection prompts as appropriate.
- **Transition**: 1-2 sentences the facilitator can say to bridge to the next slide.

### Slide Type Quick Reference

Use these timing and approach defaults:

| Slide Type | Time | Approach |
|-----------|------|----------|
| Title | 3-5 min | Welcome, introductions, logistics, icebreaker |
| Agenda | 2-3 min | Walk through sections, set pacing expectations |
| Learning Objectives | 2-3 min | Read aloud, connect to real work, promise to revisit |
| Section Divider | 1-2 min | Summarize previous section, preview next, check for questions |
| Key Concepts | 5-8 min | Introduce with examples/analogies, build connections between concepts |
| Full-Screen Image | 3-5 min | Let image land (5-10 sec silence), then walk through. Open with "What do you notice?" |
| Step-by-Step Process | 5-10 min | Sequential walkthrough, explain why behind each step, mention failure modes |
| Video Tutorial | Video + 3-5 min | Set "watch for" question before playing, debrief after |
| Code/Demo | 5-10 min | Line-by-line for critical parts, have backup screenshots, narrate live |
| Comparison | 4-6 min | Present both sides fairly, connect to audience experience |
| Knowledge Check (MC) | 3-5 min | Read aloud, think time, show of hands, explain correct + why distractors are wrong |
| Knowledge Check (TF) | 2-3 min | Quick show of hands, lean into surprise if most get it wrong |
| Knowledge Check (Discussion) | 8-12 min | Think-pair-share, circulate during small groups, synthesize themes |
| Knowledge Check (Hands-On) | As specified + 5 min | Confirm access/tools first, circulate actively, have extension task ready |
| Reflection | 5-8 min | Give genuine quiet time (3-5 min), don't fill silence, invite 2-3 volunteers |
| Key Takeaways | 3-4 min | Connect each takeaway back to learning objectives |
| Resources & Next Steps | 3-5 min | Explain what each resource is for, ask for 48-hour commitment |
| Closing | 5-10 min | Thank participants, final Q&A, feedback form, share contact info |

---

## Step 4: Write Front Matter

Place before the slide-by-slide sections:

**Training Overview:** Title, feature, target audience, estimated total duration (sum per-slide times from Step 3), learning objectives.

**Pre-Session Checklist:** Room/virtual setup, tech checks (projector, audio for videos), materials (handouts, credentials for exercises), participant pre-work, backup plans for demos.

**Adult Learning Principles (half-page max):**
Adults learn best when they understand *why* content matters (relevance), when their experience is leveraged (not lectured at), when they have autonomy, and when content is problem-centered. Engagement every 8-10 minutes minimum. Normalize wrong answers to maintain psychological safety. Chunk complex content and build in processing time.

---

## Step 5: Write Back Matter

**Session Timing Summary** — table with columns: Slide | Title | Type | Est. Time | Running Total | On Track?

**Troubleshooting:** Demo fails (use screenshot backup), running behind (which slides to abbreviate), disengaged audience (insert think-pair-share), wrong skill level (how to adjust depth), unanswerable questions ("I'll follow up after the session").

**Feedback & Follow-Up:** How to collect feedback, 1-week + 30-day follow-up cadence.

---

## Step 6: Build the .docx

Install and use `docx-js` (NOT Python):

```bash
npm install -g docx
```

Then write a Node.js script that generates the document. Validate after:

```bash
python scripts/office/validate.py output.docx
```

### Document Setup

```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        Header, Footer, AlignmentType, LevelFormat,
        TableOfContents, HeadingLevel, BorderStyle, WidthType, ShadingType,
        VerticalAlign, PageNumber, PageBreak } = require('docx');
```

- **Page size:** US Letter (width: 12240, height: 15840 DXA), 1" margins (1440 DXA)
- **Content width:** 9360 DXA (12240 - 2 x 1440)
- **Headings:** Arial bold, dark (`#141413`)
- **Body text:** Georgia regular, dark
- **Code/commands:** Courier New
- **Timing callouts:** Arial, orange (`#D97757`)

### Color Usage

| Element | Style |
|---------|-------|
| Presenter notes block | Gray background `#E8E6DC` table cell |
| Key concept boxes | Orange left border `#D97757` |
| Engagement prompt boxes | Blue left border `#6A9BCC` |
| Activity instruction boxes | Green left border `#788C5D` |
| Section divider rows | Light gray `#E8E6DC` |

### Key docx-js Rules

- **Always set page size explicitly** (defaults to A4)
- **Never use `\n`** — use separate Paragraphs
- **Never use unicode bullets** — use `LevelFormat.BULLET` with numbering config
- **Tables need dual widths** — `columnWidths` on table AND `width` on each cell, both in DXA
- **Use `ShadingType.CLEAR`** — never SOLID
- **Always add cell margins** — `{ top: 80, bottom: 80, left: 120, right: 120 }`
- **TOC requires HeadingLevel only** — no custom styles on headings
- **Override built-in styles** with exact IDs: "Heading1", "Heading2", etc. Include `outlineLevel`
- **Never use tables as dividers** — use paragraph borders instead

### Per-Slide Layout

Each slide section should have:
1. **Header row**: "SLIDE N: [Title]" with timing badge on the right and slide type in parentheses
2. **Presenter notes block**: gray-background table cell with verbatim notes
3. **Facilitation guidance**: normal paragraphs with key concepts in orange-bordered boxes
4. **Engagement & transition** (only if presenter notes lack this coverage): engagement prompts in blue-bordered boxes, transition text in italics

### Naming & Output

File: `Facilitator_Guide_[Feature]_[Profile].docx`
Save to: `Deliverables/` folder (create if needed)

---

## Step 7: Quality Check

1. **Slide count match** (most important): Count slides in .pptx, count sections in the guide. Must be identical. No gaps, no skips.
2. **Notes fidelity**: Spot-check 3-4 slides — presenter notes in guide must be verbatim from markitdown output.
3. **Audience alignment**: Developer guides shouldn't have selling language; Champion guides shouldn't have deep code walkthroughs.
4. **Timing sanity**: Sum per-slide times vs. total in front matter — should be within 5 minutes.
