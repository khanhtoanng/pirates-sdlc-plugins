# Feature workflow

A Feature adds or intentionally changes observable product behavior. Normal order is Intent (when needed) → Spec (when needed) → Architect (when needed) → Developer → independent Reviewer.

## Role sequence by mode

| Responsibility | Quick | Standard | Extended |
|---|---|---|---|
| Intent | Skip when problem and scope are clear | Run when WHY/WHO/outcome/scope needs definition | Always a stage; summarize accepted evidence if settled |
| Spec | Reuse complete accepted ACs | Run when accepted ACs are incomplete | Always a stage; show every AC ID and full revision |
| Architect | Skip for a small established pattern | Run for meaningful design/dependencies | Always a plan stage |
| Developer | Implement and verify; parallelize only independent AC slices when safe | Same, with applicable plan and handoffs | One gated build-and-verify stage; safe parallel slices may run within the stage |
| Reviewer | Fresh independent review after code changes | Fresh independent review after code changes | Separate gated review stage |

Quick requires established behavior, an established approach and low risk. Standard runs applicable roles without per-stage approvals. Extended runs every listed stage and pauses after each artifact approval.

## Extended artifacts

1. Intent — 01-intent.md
2. Spec — 02-spec.md
3. Architect — 03-plan.md
4. Developer — 04-implementation.md (TDD and verification evidence)
5. Reviewer — 05-review.md

Use one authorized task directory with state.json or an existing revisioned ticket/PR. Create only the current artifact.

## Handoffs

- **Intent** establishes WHY, WHO, outcome, scope and non-goals.
- **Spec** defines stable AC IDs, observable rules, provenance and a complete AC map. An unresolved consequential WHAT blocks planning.
- **Architect** maps every accepted AC to minimal slices, affected roots/interfaces, dependencies, test seams, operational risks and safe/unsafe parallel boundaries.
- **Developer** follows the accepted scope and `practices/tdd.md`, parallelizes only independent AC slices under `practices/delegation.md`, integrates the slices, verifies every AC and relevant regression/integration, and records exact commands/results and per-root snapshots.
- **Reviewer** independently inspects the actual integrated diff, AC coverage and Developer evidence. A stale snapshot or unverified independence cannot receive AI_PASS.

The accepted AC revision is the canonical Feature expectation. Do not add behavior silently during implementation or review. Parallel execution never changes the AC set or removes the final integration/review requirement.

## Exit outcomes

- READY_FOR_MERGE_REVIEW: accepted requirements, implementation, verification and independent review support human release review.
- NEEDS_DECISION: a consequential product/technical decision remains.
- BLOCKED: a required dependency, permission, decision, test or reviewer capability is missing.

READY_FOR_MERGE_REVIEW does not authorize merge, production migration or deployment.
