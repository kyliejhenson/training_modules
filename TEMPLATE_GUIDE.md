# Anthropic Training Template — AI System Guide

This document provides all the information an AI system needs to use the `Anthropic_Training_Template.pptx` template to produce training materials for developers, partners, and champions on new Claude features.

---

## Template Overview

The template contains **25 slides** organized into a complete training flow. Each slide uses Anthropic brand guidelines and includes standardized presenter notes that should be customized per training.

### Slide Inventory

| Slide # | Type | Purpose | When to Use |
|---------|------|---------|-------------|
| 1 | Title | Training title, feature name, date, audience | Always first — required |
| 2 | Agenda | Numbered section overview (4 items) | Always second — required |
| 3 | Learning Objectives | 4 objective cards with icons | Always third — required |
| 4 | Section Divider | Dark slide separating major sections | Before each content section |
| 5 | Key Concepts | 2x2 grid of concept cards with icons | Introducing new concepts or terminology |
| 6 | **Full-Screen Image** | Full-bleed image placeholder with caption bar | Screenshots, diagrams, photos, infographics |
| 7 | Step-by-Step Process | Numbered vertical steps with connector lines | Procedures, setup guides, workflows |
| 8 | **Video Tutorial (Embedded)** | Full-screen embedded YouTube video with media playback | Embedding a clickable video from anthropic.com/learn or youtube.com/@claude |
| 9 | Code / Demo | Dark code block with terminal styling | API examples, code snippets, CLI demos |
| 10 | Comparison | Side-by-side Before/After or Option A vs B | Showing improvements, contrasting approaches |
| 11 | **Full-Screen Image** | Full-bleed image placeholder with caption bar | Screenshots, diagrams, photos, infographics |
| 12 | **Video Tutorial (Placeholder)** | Dark video player placeholder with play button and URL bar | Embedding a video from anthropic.com/learn or youtube.com/@claude |
| 13 | Knowledge Check — Multiple Choice | Question + 4 answer options (A-D) | Testing factual recall or comprehension |
| 14 | Knowledge Check — True/False | Statement + True/False cards | Quick concept verification |
| 15 | Knowledge Check — Discussion | Open-ended prompt with guiding questions | Deeper exploration, scenario analysis |
| 16 | Knowledge Check — Hands-On Exercise | Task list + time/success criteria panel | Applied practice, building something |
| 17 | **Reflection** | 2x2 grid of reflection prompt cards (green accent) | Structured pause for learners to internalize and plan application |
| 18 | Key Takeaways | 3 numbered takeaway cards | Always near end — required |
| 19 | Resources & Next Steps | Links column + action items column + support bar | Always second-to-last — required |
| 20 | Closing / Q&A | Orange background, contact info, feedback form link | Always last — required |
| 21 | Chapter Divider 2 | Dusty Rose background, "[Chapter 2]" label | Optional — for multi-chapter trainings |
| 22 | Chapter Divider 3 | Lavender background, "[Chapter 3]" label | Optional — for multi-chapter trainings |
| 23 | Chapter Divider 4 | Cornflower Blue background, "[Chapter 4]" label | Optional — for multi-chapter trainings |
| 24 | Chapter Divider 5 | Sage Mint background, "[Chapter 5]" label | Optional — for multi-chapter trainings |
| 25 | Chapter Divider 6 | Warm Sand background, "[Chapter 6]" label | Optional — for multi-chapter trainings |

---

## Anthropic Brand Specifications

### Colors (6-digit hex, NO # prefix in PPTX code)

| Name | Hex | Theme Role | Usage |
|------|-----|------------|-------|
| Dark | `141413` | dk1, accent6 | Primary text, dark slide backgrounds |
| Light | `FAF9F5` | lt1 | Light slide backgrounds, text on dark slides |
| Mid Gray | `B0AEA5` | dk2, accent4 | Secondary text, captions, subtle elements |
| Light Gray | `E8E6DC` | lt2 | Subtle backgrounds, divider lines, video area borders |
| Orange | `D97757` | accent1, folHlink | Primary accent, CTAs, first-level emphasis, followed hyperlinks |
| Blue | `6A9BCC` | accent2, hlink | Secondary accent, knowledge check headers, links, hyperlinks |
| Green | `788C5D` | accent3 | Tertiary accent, success indicators, code slides, reflection cards |
| Tan | `D4A47F` | accent5 | Reserved theme accent (not actively used on slides) |
| White | `FFFFFF` | — | Card fills, play button icons |

### Typography

| Element | Font | Fallback | Size Range |
|---------|------|----------|------------|
| Slide titles | Test Tiempos Headline Light | Georgia | 28–44pt, bold |
| Section headers | Styrene A Medium Trial | Arial | 16–24pt, bold |
| Body text | Lora | Georgia | 12–16pt, regular |
| Code blocks | Courier New | Consolas | 11–13pt, regular |
| Captions/labels | Styrene A Medium Trial | Arial | 10–12pt |
| Theme major font | Test Tiempos Headline Light | — | Used for `+mj-lt` theme references and slide titles |
| Theme minor font | Lora | — | Used for `+mn-lt` theme references |

**Fonts:** The template uses Anthropic's brand fonts — Styrene A (sans-serif, for headings/UI), Lora (serif, for body text), and Test Tiempos Headline Light (serif, for slide titles). Slide titles specifically use Test Tiempos Headline Light for a refined, elegant appearance. Font files are included in the `fonts/` subfolder for installation on systems that will render or edit the template. If these fonts are not available, PowerPoint will fall back to Arial and Georgia respectively.

### Font Files (in `fonts/` folder)

| Font Family | Weights Available | Usage |
|-------------|-------------------|-------|
| Styrene A | Thin, Light, Medium, Bold, Black | Headings, labels, UI elements |
| Test Tiempos Headline | Light, Regular, Medium, Semibold | Large display titles (theme major font), slide titles |
| Lora | Regular, Bold, Italic | Body text, descriptions |

### Slide Layouts (for universal edits)

The template uses **1 slide master** with **6 slide layouts** that control all shared brand elements. Edit a layout to change branding across all slides that use it.

| Layout Name | Background | Brand Elements | Used By Slides |
|-------------|-----------|----------------|----------------|
| `DEFAULT` | Light (`FAF9F5`) | None (bare layout) | Not directly used by any slide |
| `DARK_BRAND` | Dark (`141413`) | Anthropic logo images | 4 (Section Divider), 21-25 (Chapter Dividers with color overrides) |
| `LIGHT_ORANGE` | Light (`FAF9F5`) | None | 2 (Agenda), 3 (Learning Objectives), 5 (Key Concepts), 6 (Full-Screen Image), 8 (Video — Embedded), 10 (Comparison), 11 (Full-Screen Image), 12 (Video — Placeholder), 18 (Key Takeaways) |
| `LIGHT_BLUE` | Light (`FAF9F5`) | None | 7 (Step-by-Step), 19 (Resources) |
| `LIGHT_GREEN` | Light (`FAF9F5`) | None | 9 (Code/Demo), 17 (Reflection) |
| `KNOWLEDGE_CHECK` | Light (`FAF9F5`) | Blue header band (1.0" height, 88% transparency / 12% opacity) | 13 (Multiple Choice), 14 (True/False), 15 (Discussion), 16 (Hands-On) |

**To make universal edits** (e.g., change accent color, adjust bar thickness, swap the wordmark), modify the corresponding layout in the unpacked PPTX `slideLayouts/` folder. Changes propagate to all slides using that layout.

### Visual Conventions

- **Card styling**: Content cards use white (`FFFFFF`) fill with rounded corners (`roundRect`, corner radius ~5%) and a colored border at reduced opacity (e.g., green borders at 40% alpha on Reflection cards). Border width is 1pt (12700 EMU).
- **Icon circles**: Icons are rendered as SVG-to-PNG with a subtle circular background tint matching their accent color at ~15% opacity.
- **Caption bars**: Full-screen image slides use a semi-transparent dark (`141413`) caption bar at the bottom with 70% opacity.
- **Chapter divider colors**: Slides 21-25 are chapter divider variants with distinct background colors (Dusty Rose, Lavender, Cornflower Blue, Sage Mint, Warm Sand) for visual separation between training chapters.

---

## How to Populate the Template

### General Rules

1. **Replace all `[BRACKETED TEXT]`** with actual content. Every placeholder is marked with square brackets.
2. **Preserve the visual structure** — do not add or remove shapes/cards unless the content requires it.
3. **Keep text concise** — slides are designed for presentation, not documentation. Body text should be 2-3 sentences max per card/section.
4. **Maintain font hierarchy** — titles bold in heading font, body text in body font, code in monospace.
5. **Use the accent color system** — orange for primary emphasis, blue for secondary/knowledge checks, green for code/success.

### Slide-by-Slide Population Guide

#### Slide 1 — Title
- Background: Solid orange (`D97757`) with dark text (`141413`)
- Replace `[TRAINING TITLE]` with the full training title (e.g., "Getting Started with Claude Tool Use")
- Replace `[Feature Name] | [Version/Date]` with the specific feature and date (e.g., "Tool Use API | v2.1 — March 2026")
- Replace `[AUDIENCE: Developers / Partners / Champions]` with the specific audience

#### Slide 2 — Agenda
- Replace all 4 topic placeholders with section names and brief descriptions
- Match the section numbers to actual content sections
- Adjust the number of agenda items if needed (duplicate or remove card rows)

#### Slide 3 — Learning Objectives
- Write 3-5 objectives using **Bloom's Taxonomy action verbs**:
  - **Remember/Understand**: define, describe, explain, identify, recognize
  - **Apply/Analyze**: implement, configure, compare, troubleshoot, demonstrate
  - **Evaluate/Create**: design, build, optimize, architect, evaluate
- Each objective should be measurable and tied to a knowledge check later in the deck
- Format: "By the end of this training, you will be able to [VERB] [WHAT] [CONTEXT]"

#### Slide 4 — Section Divider
- Background: Olive green (`788C5D`) with dark text (`141413`)
- Chapter label: "[Chapter N]" in italic Lora
- Duplicate this slide for each major section transition
- Replace `[Chapter N]` with the section/chapter number (e.g., "[Chapter 1]", "[Chapter 2]")
- Replace `[Section Title]` with the section name
- Replace the description and duration estimate

#### Slide 5 — Key Concepts
- Use for introducing 2-4 new concepts, terms, or components
- Each card gets a title and 2-3 sentence description
- Choose icons that match the concept (lightbulb for ideas, code brackets for technical, book for documentation, chat for communication)

#### Slides 6, 11 — Full-Screen Image
- Replace the entire slide background with a full-bleed image (screenshot, diagram, photo, or infographic)
- The light gray (`E8E6DC`) background with dashed orange circle and image icon is a visual placeholder — delete these shapes when inserting the actual image
- Replace `[Image Caption]` in the semi-transparent dark caption bar at the bottom with a descriptive caption
- Replace `[Source or additional context]` with the image source, attribution, or contextual note
- Image should be high-resolution (minimum 1920×1080) to fill the slide without pixelation
- Two image slots are provided at strategic points in the deck flow:
  - **Slide 6**: After Key Concepts — use for a diagram, architecture visual, or concept illustration
  - **Slide 11**: After Comparison — use for a screenshot, demo output, or real-world example
- Duplicate or remove image slides as needed; not both are required for every training

#### Slide 7 — Step-by-Step Process
- Use for setup guides, implementation procedures, or workflows
- 3-5 steps is ideal; each step has a title and one-line description
- Steps should be sequential and actionable

#### Slide 8 — Video Tutorial (Embedded)
- Slide 8 uses a **full-screen embedded YouTube video** format — it contains an actual video element with media playback timing, not a placeholder layout
- To populate: replace the embedded video reference (in the slide's relationship file) with the target YouTube URL, and update the thumbnail image
- The video plays directly within PowerPoint during presentation mode (click to play/pause)
- Best used for a feature overview or introduction video early in the deck

#### Slide 12 — Video Tutorial (Placeholder)
- Slide 12 uses the **placeholder layout** with a title, subtitle, dark video area (`roundRect` with dark fill and light gray border), orange play circle (85% alpha), white play triangle, "VIDEO TUTORIAL" label, and a URL bar
- Replace `[Video Title]` with the tutorial title (e.g., "Getting Started with Tool Use")
- Replace `[Brief description...]` with a one-line summary of what participants will learn
- Replace the URL placeholder with the actual video link from `https://www.anthropic.com/learn` or `https://www.youtube.com/@claude`
- In the actual presentation, replace the dark player area with an embedded video or a clickable screenshot linked to the YouTube URL
- Best used for an implementation demo or walkthrough video later in the deck
- Duplicate or remove video slides as needed; not both are required for every training

#### Slide 9 — Code / Demo
- Code block background: Warm sage (`E8E6DC`) with dark text
- Replace `[filename.py / terminal]` with the actual filename or context
- Paste the code example in the code block area
- Keep code to 12-15 lines maximum; use comments to highlight key lines
- Fill in the green callout box below with the key takeaway

#### Slide 10 — Comparison
- Use for Before/After, With/Without, Old API/New API comparisons
- Replace column headers with the comparison context
- Fill in 3 points per side, keeping them parallel in structure

#### Slides 13-16 — Knowledge Checks
- **Multiple Choice (Slide 13)**: Write a scenario-based question with 4 options. Include the correct answer and explanations in presenter notes.
- **True/False (Slide 14)**: Write a specific, unambiguous statement. Fill in both "why true" and "why false" explanations.
- **Discussion (Slide 15)**: Write an open-ended question that connects to real-world application. Include 3 guiding sub-questions.
- **Hands-On Exercise (Slide 16)**: Define 3 tasks, a time limit, and success criteria. Ensure participants have access to necessary tools.

#### Slide 17 — Reflection
- Uses the `LIGHT_GREEN` layout with its own light (`FAF9F5`) background, green top accent bar, and a green header band (12% opacity, same structure as the `KNOWLEDGE_CHECK` band but in green)
- The "REFLECTION" label sits inside the header band in green (`788C5D`) text
- Contains a 2×2 grid of four reflection prompt cards — white-filled rounded rectangles with green (`788C5D`) borders at 40% alpha
- Default prompts: "WHAT I LEARNED", "HOW I'LL USE IT", "WHAT SURPRISED ME", "QUESTIONS I STILL HAVE"
- Prompt labels use Styrene A Medium Trial (10pt, green), placeholder text uses Lora (12pt, italic, mid gray)
- Replace the italic placeholder text in each card with prompts tailored to the specific training topic
- Allow 3-5 minutes of quiet individual reflection, then optionally invite volunteers to share
- Can also be used as a pair/small-group discussion activity
- Consider providing sticky notes or a digital whiteboard for participants to capture reflections

#### Slide 18 — Key Takeaways
- Summarize the 3 most important things to remember
- Each takeaway should connect back to a learning objective
- Use the format: what to remember, what to do, what to apply

#### Slide 19 — Resources & Next Steps
- Provide 3-5 documentation links with descriptive names
- List 2-3 specific action items with timelines (e.g., "Try the API in sandbox within 48 hours")
- Fill in the support contact information bar

#### Slide 20 — Closing
- Background: Orange (`D97757`) with dark text (`141413`)
- Add presenter name, email, and Slack handle
- Include the training feedback form URL

#### Slides 21-25 — Chapter Divider Variants
These five optional slides provide colored chapter dividers for multi-chapter trainings. Each uses the `DARK_BRAND` layout with a distinct background color override and dark text.

- **Slide 21 — Chapter 2**: Dusty Rose (`B5758A`) background, "[Chapter 2]" in italic Lora
- **Slide 22 — Chapter 3**: Lavender (`9D8FBF`) background, "[Chapter 3]" in italic Lora
- **Slide 23 — Chapter 4**: Cornflower Blue (`7EA5CB`) background, "[Chapter 4]" in italic Lora
- **Slide 24 — Chapter 5**: Sage Mint (`ADBEB0`) background, "[Chapter 5]" in italic Lora
- **Slide 25 — Chapter 6**: Warm Sand (`CCC0AB`) background, "[Chapter 6]" in italic Lora

Use these slides to visually separate major chapters or training sections when your training is organized into multiple distinct topics. Replace the chapter number as needed for your specific structure.

---

## Presenter Notes Format

Every slide includes structured presenter notes following this template:

```
PRESENTER NOTES — [SLIDE TYPE]
-------------------------------
[Section Header]:
- [Instruction or talking point]
- [Instruction or talking point]

[Section Header]:
- [Instruction or talking point]
- [Instruction or talking point]
```

### Standard Note Sections by Slide Type

| Slide Type | Required Note Sections |
|------------|----------------------|
| Title | Welcome & Introduction, Key Setup |
| Agenda | Walk Through the Agenda, Logistics |
| Learning Objectives | Present Each Objective, Engagement |
| Section Divider | Transition, Pacing |
| Content slides | Teaching Approach/Delivery, Tips/Engagement |
| Knowledge Checks | Correct Answer, Facilitation, If Most Get It Wrong |
| Hands-On Exercise | Setup, During Exercise, After Exercise |
| Key Takeaways | Summary, Next Steps |
| Resources | Share Resources, Feedback |
| Closing | Q&A Session, Closing, Post-Session |

When populating presenter notes, always include:
1. **The correct answer** (for knowledge checks)
2. **Timing guidance** for the section
3. **Engagement prompts** (questions to ask the audience)
4. **Fallback plans** (what to do if demo fails, audience is confused, etc.)
5. **Transition language** to the next section

---

## Audience-Specific Customization

### For Developers
- Emphasize code examples and API details
- Include more Code/Demo slides (duplicate Slide 7)
- Hands-on exercises should involve writing actual code
- Knowledge checks should be code-based or scenario-based
- Resources should link to API docs, SDKs, and code repositories

### For Partners
- Focus on use cases and business value
- Use more Comparison slides showing customer impact
- Knowledge checks should be scenario-based (customer situations)
- Hands-on exercises can be lighter (sandbox exploration vs. coding)
- Resources should include partner portal, sales enablement, case studies

### For Champions (Internal Advocates)
- Balance technical depth with communication skills
- Include Discussion slides for sharing best practices
- Knowledge checks should test both technical knowledge and teaching ability
- Hands-on exercises should involve explaining/demonstrating to others
- Resources should include internal wikis, Slack channels, escalation paths

---

## Recommended Deck Structure by Training Length

### 30-Minute Quick Start (8-10 slides)
1. Title
2. Learning Objectives (2-3 objectives)
3. Section Divider
4. Key Concepts OR Step-by-Step
5. Code/Demo
6. Knowledge Check (1, any type)
7. Key Takeaways
8. Closing

### 60-Minute Standard Training (15-18 slides)
1. Title
2. Agenda
3. Learning Objectives (3-4 objectives)
4. Section Divider — Fundamentals
5. Key Concepts
6. Code/Demo
7. Knowledge Check — Multiple Choice
8. Section Divider — Implementation
9. Step-by-Step Process
10. Code/Demo
11. Knowledge Check — Hands-On Exercise
12. Section Divider — Best Practices
13. Comparison
14. Knowledge Check — Discussion
15. Key Takeaways
16. Resources & Next Steps
17. Closing

### 90-Minute Deep Dive (20-25 slides)
Use the 60-minute structure as a base, adding:
- Additional Code/Demo slides for advanced examples
- More Knowledge Checks after each major section
- A dedicated Troubleshooting/FAQ section (use Comparison layout)
- Extended Hands-On Exercise with multiple tasks
- Optional: Use the colored Chapter Divider variants (Slides 21-25) to separate major chapters or training topics visually

---

## Slide Duplication Guidelines

When creating a training deck, you will need to **duplicate** certain slide types. Here's how:

### Slides to Use Once (Never Duplicate)
- Slide 1 (Title)
- Slide 2 (Agenda)
- Slide 3 (Learning Objectives)
- Slide 17 (Reflection)
- Slide 20 (Closing)

### Slides to Duplicate as Needed
- **Slide 4 (Section Divider)**: One per major section; use with olive green background for primary section dividers
- **Slides 21-25 (Chapter Dividers)**: Optional colored variants for multi-chapter trainings; use instead of duplicating Slide 4 if you need visual color variety
- **Slide 5 (Key Concepts)**: When introducing new concept groups
- **Slides 6, 11 (Full-Screen Image)**: For screenshots, diagrams, or visual content
- **Slide 7 (Step-by-Step)**: For each procedure or workflow
- **Slides 8, 12 (Video Tutorial)**: For each embedded video
- **Slide 9 (Code/Demo)**: For each code example
- **Slide 10 (Comparison)**: For each comparison needed

### Slides to Duplicate for Assessment
- **Slide 13 (Multiple Choice)**: 1-2 per section for factual recall
- **Slide 14 (True/False)**: 1 per section for quick checks
- **Slide 15 (Discussion)**: 1 per training for deeper exploration
- **Slide 16 (Hands-On)**: 1 per training for applied practice

### Recommended Knowledge Check Distribution
- After every 10-15 minutes of content, include one knowledge check
- Alternate between check types to maintain engagement
- Place the Hands-On Exercise after all content is taught
- Place the Discussion near the end for reflection

---

## Technical Notes for AI Systems

### Editing the Template Programmatically

The template was built with **PptxGenJS** (Node.js). To modify it programmatically:

1. **Unpack**: Use `python scripts/office/unpack.py` to extract the PPTX into editable XML
2. **Duplicate slides**: Use `python scripts/add_slide.py` to copy slide layouts
3. **Edit content**: Replace `[BRACKETED TEXT]` in slide XML files using text replacement
4. **Clean**: Run `python scripts/clean.py` to remove orphaned files
5. **Repack**: Use `python scripts/office/pack.py` to rebuild the PPTX

### Placeholder Pattern

All editable content follows this regex pattern:
```
\[.*?\]
```

Specifically:
- `[ALL CAPS TEXT]` = structural labels (section numbers, type indicators)
- `[Sentence case text]` = content to be replaced with actual training content
- `[lowercase-with-hyphens]` = contact info, URLs, technical values

### Color Assignment Rules

When duplicating slides, maintain the color scheme:
- **Section Dividers**: Always use dark background (`141413`) with orange accent
- **Content Slides**: Use light background (`FAF9F5`) with section-appropriate accent:
  - First section → orange (`D97757`)
  - Second section → blue (`6A9BCC`)
  - Third section → green (`788C5D`)
  - Subsequent sections → cycle through orange, blue, green
- **Knowledge Checks**: Always use blue (`6A9BCC`) accent in the header band
- **Code Slides**: Always use green (`788C5D`) top accent

### Quality Checklist

Before delivering any training deck built from this template, verify:

- [ ] All `[BRACKETED PLACEHOLDERS]` have been replaced
- [ ] Learning objectives use Bloom's Taxonomy verbs
- [ ] Each learning objective maps to at least one knowledge check
- [ ] Knowledge checks have correct answers documented in presenter notes
- [ ] All presenter notes are customized (not left as generic templates)
- [ ] Code examples are tested and working
- [ ] Resource links are valid and accessible to the target audience
- [ ] Audience-specific customizations are applied
- [ ] Deck length matches the planned session duration
- [ ] Contact information and feedback form URL are current
