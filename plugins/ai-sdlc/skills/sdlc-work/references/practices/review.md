# Human decisions and review handoffs

This practice defines what the Coordinator presents to a human and when an explicit decision is needed. It does not define the technical code-review procedure; that belongs to `roles/reviewer.md`. Extended stage approvals and resume rules are owned by `core/modes.md`.

## Human decision ownership

| Transition | AI prepares | Human action is needed when |
|---|---|---|
| Feature Intent / Spec | Outcome, source-linked changed ACs, complete AC ID map and non-goals | A consequential WHY/WHO/WHAT/scope decision remains or the owner must accept the exact Spec revision |
| Bug diagnosis | Original symptom, expected/actual evidence, cause confidence and minimum repair | Expected behavior changes or a material safety/data decision is needed |
| Architect / fix plan | Minimal slices, dependencies, tests, compatibility and relevant risks | A material trade-off affects security, irreversible data, breaking contracts or production rollout |
| Local implementation | Exact roots, paths and bounded operations | Host/project policy requires an additional grant; planning/research alone never authorizes edits |
| Code review | Independent findings, verification gaps and residual risks | Organization-specific or high-risk final acceptance is required; review does not authorize merge/deploy |
| Spike decision | Evidence, contrary evidence, options, confidence and PROCEED/CLARIFY/STOP | Owner decides whether to create a separate Feature/Bug task |

Do not re-approve unchanged accepted sources or claim unobserved consent. AI workers do not ask the owner directly or grant themselves authority; the Coordinator raises one material question at a time.

## Human-facing cards

- **Feature:** outcome; every changed AC ID with a short meaning and pointer to its complete source-linked revision; non-goals; material risk/decision; exact action requested. If the complete AC revision is inaccessible, report `AC_ACCEPTANCE: NOT VERIFIED`.
- **Bug:** original symptom; reproduction status/evidence; cause confidence; targeted repair and regression; behavior/rights/data risk; decision requested, if any.
- **Spike:** bounded question; main and contrary evidence; compared alternatives and confidence; `PROCEED`, `CLARIFY` or `STOP`; explicit statement that no production implementation was performed.
- **Final code-change handoff:** changed roots and snapshots; AC/symptom-to-test coverage; actual commands/results and `NOT RUN` items; cross-root compatibility/release order; independent Reviewer verdict; residual risks; separate merge/deploy permissions.

A card is a navigable summary, not a substitute for the authoritative requirement, full review or approved artifact.

## Records and continuity

Prefer an existing authorized issue, PR, ticket or ADR. Standard work spanning sessions uses one compact record. Extended uses revisioned artifacts and state as defined in `core/modes.md`. If the required record cannot be persisted, report `HANDOFF: NOT DURABLE` and provide a pasteable handoff; do not claim reliable resume.

Approval applies only to the accessible source/artifact revision and scope explicitly accepted. A Spike `PROCEED` is advisory and never authorizes implementation.
