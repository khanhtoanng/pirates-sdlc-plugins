# Behavioral eval suite — host execution REQUIRED for trustworthy results

## Automated smoke suite (v0.7)

`host_cases.json` contains executable fixture-based cases for Extended Feature approval/revision/resume, security escalation, Extended Spike, research-only, small Feature, and an unrelated query. The runner starts fresh isolated fixture repositories and sessions, captures JSONL, diffs, snapshots and stage artifacts, grades actual files/state and independent fixture behavior, and emits report.json. It does not infer approval from the tested model's claims alone.

```bash
python3 tests/evals/test_grade.py
python3 tests/evals/run.py --host codex --case extended_feature_checkpoints --output eval-runs/codex-01
python3 tests/evals/run.py --host claude --runs 3 --output eval-runs/claude-01
python3 tests/evals/run.py --host cursor --runs 3 --output eval-runs/cursor-01
```

Run only in a disposable isolated OS sandbox/CI worker with authenticated host binaries, no production credentials/roots, and a budget. The fixture is not an OS security sandbox. Use normal host permissions; a denied edit or unsupported capability is a failed/unverified run, never a reason to bypass restrictions. Claude loads the native plugin with --plugin-dir; Codex/Cursor exercise project-local skill snapshots, not native plugin/reviewer discovery. Separately confirm real plugin discovery and independence using the broader scenarios below. The runner does not install global plugins or invoke model graders automatically.

Compare candidate vs previous plugin with `--plugin /path/to/previous/plugins/ai-sdlc`; for no-plugin use `--no-plugin` in a clean profile without globally installed SDLC skills. Repeated runs cost real model calls. Compare pass rates and timing in report.json, review traces for genuine skill invocation, stage execution, approvals, test evidence and quality; output headers alone do not prove these. For qualitative criteria use blinded independent rubric review.

Claude Code also supports native plugin evals (v2.1.269+):

```bash
cd plugins/ai-sdlc
claude plugin eval init
claude plugin eval . --no-publish
```

Design graders for correct/incorrect triggers, artifact existence, route, approval boundary and quality. See https://code.claude.com/docs/en/plugin-evals. Its case format differs from the shared JSON runner; do not confuse native execution with offline fixture tests. CI runs the offline tests on every PR; host suites are opt-in before release. Treat any observed approval/scope violation or fabricated evidence as release-blocking even if other scores are high.

## Broader manual host scenarios

`tests/evals/scenarios.json` defines 12 behavioral scenarios across **Feature, Bug, Spike**. Its checks cover routing, source-backed decisions, scope/permissions, regressions, convergence, cross-repo integration, snapshot freshness, reviewer independence, session resumption and POC boundaries.

## Gates

1. **Static:** `python3 tests/validate.py`. Checks ZIP content and contract consistency; no host behavior proven.
2. **Scorer sanity:** `python3 tests/evals/score.py --self-test`. Uses synthetic observations; does NOT invoke coding agents.
3. **Host discovery:** use actual Claude/Cursor/Codex sessions and confirm all three skills are callable, native reviewer is discoverable (where supported), effective plugins/versions match, and access constraints are real.
4. **Behavior:** run a representative scenario in an isolated fixture repo/worktree with controlled expected behavior, and save actual prompts, tool-call trace, Git snapshots, commands/results, decisions and reviewer context identity. Mark expected conditions observed or not observed. Repeat for all hosts before reporting cross-host support.

## Recording a run

Create a JSON file **outside** installed plugin (for example `runs/claude-bug.json`) with:

```json
{
  "scenario": "bug_reproduced",
  "host": "claude",
  "run_id": "real-host-log-20261113-01",
  "observations": {
    "route_bug": {"status": "pass", "evidence": "trace lines 10-13, actual routing decision"},
    "symptom_expected_actual": {"status": "pass", "evidence": "trace lines 18-26, status 500 vs 400"}
  }
}
```

Include **every** required key from `scenarios.json` (the partial JSON above intentionally fails). Each `status` is `pass`/`fail`/`not_run` and each pass must point to a concrete observed trace or artifact. Score with:

```bash
python3 tests/evals/score.py /path/to/observed-run.json
```

This scorer checks the stated observations and their evidence pointers; **a human still must inspect trace authenticity and actual code outcomes**. Do not claim successful host tests from a static pass or a synthetic scorer self-test. Capture host/tool versions, permissions, real root paths, snapshots including untracked changes, actual command output and independent reviewer invocation for audit.

## Minimum real-world smoke sequence

Try one no-config Feature, one reproduced Bug, one research-only Spike and one FE+BE+Flyway+Terraform read-only example on each host. Then test unavailable reviewer, security escalation, stale snapshot, missing business rule and resumed session. Prefer a matrix of `scenario × host × result × run_id` rather than duplicating verbose stage transcripts in project source. Compare old/new package against the same scenario prompts/host settings when measuring improvement. Never change production systems for an eval.
