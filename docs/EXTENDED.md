# Extended mode — ordered human approval at every applicable stage

Extended is the full human-in-the-loop mode. Each applicable role stage produces one inspectable artifact, completes its owning role's checklist, presents a review card and stops for approval of that exact revision. The Coordinator does not start the next stage until approval is explicit. The protocol is defined in core/modes.md; there is no separate human-gates.md.

## Ordered workflows

### Feature

| Order | Role | Artifact | Human checkpoint |
|---|---|---|---|
| 1 | Intent | 01-intent.md | Approve Intent revision |
| 2 | Spec | 02-spec.md | Approve complete Spec/AC revision |
| 3 | Architect | 03-plan.md | Approve technical plan revision |
| 4 | Developer (implementation + verification) | 04-implementation.md | Approve code and verification evidence |
| 5 | Independent Reviewer | 05-review.md | Approve review disposition / acknowledge next human action |

### Bug

| Order | Role | Artifact | Human checkpoint |
|---|---|---|---|
| 1 | Architect (assessment + diagnosis + fix plan) | 01-diagnosis-plan.md | Approve diagnosis and bounded repair plan |
| 2 | Developer (fix + verification) | 02-implementation.md | Approve fix and verification evidence |
| 3 | Independent Reviewer | 03-review.md | Approve review disposition / acknowledge next action |

Bug does not get fictional Feature Intent or Spec stages. A new business rule requires a separate Feature decision.

### Spike

| Order | Role | Artifact | Human checkpoint |
|---|---|---|---|
| 1 | Researcher — Scope | 01-scope.md | Approve bounded question and constraints |
| 2 | Researcher — Research | 02-research.md | Approve evidence and experiment decision |
| 3 | Researcher — Experiment Plan (optional) | 03-experiment-plan.md | Approve scratch-only plan and separate grant |
| 4 | Researcher — Experiment (optional) | 04-experiment.md | Review observed experiment results |
| 5 | Researcher — Decision | 05-decision.md | Review PROCEED, CLARIFY or STOP |

If no experiment is needed or authorized, mark both optional stages not_applicable with a reason in state. Do not create placeholder files. A Spike never authorizes production implementation.

## Artifact directory

Prefer an existing authorized ticket/PR/ADR with revisioned sections. Otherwise use one approved writable task directory. Feature example:

    .sdlc/changes/<task-id>/
      state.json
      01-intent.md
      02-spec.md
      03-plan.md
      04-implementation.md
      05-review.md

Bug and Spike use their own ordered artifacts. state.json tracks stage, status, revision, artifact path, approval history, sources, scope and relevant snapshots. Only create an artifact when its stage runs.

## Review card

Every stage review card shows task/type/mode, stage ID and revision, actual artifact path, outcome, important decisions, checklist validation, sources/AC IDs or Bug evidence, scope, exclusions, risks, unverified items and the exact next human action.

## Approval protocol

1. Execute only the current stage and load its owning role instructions.
2. Complete the role's mandatory checklist. Missing required evidence means BLOCKED or NEEDS_DECISION.
3. Create/update only the current artifact and increment its revision when revised.
4. Persist state.json with status awaiting_human_approval before returning control.
5. Present the review card and end the turn. Do not poll, sleep, invoke the next role or infer approval from silence.
6. On the next turn, reload the state and exact artifact revision. Recheck current source, scope, permissions and snapshot freshness.
7. Accept explicit approval of the current stage/revision only, for example approve spec r1. A generic continue does not approve an unseen future artifact.
8. On request for changes, revise the same stage, increment revision, rerun the checklist and request approval again. Rejection cancels the task. Ambiguity requires clarification.
9. After approval, execute only the next applicable stage.
10. Material source, requirement, plan, scope or code changes invalidate affected downstream approvals/evidence. Return to the earliest affected stage; do not reapprove unchanged unaffected artifacts.
11. Developer owns implementation and verification in one stage. A Developer verification failure blocks that stage. A Reviewer finding requires Developer repair and re-verification followed by fresh independent review.
12. Escalate after at most three AI repair/review cycles.

Approval never grants additional edit scope or privileged operations. Final Reviewer approval does not authorize merge, production migration or deployment. If durable persistence is unavailable, report HANDOFF: NOT DURABLE and provide a pasteable handoff; do not claim reliable cross-session resume.