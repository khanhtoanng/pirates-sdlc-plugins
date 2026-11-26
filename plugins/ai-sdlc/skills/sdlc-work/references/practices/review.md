# Human decisions and review handoffs

This practice defines what the Coordinator presents to a human and when an explicit decision is needed. It does not define the technical code-review procedure; that belongs to `roles/reviewer.md`. Extended stage approvals and resume rules are owned by `core/modes.md`.

## Human decision ownership

| Transition | AI prepares | Human action is needed when |
|---|---|---|
| Feature Intent / Spec | Outcome, source-linked changed ACs, complete AC ID map and non-goals | A consequential WHY/WHO/WHAT/scope decision remains or the owner must accept the exact Spec revision |
| Bug diagnosis | Original symptom, expected/actual evidence, cause confidence and minimum repair | Expected behavior changes or a material safety/data decision is needed |
| Architect / fix plan | Recommended approach and rationale; numbered outcome-oriented implementation slices; AC coverage; genuine blockers with reasons; proposed parallel groups; test seams and relevant risks | Human judges task granularity, dependencies, scope, or a material technical trade-off; Extended always requires approval of the exact plan revision |
| Local implementation | Exact roots, paths and bounded operations | Host/project policy requires an additional grant; planning/research alone never authorizes edits |
| Code review | Independent findings, verification gaps and residual risks | Organization-specific or high-risk final acceptance is required; review does not authorize merge/deploy |
| Spike decision | Evidence, contrary evidence, options, confidence and PROCEED/CLARIFY/STOP | Owner decides whether to create a separate Feature/Bug task |

Do not re-approve unchanged accepted sources or claim unobserved consent. AI workers do not ask the owner directly or grant themselves authority; the Coordinator raises one material question at a time.

## Architect plan review card

Use this card for an Architect plan handoff. It is a navigable summary of the complete plan, not a replacement for it.

- **Outcome:** what the accepted Feature or Bug work should change.
- **Approach:** recommended technical direction and the reason for any material choice.
- **Evidence and assumptions:** the few current-system findings that materially affect the plan; clearly label assumptions and unknowns.
- **Ordered tasks:** numbered, outcome-oriented slices. For each, show covered AC IDs (Feature), what it delivers, and its `Blocked by` task IDs or `None`.
- **Dependency rationale:** explain why each blocker genuinely gates a task; identify the tasks that can start now.
- **Parallel candidates:** show proposed independent groups and the main shared-resource/isolation caveat. Do not promise actual parallel dispatch before Developer validates the worktree and host.
- **Verification and risk:** key test seams, integration checks, material risks and mitigations.
- **Human action:** specify exactly whether the human is being asked to approve the plan revision, choose an option, or adjust scope.

Ask the human to review four things, without turning routine choices into an approval questionnaire:

1. **Granularity:** can each task be demonstrated or verified on its own; should any be merged or split?
2. **Dependencies:** does each blocker truly gate the task; is a prerequisite missing?
3. **Execution order:** are the ready tasks and proposed parallel groups reasonable, subject to Developer's isolation check?
4. **Approach and scope:** are material trade-offs, risks and boundaries acceptable?

For Standard, present the card and ask only for consequential decisions; routine planning does not add a human gate. For Extended, the human approves the complete, accessible plan revision (for example, `approve plan r1`) or requests changes. End the turn after the Extended handoff. Approval does not grant edit authority or permission for privileged actions.

## Other human-facing cards

- **Feature Spec:** outcome; every changed AC ID with a short meaning and pointer to its complete source-linked revision; non-goals; material risk/decision; exact action requested. If the complete AC revision is inaccessible, report `AC_ACCEPTANCE: NOT VERIFIED`.
- **Bug:** original symptom; reproduction status/evidence; cause confidence; targeted repair and regression; behavior/rights/data risk; decision requested, if any.
- **Spike:** bounded question; main and contrary evidence; compared alternatives and confidence; `PROCEED`, `CLARIFY` or `STOP`; explicit statement that no production implementation was performed.
- **Final code-change handoff:** changed roots and snapshots; AC/symptom-to-test coverage; actual commands/results and `NOT RUN` items; cross-root compatibility/release order; independent Reviewer verdict; residual risks; separate merge/deploy permissions.

A card is a navigable summary, not a substitute for the authoritative requirement, full plan, review or approved artifact.

## Records and continuity

Prefer an existing authorized issue, PR, ticket or ADR. Standard work spanning sessions uses one compact record. Extended uses revisioned artifacts and state as defined in `core/modes.md`. If the required record cannot be persisted, report `HANDOFF: NOT DURABLE` and provide a pasteable handoff; do not claim reliable resume.

Approval applies only to the accessible source/artifact revision and scope explicitly accepted. A Spike `PROCEED` is advisory and never authorizes implementation.
