---
name: generate-facilitator-guide
description: "Generate a comprehensive Facilitator Guide (.docx) from an Anthropic training PowerPoint (.pptx). Use this skill whenever the user wants to create a facilitator guide, trainer guide, session leader guide, or instructor manual from a training presentation. Also trigger when the user mentions 'facilitator guide', 'trainer guide', 'facilitation notes', 'session guide', 'run sheet', 'facilitator manual', or asks how to prepare a facilitator to deliver a training deck. This skill extracts slide content and presenter notes from the .pptx, then produces a branded Word document with per-slide facilitation guidance including key concepts to emphasize, audience engagement techniques, activity instructions, timing, and adult learning best practices."
---

# Facilitator Guide Generator

This skill produces a comprehensive, branded Facilitator Guide as a Word document (.docx) from an Anthropic training PowerPoint. The guide gives a facilitator everything they need to confidently deliver the training — slide-by-slide tactical guidance, audience engagement strategies, activity facilitation instructions, and timing — all grounded in adult learning best practices.

## Important: Read Supporting Skills First

Before doing anything else, read these skills (check available skills for paths):

1. **pptx SKILL.md** — You need the pptx skill's reading tools (`markitdown`) to extract content from the input presentation
2. **docx SKILL.md** — You need the docx skill's creation workflow (`docx-js`) to build the output Word document
3. **brand-guidelines SKILL.md** — You need Anthropic's brand colors and typography to style the output

Also read **TEMPLATE_GUIDE.md** in the workspace root — it contains the slide type inventory, presenter notes format, and audience-specific customization guidance that informs how to write facilitation notes for each slide type.

---

## Step 1: Extract Content

### Read the Presentation

Use the pptx skill's reading tools to extract everything from the input .pptx:

```bash
# Extract all text content including presenter notes
python -m markitdown input_training.pptx
```

### Build a Slide Map

Parse the markitdown output into a structured slide map. **Every single slide in the deck must be accounted for.** Count the total number of slides first, then build a map entry for each one — no exceptions, no skipping. If the deck has 28 slides, the guide must have 28 slide sections.

For each slide, capture:

- **Slide number** (1 through N, where N is the total slide count)
- **Slide type** — identify which template slide type it is (Title, Agenda, Learning Objectives, Section Divider, Key Concepts, Full-Screen Image, Step-by-Step Process, Video Tutorial, Code/Demo, Comparison, Knowledge Check variants, Reflection, Key Takeaways, Resources & Next Steps, Closing). Use TEMPLATE_GUIDE.md's slide inventory as your reference.
- **Presenter notes** — the full, verbatim notes text from the slide. Copy these exactly as they appear — do not paraphrase, summarize, or truncate.

After building the map, verify the count: the number of entries in your slide map must equal the number of slides in the deck. If they don't match, you've missed slides — go back and find them. A facilitator who discovers missing slides in the guide will lose trust in the entire document.

---

## Step 2: Identify the Audience Profile

Check the title slide for the audience identifier (the deck should include an audience tag like "AUDIENCE: Developers" or similar). Also check the filename — training decks from the generate-training skill follow the pattern `Training_[Feature]_[Profile].pptx`.

If you can identify the profile, read the corresponding profile file from `Profiles/` in the workspace to understand:

- Technical skill level
- Use case types
- Whether they need hands-on practice
- Whether they need value-based selling framing

This shapes the facilitation tone throughout the guide. For example:

- **Developers** → facilitation guidance should emphasize letting the code speak, encouraging questions about edge cases, and giving time for hands-on exploration
- **Enterprise Champions** → facilitation guidance should emphasize storytelling, connecting features to business outcomes, and creating space for participants to plan their internal advocacy
- **Solutions Engineers** → facilitation guidance should balance technical depth with customer scenario framing
- **Solutions Partners** → facilitation guidance should connect everything to client conversations and implementation advisory

If you can't identify the profile, ask the user which audience this training is for.

---

## Step 3: Generate the Facilitator Guide Content

For every slide in the deck, write a comprehensive facilitation section. The depth and focus should vary by slide type, but every section follows the same overall structure.

### Every Slide Gets a Section — No Exceptions

Before writing any content, confirm your slide count. If the deck has N slides, the guide must have exactly N slide sections. This is non-negotiable — a facilitator flipping through the guide during delivery needs to find guidance for every single slide they'll encounter. Skipping "simple" slides like section dividers or closing slides leaves the facilitator unsupported at those exact moments.

### Per-Slide Section Structure

Each slide's section in the guide should include these elements:

#### 1. Slide Header
Format: **Slide [N]: [Slide Title]** with the slide type in parentheses.

#### 2. Presenter Notes (from the deck)
Include the **complete, verbatim** presenter notes from the .pptx. These are the talking points and instructions the deck author wrote. Present them in a visually distinct block — use a table cell with a light gray background (`#E8E6DC`) or an indented style — so the facilitator can instantly distinguish the original deck notes from the additional facilitation guidance that follows.

Do not paraphrase, summarize, or edit these notes. The facilitator needs to see exactly what the deck author intended. If the notes are empty for a particular slide, state "No presenter notes in the deck for this slide."

#### 3. Additional Facilitation Tips
This is where the guide adds value beyond what's already in the deck. Provide supplementary guidance that builds on the presenter notes — context the deck author didn't include, audience-specific adjustments, warnings about common stumbling points, or deeper explanation of why a concept matters.

Frame these clearly as *additions* to the notes, not replacements. Use language like "In addition to the notes above..." or "To build on this..." The facilitator should understand that the presenter notes are the foundation and these tips are the enhancement layer.

#### 4. Key Concepts to Emphasize
Identify the 2-4 most important ideas on this slide and explain *why* they matter. This isn't just repeating the slide content — it's helping the facilitator understand what the audience absolutely must walk away understanding from this moment in the training.

Think about it from the perspective of adult learning theory: adults learn best when they understand the relevance of what they're learning. So for each key concept, briefly connect it to the audience's real work. For a Developers audience, that might be "This matters because it changes how you structure API calls." For Enterprise Champions, it might be "This is the feature your stakeholders will ask about first."

#### 5. Facilitation Tactics
Concrete, actionable guidance on *how* to deliver this slide effectively. This varies significantly by slide type (see the Slide Type Facilitation Patterns section below), but always consider:

- **Pacing**: How long to spend on this slide. Be specific ("Spend 2-3 minutes here" not "don't rush").
- **Delivery approach**: Should the facilitator lecture, ask questions, demo, or facilitate discussion?
- **Voice and energy**: Where should emphasis fall? Should the tone shift here (e.g., slowing down for a complex concept, building energy before an activity)?
- **Common pitfalls**: What tends to go wrong when facilitating this type of content? (e.g., "Participants often get stuck on X — preempt this by clarifying Y before showing the slide")

#### 6. Audience Engagement
Specific prompts and techniques to keep participants active. Adults disengage when they're passive for too long — the research is clear that engagement every 8-10 minutes is the minimum. Include:

- **Questions to ask**: Write the exact questions, not just "ask a question." For example: "Before I show the next step, what do you think happens when the model receives a tool result?" Direct questions get better responses than "any questions?"
- **Think-pair-share opportunities**: Where participants can briefly discuss with a neighbor
- **Show of hands / polls**: Quick temperature checks ("How many of you have tried this before?")
- **Real-world connections**: Prompts that invite participants to connect the content to their own experience ("Think of a time when you needed to...")

#### 7. Transitions
How to smoothly move from this slide to the next one. Write the actual transition language — a sentence or two the facilitator can say (or adapt) to bridge topics. Good transitions reinforce what was just covered and preview what's coming.

### Slide Type Facilitation Patterns

Different slide types require different facilitation approaches. Use these patterns as your guide:

#### Title Slide
- **Tone**: Warm, welcoming, sets expectations
- **Tactics**: Introduce yourself, acknowledge the audience, set the session's energy. Mention logistics (timing, breaks, questions policy). Consider an icebreaker if the group is unfamiliar with each other.
- **Engagement**: Ask participants to briefly share their name and one thing they hope to learn (for small groups) or do a quick poll (for large groups)
- **Timing**: 3-5 minutes

#### Agenda
- **Tone**: Organized, clear, forward-looking
- **Tactics**: Walk through each section briefly. Set expectations about pacing and breaks. Let participants know which sections will be most hands-on.
- **Engagement**: Ask which topics participants are most interested in — this helps the facilitator calibrate depth
- **Timing**: 2-3 minutes

#### Learning Objectives
- **Tone**: Purposeful, motivating
- **Tactics**: Read each objective aloud. Explain that these are the commitments the session makes to participants. Mention that you'll check in on these at the end.
- **Engagement**: Ask participants to mentally flag the objective most relevant to their current work
- **Timing**: 2-3 minutes

#### Section Divider
- **Tone**: Transitional, energizing
- **Tactics**: Use this as a reset moment. Briefly summarize what was just covered. Preview what's ahead. If it's been 20+ minutes, consider a stretch or bio break.
- **Engagement**: Quick check-in: "Before we move on — any burning questions from the last section?"
- **Timing**: 1-2 minutes

#### Key Concepts
- **Tone**: Clear, methodical, building understanding
- **Tactics**: Don't just read the cards. Introduce each concept, then give a concrete example or analogy. Build connections between the concepts. Use progressive disclosure — introduce the simplest concept first.
- **Engagement**: After presenting concepts, ask participants to identify which one is most relevant to their work, or which one they'd like to explore further
- **Timing**: 5-8 minutes depending on complexity

#### Full-Screen Image
- **Tone**: Visual, descriptive, analytical
- **Tactics**: Let the image land before talking. Give participants 5-10 seconds to take it in, then walk through what they're seeing. For architecture diagrams, trace the flow. For screenshots, point out the key elements.
- **Engagement**: "What do you notice first?" is a powerful opening question for visual slides
- **Timing**: 3-5 minutes

#### Step-by-Step Process
- **Tone**: Instructional, precise, supportive
- **Tactics**: Go through each step sequentially. For technical audiences, explain the *why* behind each step, not just the *what*. Mention what can go wrong at each step and how to recover.
- **Engagement**: Ask if anyone has done something similar and what their experience was
- **Timing**: 5-10 minutes depending on steps

#### Video Tutorial
- **Tone**: Transitional, contextualizing
- **Tactics**: Set up the video with a brief explanation of what participants should watch for. After the video, pause for reactions and questions. Don't just play the video and move on — the debrief is where learning happens.
- **Engagement**: Give participants a "watch for" question before playing the video. After: "What stood out to you?"
- **Timing**: Video length + 3-5 minutes for setup/debrief

#### Code/Demo
- **Tone**: Technical, precise, exploratory
- **Tactics**: Walk through the code line by line for critical sections. Highlight the patterns, not just the syntax. If doing a live demo, have a backup plan (screenshot, pre-recorded) in case of technical issues. Narrate what you're doing as you do it.
- **Engagement**: "What do you think this line does?" before explaining. Invite participants to predict outputs.
- **Timing**: 5-10 minutes

#### Comparison
- **Tone**: Analytical, balanced, decisive
- **Tactics**: Present both sides fairly before revealing which is preferred (if applicable). Use the comparison to reinforce why the new approach is better, but acknowledge the old approach's strengths.
- **Engagement**: Ask participants which side they've experienced. "How many of you are currently doing it the 'before' way?"
- **Timing**: 4-6 minutes

#### Knowledge Check — Multiple Choice
- **Tone**: Encouraging, low-stakes, educational
- **Tactics**: Read the question aloud. Give participants 30-60 seconds to think. Ask for a show of hands or use a poll. Reveal the answer and explain *why* it's correct and why the distractors are wrong. Never shame wrong answers — use them as teaching moments.
- **Engagement**: "Who's confident in their answer? Who wants to change after hearing others?" Build a safe environment for being wrong.
- **Timing**: 3-5 minutes

#### Knowledge Check — True/False
- **Tone**: Quick, punchy, clarifying
- **Tactics**: Read the statement. Quick show of hands. Explain the answer. These are great for busting common misconceptions — lean into the surprise factor if most people get it wrong.
- **Engagement**: "Raise your hand if you think this is true... now if you think it's false... interesting split! Let's find out."
- **Timing**: 2-3 minutes

#### Knowledge Check — Discussion
- **Tone**: Open, curious, collaborative
- **Tactics**: Read the prompt. Give 2-3 minutes for small group discussion, then bring it back to the full group. Don't call on people randomly — ask for volunteers, then gently invite quieter groups. Synthesize the key themes.
- **Engagement**: Use think-pair-share. Circulate during small group time to listen and identify interesting points to surface.
- **Timing**: 8-12 minutes

#### Knowledge Check — Hands-On Exercise
- **Tone**: Supportive, practical, patient
- **Tactics**: Read the instructions clearly. Confirm everyone has the necessary tools/access before starting the timer. Circulate during the exercise to check on progress, answer questions, and note common struggles. Have a "done early?" extension task ready.
- **Engagement**: Active facilitation during the exercise is the engagement. Don't sit down — walk the room (or monitor chat in virtual).
- **Timing**: As specified on the slide + 5 minutes for debrief

#### Reflection
- **Tone**: Quiet, introspective, respectful
- **Tactics**: Give participants genuine quiet time (3-5 minutes). Resist the urge to fill the silence. Optionally invite 2-3 volunteers to share one reflection. This slide consolidates learning — it's not filler.
- **Engagement**: Provide sticky notes, a digital whiteboard, or a shared doc for capturing reflections. Pair sharing can help quieter participants process.
- **Timing**: 5-8 minutes

#### Key Takeaways
- **Tone**: Confident, reinforcing, forward-looking
- **Tactics**: Read each takeaway and connect it back to the learning objectives. This is the "bookend" moment — participants should feel the arc from objectives to takeaways.
- **Engagement**: Ask participants to identify which takeaway resonates most with them
- **Timing**: 3-4 minutes

#### Resources & Next Steps
- **Tone**: Practical, supportive, empowering
- **Tactics**: Walk through the resources briefly — don't just read URLs. Explain what each resource is good for. Emphasize the action items and any deadlines.
- **Engagement**: Ask participants to commit to one specific next step they'll take within 48 hours
- **Timing**: 3-5 minutes

#### Closing
- **Tone**: Appreciative, open, encouraging
- **Tactics**: Thank participants for their time and engagement. Open the floor for final questions. Remind them about the feedback form and why their feedback matters. Share your contact info for follow-up questions.
- **Engagement**: Final open Q&A. If time permits, ask: "What's one thing you'll do differently starting tomorrow?"
- **Timing**: 5-10 minutes

---

## Step 4: Write the Front Matter

Before the slide-by-slide sections, the guide needs front matter that helps the facilitator prepare:

### Training Overview
- **Training title** (from the title slide)
- **Feature covered** (from the deck content)
- **Target audience** (from the profile)
- **Estimated duration** — calculate from the slide count using these estimates:
  - Title/Agenda/Objectives/Closing: 2-3 min each
  - Section Dividers: 1-2 min each
  - Content slides (Key Concepts, Process, Code, Comparison, Image): 5-8 min each
  - Video slides: video duration + 3-5 min
  - Knowledge Checks (MC, T/F): 3-5 min each
  - Knowledge Checks (Discussion): 8-12 min
  - Knowledge Checks (Hands-On): as specified + 5 min debrief
  - Reflection: 5-8 min
  - Key Takeaways/Resources: 3-5 min each
- **Learning objectives** (from the objectives slide)

### Pre-Session Checklist
Generate a preparation checklist tailored to the specific deck content:

- Room/virtual setup requirements
- Technology checks (projector, screen sharing, audio for videos)
- Materials needed (handouts, sticky notes, access credentials for hands-on exercises)
- Pre-work or prerequisites for participants
- Backup plans for demos/technical content
- Any files, links, or credentials participants need access to

### Facilitation Principles (Adult Learning Reminder)
A brief (half-page) reminder of the adult learning principles that underpin the guide's recommendations:

- **Relevance**: Adults learn best when they understand why the content matters to their work. Connect every concept to real application.
- **Experience**: Adults bring existing knowledge. Leverage it through questions and discussion rather than lecturing as if they're blank slates.
- **Self-direction**: Adults want to control their learning. Offer choices where possible (discussion topics, exercise approaches).
- **Problem-centered**: Adults engage with problems more than abstract theory. Use scenarios and real-world examples.
- **Respect**: Adults need to feel their time is valued. Keep the pace brisk, cut what isn't essential, and never talk down.

---

## Step 5: Write the Back Matter

After all slide sections, include:

### Session Timing Summary
A one-page table showing every slide with its estimated duration, running total, and a "checkpoint" column the facilitator can use to track pacing during delivery.

| Slide | Title | Type | Est. Time | Running Total | On Track? |
|-------|-------|------|-----------|---------------|-----------|
| 1 | [Title] | Title | 3 min | 3 min | |
| 2 | [Title] | Agenda | 2 min | 5 min | |
| ... | ... | ... | ... | ... | |

### Troubleshooting & Contingency Plans
Common issues and what to do:

- **Demo/code fails**: Switch to the screenshot backup, walk through the code conceptually
- **Running behind schedule**: Identify which slides can be abbreviated (typically second knowledge checks and one comparison slide)
- **Audience is disengaged**: Insert an unplanned think-pair-share or "what's your experience" question
- **Audience is more/less technical than expected**: Guidance on adjusting depth on the fly
- **Questions you can't answer**: "Great question — I'll follow up after the session" is always acceptable. Note it down visibly.

### Feedback and Follow-Up
- How to collect feedback (reference the feedback form from the closing slide)
- Suggested follow-up timeline (1-week check-in, 30-day follow-up)
- How to handle post-session questions

---

## Step 6: Build the Word Document

Use the docx skill's creation workflow (`docx-js`) to produce a professionally formatted .docx. Apply Anthropic brand styling from the brand-guidelines skill.

### Document Design

**Page setup:**
- US Letter (8.5" x 11")
- 1" margins all around
- Headers: Training title (left) + "Facilitator Guide" (right)
- Footers: Page numbers (centered)

**Typography** (from brand guidelines):
- Headings: Styrene A (fallback: Arial) — bold, Anthropic dark (`#141413`)
- Body text: Lora (fallback: Georgia) — regular, Anthropic dark
- Slide content quotes: Lora italic, mid gray (`#B0AEA5`)
- Code/commands: Courier New — regular
- Timing callouts: Styrene A, orange accent (`#D97757`)

**Color usage:**
- Section divider rows in tables: Light gray background (`#E8E6DC`). Note: the PPTX template includes 6 chapter divider color variants (Olive Green `#788C5D`, Dusty Rose `#B5758A`, Lavender `#9D8FBF`, Cornflower Blue `#7EA5CB`, Sage Mint `#ADBEB0`, Warm Sand `#CCC0AB`)
- Key concept emphasis boxes: Light background with orange left border
- Engagement prompt boxes: Light background with blue left border (`#6A9BCC`)
- Activity instruction boxes: Light background with green left border (`#788C5D`)
- Timing badges: Orange accent text

**Structure:**
- Title page with training title, audience, date, and Anthropic branding
- Table of contents
- Front matter sections
- Slide-by-slide guide (each slide starts on a new section, clearly numbered)
- Back matter sections

### Per-Slide Layout in the Document

For each slide section, use this visual layout:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SLIDE 3: Learning Objectives                  ⏱ 2-3 min
(Learning Objectives slide)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRESENTER NOTES (from the deck)
┃ [Complete, verbatim presenter notes from the .pptx,
┃ in a gray-background block so they're visually distinct]

ADDITIONAL FACILITATION TIPS
[Supplementary guidance that builds on the notes above —
audience-specific adjustments, deeper context, warnings]

KEY CONCEPTS TO EMPHASIZE
▸ [Concept 1] — [Why it matters for this audience]
▸ [Concept 2] — [Why it matters for this audience]

FACILITATION TACTICS
[Delivery approach, pacing, voice/energy guidance,
common pitfalls to avoid]

AUDIENCE ENGAGEMENT
┃ [Exact question to ask or engagement technique]
┃ [Second engagement prompt]

TRANSITION → NEXT SLIDE
"[Transition language to bridge to the next slide]"
```

This layout should be achieved through a combination of heading styles, bordered text boxes (using table cells with accent-colored left borders), and consistent spacing. The presenter notes block uses a gray background to visually separate the deck author's original notes from the guide's added facilitation content. The goal is a document that a facilitator can glance at mid-session and immediately find what they need.

### Naming Convention

Name the output file: `Facilitator_Guide_[Feature]_[Profile].docx`

Examples:
- `Facilitator_Guide_MCP_Developers.docx`
- `Facilitator_Guide_Skills_Enterprise_Champions.docx`

Save the output to the `Deliverables/` folder in the workspace root (the same location where
training decks are stored). If the `Deliverables/` folder doesn't exist, create it.

---

## Step 7: Quality Assurance

### Content QA
1. **Completeness check — this is the most important QA step**: Count the total slides in the .pptx (use markitdown output). Count the slide sections in the guide. These numbers must be identical. If the deck has 28 slides, the guide must have exactly 28 slide sections — no more, no fewer. Open the .docx and verify slide sections exist for slide 1 through slide N with no gaps.
2. **Notes fidelity**: Compare the presenter notes in the guide against the raw markitdown output from the .pptx. The notes in the guide should be verbatim — not paraphrased, not summarized, not truncated. Check at least 3-4 slides to confirm.
3. **Additional tips distinction**: Verify that the "Additional Facilitation Tips" content is clearly separated from the presenter notes, both visually (different styling) and in language (should reference or build on the notes, not repeat them).
4. **Audience alignment**: Verify the facilitation guidance matches the identified audience profile. Developer-focused guides shouldn't have selling language; Champion-focused guides shouldn't have deep code walkthroughs.
5. **Timing sanity**: Add up all the per-slide timing estimates and compare to the total estimated duration in the front matter. They should be within 5 minutes of each other.

### Visual QA
Convert the .docx to images and inspect:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.docx
pdftoppm -jpeg -r 150 output.pdf page
```

Check for:
- Consistent heading styles throughout
- Proper brand colors on accent elements
- Presenter notes blocks are visually distinct (gray background) from the additional facilitation tips
- No text overflow in bordered boxes
- Clean page breaks (no orphaned headers at page bottoms)
- Table formatting is consistent
- Title page looks professional

### Usability QA
Read through 3-4 slide sections as if you were a facilitator about to deliver the training. Ask yourself:
- Can I find the timing estimate instantly?
- Are the engagement prompts specific enough to actually use?
- Do the key concepts give me genuine insight beyond what's on the slide?
- Would the transition language actually work spoken aloud?

---

## Adult Learning Principles Reference

These principles from Knowles' andragogy and related research should inform every facilitation recommendation in the guide:

**The Need to Know**: Adults need to understand *why* they should learn something before investing effort. Every slide section's "Key Concepts to Emphasize" should include the why, not just the what.

**Self-Concept**: Adults see themselves as responsible for their own decisions. Facilitation guidance should respect autonomy — suggest, don't dictate. "Consider asking..." rather than "You must ask..."

**Prior Experience**: Adults bring a wealth of experience that is both a resource and a potential source of bias. Engagement techniques should tap into this experience ("How does this compare to your current approach?") while gently challenging assumptions where the new content diverges from past practice.

**Readiness to Learn**: Adults are most ready to learn things they need to know to cope with real-life situations. Facilitation notes should consistently connect content to participants' actual work contexts.

**Orientation to Learning**: Adults are problem-centered, not subject-centered. Frame content around problems it solves, not abstract capabilities.

**Motivation**: Internal motivation (personal growth, job satisfaction, self-esteem) is more powerful than external motivation. Engagement prompts should tap into intrinsic motivators when possible.

**Cognitive Load**: Working memory is limited. The guide should recommend chunking complex content, using visuals to reinforce verbal explanations, and building in processing time (think-pair-share, reflection) after dense material.

**Psychological Safety**: Adults won't participate if they fear looking foolish. Knowledge check facilitation should always normalize wrong answers and emphasize learning over performance.
