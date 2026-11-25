# Architecture decisions — consolidated SDLC modes and roles

## One coordinator, three task types and three modes

One installed plugin coordinates Feature, Bug and Spike work across Claude Code, Cursor and Codex. It does not generate a second repository harness or copy role files into projects by default.

- Task type selects the workflow: Feature (new/changed observable behavior), Bug (repair an existing violated contract), Spike (bounded research/feasibility question).
- Mode selects execution depth and human approval behavior: Quick, Standard or Extended. Auto selects a mode; it is not an execution mode.
- One Coordinator owns routing, state, permissions, stage transitions and handoffs.
- Roles are logical responsibilities, not mandatory native subagents. Delegate selectively when isolation or parallelism adds value.

## Role ownership

- Intent: WHY, WHO, outcome, scope and non-goals for Feature.
- Spec: observable WHAT, AC creation, source mapping and consistency.
- Architect: Feature technical design/plan; Bug assessment, diagnosis and minimum fix plan.
- Developer: authorized implementation and verification, including TDD, regressions/integrations and changed snapshot evidence.
- Reviewer: fresh independent review of code and Developer's evidence.
- Researcher: Spike scope, research, optional bounded scratch experiment and decision.

There is no roles/shared.md; each role owns purpose, entry conditions, numbered procedure, checklist, output and exit conditions. Global permission/state invariants live in core/runtime.md and Coordinator instructions. There is no separate Verifier role or Verification stage.

## Workflow sequences

- Feature: Intent → Spec → Architect → Developer (implement + verify) → Reviewer.
- Bug: Architect (assess + diagnose + plan) → Developer (fix + verify) → Reviewer.
- Spike: Researcher (scope → research → optional experiment plan/experiment → decision); no production Developer/Reviewer chain.

Task-specific workflow files define role applicability, order and Extended artifact names.

## Mode behavior

- Quick: minimum safe role path; no per-stage documents or approvals by default. Skip separate Intent/Spec/Architect only when expected behavior and approach are established. Developer verifies and code changes still require independent review for AI_PASS.
- Standard: all applicable responsibilities in order, selective human decisions, concise/compact record instead of a file per role.
- Extended: full applicable role workflow, ordinal artifact per stage, mandatory role checklist and explicit approval after every artifact stage. Approval binds to an exact revision; resume refreshes source/scope/snapshot.

core/modes.md owns selection plus the complete Extended approval, pause, resume, revision and invalidation protocol. There is no separate human-gates.md.

## Evidence and convergence

- Feature: accepted AC revision → plan slice → code/diff → Developer's observed test evidence → independent review.
- Bug: original expected/actual symptom → reproduction/diagnosis evidence → minimal repair → Developer's after-state/regression evidence → independent review.
- Spike: bounded question → supporting/contrary evidence → confidence/options/verdict → STOP. POC requires a separate scratch grant and never becomes production implementation implicitly.
- Verification is tied to each current Git root snapshot, including dirty patch and relevant untracked state. Any relevant code change invalidates affected verification and previous review.

## Authority and human review

A bounded user implement/fix request may authorize ordinary local edits inside selected scope, subject to host/project policy. Plan/research/spike/review requests do not grant implementation authority. Plan approval does not authorize privileged operations. Commit/push/merge, installs, secrets, cloud changes, production migration and deployment require separate authority.

An Extended approval is not an operating-system permission and does not authorize merge/deployment. AI_PASS requires actual independent review and is not human release approval.

## Multi-repository work and continuation

Treat each Git root separately: VISIBLE, RELEVANT, EDIT_APPROVED, EXCLUDED. Share one accepted Feature AC revision and maintain per-root impact, test and snapshot evidence. Release order follows actual integration dependencies, not a fixed repository order. Extended uses one authorized task directory or existing tracker, not scattered stage files.