# Workspace and multi-repository coordination

## Discovery

A workspace can be one Git repo, a monorepo, or several independent repos. Detect repository boundaries via actual local Git root/worktree metadata, not folder names, glob matches or assumed hierarchy. Capture each relevant root's real path, role/technology (observed or UNKNOWN), applicable instructions, branch/HEAD, staged/unstaged patch identity, relevant untracked paths/content, access, available tests and CI. Confirm project instructions are actually applied; adding a directory to a host does not prove its instructions were loaded.

Define separate sets:
- VISIBLE: actual directories available/readable in the host;
- RELEVANT: roots needed to understand the outcome (read-only access may suffice);
- EDIT_APPROVED: roots and paths with explicit authorized changes;
- EXCLUDED: roots not to touch, including unrelated repositories.

For a read-only Spike without code roots, repository discovery is optional. If a required root is inaccessible, report missing evidence and ask to expose it or narrow scope. Do not assume global Git transactions.

## One task home across repositories

A multi-repository task has one task record, not one copy in every repository. Select one authorized task-home root: prefer the selected workspace-level root when writable; otherwise use one explicitly selected primary repository. Store plugin-generated durable state and artifacts under that root's `.sdlc/changes/<task-id>/` directory.

Record all participating repository roots, source revisions, edit scopes and per-root snapshots in that one task record. The task-home root is not automatically an edit-approved source root. Creating/updating the task record requires write authorization for that location; source-edit permission remains separate. If there is no authorized task home, stop durable workflow progression rather than choosing a second location or copying records into each repository.

External tickets, issues, PRs and ADRs are source references. They may be linked from the local record but do not replace it or hold a competing copy of plugin state and stage artifacts.

## Impact and dependency analysis

For each accepted Feature outcome, map AC to affected roots/contracts to integration evidence. Trace actual callers, data ownership and dependencies. A common FE/BE/DB/infra workspace may involve:
- FE: views, validation, HTTP clients and generated API clients.
- BE: endpoints, business rules, DTOs and storage mappings.
- DB/migrations: schema evolution, backfill, compatibility and rollback.
- Infrastructure: resources, IAM/network, state and plan/apply risks.

Only use labels supported by inspection. Relevance is not edit authorization; a change may require FE+BE+DB but not infrastructure.

Keep one authoritative AC set. Record root and source revision plus working-tree patch/untracked identity for each implementation slice; HEAD alone is insufficient for dirty worktrees. Build the actual dependency graph. A database expand → compatible BE → FE rollout is one possible sequence, not a universal rule. Flag incompatible API/schema/infra assumptions and inter-release skew.

Design backward-compatible expand/contract where relevant. For Flyway, prefer new migrations rather than modifying applied versioned migrations after checking actual environment. A Terraform plan is evidence, never permission to apply. Destructive operations require separate authority.

## Verification and release coordination

Check each affected repository's relevant tests/lint/static analysis on its actual snapshot. Where relevant, check interface contracts, migration-to-BE compatibility, FE-to-BE behavior, infrastructure inputs/outputs and deployment sequence. Record unavailable checks as NOT RUN.

Reviewer must assess each changed root and important cross-root edge; incomplete critical integration evidence blocks whole-task AI_PASS. End with one human summary: affected versus examined-only roots, snapshot/branch per changed repo, AC to repo to test mapping, compatibility/release order, residual risk and separate PR/merge/deploy actions. Do not claim atomic commits or rollouts.

## Parallel work boundary

This file owns root discovery, impact and dependency analysis. Worker dispatch, worktree isolation, write-conflict checks and whether slices run concurrently or sequentially are defined only in delegation.md. Do not independently delegate writes based on repository boundaries alone.

## Optional workspace profile

The plugin does not require generated config. For recurring multi-repo sessions, sdlc-setup may propose one user-owned .ai-sdlc/workspace.yaml with schemaVersion: 1, repository aliases/paths and verified relationships. Treat it as an index and preference, not authority for files, permissions, requirements or deployment. This optional workspace profile is distinct from task records under .sdlc/changes/. Never auto-commit duplicates across repos or override host trust boundaries.

## Snapshot freshness

Treat each repository as separately versioned; HEAD alone is not enough to identify a dirty worktree. A change in an excluded root cannot be silently added to the approved task. Apply the Coordinator's snapshot and invalidation rules in core/runtime.md and the Developer/Reviewer handoff rules; do not reuse evidence from a stale root snapshot.
