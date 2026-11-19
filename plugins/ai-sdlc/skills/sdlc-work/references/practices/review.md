# Human review and handoff — narrow, source-backed, snapshot-aware

## Human decision ownership (Quick/Standard)

Extended additionally requires mandatory stage-by-stage review and approval as specified in core/human-gates.md; the decision-based policy below cannot bypass those gates.

| Transition | What AI prepares | When human action is necessary |
|---|---|---|
| Feature Intent / Spec | Outcome, full source-linked testable changed AC set + complete ID map | Consequential changed WHAT/scope, approval binds complete accessible revision |
| Bug diagnosis | Expected/actual, reproduction evidence, cause hypothesis, minimum fix | Consequential new expected behavior or safety decision; normal agreed regression needs no extra AC ceremony |
| Architect / fix plan | Minimal slices, tests, compatibility, risk and rollout | Only material trade-offs (security, irreversible data, breaking change, production) |
| Local implementation | Exact change roots/files/operations | An **explicit bounded implement/fix request** can grant ordinary local edits, unless project/host policy demands more; evaluation/spike/plan requests do not grant edits |
| Code review | Fresh independent reviewer findings and verification omissions | High-risk/org-specific final acceptance; still separate from merge/deploy |
| Spike decision | Question, observed and contrary evidence, options, verdict | Owner decides whether to open a new Feature/Bug, never automatic continuation |

Do not re-approve unchanged accepted sources; do not claim unobserved consent. No AI worker asks the owner directly or grants itself authority; the Coordinator handles material questions one at a time.

## Minimal human-facing cards

**Feature:** Outcome; all changed AC IDs with short meaning and pointers to exact full AC revision/sources; non-goals; material risks/decision; requested action. Human summary must map to *every* changed AC, not a hidden subset. If full revision inaccessible, `AC_ACCEPTANCE: NOT VERIFIED`.

**Bug:** Original symptom; observed reproduction; root-cause evidence/confidence; proposed targeted fix and regression; any altered behavior/rights/data risk; requested decision if necessary. Do not require speculative negative-case AC inventory.

**Spike:** Research question; evidence-backed main finding, contrary evidence and confidence; compared alternatives; `PROCEED/CLARIFY/STOP`; explicit no implementation. Human may approve a *new* implementation task separately.

**Final code-change handoff:** Changed root and snapshot list; AC/symptom→test coverage; actual commands/results + `NOT RUN`; cross-root compatibility/rollout order; independent reviewer context/verdict, residual risks and separate merge/deploy permissions. A review card is a navigable summary, never the sole source of normative decisions.

## Durable continuation without document sprawl

Use existing issue/PR/ticket/ADR when possible. Standard work spanning sessions uses one compact record. Extended uses separate inspectable stage outputs and versioned state as defined in core/human-gates.md. If record cannot be persisted, mark `HANDOFF: NOT DURABLE`, provide a pasteable summary and do not claim reliable resumption. On resume, inspect current sources, permissions and Git state.

## End-state semantics

- `ROLE READY`: proposed stage output, not owner acceptance.
- `SPEC ACCEPTED`: exact full Feature AC revision has valid authority.
- `EDIT AUTHORIZED`: bounded ordinary local file grant; separately restrict privileged/external operations.
- `VERIFY COMPLETE`: mandatory outcomes and checks observed for actual snapshot, not just planned.
- `AI_PASS`: fresh independent reviewer verified the actual snapshot; not a human approval, merge, deployment or production authorization.
- `HUMAN ACCEPTED`: actual authorized owner approved specific reviewed scope/snapshot when required.
- `SPIKE PROCEED`: evidence-backed recommendation only, not implementation approval.
