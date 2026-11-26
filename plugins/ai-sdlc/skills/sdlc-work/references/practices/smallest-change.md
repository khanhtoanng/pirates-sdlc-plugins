# Smallest complete change

Use this practice when Architect selects an approach or Developer implements an approved slice. It defines how to minimize unnecessary work without minimizing correctness. It does not replace accepted requirements, TDD, permissions or project conventions.

## Understand the change before choosing a solution

Read the accepted outcome or Bug contract and the code the change touches. Trace only the relevant flow:

- Entry points, changed functions and their callers/consumers.
- Functions and services they depend on; public interfaces and data/API contracts.
- Relevant tests, fixtures, configuration, exports and generated code.
- Affected repositories, data ownership and compatibility boundaries.
- Material failure, security, data-loss and operational consequences.

Use repository evidence to understand the project's existing patterns and expected load where it matters. Do not assume a scale target or expand into an unrelated repository-wide audit. Mark missing evidence UNKNOWN.

## Choose the first option that fully satisfies the accepted outcome

1. **Does it need to exist?** Remove unrequested behavior, flexibility, options and polish. Keep every accepted requirement and mandatory safeguard.
2. **Already in this codebase?** Reuse an existing helper, component, service or established pattern. Prefer the project's existing abstraction over introducing a competing one.
3. **Standard library or platform feature?** Use it when it fits project conventions and does not bypass an established project capability.
4. **Already-installed dependency?** Reuse it when it is the simplest compatible choice. Do not add a dependency for a small capability the project or platform already provides.
5. **Simplest clear implementation?** Prefer deletion and direct code over wrappers, layers or abstractions with no concrete need. A one-line solution is useful only when a reader understands it immediately.
6. **Otherwise, add the minimum new code** that safely completes the requirement.

Compare alternatives only when the choice materially affects correctness, compatibility, security, operational cost or maintainability. Explain the decisive trade-off; do not invent weighted scores or hypothetical future needs.

## Keep the change complete and safe

- The goal is the smallest **complete** change, not the shortest diff or code golf.
- Include every affected caller, consumer, contract, test, fixture, configuration, export and migration that the behavior requires. Do not stop at the file named in the request.
- For a Bug in shared code, inspect all relevant callers before editing. Fix an evidenced shared root cause once where appropriate, then verify the affected callers; do not patch each symptom independently.
- Preserve existing validation, error handling, authorization, data integrity, recovery behavior and accessibility when code is moved, merged or simplified.
- Prefer the correct option on meaningful edge cases when alternatives are otherwise comparable.
- Do not add an abstraction, wrapper, dependency, option or configuration item without a concrete requirement.

## Verification and handoff

- `practices/tdd.md` owns test-seam selection, the RED → GREEN → REFACTOR sequence and exceptions. Use a meaningful test for non-trivial or risky logic; do not create artificial tests for documentation-only or mechanical changes.
- Recheck the relevant flow after implementation. A passing isolated test does not replace caller, integration or regression checks when those are affected.
- Reuse the role's existing output. State material work intentionally left out, checks not run, unknowns and residual risks; never claim an unobserved result.

Architect owns the proposed approach and logical delivery plan. Developer applies this practice within the approved outcomes and boundaries. A material change to the approved design or slice returns through the Coordinator to Architect.
