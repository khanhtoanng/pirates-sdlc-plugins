# Extended mode

Extended runs the complete applicable workflow. Each stage produces one inspectable artifact, completes its role checklist and pauses for approval of that exact revision. The Coordinator starts the next stage only after approval.

## Artifact order

| Task | Order | Artifact |
|---|---|---|
| Feature | Intent → Spec → Architect → Developer → Reviewer | 01-intent.md → 02-spec.md → 03-plan.md → 04-implementation.md → 05-review.md |
| Bug | Architect → Developer → Reviewer | 01-diagnosis-plan.md → 02-implementation.md → 03-review.md |
| Spike | Researcher: Scope → Research → optional Experiment Plan → optional Experiment → Decision | 01-scope.md → 02-research.md → 03-experiment-plan.md → 04-experiment.md → 05-decision.md |

Spike experiment stages are optional. Unused optional stages are marked `not_applicable` in state with a reason; no placeholder files are created.

## Review and approval

Present the task, stage and revision; artifact path; outcome and key decisions; evidence and checklist result; scope, exclusions, risks and unverified items; and the exact next human action. The full artifact must be accessible.

For an Architect plan or Bug diagnosis/plan, the review card also summarizes the recommended approach, numbered outcome-oriented tasks, AC coverage where applicable, genuine blockers and their reasons, ready tasks, proposed parallel groups, verification seams and material risks. Ask the human to check task granularity, blocking edges, execution order and consequential approach/scope decisions. The complete task contracts remain in the artifact.

Approval applies only to the current artifact revision and does not expand edit scope. Material upstream changes invalidate affected downstream approvals/evidence. End the turn after presenting a stage; do not poll or treat silence as consent.

Architect owns the logical delivery plan. Developer validates the approved plan against the fresh baseline and host/worktree isolation, then owns actual dispatch, implementation and verification. A material plan change returns through Architect and the Coordinator; the revised plan must be approved before the Extended workflow continues.

Reviewer is a separate independent stage. Reviewer approval does not authorize merge, production migration or deployment.

For the authoritative state schema, approval/resume protocol and invalidation rules, see [core/modes.md](../plugins/ai-sdlc/skills/sdlc-work/references/core/modes.md). For the human-facing record location and file layout, see [task records](TASK_RECORDS.md).
