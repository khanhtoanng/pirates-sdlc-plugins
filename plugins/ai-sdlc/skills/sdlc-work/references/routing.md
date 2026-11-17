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

<modes>
`auto` chooses the smallest warranted intensity. User can request more rigor, but a low requested level cannot override actual high-risk gates. Multi-repository count alone is not `extended`.

| Mode | Trigger / rigor | Human checkpoints |
|---|---|---|
| `quick` | Bounded, established requirement/symptom, low-risk changes; minimal notes and test evidence | Material unknowns only; check allowed edit scope |
| `standard` | Normal feature/bug/spike requiring focused discovery, traceable tests and review | Any newly decided WHAT and consequential design/scope |
| `extended` | Real security/authorization, destructive data, breaking interface, irreversible infrastructure, regulatory or production risk | Explicit risk/design/recovery and qualified acceptance as applicable |

For spikes, depth changes research effort and evidence needed, not permission to implement. Legacy `sdlc-work spike <question>` maps to `task=spike, mode=auto` for compatibility.
</modes>

<feature-route>
1. Inspect existing ticket/contracts and relevant roots. Intent asks WHY/WHO only if consequential ambiguity remains; no speculative brainstorming transcript.
2. Spec reuses the accepted AC revision or drafts full observable source-linked ACs. Separate REQUIRED acceptance rules from VERIFY examples (`coverage.md`). **Spec gate:** all changed ACs are testable, mutually consistent, authority-backed and accepted where consequential; open material decisions block build.
3. Architect maps AC→vertical slice→root/interface/test seam, compatibility, rollback and rollout where implicated. **Plan gate:** impact and verification plan are credible; sensitive technical trade-offs resolved.
4. Confirm authorized edit scope, build slices test-first where applicable, verify and converge ACs plus dependencies, then independent review on the current snapshot. Any code change invalidates prior review.
5. Report `READY_FOR_MERGE_REVIEW` only if required evidence and independent verdict support it; this does not authorize merging, deploying or running migrations.
</feature-route>

<bug-route>
1. Record symptom, expected vs actual, occurrence, environment, severity, affected boundaries and original report reference. Preserve a useful baseline and current changes.
2. Reproduce with observed failure/log or trustworthy exact reporter evidence. Separate `REPRODUCED`, `EVIDENCED_NOT_REPRODUCED` and `UNVERIFIED`. Do not claim root cause from correlation. If evidence is inadequate for a safe fix, return diagnosis and the smallest missing reproduction request; no speculative patch.
3. Investigate cause, compare plausible causes only as needed, identify regression seam and blast radius. Build a minimum fix plan and check it preserves established behavior; a new business choice returns to Feature Spec/human gate.
4. After bounded edit authorization, capture a failing regression first where feasible; implement minimal repair and rerun original reproduction, targeted test and affected regressions. Report before/after observations, remaining gaps and affected roots.
5. Verify & Converge against **the original symptom, root-cause hypothesis, regression protection, and compatibility**, then independent review on current changed snapshot. `VERIFIED_FIX` requires credible original symptom resolution, regression evidence, required checks and independent `AI_PASS`; else return `PARTIAL`/`UNVERIFIED` explicitly.
</bug-route>

<spike-route>
1. Define one answerable question, context, constraints, success/exit evidence, in-scope roots, time/effort budget if supplied, and what is explicitly NOT being implemented.
2. Investigate existing code, available documentation, options, costs, failure cases and disconfirming evidence. Label `OBSERVED`, `SOURCE_BACKED`, `ASSUMPTION`, `UNKNOWN`. Use external citations only when accessible; do not invent up-to-date facts.
3. A POC is optional and must have a separate bounded scratch/experiment grant. A disposable unmerged scratch POC is NOT production implementation or feature acceptance; if actual production/repository code changes are proposed, end the spike and ask for a new Feature/Bug invocation plus normal change gates.
4. Return concise decision brief: question; evidence and confidence; viable options/trade-offs; recommendation `PROCEED | CLARIFY | STOP`; unanswered risks; recommended next task (if any). **STOP** without creating acceptance criteria, starting a build, or granting itself approval to proceed.
</spike-route>

<routing-examples>
- "Add a customer status to FE/API" → feature / standard (escalate only on proven risk).
- "API returns 500 for empty password instead of expected 400" → bug / quick or standard depending on impact.
- "Explore whether offline sync is feasible" → spike / standard; stop after recommendation.
- "Should we use Postgres or DynamoDB?" → spike, not a feature implementation.
- "Fix authorization bypass" → bug / extended regardless of one repository.
</routing-examples>
