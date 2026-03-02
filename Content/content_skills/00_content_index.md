# Content Index — Claude Code Skills

Sources:
- https://code.claude.com/docs/en/skills.md
- Anthropic Academy — Introduction to Agent Skills course

---

## 01_Overview

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_what_are_skills.md | Definition of skills, how they extend Claude Code, relationship to slash commands | Beginner | Technical implementation | Foundational |
| 02 | 02_where_skills_live.md | Storage locations (enterprise, personal, project, plugin) and priority ordering | Intermediate | Technical implementation, Workflow integration | Foundational |
| 03 | 03_skill_directory_structure.md | File layout of a skill directory with SKILL.md and supporting files | Intermediate | Technical implementation | Foundational |
| 04 | 04_automatic_discovery_nested_directories.md | Auto-discovery from nested directories, monorepo support, --add-dir behavior | Intermediate | Technical implementation, Workflow integration | Applied |
| 05 | 05_when_to_use_skills.md | Scenarios where skills are the right customization tool, rule of thumb | Beginner | Workflow integration, Adoption & change management | Foundational |
| 06 | 06_how_skill_matching_works.md | Semantic matching process, startup scan, confirmation prompt before loading | Intermediate | Technical implementation | Foundational |

## 02_Bundled_Skills

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_simplify_skill.md | Built-in /simplify skill for code review and cleanup | Beginner | Technical implementation, Workflow integration | Applied |
| 02 | 02_batch_skill.md | Built-in /batch skill for large-scale parallel codebase changes | Intermediate | Technical implementation, Workflow integration | Applied |

## 03_Getting_Started

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_create_your_first_skill.md | Step-by-step tutorial to create an explain-code skill | Beginner | Technical implementation | Applied |

## 04_Configuration

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_types_of_skill_content.md | Reference content vs. task content patterns | Intermediate | Technical implementation | Applied |
| 02 | 02_frontmatter_reference.md | Complete YAML frontmatter field reference table | Advanced | Technical implementation | Supplemental |
| 03 | 03_string_substitutions.md | Dynamic variable substitution ($ARGUMENTS, $N, ${CLAUDE_SESSION_ID}) | Advanced | Technical implementation | Applied |
| 04 | 04_adding_supporting_files.md | Including multiple files in a skill directory for reference material | Intermediate | Technical implementation | Applied |
| 05 | 05_control_who_invokes_a_skill.md | disable-model-invocation and user-invocable fields for access control | Intermediate | Technical implementation, Security & compliance | Applied |
| 06 | 06_restrict_tool_access.md | Using allowed-tools to constrain Claude's capabilities per skill | Advanced | Technical implementation, Security & compliance | Applied |
| 07 | 07_passing_arguments_to_skills.md | Argument passing with $ARGUMENTS, positional access with $N | Intermediate | Technical implementation | Applied |
| 08 | 08_using_scripts_efficiently.md | Running scripts without loading contents into context — output-only token usage | Advanced | Technical implementation | Supplemental |

## 05_Advanced_Patterns

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_inject_dynamic_context.md | Shell command preprocessing with !`command` syntax | Advanced | Technical implementation | Supplemental |
| 02 | 02_run_skills_in_a_subagent.md | Forked execution with context: fork and agent field | Advanced | Technical implementation | Supplemental |
| 03 | 03_restrict_claude_skill_access.md | Permission rules for controlling which skills Claude can invoke | Advanced | Technical implementation, Security & compliance | Supplemental |
| 04 | 04_generate_visual_output.md | Bundling scripts to produce interactive HTML visualizations | Advanced | Technical implementation | Supplemental |

## 06_Sharing_and_Distribution

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_sharing_skills.md | Distribution scopes: project, plugin, and managed deployment | Intermediate | Workflow integration, Adoption & change management | Applied |
| 02 | 02_enterprise_managed_settings.md | Enterprise deployment with managed settings and strictKnownMarketplaces | Advanced | Security & compliance, Adoption & change management | Supplemental |
| 03 | 03_skills_and_subagents.md | Configuring custom subagents with skills field; built-in agents can't access skills | Advanced | Technical implementation, Workflow integration | Supplemental |

## 07_Troubleshooting

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_skill_not_triggering.md | Steps to diagnose skills that don't activate when expected | Intermediate | Technical implementation | Supplemental |
| 02 | 02_skill_triggers_too_often.md | How to reduce unwanted skill activation | Intermediate | Technical implementation | Supplemental |
| 03 | 03_claude_doesnt_see_all_skills.md | Context budget limits and SLASH_COMMAND_TOOL_CHAR_BUDGET override | Advanced | Technical implementation | Supplemental |
| 04 | 04_skills_validator.md | Using the agent skills verifier to catch structural issues | Intermediate | Technical implementation, Evaluation & testing | Supplemental |
| 05 | 05_skill_doesnt_load.md | Structural requirements: directory placement, file naming, claude --debug | Intermediate | Technical implementation, Evaluation & testing | Supplemental |
| 06 | 06_wrong_skill_gets_used.md | Resolving ambiguity between similar skill descriptions | Intermediate | Technical implementation, Evaluation & testing | Supplemental |
| 07 | 07_skill_priority_conflicts.md | Diagnosing when higher-priority skills shadow yours | Intermediate | Technical implementation, Security & compliance | Supplemental |
| 08 | 08_plugin_skills_not_appearing.md | Cache clearing and reinstallation for plugin skill issues | Intermediate | Technical implementation, Evaluation & testing | Supplemental |
| 09 | 09_runtime_errors.md | Fixing dependencies, permissions, and path separator issues | Advanced | Technical implementation, Evaluation & testing | Supplemental |
| 10 | 10_quick_troubleshooting_checklist.md | At-a-glance reference for all common skill problems | Intermediate | Technical implementation, Evaluation & testing | Supplemental |

## 08_Comparison

| # | Filename | Concept Summary | Skill Level | Use Case Types | Priority |
|---|----------|----------------|-------------|----------------|----------|
| 01 | 01_claude_md_vs_skills.md | When to use CLAUDE.md (always-on) vs. skills (on-demand) | Intermediate | Workflow integration | Foundational |
| 02 | 02_skills_vs_subagents.md | Skills add context vs. subagents run in isolation | Intermediate | Workflow integration | Foundational |
| 03 | 03_skills_vs_hooks.md | Request-driven skills vs. event-driven hooks | Intermediate | Workflow integration | Foundational |
| 04 | 04_mcp_servers_vs_skills.md | MCP servers provide tools/integrations, a separate category | Intermediate | Workflow integration | Foundational |
| 05 | 05_combining_features.md | Recommended setup combining all customization features | Intermediate | Workflow integration, Adoption & change management | Applied |

---

## Tag Dimensions Quick Reference

### Technical Skill Level
- **Beginner**: No technical background required
- **Intermediate**: Assumes working knowledge of Claude products and general technical concepts
- **Advanced**: Assumes hands-on experience building with Claude; includes code and implementation patterns

### Use Case Types
- **Technical implementation**: How to build, integrate, or deploy with Claude products
- **Security & compliance**: Data handling, privacy, authentication, access management
- **Workflow integration**: Fitting Claude into existing tools, processes, and systems
- **Business value & ROI**: Impact measurement, cost justification, competitive positioning
- **Adoption & change management**: Rollout planning, training strategies, stakeholder communication
- **Evaluation & testing**: Eval frameworks, benchmarking, output quality assessment

### Instructional Priority
- **Foundational**: Core concepts everyone needs before anything else makes sense
- **Applied**: Practical, hands-on knowledge for using the feature
- **Supplemental**: Nice-to-know content — deep dives, edge cases, advanced patterns, troubleshooting

### Technical Application Practice
- **Yes**: Includes exercises, tutorials, or hands-on materials
- **No**: Informational or strategic content only

### Value-Based Selling Information
- **Yes**: Includes talking points, ROI framing, or competitive differentiation
- **No**: Focused on usage, not selling or justification
