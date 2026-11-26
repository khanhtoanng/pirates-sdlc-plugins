# Feature workflow

A Feature adds or intentionally changes observable product behavior. Normal order is Intent (when needed) → Spec (when needed) → Architect (when design or delivery slicing is needed) → Developer → independent Reviewer.

## Role sequence by mode

| Responsibility | Quick | Standard | Extended |
|---|---|---|---|
| Intent | Skip when problem and scope are clear | Run when WHY/WHO/outcome/scope needs definition | Always a stage; summarize accepted evidence if settled |
| Spec | Reuse complete accepted ACs | Run when accepted ACs are incomplete | Always a stage; show every AC ID and full revision |
| Architect | Skip for a small established pattern | Run for meaningful design, dependencies or multi-slice delivery | Always a plan stage |
| Developer | Implement and verify; validate any applicable plan and parallelize only safe independent slices | Same, with applicable plan and handoffs | One gated build-and-verify stage; validate approved plan and safe parallel slices within the stage |
| Reviewer | Fresh independent review after code changes | Fresh independent review after code changes | Separate gated review stage |

Quick requires established behavior, an established approach and low risk. Standard runs applicable roles without per-stage approvals. Extended runs every listed stage and pauses after each artifact approval.

## Extended artifacts

1. Intent — 01-intent.md
2. Spec — 02-spec.md
3. Architect — 03-plan.md
4. Developer — 04-implementation.md (TDD and verification evidence)
5. Reviewer — 05-review.md

Persist Extended Feature artifacts in the canonical task directory `.sdlc/changes/<task-id>/` selected by the Coordinator under references/core/modes.md. An existing ticket/PR may be linked as a source reference, but is not an alternate location for plugin state or stage artifacts. Create only the current artifact.

## Handoffs

- **Intent** establishes WHY, WHO, outcome, scope and non-goals.
- **Spec** defines stable AC IDs, observable rules, provenance and a complete AC map. An unresolved consequential WHAT blocks planning.
- **Architect** investigates the current system, explains material technical choices, maps every accepted AC to complete outcome-oriented slices, records genuine blocker reasons, proposes safe parallel groups, identifies test seams and assesses relevant risks.
- **Developer** validates the approved slices against the fresh baseline and actual host/worktree isolation. It owns execution-level dispatch, follows the accepted scope and `practices/tdd.md`, integrates slices, verifies every AC and relevant regression/integration, and records exact commands/results and per-root snapshots. Material plan changes return through Architect and the Coordinator.
- **Reviewer** independently inspects the actual integrated diff, AC coverage and Developer evidence. A stale snapshot or unverified independence cannot receive AI_PASS.

The accepted AC revision is the canonical Feature expectation. Do not add behavior silently during implementation or review. Parallel execution never changes the AC set or removes the final integration/review requirement.

## Exit outcomes

- READY_FOR_MERGE_REVIEW: accepted requirements, implementation, verification and independent review support human release review.
- NEEDS_DECISION: a consequential product/technical decision remains.
- BLOCKED: a required dependency, permission, decision, test or reviewer capability is missing.

READY_FOR_MERGE_REVIEW does not authorize merge, production migration or deployment.
