# Task records

This is a human-facing guide to where SDLC work is recorded. The agent runtime contract and Extended state schema live in [core/modes.md](../plugins/ai-sdlc/skills/sdlc-work/references/core/modes.md); this page does not define a second schema.

## Choose one authoritative record

Prefer an existing authorized issue, PR, ticket or ADR with revisioned sections. Otherwise, after receiving permission, use one task directory in one writable root:

```text
.sdlc/changes/<task-id>/
  state.json
  01-intent.md
  02-spec.md
  03-plan.md
  04-implementation.md
  05-review.md
```

Create only the artifacts required by the selected task route. Bug uses diagnosis-plan, implementation and review artifacts; Spike uses scope, research, optional experiment-plan/experiment and decision artifacts. Do not create placeholders for skipped or not-applicable stages.

## What the record connects

The state record identifies the current task, route, stage, artifact revision, approvals, accepted decisions, source references, repository roots, edit scope and relevant snapshots. Each code-change artifact should point to the exact source/AC revision and per-root worktree snapshot it represents.

Do not maintain competing copies of the same accepted requirement or approval. Summaries point to the authoritative full artifact; they do not replace it.

## If durable storage is unavailable

Do not claim reliable resume. Report `HANDOFF: NOT DURABLE` and provide a pasteable handoff with the current stage/revision, accepted decisions, evidence, scope, snapshots, blockers and next human action.
