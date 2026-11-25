# AI SDLC — local-first plugin for Claude Code, Cursor and Codex

**Version 0.7.0.** One installed plugin contains the SDLC coordinator, optional setup and doctor. It does not generate a second repository harness, copy role instructions into every project, install hooks/MCPs or deploy anything by default.

## Choose a task type, then an execution mode

| Task | Responsibility flow | Final result |
|---|---|---|
| **Feature** | Intent → Spec → Architect → Developer (implement + verify) → independent Reviewer; skip separate upstream roles when safe/appropriate in Quick or Standard | AC-linked implementation evidence and release readiness |
| **Bug** | Architect (assess + diagnose + minimal fix plan) → Developer (fix + verify) → independent Reviewer; Quick may use bounded Developer triage | VERIFIED_FIX, PARTIAL or UNVERIFIED |
| **Spike** | Researcher scope → research → optional separately approved scratch experiment → decision → STOP | PROCEED, CLARIFY or STOP; no automatic production implementation |

**Mode** is independent: auto (default), Quick, Standard or Extended. Severity and material risk decide the effective mode, not number of repositories. See the mode guide at plugins/ai-sdlc/skills/sdlc-work/references/core/modes.md. Legacy positional spike remains accepted as task type spike/mode auto.

| Mode | Role execution | Human involvement |
|---|---|---|
| Quick | Minimum safe role path; Developer still verifies | Material questions and actual authority only |
| Standard | All applicable responsibilities in order; concise record | Consequential WHAT/HOW/scope decisions |
| Extended | Full applicable route; ordered artifact per stage | Explicit approval after every applicable artifact stage |

Explicit Extended always wins; evidenced high risk escalates Quick/Standard. Extended approval, pause/resume, revision and invalidation are defined in core/modes.md. There is no separate human-gates.md.

## Roles and responsibility

Intent defines WHY/WHO; Spec defines observable WHAT and ACs; Architect defines technical HOW and owns Bug assessment/diagnosis/plan; Developer owns implementation, TDD and verification; Reviewer independently checks code and evidence; Researcher owns Spike. Roles are logical responsibilities, not mandatory native subagents. There is no Verifier role and no roles/shared.md; each role file has its own numbered procedure and checklist.

## Invoke locally

- **Claude Code:** /ai-sdlc:sdlc-work feature standard Add customer status in FE+BE+Flyway; inspect Terraform read-only.
- **Cursor:** Use sdlc-work for a bug in quick mode: reproduce the 500 response, fix it and verify the regression.
- **Codex:** Use sdlc-work spike standard to compare two approaches for offline sync. Research only; do not implement.
- sdlc-setup: optional read-only inspection, then exact approved configuration only if needed.
- sdlc-doctor: check plugin discovery, root access, conflicts and reviewer capability.

See docs/LOCAL_SETUP.md, docs/ARCHITECTURE.md, docs/TASK_ROUTES.md, docs/EXTENDED.md, docs/EXAMPLE_MULTI_REPO.md, docs/EXAMPLE_SPEC_REVIEW.md and docs/MIGRATION.md.

## Scope and evidence, not document sprawl

Use one accepted AC revision for Features, one original-symptom/regression record for Bugs, or one bounded question/decision brief for Spikes. Quick avoids stage files; Standard uses an existing ticket/PR or compact record; Extended uses distinct ordinal stage artifacts and resumable state in one authorized tracker or task directory, not a second harness.

A bounded explicit implement/fix request may authorize ordinary local edits in its scope, subject to host/project permissions. A plan/research/spike request does not. Separately authorize destructive operations, secrets, remote services, installs, commit/push/merge, Terraform apply, production migrations and deployment. Multi-root visibility never grants edit scope.

## Test the plugin

Run python3 tests/validate.py, python3 tests/evals/score.py --self-test and python3 tests/evals/test_grade.py for offline validation. These checks do not prove host behavior. Run actual opt-in host scenarios with tests/evals/run.py and see tests/SCENARIOS.md for Claude, Cursor and Codex evaluation guidance, limitations and baselines. Sources: docs/SOURCES.md.
