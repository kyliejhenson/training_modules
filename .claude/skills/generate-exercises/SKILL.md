---
name: generate-exercises
description: >
  Generate a branded hands-on exercise document (.docx) from a training deck's Sources manifest.
  Use this skill whenever the user wants to create exercises, labs, practice activities, hands-on
  worksheets, or participant workbooks for a training module. Also trigger when the user mentions
  'generate exercises', 'create exercises', 'hands-on lab', 'practice activity', 'participant
  exercises', 'exercise workbook', 'training exercises', or asks how participants can apply what
  they learned from a training deck. This skill reads the Training_[Feature]_[Profile]_Sources.md
  file to ensure exercises are grounded in the same content the training covered, then produces
  audience-appropriate exercises as a branded Anthropic Word document.
---

# Generate Hands-On Exercises

## What This Skill Does

Takes a `Training_[Feature]_[Profile]_Sources.md` file (the content manifest produced by the
generate-training skill) and creates a branded `.docx` exercise document with step-by-step
activities that let participants practice what they learned. Every exercise draws directly from
the source content that was used to build the training deck, so participants are reinforcing
material they've already been introduced to — not encountering new concepts for the first time.

The output is a single Word document containing multiple exercises, sequenced to follow the
training flow, with each exercise tailored to the audience profile's role and use cases.

## When to Use This Skill

- After a training deck has been generated (and ideally reviewed) via generate-training
- When the user has a `Training_[Feature]_[Profile]_Sources.md` file available
- When the user wants participants to have something to work through during or after training

## Inputs

**Required:**
- `Training_[Feature]_[Profile]_Sources.md` — the content sources manifest from generate-training

**Automatically resolved from the Sources.md:**
- The audience profile (from `Profiles/` directory)
- The source content sections (from `Content/` directory)

## Step-by-Step Workflow

### Step 1: Identify the Sources File

Ask the user which Sources.md file to use. If there's only one in the workspace, confirm it.
Extract the Feature and Profile from the filename pattern `Training_[Feature]_[Profile]_Sources.md`.

### Step 2: Load Context

Read three things:

1. **The Sources.md itself** — parse the "Source Content Files" table to get the list of
   content section file paths and which slides they mapped to.

2. **The audience profile** — load from `Profiles/profile-[name].md`. Pay close attention to:
   - `Technical Skill Level` — determines exercise complexity
   - `Use Case Types` — determines what kinds of scenarios feel relevant
   - `Needs Technical Application Practice` — if No, skip code/config exercises entirely
     and focus on scenario-based and guided-exploration exercises instead
   - `Needs Value-Based Selling Information` — if Yes, include exercises about positioning
     and articulating value, not just technical tasks
   - `Role Summary` — this tells you what the person actually does day-to-day, which is
     the key to writing scenarios that feel real to them

3. **The source content sections** — read each content file listed in the Sources.md table.
   These contain the actual concepts, procedures, code examples, and reference material that
   the exercises should draw from. Pay attention to each section's tags, especially:
   - `Instructional Priority: Applied` sections are the richest source of exercise material
   - `Technical Application Practice: Yes` sections often already contain procedural steps
     you can adapt into exercises
   - `Instructional Priority: Foundational` sections provide context but are better as
     setup/background for exercises than as exercise topics themselves

### Step 3: Design the Exercise Set

Plan the exercises before writing them. A good exercise set for a training deck typically has
3-6 exercises depending on content volume and audience. Consider:

**Sequencing**: Follow the training deck's flow. If the deck teaches concept A before concept B,
the exercises should practice A before B. Use the slide mapping from Sources.md to determine order.

**Exercise type selection** depends on the content and audience:

| Content characteristic | Best exercise type | When to use |
|----------------------|-------------------|-------------|
| Step-by-step procedures, CLI commands, config syntax | **Guided Walkthrough** | When the content has concrete steps participants can follow and verify |
| Real-world integration patterns, decision points | **Scenario-Based Challenge** | When participants need to apply judgment, not just follow steps |
| Code examples, API calls, file structures | **Code/Config Exercise** | When the audience has `Technical Application Practice: Yes` |

**Audience adaptation** — this is critical. The same underlying content should produce very
different exercises depending on who's doing them:

- **Developers**: Deep technical exercises. Multi-step builds, debugging challenges, code that
  must actually work. They want to get their hands dirty with implementation details.

- **Solutions Engineers**: Technical exercises with a customer lens. "A customer asks you to..."
  framing. Include both the technical execution AND how to explain what you did and why.

- **Solutions Partners**: Moderate technical depth but broader scope. Exercises that span
  architecture decisions, implementation guidance, and communicating value to stakeholders.

- **Enterprise Champions**: No code exercises. Instead, scenario-based activities about
  evaluating tools, building business cases, planning rollouts, and articulating value to
  executives. Think "advisor exercises" not "builder exercises."

### Step 4: Write Each Exercise

Every exercise follows this structure:

#### Exercise Header
- **Exercise number and title** — descriptive, action-oriented (e.g., "Exercise 3: Configure
  OAuth Authentication for a Remote MCP Server")
- **Objective** — one sentence stating what the participant will be able to do after completing
  this exercise
- **Estimated time** — realistic estimate (10-30 minutes per exercise typically)
- **What you'll need** — prerequisites, tools, access requirements
- **Difficulty** — Beginner / Intermediate / Advanced (aligned with profile skill level)

#### Scenario (for scenario-based and guided exercises)
A 2-4 sentence setup that puts the participant in a realistic situation relevant to their role.
Use the profile's Role Summary to craft scenarios that feel like actual work situations, not
contrived classroom examples.

Good scenario for a Developer:
> "Your team is building a Claude-powered code review tool. You need to add an MCP server
> that gives Claude access to your GitHub repositories so it can read pull request diffs."

Good scenario for an Enterprise Champion:
> "Your CTO has asked you to evaluate whether Claude Code's MCP integration can replace
> three separate vendor tools your engineering teams currently use. You need to assess
> capabilities and build a recommendation."

#### Step-by-Step Instructions
Numbered steps that guide the participant through the exercise. Each step should:

- **Be specific and verifiable** — the participant should know when they've completed each step.
  "Configure the server" is too vague. "Add the following to your claude_config.json" is specific.
- **Include the actual content** — don't just reference the training material abstractly.
  If the exercise involves writing a configuration file, show the structure. If it involves
  running a command, show the command.
- **Build progressively** — early steps set up, middle steps do the core work, later steps
  verify and extend.
- **Include checkpoint moments** — after key steps, tell participants what they should see
  or be able to verify. "At this point, you should see three tools listed in the output."

For **Guided Walkthroughs**: Steps are detailed and explicit. Participants follow along.
Include exact commands, expected outputs, and what to do if something doesn't match.

For **Scenario-Based Challenges**: Steps are higher-level. Give the goal and constraints,
provide hints, but let participants figure out the approach. Include a "Solution Approach"
section at the end they can check against.

For **Code/Config Exercises**: Provide starter code or templates where helpful, but have
participants write the key parts themselves. Include expected output to validate against.

#### Success Criteria
A short checklist (3-5 items) that participants can use to verify they completed the exercise
correctly. These should be observable outcomes, not subjective assessments.

- "The MCP server appears in your `claude mcp list` output"
- "Your skill triggers when you type 'help me review this PR'"
- "The configuration file passes validation with no errors"

For non-technical exercises (Enterprise Champions), success criteria are about deliverable
completeness:
- "Your recommendation memo includes at least 3 specific capability comparisons"
- "Your rollout plan covers all 4 phases discussed in the training"

#### Bonus Challenge (Optional)
A stretch goal for participants who finish early. Should extend the exercise in a meaningful
direction, not just repeat it with different inputs. This is also useful for mixed-ability
groups — faster participants have something to do while others catch up.

### Step 5: Write the Document Front Matter

Before the exercises, include:

1. **Title page** — "Hands-On Exercises: [Feature] for [Profile]"
2. **Overview** — 2-3 sentences on what these exercises cover and how they connect to the training
3. **Before You Begin** — any setup, prerequisites, or environment requirements that apply to
   all exercises (install a tool, clone a repo, ensure access to something)
4. **How to Use This Document** — brief guidance: work through exercises in order, they build
   on each other, estimated total time, it's OK to refer back to training materials

### Step 6: Build the Word Document

Use the docx skill to create a branded Anthropic Word document. Read the docx SKILL.md for
the technical workflow (either docx-js creation or unpack/edit/repack for templates).

**Document styling requirements:**

- **Page size**: US Letter (8.5" x 11"), portrait orientation
- **Margins**: 1" all sides
- **Colors**: Use Anthropic brand palette
  - Headings: Dark `#141413`
  - Body text: Dark `#141413`
  - Accent elements (exercise headers, divider lines): Orange `#D97757`
  - Hint/tip boxes: Light Gray `#E8E6DC` background
  - Code blocks: Dark `#141413` background with Light `#FAF9F5` text
  - Success criteria checkboxes: Green `#788C5D`
  - Bonus challenge: Blue `#6A9BCC` accent
- **Typography**:
  - Document title: Styrene A / Arial, 28pt, bold
  - Exercise titles: Styrene A / Arial, 20pt, bold
  - Section headers (Objective, Scenario, Steps, etc.): Styrene A / Arial, 14pt, bold
  - Body text: Lora / Georgia, 11pt, regular
  - Code/commands: Courier New, 10pt
  - Step numbers: Styrene A / Arial, 11pt, bold, Orange accent
- **Exercise separation**: Page break before each new exercise
- **Code blocks**: Gray background (#E8E6DC), dark text, Courier New font, with adequate
  padding. For multi-line code, preserve formatting exactly.
- **Tip/Note callouts**: Light gray background box with "Tip:" or "Note:" prefix in bold
- **Success criteria**: Presented as a checkbox list (empty checkboxes participants can check off)

### Step 7: Quality Assurance

Before delivering, verify:

1. **Content grounding**: Every exercise traces back to at least one content section from the
   Sources.md. No exercise introduces concepts that weren't in the training.

2. **Audience fit**: Exercise types and complexity match the profile. No code exercises for
   Enterprise Champions. No oversimplified exercises for Developers.

3. **Completeness**: Every step is specific enough to follow without guessing. Commands include
   expected output. Configurations include the full structure needed.

4. **Progressive flow**: Exercises build in complexity. The first exercise is approachable,
   the last exercise is challenging.

5. **Time realism**: Total exercise time is reasonable for a training session (typically
   45-90 minutes of exercises for a full training deck).

6. **No placeholders**: No `[TODO]`, `[INSERT]`, or `<placeholder>` text anywhere. Every field
   is populated with real content.

7. **Self-contained**: A participant with the stated prerequisites should be able to complete
   every exercise using only this document and the tools listed in "What You'll Need." They
   shouldn't need to hunt through other materials.

Save the final document as `Exercises_[Feature]_[Profile].docx` in the `Deliverables/` folder
in the workspace root (the same location where training decks are stored). If the `Deliverables/`
folder doesn't exist, create it.

## Output Naming

`Exercises_[Feature]_[Profile].docx`

Example: `Exercises_MCP_Developers.docx`

## Reference: Exercise Type Templates

See `references/exercise-templates.md` for detailed structural templates for each exercise type,
with examples drawn from MCP and Skills content.
