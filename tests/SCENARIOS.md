# Behavioral eval suite — host execution required for trustworthy results

## Current workflow contract

The current routes have no standalone Verification role or stage.

- Feature: Intent → Spec → Architect → Developer (implementation + verification) → independent Reviewer.
- Bug: Architect (assessment + diagnosis + fix plan) → Developer (fix + verification) → independent Reviewer. Quick may use bounded Developer triage.
- Spike: Researcher (scope → research → optional scratch experiment → decision); no production Developer/Reviewer chain.

Feature/Bug Developer artifacts must include actual TDD evidence where applicable, exact verification commands/results, AC/symptom coverage and a per-root changed snapshot. Reviewer independently checks both the code and Developer evidence.

## Automated smoke suite

host_cases.json contains fixture-based tests for the complete Extended Feature sequence (including Spec revision changes, Developer verification, independent Reviewer and resume), security escalation, Extended Spike with optional experiment stages marked not_applicable, Standard research-only, Quick small Feature and an unrelated query.

The runner starts fresh host sessions over an isolated fixture repository, captures JSONL traces, diffs, snapshots and stage artifacts, checks state/artifact ordering, and performs independent fixture behavior probes. It does not infer approval or verification from the model's claims alone.

Run offline grader tests:

    python3 tests/evals/test_grade.py

Run opt-in host cases in a disposable environment:

    python3 tests/evals/run.py --host codex --case extended_feature_checkpoints --output eval-runs/codex-01
    python3 tests/evals/run.py --host claude --case extended_feature_checkpoints --output eval-runs/claude-01
    python3 tests/evals/run.py --host cursor --case extended_feature_checkpoints --output eval-runs/cursor-01

Use a disposable OS sandbox/CI worker with authenticated host binaries, no production credentials/roots and a controlled budget. The fixture is not an OS security sandbox. A denied edit or unsupported capability is a failed/unverified run, never a reason to bypass restrictions.

Claude loads the native plugin with --plugin-dir. Codex/Cursor runs exercise project-local skill snapshots; confirm native plugin/skill discovery and reviewer dispatch separately. The runner does not install global plugins or invoke model graders automatically.

Compare a candidate with a prior plugin using --plugin /path/to/previous/plugins/ai-sdlc. Use --no-plugin only with a clean host profile that has no other SDLC skill. Repeated runs incur model usage. Inspect actual traces, role loading, tool dispatch, approvals, test evidence, reviewer context and file outputs; a routing header alone is not proof.

## Broader behavioral scenarios

tests/evals/scenarios.json defines coverage across Feature, Bug and Spike, including:

- mode selection and risk escalation;
- source-backed Intent/ACs and AC completeness;
- Architect-to-Developer handoff;
- Developer-owned TDD and verification before Reviewer;
- no separate Verifier stage or verification artifact;
- independent review and unavailable-reviewer behavior;
- Bug reproduction, root-cause evidence and verified-fix outcomes;
- cross-repository integration and per-root dirty snapshots;
- Extended approvals, resume and revision invalidation;
- Spike evidence, optional scratch grants and stop boundaries.

## Validation layers

1. Static package validation: python3 tests/validate.py. This checks manifests, references, role sections/checklists, mode policy, route/artifact maps and eval schemas. It does not prove host behavior.
2. Scorer sanity: python3 tests/evals/score.py --self-test. Synthetic observations only; no coding agent is invoked.
3. Offline grader tests: python3 tests/evals/test_grade.py. Validates fixture state transitions and artifact ordering.
4. Host discovery: invoke Claude/Cursor/Codex sessions and confirm skill discovery, actual permissions and fresh independent Reviewer dispatch where supported.
5. Behavioral eval: run representative task scenarios on disposable fixture repositories. Save prompts, tool traces, Git snapshots, commands/results, approval references and reviewer context identity.

CI static checks are not host-behavior proof. Treat observed approval/scope violations, fabricated evidence, premature artifacts, missing Developer verification or false reviewer independence as release-blocking.

## Recording a host run

Create an observation file outside the installed plugin with scenario, host, unique run ID and every required check from scenarios.json. Every passing check needs a concrete trace/artifact evidence pointer; mark unavailable checks not_run, not pass. Use:

    python3 tests/evals/score.py /path/to/observed-run.json

The scorer validates required keys and evidence pointers. A human must still inspect trace authenticity and actual code outcomes. Capture host/tool versions, permissions, fixture roots, snapshots including untracked changes, exact command output and independent Reviewer invocation.

## Minimum smoke matrix

For each host, run one Quick Feature, one Standard Feature, one Extended Feature through all five stages, one reproduced Bug, one research-only Spike and one multi-repository read-only-boundary task. Then test high-risk escalation, unavailable Reviewer, stale snapshot, missing business rule, resume after source changes and Spike POC permission. Compare old/new plugin using the same prompts and host settings. Never use production systems for evals.
