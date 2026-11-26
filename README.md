# AI SDLC — local-first plugin for Claude Code, Cursor, Codex and GitHub Copilot

**Version 0.8.0.** One installed plugin coordinates engineering work across one or more repositories. It does not generate project harness files or install hooks, MCPs or integrations by default.

## Choose a task type and mode

| Task | Workflow | Result |
|---|---|---|
| **Feature** | Intent → Spec → Architect → Developer → Reviewer | Accepted ACs, implementation evidence and release readiness |
| **Bug** | Architect → Developer → Reviewer | VERIFIED_FIX, PARTIAL or UNVERIFIED |
| **Spike** | Researcher: scope → research → optional experiment → decision | PROCEED, CLARIFY or STOP |

| Mode | Use it for | Human involvement |
|---|---|---|
| **Quick** | Clear, low-risk work using an established approach | Material questions and authority boundaries |
| **Standard** | Normal engineering work with analysis or coordination | Consequential WHAT, HOW and scope decisions |
| **Extended** | Complex, high-risk or explicitly supervised work | Approval of each applicable artifact stage |

Auto selects the smallest safe mode; it is a selector, not a fourth mode. Explicit Extended is never downgraded.

Start with the [human user guide](docs/USER_GUIDE.md), then use the [documentation index](docs/README.md) for installation, task records, host support and evaluation.

## Invoke locally

- **Claude Code:** `/ai-sdlc:sdlc-work feature standard Add customer status in FE and BE`
- **Cursor:** `sdlc-work bug quick Reproduce and fix the login 500 response`
- **GitHub Copilot in VS Code:** `/sdlc-work feature standard Add customer status`
- **GitHub Copilot CLI:** `copilot -p "Use /sdlc-work feature standard Add customer status" --plugin-dir /path/to/plugins/ai-sdlc`
- **Codex:** `sdlc-work spike standard Compare two approaches for offline sync`

Optional skills: `sdlc-setup` inspects or configures an approved workspace; `sdlc-doctor` checks plugin and host readiness.

## Task records

Quick normally returns a chat result. Standard creates a compact record when continuity is needed. Extended requires durable state and ordered stage artifacts.

Every durable plugin-generated record lives under `.sdlc/changes/<task-id>/` in one selected task-home root. External issues, PRs and ADRs remain source references; they do not replace the local task record or become a second state store. Multi-repository work uses one task directory, not one copy per repository.

See [Task records](docs/TASK_RECORDS.md) for location, file layout, approval and resume behavior.

## Documentation boundary

- `docs/` explains the plugin to people; it is not loaded as agent instructions.
- `plugins/ai-sdlc/skills/` contains installed skills and normative runtime instructions.
- `tests/` describes and evaluates expected behavior.

Start at [docs/README.md](docs/README.md). Maintainers can read [architecture](docs/ARCHITECTURE.md), [changelog](docs/CHANGELOG.md) and [migration](docs/MIGRATION.md).
