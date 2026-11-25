# Three task types — workflow routes and examples

Task type selects the workflow. Mode selects how much process and human approval is applied. Use auto unless a mode is explicitly requested. See core/modes.md for exact behavior.

## Feature — add customer status

Request example: sdlc-work feature standard Add customer status to FE and BE, with a Flyway migration only if necessary. Terraform read-only.

Responsibility order: Intent (if WHY/WHO/scope needs definition) → Spec (if complete accepted ACs do not exist) → Architect (if technical design/task mapping is needed) → Developer (implementation + verification) → independent Reviewer.

- Intent: problem, target user, expected outcome, scope and non-goals.
- Spec: stable AC IDs, observable/testable behavior, provenance and complete AC map.
- Architect: map every AC to implementation slice/root/interface/test seam; order actual dependencies and assess relevant risks.
- Developer: implement authorized slices with TDD where applicable; verify every accepted AC, meaningful regressions and integrations; record commands/results and per-root snapshot.
- Reviewer: inspect actual diff, all ACs and Developer evidence in a fresh independent context.

Extended artifacts: 01-intent.md, 02-spec.md, 03-plan.md, 04-implementation.md, 05-review.md and state.json. No separate verification.md.

Quick: Developer → Reviewer when expected behavior is established and risk is low. Standard: run applicable upstream responsibilities without approval after each. Extended: separate approval after every artifact.

## Bug — endpoint returns 500 instead of existing 400 contract

Request example: sdlc-work bug quick Fix a login endpoint returning 500 for an empty password; verify existing 400 contract.

Responsibility order: Architect (assessment + diagnosis + minimum fix plan; Quick may let Developer do bounded triage) → Developer (fix + verification) → independent Reviewer.

Extended artifacts: 01-diagnosis-plan.md, 02-implementation.md, 03-review.md and state.json. Do not create Feature Intent/Spec stages or a separate verification.md.

If expected behavior is unclear or a new business rule is required, stop for Feature Spec/owner acceptance. If reproduction is unavailable, report EVIDENCED_NOT_REPRODUCED or UNVERIFIED. Use VERIFIED_FIX only with credible original-symptom resolution, regression evidence, required checks and independent AI_PASS.

## Spike — assess offline synchronization

Request example: sdlc-work spike standard Determine feasibility of offline sync for mobile. Research only.

Researcher owns Scope → Research → optional Experiment Plan → optional Experiment → Decision. Compare realistic options and contrary evidence. A POC requires a separate scratch grant. Return PROCEED, CLARIFY or STOP; no automatic production implementation or code-review chain.

Extended artifacts: 01-scope.md, 02-research.md, optional 03-experiment-plan.md and 04-experiment.md, 05-decision.md and state.json. Mark unused experiment stages not_applicable without placeholder files.

## Boundary cases

- Tiny known Feature: Quick can skip separate Intent/Spec/Architect; Developer still verifies and Reviewer remains independent.
- Bug without credible reproduction: diagnosis, not a speculative patch.
- Bug fix requiring a new product rule: Feature decision before code changes.
- Multiple repositories alone do not imply Extended; assess contract/security/data/rollout risk.
- Research and implement if feasible: complete Spike first and request a separately scoped Feature/Bug for implementation.