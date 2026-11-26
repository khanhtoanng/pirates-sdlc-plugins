# User guide

AI SDLC is one installed plugin for coordinating engineering work. It routes tasks to roles, controls handoffs and approvals, and keeps implementation evidence connected to accepted outcomes. It is not a project template or harness generator.

For installation, see [Hosts](HOSTS.md). For saved artifacts and resume, see [Task records](TASK_RECORDS.md).

## 1. Choose a task type

Task type answers **what workflow should run**.

| Type | Use it when | Main flow | Outcome |
|---|---|---|---|
| **Feature** | Add or intentionally change observable behavior | Intent → Spec → Architect → Developer → Reviewer | Accepted behavior, implementation and verification evidence |
| **Bug** | Existing behavior violates an established expectation | Architect → Developer → Reviewer | VERIFIED_FIX, PARTIAL or UNVERIFIED with evidence |
| **Spike** | Answer a bounded research or feasibility question | Researcher: scope → research → optional experiment → decision | PROCEED, CLARIFY or STOP |

A Bug that needs a new business rule must pause and resolve it through Feature Spec before implementation. A Spike does not turn into production implementation; start a separate Feature or Bug after the decision.

## 2. Choose the execution mode

Mode answers **how much analysis, ceremony and human approval are needed**. It does not change safety, verification or independent-review requirements.

| Mode | Use it when | Human involvement |
|---|---|---|
| **Quick** | Work is clear, low-risk and follows an established approach | Material questions and authority boundaries |
| **Standard** | Normal work needs some analysis, design or coordination | Consequential WHAT, HOW, scope and risk decisions |
| **Extended** | Work is complex, high-risk or explicitly supervised | Approve every applicable artifact stage and revision |

Auto selects the smallest safe mode; it is not a fourth mode. Explicit Extended is never downgraded. Security, data, compatibility or rollout risks can require escalation.

## 3. Understand the role handoffs

The Coordinator routes the task, checks prerequisites, manages state and permissions, and presents human decisions.

| Role | Owns |
|---|---|
| **Intent** | Why the work matters, target user, outcome, scope and non-goals |
| **Spec** | Observable behavior, acceptance criteria (ACs), provenance and complete AC summary |
| **Architect** | Technical approach, trade-offs, AC-to-slice mapping, dependencies, test seams and proposed plan |
| **Developer** | Execution feasibility, dispatch, authorized implementation, TDD, integration and verification |
| **Reviewer** | Independent inspection of actual integrated changes and Developer evidence |
| **Researcher** | Spike scope, research, optional approved experiment and decision |

Architect owns the logical delivery plan. Developer checks it against the current repository and host capabilities, then owns actual execution. Material plan changes return through the Coordinator and Architect.

Developer performs implementation and verification; there is no separate Verifier role or verification artifact. Reviewer independently checks code and evidence after code changes.

## 4. What happens in each mode

### Quick

Use the minimum safe path. Separate Intent, Spec or Architect work can be skipped only when the problem, accepted behavior and approach are already clear. Developer still verifies changes, and code changes still require a genuinely independent Reviewer before AI_PASS.

Quick normally returns the result in chat and creates no stage files. A durable record explicitly requested by the user must still use the canonical location in [Task records](TASK_RECORDS.md).

Typical paths: Feature: Developer → Reviewer; Bug: bounded Developer triage/fix/verification → Reviewer; Spike: Researcher scope/research/decision with no production edits.

### Standard

Run each applicable workflow responsibility without approval after every role. Ask the human about consequential product, technical, scope, risk or authority decisions; routine handoffs do not need a checkpoint.

Create a compact durable record when work spans multiple repositories, needs cross-session continuity, or the user asks to resume. It lives under `.sdlc/changes/<task-id>/task.md`. Do not create files just to mirror a small completed chat task.

### Extended

Run the complete applicable workflow. Each stage completes its role checklist, writes one inspectable artifact and pauses for approval of that exact revision.

| Task | Approval order | Stage files |
|---|---|---|
| Feature | Intent → Spec → Architect → Developer → Reviewer | 01-intent.md → 02-spec.md → 03-plan.md → 04-implementation.md → 05-review.md |
| Bug | Architect → Developer → Reviewer | 01-diagnosis-plan.md → 02-implementation.md → 03-review.md |
| Spike | Researcher: Scope → Research → optional Experiment Plan → optional Experiment → Decision | 01-scope.md → 02-research.md → optional 03-experiment-plan.md and 04-experiment.md → 05-decision.md |

Extended requires `state.json` and stage artifacts in one authorized `.sdlc/changes/<task-id>/` directory. The review card identifies the stage, revision, artifact path, decisions, evidence, risks and next action. Approval applies only to that revision; it does not expand edit scope or authorize merge, migration or deployment.

Unused optional Spike stages are marked `not_applicable` in state; no placeholder files are created. If durable storage is unavailable, report `HANDOFF: NOT DURABLE` and provide a pasteable handoff. Do not claim reliable resume.

## 5. Invoke a workflow

```text
sdlc-work feature standard Add customer status to FE and BE
sdlc-work bug quick Fix a reproduced login 500 and verify the existing 400 contract
sdlc-work spike standard Compare two approaches for offline synchronization; research only
sdlc-work feature extended Add customer status and pause at every approval stage
sdlc-work resume customer-status
```

Host-specific invocation prefixes are in [Hosts](HOSTS.md).

## 6. Understand authority

A scoped implement/fix request may authorize ordinary local edits within its stated scope and host/project policy. Planning, research and review are read-only unless separate authority is provided. Plan approval is not edit authority.

Commits, pushes, merges, installs, secrets, spending, cloud changes, production migrations and deployment require separate authorization. Host access to a directory does not mean the task is approved to edit it.

## 7. Where work is saved

Every durable plugin-generated record lives under `.sdlc/changes/<task-id>/` in one selected task-home root. External tickets, PRs and ADRs are source references, not alternate plugin-state stores.

See [Task records](TASK_RECORDS.md) for directory layout, task ID rules, multi-repository behavior, artifact audiences and migration of older records.
