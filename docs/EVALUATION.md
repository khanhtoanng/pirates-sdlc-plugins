# Evaluation guide

The evaluation suite checks different layers of plugin quality. A pass at one layer does not prove the layers above it.

## Evaluation layers

| Layer | Command/source | What it checks | What it does not prove |
|---|---|---|---|
| Static package validation | `python3 tests/validate.py` | Manifests, links and selected runtime/workflow contracts | Real host discovery or agent behavior |
| Scorer self-test | `python3 tests/evals/score.py --self-test` | Scorer handling of synthetic observations | Any real host run |
| Offline grader tests | `python3 tests/evals/test_grade.py` | State transitions and artifact ordering against fixtures | Model reasoning, host delegation or security isolation |
| Host smoke run | `python3 tests/evals/run.py` | Actual CLI invocation, fixture changes, records and selected state checks | Full GUI behavior or every native installation path |
| Manual host evaluation | Host UI/CLI and recorded evidence | Discovery, permissions, delegation, Reviewer context and host-specific behavior | A universal guarantee for other versions/configurations |

`tests/evals/scenarios.json` is an expected-behavior catalog, not a report of completed runs. The runner captures traces and fixture evidence. The observation scorer checks that a human supplied evidence pointers; it does not independently prove authenticity or agent independence.

## Human-facing artifact quality

The behavioral catalog includes dedicated Spec and Architect output scenarios. Review the actual generated Markdown, not only whether a host emitted the expected headings.

| Artifact | Required human-review checks |
|---|---|
| Spec | One authoritative table contains every full, testable AC; each row identifies its source/basis; VERIFY examples are separate; scope and consequential decisions are concise; technical design and duplicate AC summaries are absent. |
| Architect plan | Summary comes first; every task maps to actual CREATE/UPDATE file paths and specific code responsibilities; test files are mapped; every accepted AC is covered; blockers have genuine reasons; unknown paths are never guessed. |

Judge whether a human can understand what is being accepted and whether Developer can act from the plan without reconstructing the design from prose. A valid Markdown table may still be too vague, verbose or unsupported by repository evidence. Compare before/after host runs using the same fixture and prompts.

## Run offline checks

These do not invoke a coding agent:

```bash
python3 tests/validate.py
python3 tests/evals/score.py --self-test
python3 tests/evals/test_grade.py
```

## Run opt-in host scenarios

Use a disposable fixture environment and authenticated host CLI:

```bash
python3 tests/evals/run.py --host claude --case extended_feature_checkpoints --output eval-runs/claude-01
python3 tests/evals/run.py --host codex --case extended_feature_checkpoints --output eval-runs/codex-01
python3 tests/evals/run.py --host cursor --case extended_feature_checkpoints --output eval-runs/cursor-01
python3 tests/evals/run.py --host copilot --case extended_feature_checkpoints --output eval-runs/copilot-01
```

The runner invokes model-backed sessions and may incur usage costs. Use disposable repositories/accounts with no production credentials or unrelated writable roots. The fixture repository is not an OS security sandbox. Do not bypass denied permissions.

## Understand host coverage

- Claude and Copilot CLI runs load the native plugin directory.
- Cursor and Codex paths in the current runner copy project-local skill snapshots into the fixture. They do not establish the same thing as native plugin installation and discovery.
- VS Code Copilot discovery and workflow behavior require manual GUI checks; the CLI runner does not drive the VS Code UI.
- Discovering a Reviewer agent does not prove it was dispatched. Inspect the actual handoff and returned result.
- A read-only tool list or instruction does not automatically prove a separate worktree or OS-level sandbox.

See [Hosts](HOSTS.md) for installation guidance and the host matrix, and [tests/SCENARIOS.md](../tests/SCENARIOS.md) for scenario details.

## Interpret results

Treat incorrect routing, unauthorized writes, fabricated test evidence, premature stage artifacts, stale approvals, unsafe concurrent writes and false claims of Reviewer independence as serious failures.

Capture host/version, plugin revision, command, permissions, fixture roots, transcript, tool calls, snapshots, changed files, stage artifacts and Reviewer identity/context. Mark unavailable checks as `not_run`, not pass. Compare candidate and previous versions with the same prompts and host settings.

A passing static or offline check is evidence about package consistency, not proof that a host followed the workflow. A host-specific pass applies only to the recorded version, configuration and scenario.
