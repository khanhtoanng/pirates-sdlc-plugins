# Extended mode

Extended runs the complete applicable workflow. Each stage produces one inspectable artifact, completes its role checklist and pauses for approval of that exact revision. The Coordinator starts the next stage only after approval.

## Artifact order

| Task | Order | Artifact |
|---|---|---|
| Feature | Intent → Spec → Architect → Developer → Reviewer | 01-intent.md → 02-spec.md → 03-plan.md → 04-implementation.md → 05-review.md |
| Bug | Architect → Developer → Reviewer | 01-diagnosis-plan.md → 02-implementation.md → 03-review.md |
| Spike | Researcher: Scope → Research → optional Experiment Plan → optional Experiment → Decision | 01-scope.md → 02-research.md → 03-experiment-plan.md → 04-experiment.md → 05-decision.md |

Spike experiment stages are optional. Mark unused stages not_applicable in state with a reason; do not create placeholder files.

## Durable record

Prefer an existing authorized ticket, PR or ADR with revisioned sections. Otherwise, use one approved task directory:

    .sdlc/changes/<task-id>/
      state.json
      01-intent.md
      02-spec.md
      03-plan.md
      04-implementation.md
      05-review.md

Use only the artifacts required by the selected route. state.json tracks the current stage, status, revision, artifact, approval, sources, scope and relevant snapshots.

## Stage review

Present the task, stage and revision; artifact path; outcome and key decisions; evidence and checklist result; scope, exclusions, risks and unverified items; and the exact next human action. The full artifact must be accessible.

## Approval

Follow the approval, revision, resume and invalidation protocol in [core/modes.md](../plugins/ai-sdlc/skills/sdlc-work/references/core/modes.md). End the turn after presenting a stage for approval; do not poll or treat silence as consent. Approval applies only to the current artifact revision and does not expand edit scope. Material upstream changes invalidate affected downstream evidence. Developer owns implementation and verification; Reviewer is a separate independent stage.

Reviewer approval does not authorize merge, production migration or deployment. When durable state cannot be saved, report HANDOFF: NOT DURABLE and provide a pasteable handoff.
