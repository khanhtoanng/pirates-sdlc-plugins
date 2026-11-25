# Feature workflow

A Feature adds or intentionally changes observable product behavior. Normal responsibility order is Intent (when needed) → Spec (when needed) → Architect (when needed) → Developer (implementation + verification) → independent Reviewer.

## Role sequence and mode applicability

| Order | Responsibility | Quick | Standard | Extended |
|---|---|---|---|---|
| 1 | Intent | Skip when problem/user/outcome/scope are clear | Run when WHY/WHO/outcome/scope need clarification | Always a distinct stage; summarize accepted evidence if already settled |
| 2 | Spec | Reuse complete accepted ACs; stop if expected behavior is materially unknown | Run when changed behavior lacks a complete accepted AC set | Always a distinct stage; show every AC ID and exact full revision |
| 3 | Architect | Skip separate stage for a small established pattern | Run for meaningful design, dependencies, or multi-component slicing | Always a distinct stage and plan artifact |
| 4 | Developer | Implement + verify | Implement + verify | One gated implementation + verification stage |
| 5 | Reviewer | Fresh independent review after code changes | Fresh independent review after code changes | Separate gated independent review |

Quick is permitted only when requirements and approach are established and risk is low. Standard executes all applicable responsibilities in order without mandatory stage-by-stage approvals. Extended executes every listed Feature stage, produces one artifact per stage and pauses after each approval.

## Extended artifacts

- Intent: 01-intent.md
- Spec: 02-spec.md
- Architect: 03-plan.md
- Developer: 04-implementation.md (includes TDD and all verification evidence)
- Reviewer: 05-review.md

Use one authorized task directory with state.json or an existing revisioned ticket/PR record. Create only the current artifact. Do not create verification.md or a separate Verifier stage.

## Feature-specific handoffs

1. Intent establishes WHY, WHO, outcome, scope and non-goals. It does not define ACs or technical design.
2. Spec creates stable AC IDs, observable/testable rules, provenance, REQUIRED versus VERIFY classification, decisions and a complete AC map. Unresolved consequential WHAT blocks planning.
3. Architect maps every accepted AC to minimal implementation slices, affected roots/interfaces, actual dependency order, test seams and relevant risks. It does not implement or claim tests ran.
4. Developer follows the accepted scope and plan, performs TDD where applicable, implements in slice order, verifies each AC plus meaningful regressions/integrations, inspects the actual diff and records exact commands/results and per-root snapshots.
5. Reviewer uses a fresh independent context to inspect the actual diff, all ACs and Developer evidence. A stale snapshot or missing independent context cannot receive AI_PASS.
6. Coordinator reports READY_FOR_MERGE_REVIEW only when requirements, verification evidence and independent review support it. This does not authorize merge, production migration or deployment.

## Exit outcomes

- READY_FOR_MERGE_REVIEW: accepted requirements, implementation, verification and independent review support human release review.
- BLOCKED: a required dependency, permission, decision, test or reviewer capability is missing.
- NEEDS_DECISION: a consequential product or technical decision needs the owner.

The accepted AC revision is the single canonical Feature expectation. Do not silently add behavior during implementation or review.