# AI SDLC — local-first plugin for Claude Code, Cursor and Codex

**Version 0.8.0.** One installed plugin coordinates engineering work across one or more repositories. It does not generate project harness files or install hooks, MCPs or integrations by default.

## Choose a task type and mode

| Task | Workflow | Result |
|---|---|---|
| **Feature** | Intent → Spec → Architect → Developer → Reviewer | Accepted ACs, implementation evidence and release readiness |
| **Bug** | Architect → Developer → Reviewer | VERIFIED_FIX, PARTIAL or UNVERIFIED |
| **Spike** | Researcher: scope → research → optional experiment → decision | PROCEED, CLARIFY or STOP |

Upstream Feature roles run when needed in Quick and Standard. Extended runs every applicable stage.

| Mode | Use it for | Human involvement |
|---|---|---|
| **Quick** | Clear, low-risk work using an established approach | Material questions and authority boundaries |
| **Standard** | Normal engineering work with some analysis or coordination | Consequential WHAT, HOW and scope decisions |
| **Extended** | Complex, high-risk or explicitly supervised work | Approval of each applicable artifact stage |

Auto selects the smallest safe mode; it is a selector, not a fourth mode. Explicit Extended is never downgraded. See [mode policy](plugins/ai-sdlc/skills/sdlc-work/references/core/modes.md).

## Role ownership

Intent defines the problem and outcome; Spec defines observable behavior and acceptance criteria; Architect plans the technical approach and diagnoses Bugs; Developer implements and verifies; Reviewer independently checks code and evidence; Researcher owns Spikes. The Coordinator controls routing, permissions, state and handoffs.

## Invoke locally

- **Claude Code:** `/ai-sdlc:sdlc-work feature standard Add customer status in FE and BE`
- **Cursor:** `sdlc-work bug quick Reproduce and fix the login 500 response`
- **Codex:** `sdlc-work spike standard Compare two approaches for offline sync`

Optional skills: `sdlc-setup` inspects or configures an approved workspace; `sdlc-doctor` checks plugin and host readiness.

See [local setup](docs/LOCAL_SETUP.md), [architecture](docs/ARCHITECTURE.md), [task routes](docs/TASK_ROUTES.md), [Extended guide](docs/EXTENDED.md) and [migration](docs/MIGRATION.md).

## Records and authority

Quick normally returns a chat result. Standard uses an existing ticket/PR or one compact record. Extended creates ordered stage artifacts and revisioned state in one authorized tracker or task directory.

A bounded implement/fix request may authorize ordinary local edits within its scope, subject to host and project policy. Planning, research and review are read-only. Destructive operations, secrets, installs, remote services, commits, pushes, merges, production migrations and deployment require separate authority.

## Validate

Run `python3 tests/validate.py`, `python3 tests/evals/score.py --self-test` and `python3 tests/evals/test_grade.py`. These are offline checks, not proof of host behavior. Run opt-in host scenarios with `tests/evals/run.py`; see `tests/SCENARIOS.md` and `docs/SOURCES.md`.
