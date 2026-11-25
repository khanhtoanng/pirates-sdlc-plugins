# Task routes

Task type selects the workflow; mode selects its depth and human approval. Auto chooses the smallest safe mode. See core/modes.md for selection rules.

## Feature — add customer status

Example: `sdlc-work feature standard Add customer status to FE and BE; use Flyway only if needed; keep Terraform read-only.`

**Order:** Intent (when problem/scope needs clarity) → Spec (when accepted ACs are incomplete) → Architect (when design or slicing is needed) → Developer → independent Reviewer.

- Intent: problem, target user, outcome, scope and non-goals.
- Spec: stable, testable ACs with source mapping and a complete AC summary.
- Architect: map each AC to implementation slices, roots, interfaces, dependencies and test seams.
- Developer: implement authorized slices with TDD where applicable; verify each AC and relevant regressions/integrations.
- Reviewer: inspect the actual diff, AC coverage and Developer evidence in a fresh context.

Extended artifacts: 01-intent.md, 02-spec.md, 03-plan.md, 04-implementation.md, 05-review.md.

## Bug — endpoint returns 500 instead of the existing 400 contract

Example: `sdlc-work bug quick Fix the login 500 for an empty password and verify the existing 400 contract.`

**Order:** Architect (assessment, diagnosis and minimum repair plan) → Developer (fix and verify) → independent Reviewer. Quick may use bounded Developer triage for a clear, low-risk Bug.

Extended artifacts: 01-diagnosis-plan.md, 02-implementation.md, 03-review.md. If expected behavior is unclear or a new business rule is needed, route it through Feature Spec and owner acceptance. Report reproduction status honestly; use VERIFIED_FIX only with credible symptom resolution, regression evidence, required checks and independent AI_PASS.

## Spike — assess offline synchronization

Example: `sdlc-work spike standard Assess offline sync feasibility for mobile. Research only.`

**Order:** Researcher scope → research → optional separately approved scratch experiment → decision. Compare viable options and contrary evidence; return PROCEED, CLARIFY or STOP. Production implementation requires a separate Feature/Bug task.

Extended artifacts: 01-scope.md, 02-research.md, optional 03-experiment-plan.md and 04-experiment.md, then 05-decision.md.

## Boundary cases

- Tiny, established Feature: Quick may skip separate Intent, Spec and Architect work.
- Bug without credible reproduction: report the evidence gap; do not make a speculative patch.
- Bug requiring a new product rule: resolve it as a Feature decision before implementation.
- Multiple repositories alone do not imply Extended; assess contract, security, data and rollout risk.
- Research followed by implementation: finish the Spike, then start a separately scoped Feature/Bug.
