# Behavioral eval suite — host execution required for trustworthy results

## Current workflow contract

The current routes have no standalone Verification role or stage.

- Feature: Intent → Spec → Architect → Developer (implementation + verification) → independent Reviewer.
- Bug: Architect (assessment, diagnosis and fix plan) → Developer (fix + verification) → independent Reviewer. Quick may use bounded Developer triage.
- Spike: Researcher (scope → research → optional scratch experiment → decision); no production Developer/Reviewer chain.

Developer owns TDD and integrated verification. practices/tdd.md is the single source for RED/GREEN/REFACTOR, exceptions and evidence. practices/delegation.md is the single source for worker dispatch, safe parallel AC slices and independent Reviewer isolation. Coverage classification, human decision cards and multi-root discovery are owned by their respective practice files.

## Automated smoke suite

host_cases.json contains fixture-based tests for the complete Extended Feature sequence (including Spec revision changes, Developer verification, independent Reviewer and resume), security escalation, Extended Spike with optional experiment stages marked not_applicable, Standard research-only, Quick small Feature and an unrelated query.

The runner starts fresh host sessions over an isolated fixture repository, captures JSONL traces, diffs, snapshots and stage artifacts, checks state/artifact ordering, and performs independent fixture behavior probes. It does not infer approval or verification from the model's claims alone.

Run offline grader tests:

    python3 tests/evals/test_grade.py

Run opt-in host cases in a disposable environment:

    python3 tests/evals/run.py --host codex --case extended_feature_checkpoints --output eval-runs/codex-01
    python3 tests/evals/run.py --host claude --case extended_feature_checkpoints --output eval-runs/claude-01
    python3 tests/evals/run.py --host cursor --case extended_feature_checkpoints --output eval-runs/cursor-01
    python3 tests/evals/run.py --host copilot --case extended_feature_checkpoints --output eval-runs/copilot-01

Use a disposable OS sandbox/CI worker with authenticated host binaries, no production credentials/roots and a controlled budget. The fixture is not an OS security sandbox. A denied edit or unsupported capability is a failed/unverified run, never a reason to bypass restrictions.

Claude and Copilot CLI load the native plugin with --plugin-dir. Copilot CLI runs use `--output-format=json`, a scoped tool allow-list and `COPILOT_PLUGIN_DIR_ONLY=true`; the runner captures JSONL events. Codex/Cursor runs exercise project-local skill snapshots; confirm native plugin/skill discovery and Reviewer dispatch separately. VS Code Copilot plugin discovery and agent dispatch remain a manual host check. The runner does not install global plugins or invoke model graders automatically.

Compare a candidate with a prior plugin using --plugin /path/to/previous/plugins/ai-sdlc. Use --no-plugin only with a clean host profile that has no other SDLC skill. Repeated runs incur model usage. Inspect actual traces, role loading, tool dispatch, approvals, worker isolation, test evidence, Reviewer context and file outputs; a routing header alone is not proof.

## Broader behavioral scenarios

tests/evals/scenarios.json defines expected behaviors across Feature, Bug and Spike, including:

- mode selection, risk escalation and source-backed Intent/ACs;
- AC completeness and traceability from accepted behavior to implementation and tests;
- Architect alternatives, decision rationale, operational risks, impact tracing and dependency/parallel-slice analysis;
- Architect/Developer smallest-complete-change selection, existing-code reuse, preservation of safeguards and proportionate tests;
- Developer TDD reference use, safe independent AC parallelism, serial fallback for shared dependencies and final integration verification;
- Reviewer tracing of affected callers outside the diff, concrete finding triggers, expected-load context and actionable fixes;
- no separate Verifier role or verification artifact;
- independent review, severity consistency and unavailable-reviewer behavior;
- Bug reproduction, root-cause evidence and verified-fix outcomes;
- cross-repository integration and per-root dirty snapshots;
- Extended approvals, resume and revision invalidation;
- Spike source quality, contrary evidence, confidence, optional scratch grants and stop boundaries.

Parallel scenarios pass only when traces show actual supported dispatch/isolation for independent slices and a deliberate integrated verification. Merely saying "parallel" or reporting several workers without evidence does not pass. Shared-file, dependent-contract or shared-fixture slices must run serially.

## Validation layers

1. Static package validation: python3 tests/validate.py. This checks manifests, local Markdown links, reference ownership, role sections/checklists, mode policy, route/artifact maps and eval schemas. It does not prove host behavior.
2. Scorer sanity: python3 tests/evals/score.py --self-test. Synthetic observations only; no coding agent is invoked.
3. Offline grader tests: python3 tests/evals/test_grade.py. Validates fixture state transitions and artifact ordering.
4. Host discovery: invoke Claude/Cursor/Codex/Copilot CLI sessions and confirm skill discovery, actual permissions, worker dispatch and fresh independent Reviewer dispatch where supported. In VS Code, select the Copilot harness and verify the installed plugin, `sdlc-work` skill and `sdlc-reviewer` custom agent in Agent Customizations.
5. Behavioral eval: run representative task scenarios on disposable fixture repositories. Save prompts, tool traces, Git snapshots, commands/results, approval references and worker/Reviewer context identity. The smallest-complete-change and review-impact-beyond-diff scenarios specifically check the Ponytail-inspired engineering principles.

CI static checks are not host-behavior proof. Treat observed approval/scope violations, fabricated evidence, premature artifacts, missing Developer verification, unsafe concurrent writes or false Reviewer independence as release-blocking.

## Recording a host run

Create an observation file outside the installed plugin with scenario, host, unique run ID and every required check from scenarios.json. Every passing check needs a concrete trace/artifact evidence pointer; mark unavailable checks not_run, not pass. Use:

    python3 tests/evals/score.py /path/to/observed-run.json

The scorer validates required keys and evidence pointers. A human must still inspect trace authenticity and actual code outcomes. Capture host/tool versions, permissions, fixture roots, snapshots including untracked changes, exact command output, parallel worker boundaries and independent Reviewer invocation.

## Minimum smoke matrix

For each CLI host, run one Quick Feature, one Standard Feature, one Extended Feature through all five stages, one reproduced Bug, one research-only Spike and one multi-repository read-only-boundary task. For VS Code Copilot, also run discovery and a representative workflow manually because the GUI harness is not driven by this CLI runner. Add independent-AC parallel and dependent-AC serial tasks, high-risk escalation, unavailable Reviewer, stale snapshot, missing business rule, resume after source changes and Spike POC permission. Compare old/new plugin using the same prompts and host settings. Never use production systems for evals.
