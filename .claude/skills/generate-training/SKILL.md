---
name: generate-training
description: "Generate a branded training PowerPoint from the Anthropic_Training_Template.pptx. Use this skill whenever the user wants to create a training deck, training presentation, training module, or training slides about a Claude Code feature. Also trigger when the user mentions 'training powerpoint', 'training pptx', 'generate training', 'create training deck', or references the Anthropic training template. This skill handles audience selection, content filtering by profile tags, and presenter notes generation — producing a text-complete training presentation. Images and video links are added separately using the add-training-media skill after the user reviews the text content."
---

# Training PowerPoint Generator

This skill generates branded training presentations using the Anthropic_Training_Template.pptx. It selects content based on audience profile tags and writes presenter notes for every slide.

**Note on media**: This skill intentionally does NOT insert images or add clickable video links. All media operations — image insertion, video hyperlinks, and visual polish — are handled by the separate `add-training-media` skill, which runs after you've reviewed and approved the text content. This two-step approach produces much more reliable results because media insertion requires careful XML coordination that works best as a focused pass.

## Important: Read the PPTX Skill First

Before doing anything else, read the pptx SKILL.md file at the skill location for pptx (check available skills). The pptx skill contains the template editing workflow, scripts, QA process, and formatting rules you must follow. This skill builds on top of the pptx skill — it provides the *what* (content selection, audience matching, structure), while the pptx skill provides the *how* (XML editing, slide operations, visual QA).

Also read the TEMPLATE_GUIDE.md file in the workspace root — it contains the complete slide inventory, brand specs, population guide, and presenter notes format for the Anthropic training template.

---

## Step 1: Ask the User Two Questions

Before generating anything, ask the user two questions using AskUserQuestion. You need to know the **audience profile** and the **feature topic**.

### Question 1: Which Profile?

Scan the `Profiles/` folder in the workspace to discover available profiles. Each profile is a markdown file named `profile-<name>.md`. Present the available profiles as options.

Read each profile file to extract the role summary for the option description.

Example (the actual options depend on what's in the folder):

```
Question: "Which audience profile is this training for?"
Options based on files found in Profiles/ folder, e.g.:
- Developers — Engineers building applications and integrations with Claude
- Enterprise Champions — Internal advocates driving Claude adoption
- Solutions Engineers — Technical experts bridging product capabilities with customer needs
- Solutions Partners — External partners helping enterprise customers implement Claude
```

### Question 2: Which Feature?

Scan the `Content/` folder to discover available feature topics. Each subfolder in Content/ (e.g., `content_mcp`, `content_skills`) represents a feature. Present these as options.

Read the `00_content_index.md` in each feature folder to get the feature name for the option description.

```
Question: "Which feature should the training cover?"
Options based on subfolders found in Content/, e.g.:
- MCP (Model Context Protocol) — Based on content_mcp/
- Skills — Based on content_skills/
```

---

## Step 2: Load the Profile and Filter Content

### Load the Profile

Read the selected profile file from `Profiles/`. Extract these tag values:

- **Technical Skill Level** (e.g., Advanced, Intermediate, Beginner)
- **Use Case Types** (list, e.g., Technical implementation, Security & compliance)
- **Needs Technical Application Practice** (Yes/No)
- **Needs Value-Based Selling Information** (Yes/No)

### Load the Content Index

Read `00_content_index.md` from the selected feature's Content subfolder. This index lists every content section with its tags:

- File path
- Concept summary
- Skill Level
- Use Case Types

### Filter Content by Profile Tags

A content section matches a profile when ALL of these are true:

1. **Skill Level**: The content's skill level must be at or below the profile's level.
   - Profile = Advanced: matches Advanced, Intermediate, and Beginner content
   - Profile = Intermediate: matches Intermediate and Beginner content
   - Profile = Beginner: matches only Beginner content

2. **Use Case Types**: At least one of the content's use case types must appear in the profile's use case types list.

### Handle Partial Matches

If some content sections match the feature but NOT the profile tags, present the user with what was found and what was excluded. Show them both lists and ask which excluded content (if any) they'd like to include anyway. This lets the user make informed decisions about edge cases rather than silently dropping content.

---

## Step 3: Plan the Slide Deck

The deck structure should be **fully dynamic** — driven by the filtered content, not a fixed outline. The only constraints are:

- The template's required slides (Title, Key Takeaways, Resources & Next Steps, Closing) must be included
- Beyond those, generate slides based on the volume and type of matched content

### Slide Type Selection

Map each content section to the most appropriate template slide type based on the content's nature:

| Content Nature | Template Slide Type |
|---------------|-------------------|
| Definitions, terminology, conceptual overviews | Key Concepts (Slide 5) |
| Step-by-step procedures, setup guides | Step-by-Step Process (Slide 7) |
| Code examples, API usage, CLI commands | Code/Demo (Slide 9) |
| Before/after, comparing approaches | Comparison (Slide 10) |
| Visual diagrams, screenshots, architecture | Full-Screen Image (Slides 6, 11) |
| Video tutorials available for the topic | Video Tutorial (Slides 8, 12) |

### Group Content into Sections

Group related content sections into logical training sections. Create a Section Divider slide before each group using one of the 6 chapter divider slides (Slide 4: Olive Green, Slide 21: Dusty Rose, Slide 22: Lavender, Slide 23: Cornflower Blue, Slide 24: Sage Mint, Slide 25: Warm Sand). Assign a different color to each section for visual variety. Aim for 2-4 major sections depending on content volume.

### Add Knowledge Checks

After every 10-15 minutes of content (roughly every 3-5 content slides), insert a knowledge check. Vary the types:

- Multiple Choice (Slide 13) for factual recall
- True/False (Slide 14) for quick concept checks
- Discussion (Slide 15) for deeper exploration
- Hands-On Exercise (Slide 16) only if profile has `Needs Technical Application Practice: Yes`

### Add a Reflection Slide

Include the Reflection slide (Slide 17) before Key Takeaways. Customize the four reflection prompts to match the specific feature being trained.

### Scale the Deck

Do not apply fixed slide count limits. Create as many slides as the topic needs to be covered thoroughly within a reasonable training session length. Let the matched content drive the deck size — if the content requires 40 slides to teach well, build 40 slides. Where closely related sections can be combined onto a single slide without losing clarity, do so, but never drop or compress content just to hit an arbitrary count.

---

## Step 4: Write Presenter Notes

Every slide must have customized presenter notes. Use only the slide name as a header before the Say and Do sections — do not include decorative text like "PRESENTER NOTES -- KEY CONCEPTS" or dashed separator lines.

```
[Slide Name]
Say:
[Verbatim script of what the facilitator should say.]

Do:
- [Action the facilitator should take.]
```

### What to Include in Notes

1. **Talking points** derived from the content sections mapped to that slide. The slide shows a summary; the notes contain the full context the presenter needs.
2. **Timing guidance** — estimate minutes for the slide.
3. **Engagement prompts** — questions to ask the audience.
4. **Transition language** — how to connect to the next slide.
5. **Correct answers** — for knowledge check slides, include the answer and explain why.
6. **Facilitation tips** — for discussion and hands-on slides, include guidance on managing the activity.

### Audience-Specific Note Adjustments

Tailor the depth and focus of presenter notes based on the profile:

- **Developers**: Emphasize technical details, code walkthrough guidance, implementation tips
- **Enterprise Champions**: Emphasize business value framing, change management talking points, ROI discussion guidance
- **Solutions Engineers**: Balance technical depth with value positioning, include customer scenario handling
- **Solutions Partners**: Include client conversation guidance, implementation advisory tips, lifecycle context

---

## Step 5: Build the Presentation

Now use the pptx skill's template editing workflow to build the actual .pptx file:

1. **Analyze the template**: Run thumbnail.py and markitdown on `Anthropic_Training_Template.pptx`
2. **Unpack**: Use unpack.py to extract the template
3. **Structural changes**:
   - Duplicate slides as needed using add_slide.py
   - Remove unneeded slides
   - Reorder slides in presentation.xml to match your planned structure
4. **Content population**: Edit each slide's XML to replace all bracketed placeholders with actual content, including video slide text (titles, descriptions, URLs). Use the Edit tool, not sed or scripts.
   - **Header capitalization**: Only capitalize the first word of a header unless it contains a proper noun. For example, write "Core skills concepts" not "Core Skills Concepts"; but "Understanding Claude Code" keeps "Claude Code" capitalized.
5. **Presenter notes**: Add notes to each slide's notes XML
6. **Clean and pack**: Run clean.py then pack.py to produce the final .pptx

**Do NOT insert images or add hyperlinks to video slides.** Leave all media placeholders as-is. The `add-training-media` skill handles image insertion and making video elements clickable in a separate pass.

### Naming Convention

Name the output file: `Training_[Feature]_[Profile].pptx`

Examples:
- `Training_MCP_Developers.pptx`
- `Training_Skills_Enterprise_Champions.pptx`

Save the output to the workspace folder.

---

## Step 6: Quality Assurance

Follow the pptx skill's QA process:

1. **Content QA**: Run markitdown on the output and check for:
   - Any remaining `[BRACKETED PLACEHOLDERS]`
   - Missing content sections
   - Typos or formatting errors

2. **Visual QA**: Convert to images and inspect for:
   - Overlapping elements
   - Text overflow
   - Proper brand colors and fonts

3. **Verify presenter notes**: Check that every slide has customized notes (not template defaults).

4. **Verify content-profile alignment**: Confirm that only content matching the selected profile's tags was included (plus any user-approved exceptions).

---

## Step 7: Finalize Deliverables

After QA passes, perform these two finalization steps before presenting to the user:

### 7a: Copy to Deliverables

Copy the finished `.pptx` file into the `Deliverables/` folder in the workspace root. This folder is the canonical location for all completed training outputs. If the `Deliverables/` folder doesn't exist, create it.

```
cp Training_[Feature]_[Profile].pptx Deliverables/
```

### 7b: Generate a Content Sources Manifest

Create a markdown file that lists every source content file used to build the training deck. Name it to match the deck: `Training_[Feature]_[Profile]_Sources.md` and save it alongside the deck in the `Deliverables/` folder.

The file should contain:

```markdown
# Content Sources: Training_[Feature]_[Profile]

**Audience Profile**: [Profile name]
**Feature Topic**: [Feature name]
**Generated**: [Date]

## Source Content Files

| # | Content File | Concept Summary | Slide(s) Used In |
|---|-------------|-----------------|------------------|
| 1 | Content/content_[feature]/[subfolder]/[file].md | [Brief concept description] | Slide [N] |
| 2 | ... | ... | ... |

## Excluded Content (Did Not Match Profile)

| # | Content File | Reason Excluded |
|---|-------------|-----------------|
| 1 | ... | Skill level too high / No use case overlap |
```

List every content section from the `00_content_index.md` that was included, mapping each to the slide(s) it fed into. Also list any sections that were excluded during profile filtering, with the reason. This provides a complete audit trail from source content to finished deck.

### 7c: Update the Deliverable Registry

Read (or create) `.content-monitor/deliverable-registry.json`. Add an entry for this deliverable so the `content-refresh` skill can trace content changes back to affected slides. The entry should capture the same content-to-slide mapping from Step 7b in a structured format.

If the registry file doesn't exist, create it with this structure:

```json
{
  "metadata": {
    "description": "Maps each deliverable PPTX to the content sections and slides that use them.",
    "last_updated": "[today's date]"
  },
  "deliverables": []
}
```

Append a new entry to the `deliverables` array:

```json
{
  "file": "Deliverables/Training_[Feature]_[Profile].pptx",
  "feature": "content_[feature]",
  "profile": "[profile name]",
  "generated_date": "[today's date]",
  "content_map": [
    {
      "section": "[subfolder]/[filename].md",
      "slides": [5, 6],
      "usage": "[Brief description of how this content was used on these slides]"
    }
  ]
}
```

If the registry already has an entry for the same deliverable file path (i.e., the deck is being regenerated), replace the existing entry with the new one. Update the `metadata.last_updated` field.

---

## Step 8: Present to User and Suggest Media Insertion

After finalization, present both the finished `.pptx` file and the content sources manifest from the `Deliverables/` folder to the user so they can access them directly. Then ask them to review the text content. Frame it clearly as a text-complete draft that's ready for media:

> "Here's your training deck with all the text content, presenter notes, and structure in place. The slides still have placeholder images and the video slides aren't clickable yet — take a look at the content and let me know if you're happy with it. Once you're satisfied, I can run the add-training-media skill to insert the actual screenshots and make the video links clickable."

Present both files using `computer://` links:
- `Deliverables/Training_[Feature]_[Profile].pptx` — the training deck
- `Deliverables/Training_[Feature]_[Profile]_Sources.md` — the content sources manifest

Wait for the user to confirm they're happy with the text content before suggesting they run the `add-training-media` skill. If they want changes, make them first, then re-suggest the media skill when they're satisfied.

---

## Reference: Content Tag Matching Quick Guide

| Profile | Skill Level | Use Case Types | Practice? | Selling? |
|---------|-------------|----------------|-----------|----------|
| Developers | Advanced | Technical implementation, Security & compliance, Evaluation & testing | Yes | No |
| Enterprise Champions | Intermediate | Security & compliance, Workflow integration, Business value & ROI, Adoption & change management | No | Yes |
| Solutions Engineers | Advanced | Technical implementation, Security & compliance, Workflow integration, Business value & ROI, Evaluation & testing | Yes | Yes |
| Solutions Partners | Intermediate | All six use case types | Yes | Yes |

This table is a quick reference — always read the actual profile files for authoritative tag values, since new profiles may be added.
