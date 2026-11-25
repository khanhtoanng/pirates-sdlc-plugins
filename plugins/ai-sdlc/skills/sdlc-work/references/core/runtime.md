# Coordinator runtime

The Coordinator owns routing, state, permissions, stage transitions and human handoffs.

## Instruction ownership

- routing.md classifies Feature, Bug and Spike.
- modes.md selects execution depth and defines Extended approval/resume.
- workflows/ defines role order and mode applicability.
- roles/ defines each role's procedure, checklist, output and exit conditions.
- practices/ contains reusable TDD, coverage, review, delegation, workspace and integration guidance.
- Host adapters describe platform capabilities and limitations.

## Invariants

- Classify each root as VISIBLE, RELEVANT, EDIT_APPROVED or EXCLUDED. Read access is not edit consent.
- Distinguish OBSERVED, SOURCE_BACKED, OWNER_ACCEPTED (with scope/revision), PROPOSED, ASSUMPTION, UNKNOWN, NOT RUN and NOT VERIFIED.
- Inspect project instructions, request/source and Git state before editing. Preserve staged, unstaged and untracked user work; recheck after resume and before transitions.
- Keep one canonical Feature AC revision, one original Bug symptom/expected contract with reproduction evidence, or one bounded Spike question and decision.
- Prefer an existing ticket/PR/ADR. Quick avoids files by default; Standard uses a compact record; Extended uses ordered artifacts and revisioned state.
- Do not create downstream artifacts before their prerequisites and approval gates pass.

## State contract

Track only fields relevant to the selected task:

- **Task:** type, requested/effective mode, reason, request reference and accepted decisions.
- **Roots:** visibility, relevance, edit scope, exclusions and project instructions.
- **Snapshots:** per-root branch/HEAD, staged and unstaged patch identity, and relevant untracked paths/content. HEAD alone does not identify a dirty worktree.
- **Feature:** accepted Spec revision and AC IDs.
- **Bug:** expected/actual symptom, reproduction status and cause evidence.
- **Spike:** bounded question, evidence, confidence and verdict.
- **Delivery:** plan/slices, verification evidence, authority and independent review snapshot/outcome.

Quick/Standard state may live in task context or a compact record. Extended requires durable state or HANDOFF: NOT DURABLE.

## Authorization

- A bounded implement/fix request may authorize ordinary local edits within its scope, subject to host/project policy.
- Evaluate, plan, research, Spike and review requests are read-only unless additional authority is given.
- Plan approval is not blanket edit authorization. A local edit grant does not authorize unrelated roots, destructive changes, installs, secrets, spending, commits, pushes, merges, cloud changes, production migrations or deployment.
- Use host permissions, hooks, CI and protected environments where available. Markdown instructions are not a security boundary. Narrow or stop when scope cannot be enforced safely.

## Transition checks

| Stage | Required evidence | Block when |
|---|---|---|
| Intake | Task type, mode, reason, scope, sources and risk | Material mismatch or unknown |
| Feature Intent | Grounded problem, user, outcome and boundaries | Consequential WHY/WHO/scope unresolved |
| Feature Spec | Source-linked, testable AC revision and complete AC map | Conflicting ACs or unresolved WHAT |
| Feature Architect | AC-to-slice/root/interface/test-seam map and dependency order | Material HOW or safety issue unresolved |
| Bug Architect | Expected/actual, qualified reproduction, cause evidence and minimal plan | Contract or diagnosis unsupported |
| Edit gate | Bounded local scope and actual host permission | Missing authority/access or unclear scope |
| Developer | Current baseline, authorized changes, AC/symptom coverage and observed test evidence | Test failure, scope drift or stale baseline |
| Reviewer | Fresh independent context inspected exact diff and evidence | Independence unverified, stale snapshot or missing evidence |
| Spike Researcher | Bounded question, supporting/contrary evidence, options and verdict | Scope, evidence or experiment authority insufficient |

A role's READY is a proposal. The Coordinator checks prerequisites and evidence before handoff.

## Verification and review

Developer verifies each accepted Feature AC or the Bug's original symptom, runs relevant regression/integration checks, records exact commands/results and binds evidence to the current per-root snapshot. Missing checks are NOT RUN or BLOCKED, not success.

Reviewer independently inspects the actual diff (including relevant untracked files), accepted expectations, test evidence, and implicated security, data, compatibility and integration risks. Self-review cannot yield AI_PASS. A code change after verification invalidates affected evidence; a change after review requires fresh verification and review.

For Bug, use VERIFIED_FIX only when the original symptom is credibly resolved, regression evidence exists, required checks are credible and independent review is AI_PASS. Otherwise report PARTIAL or UNVERIFIED.

For Feature, distinguish IMPLEMENTED, VERIFIED, REVIEWED and READY_FOR_MERGE_REVIEW. None means merged or deployed.

## Completion

Return the route/mode and reason, accepted expectation, relevant roots and snapshots, work performed, actual test commands/results, missing evidence, independent review verdict, residual risks and next human action. When Extended approval is pending, return the review card and end the turn.
