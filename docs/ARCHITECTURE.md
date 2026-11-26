# Architecture

This page is for maintainers. For how to use the plugin, start with the [User guide](USER_GUIDE.md); for installation and host capabilities, see [Hosts](HOSTS.md).

## Operating model

One installed plugin coordinates Feature, Bug and Spike work across Claude Code, Cursor, Codex, and GitHub Copilot (VS Code and CLI).

- **Task type** chooses the workflow: Feature changes product behavior, Bug repairs a violated contract, and Spike answers a bounded research question.
- **Mode** chooses execution depth and approval behavior: Quick, Standard or Extended. Auto selects a mode.
- **Coordinator** owns routing, risk, task-record location, state, permissions, stage transitions and human handoffs.
- **Roles** define responsibilities. Native subagent delegation is used when isolation or parallelism adds value, not as a requirement for every role.

## Role ownership

| Role | Responsibility |
|---|---|
| Intent | Feature problem, user, outcome, scope and non-goals |
| Spec | Observable behavior, acceptance criteria and source mapping |
| Architect | Feature technical approach, AC-to-slice mapping, logical dependency graph and proposed delivery plan; Bug assessment, diagnosis and minimum repair plan |
| Developer | Validate the plan against the current baseline and host/worktree capabilities; actual dispatch, authorized implementation, TDD, integration and verification |
| Reviewer | Independent review of the actual integrated diff and Developer evidence |
| Researcher | Spike scope, evidence-based research, optional scratch experiment and decision |

Architect owns the logical delivery graph. Developer owns execution feasibility and actual dispatch. A material plan change returns through the Coordinator and Architect; Developer does not silently redesign an approved plan.

## Workflow order

- **Feature:** Intent (when needed) → Spec (when needed) → Architect (when design, dependencies or delivery slicing are needed) → Developer → independent Reviewer.
- **Bug:** Architect → Developer → independent Reviewer. A clearly reproduced, low-risk Bug may use bounded Developer triage in Quick.
- **Spike:** Researcher scope → research → optional approved experiment → decision. Production implementation is a separate Feature/Bug task.

Workflow files define role applicability, order and Extended artifact names. Architect proposes complete, outcome-oriented slices and genuine blocker relationships. Developer validates safe execution and may parallelize only independent, non-conflicting slices; final integration verification and independent review remain mandatory.

## Shared practice ownership

- `coverage.md` classifies accepted rules versus verification examples and consequential questions.
- `tdd.md` owns test-seam guidance, RED/GREEN/REFACTOR and TDD evidence.
- `delegation.md` owns plan-to-dispatch boundaries, actual worker dispatch, safe parallel execution and independent Reviewer isolation.
- `review.md` owns human decision policy and review handoff cards, including Architect plan review.
- Role files own role procedures and outputs; `runtime.md` owns Coordinator invariants; `modes.md` owns mode, task-record persistence and Extended state/approval policy.

## Task-record ownership

Durable plugin-generated records live in one canonical task directory under `.sdlc/changes/<task-id>/` relative to a selected task-home root. Quick has no record by default; Standard uses one compact `task.md` when continuity is needed; Extended requires `state.json` and applicable stage artifacts. External tickets, PRs and ADRs remain source references rather than alternate plugin-state stores. Multi-repository work uses one selected workspace/primary root.

The Coordinator selects and creates the directory and passes its path to every role. Record-write permission and source-edit permission are separate. See [Task records](TASK_RECORDS.md).

## Evidence and authority

Feature evidence follows the accepted AC revision through plan, code, tests and review. Bug evidence follows the original expected/actual symptom through diagnosis, repair, regression tests and review. Spike evidence supports a bounded verdict and stops before production implementation.

Verification and review are tied to each relevant Git root's current snapshot, including dirty changes and relevant untracked files. A code change invalidates affected verification; a post-review change requires fresh verification and review.

A scoped implement/fix request may authorize ordinary local edits. Plan approval is not edit authority. Commits, pushes, merges, installs, secrets, cloud changes, production migrations and deployment require separate authorization.

## Multi-repository work

Classify each root as VISIBLE, RELEVANT, EDIT_APPROVED or EXCLUDED. Keep one accepted AC set and one task record, track evidence per root, and order delivery by actual integration dependencies. Visibility alone never grants edit access.
