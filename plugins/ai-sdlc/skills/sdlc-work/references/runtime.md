# Coordinator runtime — state, transitions and evidence

<identity>
One Coordinator owns routing, state and explicit authority. `routing.md` owns Feature/Bug/Spike paths and modes. `roles.md` owns responsibility and role outputs. No file or native subagent per stage is required. Project instructions and current real tool permissions still apply.
</identity>

<invariants>
- Never equate `VISIBLE`, `RELEVANT`, `EDIT_APPROVED`, and `EXCLUDED` roots. Read access is not edit consent; host permissions still enforce operations.
- `OBSERVED` (from real inspection), `SOURCE_BACKED`, `OWNER_ACCEPTED` (with scope/revision), `PROPOSED`, `UNKNOWN`, `NOT RUN` and `NOT VERIFIED` are different. An agent may not self-grant approvals or report an unobserved test as passing.
- Inspect appropriate current project instructions, request/ticket and change state before affecting files. Don't overwrite staged/unstaged/untracked user work. Re-check upon resuming or after edits; no assumed common HEAD across repositories.
- Keep a single canonical accepted AC set for Feature, a single original symptom plus regression/evidence record for Bug, or a single bounded question/decision record for Spike. Do not force Feature ACs into other routes.
- Prefer the existing ticket, PR or ADR as durable source. For multi-session work without a suitable persistent record, propose **one** short record with owner-approved location, not five per-role files; when not available label handoff `NOT DURABLE` and do not claim reliable cross-session continuation.
- Ask the human only for genuinely consequential outstanding decisions, normally one at a time after gathering evidence. Accepted decisions are not asked again unless materially stale.
</invariants>

<state-contract>
Track only fields relevant to selected route; values can live in existing ticket/PR, session record or a compact work record:

- `task_type`: `feature | bug | spike` and `mode`: `quick | standard | extended` (selected from `auto`).
- `request_ref`: original source/revision and `known_decisions`: exact approval/evidence with owner/time or `NOT VERIFIED`.
- `roots`: `VISIBLE`, `RELEVANT`, `EDIT_APPROVED`, `EXCLUDED`, plus affected interfaces and applied project instructions.
- `baseline` and `changed_snapshot` **per relevant root**: branch/HEAD plus staged+unstaged patch identity and relevant untracked contents/paths; refresh after edits. An uncommitted worktree is not identified by HEAD alone. Do not require a cryptographic hash where a reproducible git diff or content description is sufficient.
- `spec_ref + AC IDs/acceptance` for Feature; `symptom/ref + reproduction state + root cause evidence` for Bug; `question + evidence/confidence + verdict` for Spike.
- `design_and_verification`: planned slices/tests/integration/rollback as relevant; `authority`: permitted local edit roots/paths and separately permitted external/privileged actions.
- `verification`: observed exact commands/outcomes/time or `NOT RUN`, AC/symptom coverage, integration edges and omissions; `review`: independent context identity, reviewed snapshot, outcome/findings.
</state-contract>

<authorization>
- An explicit user instruction to **implement/fix** a clearly bounded feature or bug in selected local files/repositories can provide `EDIT_APPROVED` for ordinary project-local changes **within that request**, subject to real host policy and any stricter project/organization requirement. A request to evaluate, plan, spike, review, inspect, or propose is read-only; ambiguous or broadened scope requires an explicit grant.
- Spec/plan approval is NOT a grant for unrequested edits. A request to implement is NOT blanket authority to edit all visible roots, delete user work, install software, alter unrelated dependencies, spend money, fetch secrets, commit/push/merge, change cloud resources, run production migrations, deploy or perform external side effects.
- Enforce high-risk operations using host permissions, hooks, CI and protected environment controls when available; Markdown instructions alone cannot enforce filesystem/runtime restrictions. If scope cannot be enforced, narrow or stop.
</authorization>

<transition-gates>
Before advancing, Coordinator checks these entry, exit and block conditions. A `READY` worker status is a **proposal** until the gate is checked.

| Stage | Entry | Required exit evidence | Block / next |
|---|---|---|---|
| Intake & route | Request exists | Type, mode/reason, scope, sources, visible roots and baseline as relevant | Material mismatch → clarify, otherwise route |
| Feature Intent / Spec | Feature request, observed current behavior | Source-backed, testable, consistent ACs; full revision accepted when WHAT is new/consequential; unresolved choices excluded | Material WHAT unknown → `NEEDS_DECISION`, never Build |
| Bug assess | Bug request + baseline | Original expected/actual, `REPRODUCED` or credible `EVIDENCED_NOT_REPRODUCED`, cause hypothesis with evidence | Evidence too weak for safe patch → `UNVERIFIED`/STOP |
| Architect / fix plan | Accepted WHAT or credible bug cause | Small slices, affected files/interfaces, verification seams, actual risky trade-offs and rollback/compatibility when needed | Unresolved material HOW/risk → approval, else authorize |
| Edit gate | Implementation requested and plan scope known | Precisely bounded local change grant, host permission, protected ops excluded | Missing grant/access → plan only |
| Developer | Edit gate passed, fresh baseline | Identifiable changed snapshot, observed test results, justified TDD evidence/exception, scope check | Failures/side effects → repair or BLOCK |
| Verify & Converge | Actual changes and expectations | All applicable ACs/symptom covered, meaningful regression, integrations/contracts and omitted tests identified on **current** snapshot | Missing critical requirement/evidence → repair or `BLOCKED`, not pass |
| Independent Reviewer | Stable changed snapshot | Fresh separate reviewer actually inspected diff, coverage and evidence on same snapshot; actionable verdict | No fresh review → `REVIEW: PENDING`; findings → repair and re-verify/re-review |
| Human handoff | Current verdict or documented limits | Changed/reviewed snapshot, evidence, outstanding risks, release order and separate next permissions | AI never authorizes merge/deploy |
| Spike decision | Bounded question and sources | Evidence for/against, confidence, `PROCEED/CLARIFY/STOP`, explicit no-build termination | Insufficient evidence → `CLARIFY`, STOP |

Quick may omit unnecessary role prose, not the safety/evidence gates. Standard/Extended increase thoroughness for actual risk. A spike does not enter Edit/Developer/Reviewer by default. A sandbox POC needs its own approval and can never be presented as reviewed product code.
</transition-gates>

<verify-and-converge>
1. **Correctness:** verify each changed Feature AC or Bug original symptom with independent observation where possible. A passing unrelated test is not proof.
2. **Completeness:** compare source goal → accepted ACs / bug symptom → planned slices → actual diff → tests; flag missing behavior, forgotten tasks and scope drift. Do not count a test file's existence as test execution.
3. **Integration:** check affected roots, API/schema/deployment skew, data and authorization paths where implicated. Mark inaccessible checks `NOT RUN` with impact rather than claiming them.
4. **Freshness:** bind result to changed snapshot; after repair/rebase/new file changes invalidate affected verification/review and re-run appropriately. Up to three AI repair/review rounds before human escalation.
5. `AI_PASS` only after actual independent current-snapshot reviewer concludes required evidence is complete. On Bug, additionally distinguish `VERIFIED_FIX | PARTIAL | UNVERIFIED`; on Feature, distinguish `IMPLEMENTED`, `VERIFIED`, `REVIEWED`, and `READY_FOR_MERGE_REVIEW` (not MERGED or DEPLOYED).
</verify-and-converge>

<completion>
Return one short outcome: route/mode and reason, authoritative expectation (AC revision / bug original symptom / spike question), roots and snapshots if applicable, what changed or researched, observed tests and missing evidence, reviewer independence/verdict when needed, decisions and human next action. Do not generate redundant stage reports.
</completion>
