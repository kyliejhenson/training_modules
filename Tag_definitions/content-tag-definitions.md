# Content Tag Definitions

Use these tags to classify content pieces so they can be matched to the appropriate audience profiles.

---

## Technical Skill Level

Indicates the depth of technical knowledge assumed by the content.

- **Beginner**: No technical background required. Concepts are explained in plain language without assuming familiarity with APIs, code, or system architecture.
- **Intermediate**: Assumes working knowledge of Claude products and general technical concepts. May reference integrations, configurations, or architectural decisions without step-by-step technical instruction.
- **Advanced**: Assumes hands-on experience building with Claude. Content includes code, API details, implementation patterns, or deep technical guidance.

---

## Use Case Types

Each content piece should be tagged with one or more of the following. A piece of content can carry multiple tags if it genuinely serves multiple needs.

- **Technical implementation**: Content that explains how to build, integrate, or deploy with Claude products. Includes API usage, SDKs, code examples, configuration guides, and deployment patterns.
- **Security & compliance**: Content covering data handling, privacy controls, authentication, access management, governance frameworks, and regulatory considerations relevant to Claude usage.
- **Workflow integration**: Content focused on fitting Claude into existing tools, processes, and systems. Covers design patterns for embedding Claude into business operations rather than the mechanics of building the integration itself.
- **Business value & ROI**: Content that articulates why Claude matters in business terms. Includes impact measurement, cost justification, competitive positioning, and use case framing for decision-makers.
- **Adoption & change management**: Content that supports driving usage after a decision has been made. Covers rollout planning, internal training strategies, stakeholder communication, success metrics for adoption, and overcoming resistance.
- **Evaluation & testing**: Content about measuring whether Claude implementations are working correctly. Includes eval frameworks, benchmarking approaches, output quality assessment, and validation methodologies.

---

## Technical Application Practice

Indicates whether the content includes or supports hands-on practice.

- **Yes**: Content includes exercises, sandbox environments, sample projects, code-along tutorials, or other materials designed for the audience to practice applying what they've learned.
- **No**: Content is informational or strategic and does not require the audience to build or test anything themselves.

---

## Value-Based Selling Information

Indicates whether the content equips the audience to position Claude's value to others.

- **Yes**: Content includes talking points, ROI framing, objection handling, competitive differentiation, or other materials that help the audience advocate for Claude to internal stakeholders or external clients.
- **No**: Content is focused on usage and does not address how to sell or justify Claude to others.

---

## Instructional Priority

Indicates how essential this concept is for building a working understanding of the feature. Used downstream by training generation to sequence content according to adult learning best practices (foundational understanding first, then application, then depth).

- **Foundational**: Core concepts that everyone needs before anything else makes sense. Definitions, mental models, "what is this and why does it exist" explanations. A learner who skips foundational content will struggle with everything that follows. Examples: what a feature is, where it lives, how it works at a high level.
- **Applied**: Practical, hands-on knowledge for using the feature. How to build, configure, invoke, and integrate. This is the "now go do it" layer — it assumes foundational understanding is already in place. Examples: step-by-step tutorials, configuration references, argument passing, code examples.
- **Supplemental**: Nice-to-know content — deep dives, edge cases, advanced patterns, troubleshooting, and optimization. Valuable for practitioners who already have a working understanding and want to go further, but not essential for initial competence. Examples: advanced configuration options, debugging guides, enterprise deployment, performance optimization.
