# Coordinator runtime — state, permissions and evidence

## Ownership

- core/routing.md classifies Feature, Bug and Spike.
- core/modes.md selects execution depth and owns Extended approval, pause, resume, revision and invalidation.
- workflows/ defines ordered role responsibilities for each task type.
- roles/ defines each role's numbered procedure, mandatory checklist, output and exit conditions.
- practices/ contains reusable engineering practices such as TDD, coverage, delegation and review.
- One Coordinator owns routing, state, permissions, stage transitions and human handoffs.

There is no generic shared-role instruction file and no separate Verifier role. Developer owns implementation and verification. Reviewer is independent and checks the code and Developer's evidence.

## Invariants

- Never equate VISIBLE, RELEVANT, EDIT_APPROVED and EXCLUDED roots. Read access is not edit consent; actual host permissions still apply.
- OBSERVED, SOURCE_BACKED, OWNER_ACCEPTED (with scope/revision), PROPOSED, ASSUMPTION, UNKNOWN, NOT RUN and NOT VERIFIED are distinct. A role cannot self-grant approval or report unobserved tests as passing.
- Inspect relevant project instructions, request/ticket, source and Git state before affecting files. Do not overwrite staged, unstaged or untracked user work. Recheck when resuming or after edits.
- Keep one canonical accepted AC revision for Feature; one original symptom/expected behavior plus reproduction evidence for Bug; and one bounded research question/decision record for Spike.
- Prefer existing tickets/PRs/ADRs. Quick avoids artifacts by default; Standard uses concise existing/compact records; Extended uses ordered, inspectable stage artifacts and revisioned state according to core/modes.md.
- Quick and Standard ask only for consequential decisions. Extended pauses after every applicable artifact-producing stage.
- Do not create downstream artifacts before their prerequisite stage passes its applicable transition/approval gate.

## State contract

Track only fields applicable to the selected route:

- task_type: feature | bug | spike; mode: quick | standard | extended; retain requested mode and reason.
- request_ref: original request/ticket and revision; known_decisions: exact evidence/approval and owner when known.
- roots: VISIBLE, RELEVANT, EDIT_APPROVED, EXCLUDED; include affected interfaces and project instructions.
- baseline and changed_snapshot per relevant root: branch/HEAD plus staged/unstaged patch identity and relevant untracked paths/content. HEAD alone is not a complete dirty-worktree identity.
- Feature: spec_ref, AC IDs and acceptance source/revision.
- Bug: original symptom, expected/actual, reproduction status and root-cause evidence.
- Spike: bounded question, evidence/confidence and verdict.
- design_and_verification: planned slices/test seams and observed verification evidence. Verification is owned by Developer, not a separate workflow stage.
- authority: bounded local edit roots/paths and separately authorized privileged/external actions.
- review: independent context identity, reviewed snapshot, outcome and findings.

Quick/Standard state may live in task context, ticket/PR or compact record. Extended requires durable state or truthful HANDOFF: NOT DURABLE outcome.

## Authorization

- A user request to implement/fix a clearly bounded local Feature/Bug can authorize ordinary local changes within that request, subject to host policy and stricter project/organization rules.
- A request to evaluate, plan, investigate, spike or review is read-only unless additional authority is explicitly granted.
- Spec/Plan approval is not blanket edit authorization. A user implementation request does not authorize every visible root, deletion of user work, installs, unrelated dependency changes, secrets, spending, commits/pushes/merges, cloud changes, production migrations or deployment.
- Use host permissions, hooks, CI and protected environments for enforcement where available. Markdown instructions alone are not a security boundary. If scope cannot be safely enforced, narrow or stop.

## Transition checks

A role's READY status is a proposal. Coordinator checks prerequisites and evidence before handoff.

| Responsibility | Entry | Required exit evidence | Block condition |
|---|---|---|---|
| Intake/route | User request | Task type, requested/effective mode, reason, scope, sources and risk | Material mismatch or consequential unknown |
| Feature Intent | WHY/WHO/scope unclear, or Extended requires it | Grounded outcome, target user, scope and non-goals | Material product intent unresolved |
| Feature Spec | Changed behavior lacks complete accepted ACs, or Extended requires it | Full source-linked, testable AC revision and complete ID map | Conflicting/untestable ACs or unresolved consequential WHAT |
| Feature Architect | Accepted WHAT and technical planning needed, or Extended requires it | AC-to-slice/root/interface/test-seam map, dependency order and relevant risks | Unresolved material HOW or unsafe plan |
| Bug Architect | Reported contract violation | Expected/actual, reproduction or qualified evidence, credible cause, regression seam and minimal plan | Evidence too weak or behavior contract unclear |
| Edit gate | Implementation requested; scope known | Bounded local grant and actual host permission; protected operations excluded | Missing authority/access or unclear scope |
| Developer build + verify | Edit gate passed; accepted Feature WHAT or credible Bug contract; fresh baseline | Actual changes, TDD evidence/exception, exact commands/results, AC/symptom coverage, regression/integration evidence, changed snapshot and honest gaps | Required verification missing, test failure, scope drift or stale baseline |
| Independent Reviewer | Stable changed snapshot and Developer evidence | Fresh independent context inspected exact diff/evidence and returned actionable verdict | Independence not verified, stale snapshot or missing evidence |
| Spike Researcher | Bounded feasibility question | Scope, supporting/contrary evidence, options, confidence, verdict and optional approved experiment results | Scope unclear, unsupported conclusion or no experiment authority |

## Developer verification and independent review

Developer must verify every applicable accepted Feature AC or the Bug's original symptom, run meaningful regression/integration checks, record exact commands and actual outcomes, inspect the changed diff and bind evidence to the current per-root snapshot. A passing unrelated test is not proof. Missing required checks are NOT RUN/BLOCKED, not success.

Reviewer independently inspects the actual diff (including relevant untracked files), accepted ACs or original Bug symptom, Developer's test evidence, security/data/compatibility risks and completeness. Self-review cannot yield AI_PASS. Any code change after verification invalidates affected evidence; any code change after review requires fresh verification and independent review.

For Bug, use VERIFIED_FIX only when credible evidence shows the original symptom resolved, regression evidence exists, required checks are credible and independent review is AI_PASS. Otherwise report PARTIAL or UNVERIFIED.

For Feature, distinguish IMPLEMENTED, VERIFIED, REVIEWED and READY_FOR_MERGE_REVIEW. None means merged or deployed.

## Completion

Return route/mode and reason, authoritative expectation (AC revision, Bug symptom or Spike question), relevant roots/snapshot, work performed, actual test commands/results and missing evidence, independent review verdict when applicable, unresolved risks and human next action. Extended returns the current review card and ends the turn while approval is pending.