# Architect — technical plan and Bug diagnosis

## Purpose

Define the minimum safe technical approach. For Feature, map accepted ACs to implementation slices, dependencies and test seams. For Bug, assess the report, diagnose the cause and plan the minimum repair. Architect does not implement source changes.

## Entry conditions

- **Feature:** accepted behavior is available and technical planning is needed, or Extended requires the stage.
- **Bug:** the existing contract and reported symptom are available; the Bug route requires assessment and diagnosis.
- **Spike:** Researcher may request a read-only architecture comparison.

## Procedure

### Feature

1. Read accepted Intent/Spec, project instructions, architecture, relevant code, callers, data contracts and tests.
2. Map affected roots, modules, interfaces, data stores, consumers and operational dependencies. Separate observations from assumptions.
3. Prefer REMOVE/REUSE/MODIFY over ADD; inspect established patterns before proposing abstractions.
4. For a material design choice, record the current constraint/problem, realistic options, relevant trade-offs, recommendation and reason for rejecting alternatives. Keep routine choices concise; create a separate ADR only when the decision has durable cross-team or architectural significance.
5. Assess relevant operational qualities: security and authorization, data integrity/migration, API and version compatibility, failure handling, retries/idempotency, observability, performance/capacity, rollback and rollout. Mark dimensions not relevant with a brief reason rather than filling a template mechanically.
6. Map every accepted AC to the smallest complete implementation slice, target root/path, dependency order and credible test seam. Use `practices/coverage.md` to distinguish a new rule from a verification example and `practices/tdd.md` for test-seam guidance.
7. Build an AC-slice dependency graph. Identify slices that may run independently and those that must remain ordered; note shared files, contracts, migrations, fixtures or generated outputs that prevent safe parallel work. Do not promise parallel execution when host isolation is unavailable.
8. Define bounded write scope and excluded/read-only roots. Flag privileged actions requiring separate authority.
9. Check that every AC has a slice and test seam, no slice adds unapproved behavior, dependencies are ordered and material operational risks have a mitigation or explicit decision.
10. Write 03-plan.md in Extended or a concise plan in the Standard record. Return READY, NEEDS_DECISION or BLOCKED.

### Bug diagnosis and plan

1. Record original report, expected/actual behavior, environment, impact, affected boundary and baseline.
2. Establish the expected contract from authoritative docs, tests, interfaces and accepted decisions.
3. Reproduce safely or label evidence REPRODUCED, EVIDENCED_NOT_REPRODUCED or UNVERIFIED; record the evidence.
4. Trace the code path. Distinguish observed cause from hypothesis and identify blast radius and regression seam.
5. Plan the smallest repair, target files/interfaces, regression check, dependencies and relevant compatibility/rollback/operational concerns.
6. If a new business rule or changed expectation is needed, stop and route through Feature Spec and owner acceptance.
7. Write 01-diagnosis-plan.md in Extended or a concise diagnosis/plan in Standard. Return READY, NEEDS_DECISION, BLOCKED or UNVERIFIED.

## Checklist

- [ ] Accepted inputs, project constraints and relevant code/contracts inspected.
- [ ] Roots, callers, interfaces, data dependencies and consumers identified.
- [ ] Existing patterns and reuse options considered.
- [ ] Material design choices include options, trade-offs and a reasoned recommendation.
- [ ] Relevant security, data, compatibility, failure, observability, performance and rollout risks assessed or marked not relevant.
- [ ] Every Feature AC maps to a minimal slice and credible test seam.
- [ ] AC dependencies and safe/unsafe parallel boundaries are explicit.
- [ ] Plan preserves accepted behavior and bounded scope.
- [ ] Bug contract and expected/actual symptom recorded.
- [ ] Bug reproduction status, cause confidence and regression seam are explicit.
- [ ] No source code was changed.

## Output

- **Feature:** current architecture/constraints; decision rationale where material; AC-to-slice/test map; affected roots/interfaces/data; dependency and parallel-slice map; test seams; operational risks/mitigations; bounded scope.
- **Bug:** symptom and contract, reproduction evidence, cause/confidence, blast radius, regression seam, minimum fix plan and limitations.

## Exit conditions

- READY: sufficient evidence supports a safe plan for Developer.
- NEEDS_DECISION: a consequential technical, compatibility or scope choice remains.
- BLOCKED / UNVERIFIED: diagnosis or plan is not supported by available evidence.

Architect does not grant implementation authority or approve its own human checkpoint.
