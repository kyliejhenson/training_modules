# MCP Documentation — Modular Content Index

This index lists every modular content section created from MCP documentation sources, organized by subfolder. Each section covers one concept and is tagged for audience matching.

**Sources:**
- Sections 01–07: Claude Code MCP documentation
- Sections 08–13: Introduction to Model Context Protocol (Anthropic Academy)

---

## 01_Overview
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 1 | `01_what_is_mcp.md` | What is MCP | Beginner | Workflow integration | Foundational |
| 2 | `02_what_you_can_do_with_mcp.md` | MCP capabilities and use cases | Beginner | Business value & ROI, Workflow integration | Foundational |
| 3 | `03_popular_mcp_servers.md` | Available pre-built MCP servers | Beginner | Workflow integration | Foundational |

## 02_Installation
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 4 | `01_adding_remote_http_server.md` | Adding an HTTP MCP server | Advanced | Technical implementation | Applied |
| 5 | `02_adding_remote_sse_server.md` | Adding an SSE MCP server (deprecated) | Advanced | Technical implementation | Applied |
| 6 | `03_adding_local_stdio_server.md` | Adding a local stdio MCP server | Advanced | Technical implementation | Applied |
| 7 | `04_managing_mcp_servers.md` | List, inspect, remove servers | Intermediate | Technical implementation | Applied |
| 8 | `05_dynamic_tool_updates.md` | Live tool refresh via list_changed | Intermediate | Technical implementation | Supplemental |
| 9 | `06_windows_specific_setup.md` | Windows cmd /c wrapper requirement | Advanced | Technical implementation | Supplemental |
| 10 | `07_adding_mcp_from_json.md` | Adding servers from JSON config | Advanced | Technical implementation | Applied |
| 11 | `08_importing_from_claude_desktop.md` | Importing servers from Claude Desktop | Intermediate | Technical implementation, Workflow integration | Applied |
| 12 | `09_using_mcp_from_claude_ai.md` | Using Claude.ai MCP servers in Claude Code | Intermediate | Workflow integration | Applied |

## 03_Configuration
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 13 | `01_installation_scopes_overview.md` | Overview of local, project, user scopes | Intermediate | Technical implementation | Foundational |
| 14 | `02_local_scope.md` | Local scope details | Intermediate | Technical implementation | Applied |
| 15 | `03_project_scope.md` | Project scope and .mcp.json | Intermediate | Technical implementation, Security & compliance | Applied |
| 16 | `04_user_scope.md` | User scope details | Intermediate | Technical implementation | Applied |
| 17 | `05_choosing_the_right_scope.md` | Scope selection guide and precedence | Intermediate | Technical implementation, Adoption & change management | Applied |
| 18 | `06_environment_variable_expansion.md` | Env var expansion in .mcp.json | Advanced | Technical implementation, Security & compliance | Supplemental |

## 04_Authentication
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 19 | `01_oauth_authentication.md` | OAuth 2.0 authentication flow | Intermediate | Technical implementation, Security & compliance | Applied |
| 20 | `02_preconfigured_oauth_credentials.md` | Pre-configured OAuth credentials | Advanced | Technical implementation, Security & compliance | Supplemental |

## 05_Advanced_Features
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 21 | `01_plugin_provided_mcp_servers.md` | Plugin-bundled MCP servers | Intermediate | Technical implementation, Workflow integration | Supplemental |
| 22 | `02_claude_code_as_mcp_server.md` | Using Claude Code as an MCP server | Advanced | Technical implementation | Supplemental |
| 23 | `03_mcp_output_limits.md` | Token limits and warnings | Intermediate | Technical implementation | Supplemental |
| 24 | `04_using_mcp_resources.md` | Referencing MCP resources with @ | Intermediate | Technical implementation | Supplemental |
| 25 | `05_mcp_tool_search.md` | Dynamic on-demand tool loading | Advanced | Technical implementation | Supplemental |
| 26 | `06_mcp_prompts_as_commands.md` | MCP prompts as slash commands | Intermediate | Technical implementation, Workflow integration | Supplemental |

## 06_Enterprise_Management
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 27 | `01_managed_mcp_overview.md` | Centralized MCP control options | Intermediate | Security & compliance, Adoption & change management | Supplemental |
| 28 | `02_exclusive_control_managed_mcp.md` | Locking servers via managed-mcp.json | Advanced | Security & compliance, Technical implementation | Supplemental |
| 29 | `03_policy_based_control.md` | Allowlists and denylists | Advanced | Security & compliance, Technical implementation | Supplemental |

## 07_Practical_Examples
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 30 | `01_monitor_errors_with_sentry.md` | Sentry integration walkthrough | Intermediate | Workflow integration, Technical implementation | Applied |
| 31 | `02_connect_to_github.md` | GitHub integration walkthrough | Intermediate | Workflow integration, Technical implementation | Applied |
| 32 | `03_query_postgresql.md` | PostgreSQL integration walkthrough | Intermediate | Workflow integration, Technical implementation | Applied |

## 08_MCP_Fundamentals
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 33 | `01_what_is_mcp_protocol.md` | What is the Model Context Protocol | Beginner | Workflow integration | Foundational |
| 34 | `02_the_problem_mcp_solves.md` | The integration problem MCP solves | Beginner | Business value & ROI, Workflow integration | Foundational |
| 35 | `03_how_mcp_works.md` | How MCP shifts tool integration to dedicated servers | Beginner | Technical implementation, Workflow integration | Foundational |
| 36 | `04_mcp_servers_explained.md` | MCP servers as standardized service interfaces | Beginner | Technical implementation, Workflow integration | Foundational |
| 37 | `05_mcp_vs_direct_api_calls.md` | MCP vs direct API calls and tool use | Beginner | Technical implementation, Business value & ROI | Foundational |

## 09_MCP_Clients
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 38 | `01_mcp_client_role.md` | The MCP client as communication bridge | Intermediate | Technical implementation | Foundational |
| 39 | `02_transport_agnostic_communication.md` | Transport agnostic protocol support | Intermediate | Technical implementation | Applied |
| 40 | `03_mcp_message_types.md` | ListTools and CallTool message types | Intermediate | Technical implementation | Applied |
| 41 | `04_end_to_end_request_flow.md` | 12-step end-to-end request flow | Intermediate | Technical implementation, Workflow integration | Applied |
| 42 | `05_project_setup.md` | CLI chatbot project setup with UV | Advanced | Technical implementation | Applied |
| 43 | `06_client_architecture.md` | MCP client class and session architecture | Advanced | Technical implementation | Applied |
| 44 | `07_implementing_list_and_call_tools.md` | Implementing list_tools and call_tool | Advanced | Technical implementation | Applied |
| 45 | `08_testing_complete_flow.md` | Testing the complete client-server flow | Advanced | Technical implementation | Applied |

## 10_Building_MCP_Servers
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 46 | `01_initializing_server_with_sdk.md` | Initializing a server with FastMCP | Advanced | Technical implementation | Applied |
| 47 | `02_defining_tools_with_decorators.md` | Defining tools with decorators and Field | Advanced | Technical implementation | Applied |
| 48 | `03_building_an_edit_tool.md` | Building a multi-parameter edit tool | Advanced | Technical implementation | Applied |
| 49 | `04_sdk_approach_benefits.md` | Benefits of the SDK approach | Intermediate | Technical implementation, Business value & ROI | Foundational |
| 50 | `05_server_inspector.md` | The MCP Server Inspector for debugging | Intermediate | Technical implementation, Evaluation & testing | Applied |
| 51 | `06_inspector_development_workflow.md` | Inspector development workflow | Intermediate | Technical implementation, Evaluation & testing | Applied |

## 11_Resources
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 52 | `01_what_are_mcp_resources.md` | What are MCP resources | Intermediate | Technical implementation, Workflow integration | Foundational |
| 53 | `02_direct_resources.md` | Direct resources with static URIs | Advanced | Technical implementation | Applied |
| 54 | `03_templated_resources.md` | Templated resources with URI parameters | Advanced | Technical implementation | Applied |
| 55 | `04_resource_mime_types.md` | Resource MIME types and serialization | Advanced | Technical implementation | Supplemental |
| 56 | `05_testing_resources_with_inspector.md` | Testing resources with the inspector | Intermediate | Technical implementation, Evaluation & testing | Applied |
| 57 | `06_implementing_client_resource_reading.md` | Implementing client-side resource reading | Advanced | Technical implementation | Applied |
| 58 | `07_resource_ux_in_cli.md` | Resource UX with @ mentions in the CLI | Intermediate | Workflow integration | Applied |

## 12_Prompts
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 59 | `01_what_are_mcp_prompts.md` | What are MCP prompts | Intermediate | Technical implementation, Workflow integration | Foundational |
| 60 | `02_defining_prompts_with_decorators.md` | Defining prompts with decorators | Advanced | Technical implementation | Applied |
| 61 | `03_prompt_benefits.md` | Benefits of MCP prompts | Beginner | Business value & ROI, Workflow integration | Foundational |
| 62 | `04_implementing_client_prompt_functions.md` | Client-side list_prompts and get_prompt | Advanced | Technical implementation | Applied |
| 63 | `05_prompt_workflow.md` | The MCP prompt workflow end-to-end | Intermediate | Technical implementation, Workflow integration | Applied |

## 13_MCP_Primitives_Review
| # | File | Concept | Skill Level | Use Case Types | Priority |
|---|------|---------|-------------|----------------|----------|
| 64 | `01_tools_model_controlled.md` | Tools as model-controlled primitives | Intermediate | Technical implementation, Workflow integration | Foundational |
| 65 | `02_resources_app_controlled.md` | Resources as app-controlled primitives | Intermediate | Technical implementation, Workflow integration | Foundational |
| 66 | `03_prompts_user_controlled.md` | Prompts as user-controlled primitives | Intermediate | Technical implementation, Workflow integration | Foundational |
| 67 | `04_choosing_the_right_primitive.md` | Choosing the right MCP primitive | Intermediate | Technical implementation, Workflow integration | Applied |

---

## Tag Dimensions Used

- **Technical Skill Level**: Beginner · Intermediate · Advanced
- **Use Case Types**: Technical implementation · Security & compliance · Workflow integration · Business value & ROI · Adoption & change management · Evaluation & testing
- **Instructional Priority**: Foundational · Applied · Supplemental
- **Technical Application Practice**: Yes / No
- **Value-Based Selling Information**: Yes / No
