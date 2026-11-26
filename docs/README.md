# Documentation

This directory explains AI SDLC to people. It is not loaded as agent instructions; normative runtime instructions live under `plugins/ai-sdlc/skills/`.

## Start here

1. [User guide](USER_GUIDE.md) — task types, modes, roles, handoffs and human approval.
2. [Hosts](HOSTS.md) — install Claude Code, Cursor, Codex or GitHub Copilot and understand host capabilities.
3. [Task records](TASK_RECORDS.md) — where artifacts are saved, what each file means, and how approval/resume works.
4. [Evaluation](EVALUATION.md) — what static checks, offline checks and actual host runs do and do not prove.

## Examples

- [Spec review](EXAMPLE_SPEC_REVIEW.md) — concise AC table, source/basis labels and VERIFY examples.
- [Architect plan](EXAMPLE_PLAN.md) — actionable task-to-file/code-change table, dependencies and verification.
- [Multi-repository work](EXAMPLE_MULTI_REPO.md) — one Feature coordinated across FE, BE, migrations and read-only infrastructure.

## Maintainers

- [Architecture](ARCHITECTURE.md) — runtime ownership, roles, evidence and repository boundaries.
- [Changelog](CHANGELOG.md) — release history.
- [Migration](MIGRATION.md) — plugin upgrades and older task records.
- [Sources](SOURCES.md) — platform specifications and workflow research.

[TASK_ROUTES.md](TASK_ROUTES.md), [EXTENDED.md](EXTENDED.md) and [LOCAL_SETUP.md](LOCAL_SETUP.md) remain as compatibility links to the consolidated guides.
