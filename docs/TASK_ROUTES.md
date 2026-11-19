# Three supported task types — examples and expected artifacts

Task type is independent from execution mode. Use `auto` unless you need explicit `quick`, `standard` or `extended`. Examples describe expected workflow decisions, **not performed host runs**.

For Extended, each applicable route stage requires human approval before the next begins, regardless of prior acceptance or risk determination. See [Extended guide](EXTENDED.md) for the exact stage sequence and resume protocol. The compact artifact advice below refers to Quick/Standard.

## Feature — add customer status

**Request:** `sdlc-work feature standard Add customer status to FE and BE, with a Flyway migration only if necessary. Terraform read-only.`

- **Intake:** inspect four roots, current instructions/contracts/tests; separately mark actual edit scope. Identify preexisting branch/untracked changes.
- **Intent/Spec:** reuse accepted issue. If status states or access rights are not settled in source, ask only material owner questions. Full source-linked ACs (for example `AC-01` API returns persisted accepted status; `AC-02` FE shows it) need owner acceptance when their behavior is newly proposed.
- **Architect:** map each AC to minimal slice, per-root code and test seam; decide migration and compatibility based on actual schema. Determine real release dependencies, not a hardcoded Flyway→BE→FE order.
- **Developer:** when local edits are authorized, use targeted RED/GREEN and actual regression/integration checks. Preserve unrelated user work.
- **Verify/Converge + Reviewer:** all ACs, tests and integration edges accounted for on current per-root diff snapshot; independent review. Handoff separate merge/deploy decisions.

**Durable record:** authoritative full AC revision plus work/evidence at existing ticket/PR, not a mandatory five-file tree. See `EXAMPLE_SPEC_REVIEW.md` and `EXAMPLE_MULTI_REPO.md` for more detail.

## Bug — endpoint returns 500 instead of existing 400 contract

**Request:** `sdlc-work bug quick Fix a login endpoint returning 500 for an empty password; verify existing 400 contract.`

- **Assess:** capture supplied report and environment, inspect documented/current API behavior and reproduce `actual=500`, `expected=400` if possible. Do not invent a reproduction or treat a guessed cause as fact.
- **Diagnose:** trace one credible cause and associated test seam. If existing contract is actually unclear, stop and clarify expected WHAT rather than silently pick status 400.
- **Fix:** bounded implement request may authorize matching local code paths; add a regression RED for the actual failure when feasible, fix minimally, execute GREEN and relevant non-regression checks.
- **Verify/Converge:** show before/after response on applicable environment, meaningful regression and integration checks, affected snapshot; independent reviewer checks defect **and** completeness. If reproduction or critical test unavailable, say `PARTIAL`/`UNVERIFIED`, not `VERIFIED_FIX`.

**Durable record:** symptom/expected/actual, reproduction evidence, cause, change/test commands and verdict; no new Feature AC set unless expected product behavior changes.

## Spike — choose offline synchronization approach

**Request:** `sdlc-work spike standard Determine feasibility of offline sync for mobile. Compare alternatives; research only.`

- **Bound:** question, constraints, existing architecture evidence, scope, success/stop criteria. No automatic repo edits.
- **Research:** inspect current contracts where available, compare approaches and disconfirming evidence, risks and practical unknowns. Mark assumptions vs observed facts, cite external sources when actually used.
- **Decide:** return `PROCEED` (recommend separate implementation planning), `CLARIFY` (critical unknown), or `STOP` (not warranted) with confidence, trade-offs and unanswered questions.
- **Stop:** no Spec/AC/build/reviewer chain and no silent feature implementation. A POC would require a separately approved disposable scratch scope.

**Durable record:** brief research decision or existing issue comment, not `intent.md` + `spec.md` + `plan.md`.

## Boundary cases

- "Investigate API error" with no fix requested → Bug diagnosis only (read-only), not an implicit code-edit grant.
- "Add a validation rule to fix a bug" → if existing contract does **not** establish that rule, clarify new Feature WHAT before changing product behavior.
- "Research and implement if feasible" → finish Spike first, report recommendation, request a separately bounded Feature task. Avoid treating one instruction as unlimited end-to-end authority.
- Security bypass in one repo → Bug / Extended; two simple repos do not automatically mean Extended.
