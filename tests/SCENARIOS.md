# Behavioral eval suite — host execution REQUIRED for trustworthy results

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
