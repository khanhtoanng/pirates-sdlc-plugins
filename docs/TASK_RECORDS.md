# Task records

This guide explains where durable work is saved and how to understand the files. The normative approval protocol and machine-readable state contract live in the installed Coordinator instructions: `plugins/ai-sdlc/skills/sdlc-work/references/core/modes.md`.

## Canonical location

**Every durable plugin-generated task record must live under `.sdlc/changes/<task-id>/` in one selected task-home root.**

An existing Jira issue, GitHub issue, PR or ADR can remain the source request and hold links to the work. It does not replace the local task record, store a second copy of plugin state, or change the required artifact location.

Do not put task state or stage artifacts in the plugin installation, a temporary directory, a host-specific agent folder, or a different per-role/per-repository location.

## Choose the task home

For a single repository, use that repository's root.

For a multi-repository workspace, use one selected workspace-level root when it is writable and authorized. Otherwise use one explicitly selected primary repository as the task home. Store references and per-root snapshots for every participating repository in that single record. Do not create duplicate task directories in FE, BE, migration or infrastructure repositories.

The Coordinator must verify that the host can read and write the selected task home and that creating the record is authorized. A host's directory access is not approval to edit source files. If no authorized task home is available, do not silently fall back to an external tracker or another directory.

## Persistence by mode

| Mode | Durable record |
|---|---|
| Quick | None by default. Return a concise chat result. If the user explicitly requests a durable record, use the canonical location. |
| Standard | One compact `task.md` when continuity is needed, such as multi-repository coordination, cross-session resume or an explicit user request. |
| Extended | Required: one `state.json` plus the applicable ordered stage artifacts. Do not proceed through an approval checkpoint without durable state. |

## Directory layout

Feature Extended:

```text
.sdlc/
  changes/
    customer-status/
      state.json
      01-intent.md
      02-spec.md
      03-plan.md
      04-implementation.md
      05-review.md
```

Bug uses `01-diagnosis-plan.md`, `02-implementation.md` and `03-review.md`.

Spike uses `01-scope.md`, `02-research.md`, optional `03-experiment-plan.md` and `04-experiment.md`, then `05-decision.md`. Unused optional stages are recorded as `not_applicable` in `state.json`; do not create placeholder files.

Standard uses one compact `task.md`, not a reduced copy of the Extended state machine.

## Task ID and creation rules

Use a short, descriptive, filesystem-safe task ID: lowercase letters and numbers separated by hyphens (for example, `customer-status` or `fix-login-timeout`). Check whether the directory exists before creating it. If the name is already in use by another task, append a short unique suffix; never overwrite or silently reuse another task's record.

The Coordinator creates the task directory once and passes its canonical path to every role. Roles must not independently choose another output directory. Keep artifact links relative to that task directory where practical.

Do not automatically add `.sdlc/` to `.gitignore`, stage it, commit it or publish it. The project owner controls repository tracking and retention under existing project policy. Do not write credentials, access tokens or other secrets into task records.

## What each file is for

| File | What it contains | Primary reader |
|---|---|---|
| `state.json` | Task type/mode, current stage, statuses, revisions, approvals, source references, repository roots, scope and snapshots | Coordinator/tooling |
| `01-intent.md` | Problem, target user, outcome, scope and non-goals | Human |
| `02-spec.md` | Observable behavior, accepted ACs, sources and exclusions | Human |
| `03-plan.md` | Recommended approach, alternatives, delivery slices, dependencies, risks and test seams | Human |
| `04-implementation.md` | Changed roots/files, AC coverage, TDD and verification commands/results, snapshots and unverified checks | Human |
| `05-review.md` | Independent findings, severity, evidence, verdict and remaining risks | Human |
| `task.md` | Compact Standard handoff: request, decisions, scope, status, evidence and next action | Human |

Bug and Spike artifacts contain the equivalent information for their own routes. Create only files required by the selected workflow.

Human-facing artifacts explain decisions and evidence; they do not reproduce internal agent instructions or raw tool traces. Link to supporting source rather than copying competing versions of an accepted requirement.

## State, approval and resume

`state.json` is the machine-readable record for Extended. It tracks task type, requested/effective mode, stage map, current status, artifact revisions, approvals, source references, repository roots, edit scope and relevant snapshots.

Approval is tied to one exact stage and revision. A request for changes revises that artifact and increments its revision. A material upstream change invalidates affected downstream approvals and evidence. Resume reloads the record, checks its revision and approval, and revalidates permissions, source and Git snapshots.

The full schema and transition rules are in [core/modes.md](../plugins/ai-sdlc/skills/sdlc-work/references/core/modes.md). This guide explains the user-visible meaning and does not define a second schema.

```text
sdlc-work resume customer-status
sdlc-work resume .sdlc/changes/customer-status
```

The Coordinator resolves the task home and reloads its state and current artifact. Chat history is not a durable record.

## Multi-repository example

```text
workspace/
  .sdlc/
    changes/
      customer-status/
        state.json
        01-intent.md
        02-spec.md
        03-plan.md
        04-implementation.md
        05-review.md
  frontend/
  backend/
  flyway/
  terraform/
```

This is one task record. State identifies each repository, edit scope, branch/HEAD, dirty changes and evidence. Terraform can be examined-only/read-only without implying permission to change it.

## If durable storage is unavailable

Extended must stop at the persistence boundary and report `HANDOFF: NOT DURABLE`. Provide a pasteable handoff with stage/revision, accepted decisions, evidence, scope, snapshots, blockers and next action. Do not claim reliable resume.

For tasks created before this policy, see [Migration](MIGRATION.md). Existing records are not moved or rewritten automatically.
