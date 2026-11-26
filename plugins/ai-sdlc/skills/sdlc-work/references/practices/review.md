# Human decisions and review handoffs

This practice defines what the Coordinator presents to a human and when an explicit decision is needed. It does not define the technical code-review procedure; that belongs to `roles/reviewer.md`. Extended stage approvals and resume rules are owned by `core/modes.md`.

## Human decision ownership

| Transition | AI prepares | Human action is needed when |
|---|---|---|
| Feature Intent / Spec | Outcome, the full source-linked AC table, scope and consequential decisions | A consequential WHY/WHO/WHAT/scope decision remains or the owner must accept the exact Spec revision |
| Bug diagnosis | Original symptom, expected/actual evidence, cause confidence and minimum repair | Expected behavior changes or a material safety/data decision is needed |
| Architect / fix plan | Recommended approach; task-to-file/code-change table; AC coverage; genuine blockers; test seams and material risks | Human judges task granularity, target files, code responsibilities, dependencies, scope or a material technical trade-off; Extended always requires approval of the exact plan revision |
| Local implementation | Exact roots, paths and bounded operations | Host/project policy requires an additional grant; planning/research alone never authorizes edits |
| Code review | Independent findings, verification gaps and residual risks | Organization-specific or high-risk final acceptance is required; review does not authorize merge/deploy |
| Spike decision | Evidence, contrary evidence, options, confidence and PROCEED/CLARIFY/STOP | Owner decides whether to create a separate Feature/Bug task |

Do not re-approve unchanged accepted sources or claim unobserved consent. AI workers do not ask the owner directly or grant themselves authority; the Coordinator raises one material question at a time.

## Spec review card

The Spec artifact's **Acceptance criteria** table is the authoritative list. The handoff card must navigate that table rather than create a second summary containing duplicate AC prose.

- **Outcome:** one or two sentences describing the user-visible result.
- **Acceptance criteria:** show the complete AC table or a compact view preserving every AC ID, full behavior and source/basis label.
- **Verification examples:** keep examples visibly separate from requirements and link each to its AC.
- **Scope:** concise in-scope and out-of-scope behavior.
- **Decisions:** consequential unresolved WHAT only; identify the exact owner action.
- **Human action:** accept the complete Spec revision or request a specific change.

If the complete source-linked AC revision is inaccessible, report `AC_ACCEPTANCE: NOT VERIFIED`. Do not imply approval of partial content. Extended approval applies to the exact full Spec revision.

## Architect plan review card

Use this card for an Architect plan handoff. It is a navigable summary of the complete plan, not a replacement for it. Keep the full plan's implementation table accessible.

- **Outcome and approach:** what accepted behavior will change and the recommended technical direction.
- **Implementation tasks:** show task ID, outcome/action, actual file operation and path, specific code responsibility, covered AC IDs and blockers. Repeat task IDs for additional file rows; do not collapse several file changes into a vague task description.
- **Unknown targets:** identify any `UNKNOWN` file path and the evidence needed to locate it. Never present guessed paths as verified.
- **Dependencies and ready work:** explain why each blocker genuinely gates a task and which tasks can start now.
- **Parallel candidates:** show proposed independent groups and the main shared-resource/isolation caveat. Do not promise actual parallel dispatch before Developer validates the worktree and host.
- **Verification and risk:** key AC/test-seam mapping, integration checks and material mitigations.
- **Human action:** specify exactly whether the human is being asked to approve the plan revision, choose an option or adjust scope.

Ask the human to review four things without turning routine choices into an approval questionnaire:

1. **Task and file mapping:** does each task deliver a reviewable outcome, and are the target files and proposed code responsibilities plausible?
2. **Dependencies:** does each blocker truly gate the task; is a prerequisite missing?
3. **Execution order:** are the ready tasks and proposed parallel groups reasonable, subject to Developer's isolation check?
4. **Approach and scope:** are material trade-offs, risks and boundaries acceptable?

For Standard, present the card and ask only for consequential decisions; routine planning does not add a human gate. For Extended, the human approves the complete, accessible plan revision (for example, `approve plan r1`) or requests changes. End the turn after the Extended handoff. Approval does not grant edit authority or permission for privileged actions.

## Other human-facing cards

- **Bug:** original symptom; expected/actual contract; reproduction status/evidence; observed cause versus hypothesis and confidence; repair task/file table; regression seam; behavior/rights/data risk; decision requested, if any.
- **Spike:** bounded question; main and contrary evidence; compared alternatives and confidence; `PROCEED`, `CLARIFY` or `STOP`; explicit statement that no production implementation was performed.
- **Final code-change handoff:** changed roots and snapshots; AC/symptom-to-test coverage; actual commands/results and `NOT RUN` items; cross-root compatibility/release order; independent Reviewer verdict; residual risks; separate merge/deploy permissions.

A card is a navigable summary, not a substitute for the authoritative requirement, full plan, review or approved artifact.

## Records and continuity

Prefer an existing authorized issue, PR, ticket or ADR. Standard work spanning sessions uses one compact record. Extended uses revisioned artifacts and state as defined in `core/modes.md`. If the required record cannot be persisted, report `HANDOFF: NOT DURABLE` and provide a pasteable handoff; do not claim reliable resume.

Approval applies only to the accessible source/artifact revision and scope explicitly accepted. A Spike `PROCEED` is advisory and never authorizes implementation.
