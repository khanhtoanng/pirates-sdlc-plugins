# AI SDLC — local-first plugin for Claude Code, Cursor and Codex

**Version 0.7.0.** One installed plugin contains the SDLC coordinator, optional setup, and doctor. It does **not** generate a second repository harness, copy role instructions to every repo, install hooks/MCPs, or deploy anything by default.

## Choose a task type, then an execution mode

| Task | Flow | Final result |
|---|---|---|
| **Feature** | Intent/Spec where needed → Architect/test plan → authorized Build → Verify & Converge → independent Review | AC-linked implementation evidence and release readiness |
| **Bug** | Symptom → Reproduce/diagnose → minimal fix plan → authorized Fix → verify original symptom + regressions → independent Review | `VERIFIED_FIX`, `PARTIAL` or `UNVERIFIED` |
| **Spike** | Bounded question → research both sides → optional authorized disposable POC → decision → STOP | `PROCEED`, `CLARIFY` or `STOP`; no automatic code implementation |

**Mode** is independent: `auto` (default), `quick`, `standard`, `extended`. Severity and material risk decide mode, not number of repos. Legacy `sdlc-work spike <question>` remains accepted as type `spike`, mode `auto`.

| Mode | Human review | Record |
|---|---|---|
| Quick | Material ambiguity and permissions only | Compact summary |
| Standard | Consequential decisions | Existing ticket or compact record |
| Extended | **Explicit approval of every applicable stage** | Stage artifacts + resumable state |

Explicit Extended always wins; high risk escalates Quick/Standard. See [Extended guide](docs/EXTENDED.md).

The five logical responsibilities remain **Intent, Spec, Architect, Developer, Reviewer**, but the selected route invokes only those needed. `sdlc-work` is a progressively loaded skill, not a mandatory five-agent orchestration. Review on code-changing Feature/Bug requires an actually fresh independent host context to claim `AI_PASS`.

## Invoke locally

- **Claude Code:** `/ai-sdlc:sdlc-work feature standard Add customer status in FE+BE+Flyway; inspect Terraform read-only.`
- **Cursor:** `Use sdlc-work for a bug in quick mode: reproduce the 500 response, fix it, and verify the regression.`
- **Codex:** `Use sdlc-work spike standard to compare two approaches for offline sync. Research only; do not implement.`
- `sdlc-setup`: optional read-only inspection, then exact approved configuration *only if needed*.
- `sdlc-doctor`: check plugin discovery, root access, conflicts and reviewer capability.

See [Local Setup](docs/LOCAL_SETUP.md) for host installation, [Architecture](docs/ARCHITECTURE.md) for gates, [Task Routes](docs/TASK_ROUTES.md) for examples, [Multi-Repo](docs/EXAMPLE_MULTI_REPO.md), [Spec Review](docs/EXAMPLE_SPEC_REVIEW.md), and [Migration](docs/MIGRATION.md).

## Scope and evidence, not document sprawl

Use one accepted AC revision for Features, one original-symptom/regression record for Bugs, or one bounded question/decision brief for Spikes. Quick/Standard avoid mandatory stage files; Extended uses distinct, revisioned stage artifacts in an authorized tracker or one task directory, not a second harness.

An explicit bounded **implement/fix** request may authorize ordinary local edits in its own scope, subject to host/project permission; a **plan/research/spike** request does not. Separately authorize destructive operations, secrets, remote services, installs, commit/push/merge, Terraform apply, production migrations and deployment. Multi-root visibility never grants edit scope.

## Test the plugin

`python3 tests/validate.py`, `python3 tests/evals/score.py --self-test` and `python3 tests/evals/test_grade.py` run offline validation. These checks **do not prove host behavior**. Run real opt-in host scenarios with `python3 tests/evals/run.py --host claude --case extended_feature_checkpoints --output eval-runs/claude-01`. See [evaluation guide](tests/SCENARIOS.md) for Claude native evals, Codex/Cursor runners, limitations and baselines. Sources: [docs/SOURCES.md](docs/SOURCES.md).
