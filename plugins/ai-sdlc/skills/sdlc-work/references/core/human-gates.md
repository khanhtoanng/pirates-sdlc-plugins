# Extended checkpoints — authoritative stage and approval policy

Extended is a **human-checkpoint-driven** workflow, not just extra analysis. Applies even when existing requirements are already accepted or no new decision is needed. Quick/Standard retain decision-based gates in practices/review.md; existing authority and safety checks apply in all modes.

## Ordered stage IDs and artifacts

| Task | Stage ID (in order) | Review artifact / human focus |
|---|---|---|
| Feature | intent | intent.md — WHY/WHO, scope, non-goals |
| Feature | spec | spec.md — full source-backed ACs and map covering every AC ID |
| Feature | plan | plan.md — design, slices, tests, scope, compatibility/rollback |
| Feature | implementation | implementation.md — actual changes, scope, TDD, changed snapshot |
| Feature | verification | verification.md — observed AC→test evidence, integrations and gaps |
| Feature | review | review.md — independent verdict, findings, current snapshot, next permissions |
| Bug | assessment | assessment.md — expected/actual, environment, severity, baseline |
| Bug | diagnosis | diagnosis.md — reproduction, credible cause/evidence and uncertainty |
| Bug | plan | plan.md — minimal repair, regression tests, blast radius/rollback |
| Bug | implementation | implementation.md — actual fix, before/after and changed snapshot |
| Bug | verification | verification.md — original symptom and meaningful regressions |
| Bug | review | review.md — independent verdict, gaps and next permissions |
| Spike | scope | scope.md — bounded question, constraints, exit criteria |
| Spike | research | research.md — evidence, contrary evidence, options, confidence |
| Spike | experiment-plan | experiment-plan.md — optional scratch-only scope and grant |
| Spike | experiment | experiment.md — optional observed results and limitations |
| Spike | decision | decision.md — PROCEED/CLARIFY/STOP and rationale; no build |

- Feature Intent and Spec are distinct in Extended even if preaccepted: summarize existing evidence instead of inventing or re-deciding requirements. Bug does not need fictional feature ACs. Spike has no production build or code reviewer. Approve research before deciding if an experiment is needed. Without an experiment, explicitly record both optional stages NOT_APPLICABLE with reason.
- Respect the requested stopping point: plan-only/diagnosis-only/review-only requests never expand into implementation. Record downstream stages NOT_APPLICABLE with reason or leave pending for separately authorized continuation. Missing evidence is BLOCKED, not NOT_APPLICABLE.
- Intake is classification, not an extra SDLC stage; show routing and scope before starting. Do not invoke downstream roles, generate downstream artifacts or run their actions before the previous checkpoint is approved. Developer's own TDD/test execution belongs to implementation, not the later independent convergence stage.
- In Extended, split combined runtime evidence rows: Intent needs outcome and scope, not completed ACs; Spec needs a complete proposed AC revision with no unresolved material choices, then human approval supplies acceptance if needed; Bug Assessment needs symptom/expected/actual/baseline, Diagnosis needs the reproduction and cause evidence. Do not require downstream evidence prematurely.

## Transition protocol

1. Run ONLY the current stage. Check its exit evidence (runtime.md and selected workflow/role), including unknowns, actual permissions and prerequisites. AI validation is not human approval. If incomplete, mark BLOCKED or NEEDS_DECISION and ask for missing evidence/decision. Do not advance.
2. Persist its inspectable artifact and update state to `awaiting_human_approval` with revision and relevant snapshots. Present a short card with stage ID, revision, actual artifact link/path, decision summary, risks, exclusions, evidence/limitations and AI validation status. Human must have access to the full artifact.
3. End the turn. Do not sleep/poll, execute the next stage, treat silence as consent, or ask a worker to simulate an owner. Use native ask/approval UI if available, otherwise return a clear chat prompt. Tool approval is not stage approval.
4. On next user turn, reload the exact state/artifact and check current sources/scopes/snapshots. Accept only explicit approval of the current named stage and revision (e.g. `approve intent r1`), or unambiguous reply to the displayed exact stage. Record human message/reference, time, stage and revision; never invent authority. A generic implement request or advance-all instruction is not approval for unseen future artifacts.
5. Request changes: return to current stage, record feedback, increment revision, validate again and stop for new approval. Reject/cancel: stop with status cancelled. Ambiguous response: clarify, no advance. Approved: mark that stage approved; only then start the next applicable stage. Last approval completes the route with its evidence-based disposition, not merge/deploy authorization.
6. Material change to an artifact, source, scope, plan or code snapshot invalidates the corresponding and dependent approvals/verification/review. Preserve history and return to earliest affected stage. If verification or review finds a material defect, present the blocked result and proposed repair to the human and stop before re-entering implementation. Repeat human gates for changed/dependent artifacts and use a fresh reviewer; max three AI repair/review loops before escalation. Do not repeat approval of unaffected unchanged outputs.
7. Required stage approval never waives edit authorization or independent review. If independent reviewer unavailable, report pending/blocked; the human can acknowledge limitations but cannot turn missing evidence into AI_PASS.

## Durable records

Use an existing authorized ticket/PR/ADR with distinct stage sections and revision identifiers, or ask once for permission to create a single task folder such as `.sdlc/changes/<task-id>/` in one agreed writable root. Do not scatter files across repos. Use only applicable stage files plus state.json. Documentation-only writes do not authorize source edits; read-only scope must stay read-only.

For the local folder format, maintain state.json with `schema_version: 1`, `task_id`, `task_type`, `requested_mode`, `mode`, `mode_reason`, `current_stage`, `status`, `stages` keyed by every route stage ID plus source/scope/snapshot/authority references and approval history. Each stage has status (pending, in_progress, awaiting_human_approval, approved, blocked, needs_decision, cancelled, invalidated, not_applicable), integer revision (0 before creation), artifact path/section, evidence and approval when approved. An approval is an object with integer `revision`, `response_ref` (exact quoted human response or durable message locator), and time when available. Top status is current stage status or completed/cancelled; stage table and top agree; on completion current_stage remains the last approved stage. Update record before returning control, never create placeholder downstream artifacts. A tracker may use equivalent fields.

If a durable location is denied/unavailable, report HANDOFF: NOT DURABLE; provide pasteable state and stop at current checkpoint, with no claim of reliable cross-session continuation. On resume, use `sdlc-work resume <task-id or record>` or identify the existing task naturally; do not reroute a pending task unless new facts warrant it. Check approval and snapshot freshness before continuing.
