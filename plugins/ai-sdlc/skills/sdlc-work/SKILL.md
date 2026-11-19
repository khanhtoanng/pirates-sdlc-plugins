---
name: sdlc-work
description: Coordinate SDLC feature delivery, bug diagnosis/fix, or bounded technical feasibility research in one or multiple repositories. Auto-select quick, standard, or extended (mandatory per-stage human review), or resume a pending SDLC task. Use for scoped engineering work and explicit SDLC requests, not unrelated explanations or general Q&A.
argument-hint: "[feature|bug|spike] [auto|quick|standard|extended] <request> [selected roots] | resume <task-id or record>"
---

# AI SDLC work — router and coordinator

<purpose>
Execute the SDLC from this installed plugin. Do not bootstrap or duplicate agent/role files in the project. One coordinator owns the state; Intent, Spec, Architect, Developer and Reviewer are **logical roles**, not mandatory subagents. Only three task types exist: `feature`, `bug`, `spike`.
</purpose>

<start>
1. Read `references/core/routing.md`, `references/core/modes.md` and `references/core/runtime.md`. Inspect current request, sources, project rules, risk and Git state proportionately. Classify type and mode independently; legacy positional spike selects type spike/mode auto. State route, requested/effective mode, reason and scope. If resuming, reload state and pending approval instead of starting over.
2. Read ONLY the selected workflow: `references/workflows/feature.md`, `references/workflows/bug.md`, or `references/workflows/spike.md`. Read `references/core/human-gates.md` for Extended (including escalation/resume). Extended: never advance to any next applicable stage until explicit approval of the exact current artifact revision; persist stage state, present review card and END TURN.
3. Load on demand: `references/roles/shared.md` and relevant role in references/roles/ (intent, spec, architect, developer, reviewer, researcher); `references/practices/coverage.md` for ACs/regressions; `references/practices/tdd.md` before executable changes; `references/practices/workspace.md` for multi-root; `references/practices/review.md` for review/handoffs; `references/practices/delegation.md` for independent review; hosts/{claude,cursor,codex}.md only for actual host capabilities; `references/practices/integrations.md` for selected add-ons.
4. Follow route and runtime evidence checks; re-evaluate risk each stage. User-specified scoped implementation may authorize ordinary local edits under real host permissions, but never bypass Extended checkpoints or grant excluded roots, commit/push/merge, applied migrations, production, deployment or external side effects.
5. Return factual evidence and the route-specific outcome. If necessary permissions, decisions, access, or tests are missing, report the precise blocked or unverified state; do not fabricate approval or results.
</start>

<routes>
See the chosen workflow and mode policy; these references own the stage sequence and gates.
</routes>

<guardrails>
Do not manufacture current test outputs, reviewer isolation, approvals, or implementation status. A self-review cannot yield `AI_PASS`. A source edit reviewed on a stale snapshot needs re-verification/review. If reviewer cannot actually run independently, report `INDEPENDENCE: NOT VERIFIED` and `REVIEW: PENDING`; never imply final AI approval. A research-only spike needs no feature ACs, production implementation, or code reviewer.
</guardrails>
