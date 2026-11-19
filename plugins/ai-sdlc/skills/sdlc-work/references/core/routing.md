# Task routing — authoritative Feature / Bug / Spike classification

<task-types>
Task type answers **what workflow** to run. Mode answers **how much rigor** to apply. These are independent axes; never treat `spike` as a risk mode. Classify exactly one primary type per invocation; split mixed requests into named, sequential outcomes with separate approvals.

| Type | Use when | Core route | Exit outcome |
|---|---|---|---|
| `feature` | Add or intentionally change accepted observable behavior | Understand WHY/WHAT → source-backed AC readiness → HOW and verification plan → authorized build → converge → independent review | Delivery evidence + release readiness |
| `bug` | Existing behavior violates an accepted expectation or reproducible contract | Report symptom → reproduce/baseline → diagnose cause → plan minimum fix + regression → authorized fix → verify original failure and regressions → independent review | `VERIFIED_FIX`, `PARTIAL`, or `UNVERIFIED` + evidence |
| `spike` | Answer feasibility, research or architectural uncertainty without committing to production implementation | Bound question → inspect/research → compare options and counterevidence → optional approved POC → decision brief → STOP | `PROCEED`, `CLARIFY`, or `STOP`, advisory only |

Only the three task types above are valid. Refactoring, dependency updates and infrastructure changes are **not additional task types**: route to `feature` when knowingly changing accepted outcome/contract; route to `bug` when repairing a demonstrated regression; route to `spike` when assessing approach without committed implementation. For behavior-preserving maintenance, route as `feature` with explicit invariants and regression proof, without inventing new product ACs. If actual bug repair requires a changed product rule, pause for accepted WHAT under Feature Spec before proceeding.
</task-types>

<decision-procedure>
1. Identify the desired outcome and requested authority (research/diagnose/plan only vs implementation). Read the request and proportionate source evidence first.
2. If the goal is to answer a feasibility or choice question without committed delivery, select spike. Investigation of a reported defect with a known or claimed existing expectation is bug diagnosis, even without a fix request.
3. If an existing contract is allegedly violated, select bug; unverified reproduction is a diagnosis state, not proof of the defect. If the expected contract is genuinely ambiguous, clarify before changing behavior.
4. If a new/changed capability or committed maintenance/refactor/upgrade is requested, select feature. Preserve invariants for maintenance.
5. Respect a supplied type unless evidence reveals a material mismatch, in which case explain and clarify before proceeding. Split mixed outcomes; finish a spike before a separately authorized feature/bug. Never infer edit permission from type.
6. Report task_type, requested_mode, effective mode (after core/modes.md), scope, reason, risk and material unknowns in a concise intake card. Include the machine-readable line `SDLC_ROUTE: task_type=feature; mode=standard` (substitute actual values). Repeat that line on resume and escalation. Do not invent evidence or emit it in unrelated chat.
</decision-procedure>

<routing-examples>
- "Add a customer status to FE/API" → feature / standard (escalate only on proven risk).
- "API returns 500 for empty password instead of expected 400" → bug / quick or standard depending on impact.
- "Explore whether offline sync is feasible" → spike / standard; stop after recommendation.
- "Should we use Postgres or DynamoDB?" → spike, not a feature implementation.
- "Fix authorization bypass" → bug / extended regardless of one repository.
</routing-examples>
