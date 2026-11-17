---
name: sdlc-work
description: Execute evidence-backed Feature delivery, Bug diagnosis/fix, or a bounded research Spike in one or multiple repositories. Choose quick, standard, or extended rigor without generating a project harness. Use for SDLC feature work, bug fixing, feasibility research, and scoped implementation.
argument-hint: "[feature|bug|spike] [auto|quick|standard|extended] <request> [selected roots]"
---

# AI SDLC work — router and coordinator

<purpose>
Execute the SDLC from this installed plugin. Do not bootstrap or duplicate agent/role files in the project. One coordinator owns the state; Intent, Spec, Architect, Developer and Reviewer are **logical roles**, not mandatory subagents. Only three task types exist: `feature`, `bug`, `spike`.
</purpose>

<start>
1. Read `references/routing.md` to classify the task and determine required route; choose `auto` (default), `quick`, `standard` or `extended` rigor independently. Legacy positional `spike` means task type `spike` with mode `auto`. Ask only if the ambiguity materially changes what is authorized or expected; otherwise infer from the request and state the choice.
2. Read `references/runtime.md` for coordinator transitions, approvals and evidence states. Inspect relevant source, request, accepted decisions, effective repository rules and Git changes proportionately before implementation. In a research-only spike without a repository, code/Git inspection is optional.
3. **Load on demand**, not all references upfront: `roles.md` when exercising a role; `coverage.md` for feature ACs and meaningful bug regression cases; `tdd.md` before executable changes; `workspace.md` for multiple roots or integration boundaries; `review.md` for human gates/handoffs; `delegation.md` for independent review; `hosts/{claude,cursor,codex}.md` only for actual host capabilities; `integrations.md` only for explicitly selected add-ons.
4. Follow the selected route and stage exit checks in `runtime.md`. User-specified scoped implementation can authorize ordinary local edits under real host permissions; never interpret it as rights to edit excluded roots, commit/push/merge, apply migrations, mutate production, deploy, or perform external side effects.
5. Return factual evidence and the route-specific outcome. If necessary permissions, decisions, access, or tests are missing, report the precise blocked or unverified state; do not fabricate approval or results.
</start>

<routes>
- **Feature:** grounded Intent/Spec as needed → Architect/verification plan → scope gate → vertical-slice Developer → Verify & Converge → independent Reviewer for code changes → release-readiness handoff.
- **Bug:** capture symptom and baseline → reproduce or establish credible failing evidence → investigate root cause → scoped fix/test plan → scope gate → regression-first Developer → verify original symptom and regressions → independent Reviewer → fix disposition.
- **Spike:** bound question and investigation budget → research evidence for and against options, optional explicitly authorized disposable POC → recommendation with confidence and unresolved unknowns → **STOP**. It never silently becomes feature implementation.
</routes>

<guardrails>
Do not manufacture current test outputs, reviewer isolation, approvals, or implementation status. A self-review cannot yield `AI_PASS`. A source edit reviewed on a stale snapshot needs re-verification/review. If reviewer cannot actually run independently, report `INDEPENDENCE: NOT VERIFIED` and `REVIEW: PENDING`; never imply final AI approval. A research-only spike needs no feature ACs, production implementation, or code reviewer.
</guardrails>
