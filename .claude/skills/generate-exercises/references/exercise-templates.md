# Exercise Type Templates

This reference provides structural templates for each exercise type. When writing exercises,
adapt these structures to the specific content and audience rather than copying them rigidly.

## Guided Walkthrough Template

Best for: procedural content, CLI workflows, configuration tasks, first-time setup.
These exercises hold the participant's hand through each step so they build confidence with
new tools and workflows before being asked to problem-solve on their own.

### Structure

```
## Exercise N: [Action Verb] + [What They're Building/Configuring]

**Objective:** By the end of this exercise, you will be able to [specific observable skill].

**Estimated Time:** [15-25 minutes]

**What You'll Need:**
- [Tool/access requirement 1]
- [Tool/access requirement 2]

**Difficulty:** [Beginner / Intermediate / Advanced]

### Scenario
[2-4 sentences placing the participant in a realistic work situation that motivates
why they'd do this task.]

### Steps

**Step 1: [Setup action]**
[Explain what to do and why this step matters.]

    [command or code to run]

You should see:

    [expected output]

**Step 2: [Core action]**
[Explain the next step. If there's a decision point, explain what to consider.]

    [command, code, or configuration to write]

> **Tip:** [Helpful context that aids understanding, not just completion]

**Step 3: [Verification]**
[How to confirm the previous step worked.]

    [verification command]

**Checkpoint:** At this point, you should see [specific observable result]. If you see
[common error] instead, [what to do about it].

[Continue with remaining steps...]

### Success Criteria
- [ ] [Observable outcome 1]
- [ ] [Observable outcome 2]
- [ ] [Observable outcome 3]

### Bonus Challenge
[A meaningful extension that goes beyond the walkthrough. Should require some independent
thinking, not just repeating the same steps with different inputs.]
```

### Example: Guided Walkthrough for MCP (Developers)

> **Exercise 1: Add and Test a Remote MCP Server**
>
> **Objective:** By the end of this exercise, you will be able to add a remote HTTP MCP
> server to Claude Code and verify it's working by listing its available tools.
>
> **Estimated Time:** 15 minutes
>
> **What You'll Need:**
> - Claude Code installed and authenticated
> - Terminal access
> - A GitHub personal access token (read-only scope is fine)
>
> **Difficulty:** Intermediate
>
> **Scenario:**
> Your team wants Claude to be able to read and search your GitHub repositories directly.
> You'll add the GitHub MCP server so Claude can access repo content, pull requests, and
> issues during coding sessions.
>
> **Step 1: Add the GitHub MCP server**
> Run the following command, replacing `YOUR_TOKEN` with your GitHub personal access token:
>
>     claude mcp add github-server \
>       --transport http \
>       --url https://api.githubcopilot.com/mcp/ \
>       --header "Authorization: Bearer YOUR_TOKEN"
>
> You should see confirmation that the server was added.
>
> **Step 2: Verify the server appears in your configuration**
>
>     claude mcp list
>
> You should see `github-server` in the output with status "configured."
>
> [etc.]

---

## Scenario-Based Challenge Template

Best for: decision-making skills, architecture choices, integration planning, evaluation tasks.
These exercises describe a situation and desired outcome but let participants figure out the
approach themselves. Hints guide without giving away the answer.

### Structure

```
## Exercise N: [Challenge Framing — What They Need to Achieve]

**Objective:** By the end of this exercise, you will be able to [skill involving judgment
or problem-solving, not just execution].

**Estimated Time:** [20-30 minutes]

**What You'll Need:**
- [Tool/access requirement 1]
- [Any reference material they should have open]

**Difficulty:** [Intermediate / Advanced]

### The Scenario
[3-5 sentences describing a realistic situation with enough detail that the participant
understands the constraints, stakeholders, and success criteria. Include specific details
that make it feel real — team names, tool names, rough numbers.]

### Your Task
[Clear statement of what they need to produce or decide. Be specific about the deliverable
but not about the approach.]

### Constraints
- [Constraint that shapes their approach]
- [Another constraint]
- [Resource or time limitation]

### Hints (Use If Needed)

<details>
**Hint 1:** [Gentle nudge toward the right starting point]
</details>

<details>
**Hint 2:** [More specific guidance about a key concept from the training]
</details>

<details>
**Hint 3:** [Nearly gives away the approach but still requires them to execute]
</details>

### Success Criteria
- [ ] [Deliverable completeness check]
- [ ] [Quality check — addresses the scenario's constraints]
- [ ] [Shows understanding of the underlying concept]

### Solution Approach
[After participants attempt the exercise, they can read this section to compare their
approach. Don't present it as "the answer" — present it as one effective approach.
Explain the reasoning behind key decisions.]

### Bonus Challenge
[Introduce a complication to the scenario that requires adapting their solution.]
```

### Example: Scenario-Based Challenge for MCP (Solutions Engineers)

> **Exercise 3: Design an MCP Integration Architecture for a Customer**
>
> **Objective:** By the end of this exercise, you will be able to assess a customer's
> tool landscape and recommend which MCP servers to deploy, with justification.
>
> **Scenario:**
> Acme Corp's engineering team (40 developers) currently uses Jira for issue tracking,
> GitHub for source control, and Datadog for monitoring. They've purchased Claude Code
> team licenses and want Claude to have context from all three systems. Their security
> team requires that all external service connections use OAuth rather than static tokens,
> and they have a strict policy against stdio-based servers in production.
>
> **Your Task:**
> Prepare a one-page integration recommendation that specifies which MCP servers to add,
> the transport type for each, and how authentication should be configured. Include a brief
> rationale for each choice that you could present to the customer's security team.
>
> [etc.]

---

## Code/Config Exercise Template

Best for: audiences with `Technical Application Practice: Yes`, content with code examples,
API interactions, file structures. Participants write real code or configuration and validate
it works.

### Structure

```
## Exercise N: [Build/Write/Implement] + [What]

**Objective:** By the end of this exercise, you will have a working [thing] that [does what].

**Estimated Time:** [15-30 minutes]

**What You'll Need:**
- [Runtime/language requirement]
- [Editor or IDE]
- [Any packages to install]

**Difficulty:** [Intermediate / Advanced]

### Scenario
[Brief context for why they're writing this code.]

### Starter Code (if applicable)
[Provide a skeleton that handles boilerplate so participants focus on the interesting parts.
Clearly mark where they need to add code.]

    # [filename]
    [code with TODO comments marking where participants write code]

### Requirements
[Specific, testable requirements for what their code must do. Numbered list.]

1. [Requirement with specific input/output behavior]
2. [Requirement about error handling or edge cases]
3. [Requirement about structure or patterns to use]

### Steps

**Step 1: [First piece to implement]**
[Guidance on what to write, referencing concepts from the training. Don't give the
exact code — describe what it should do and point to the relevant pattern.]

**Step 2: [Next piece]**
[Continue building. Each step should be testable independently if possible.]

**Step 3: Test your implementation**

    [command to run/test]

Expected output:

    [what success looks like]

### Success Criteria
- [ ] [Code runs without errors]
- [ ] [Specific behavior works as expected]
- [ ] [Edge case is handled]

### Reference Solution
[Complete working solution they can compare against. Include comments explaining
key decisions.]

### Bonus Challenge
[Extend the code to handle a more complex case.]
```

---

## Adapting Templates by Audience

### For Enterprise Champions (No Technical Practice)

Enterprise Champions don't write code. Their exercises should use the Scenario-Based
Challenge template but adapted for strategic and business tasks:

- **Scenarios** involve evaluating tools, building business cases, planning rollouts,
  presenting to executives, assessing security postures, or comparing vendor capabilities
- **Deliverables** are memos, comparison matrices, rollout plans, talking points, or
  evaluation criteria — things they'd actually produce in their role
- **Success criteria** check for completeness, stakeholder coverage, and whether the
  deliverable addresses the right concerns for their audience
- **No CLI commands, no code blocks, no configuration files**

Example exercise types for Enterprise Champions:
- "Build a business case memo for adopting [feature]"
- "Create an evaluation rubric comparing [feature] against alternatives"
- "Draft a 90-day rollout plan for [feature] across your organization"
- "Prepare three talking points for your CTO about [security/compliance topic]"

### For Solutions Partners (Intermediate + Broad Scope)

Solutions Partners span technical and business conversations, so their exercises should
alternate between hands-on technical work (at intermediate depth) and client-facing
deliverables:

- Technical exercises use simplified configurations and emphasize patterns over edge cases
- Scenario exercises frame them as advising a client, not doing their own internal work
- Include exercises that combine technical setup with explaining the choice to a stakeholder

### For Solutions Engineers (Advanced + Customer Lens)

Solutions Engineers are technically deep but always operating in a customer context:

- Code exercises should work end-to-end, not just snippets
- Scenarios should include customer-facing communication as part of the deliverable
- "Explain what you did and why" should be woven into technical exercises

### For Developers (Advanced + Pure Technical)

Developers want the deepest technical exercises with the least hand-holding:

- Guided walkthroughs can move faster with less explanation of basics
- Code exercises should involve real implementation, not toy examples
- Bonus challenges should push toward production-quality patterns
- Skip business justification and focus on "does it work correctly"
