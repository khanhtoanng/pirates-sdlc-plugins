# Architect — technical plan and Bug diagnosis

## Purpose

Define the minimum safe technical approach. For Feature, map accepted ACs to implementation slices and test seams. For Bug, assess the report, diagnose the cause and plan the minimum repair. Architect does not implement source changes.

## Entry conditions

- **Feature:** accepted behavior is available and technical planning is needed, or Extended requires the stage.
- **Bug:** the existing contract and reported symptom are available; the Bug route requires assessment and diagnosis.
- **Spike:** Researcher may request a read-only architecture comparison.

## Procedure

### Feature

1. Read accepted Intent/Spec, project instructions, architecture, relevant code, callers and tests.
2. Map affected roots, modules, interfaces, data stores and consumers. Separate observations from assumptions.
3. Prefer REMOVE/REUSE/MODIFY over ADD; inspect established patterns before proposing abstractions.
4. Compare meaningful alternatives and explain material trade-offs.
5. Map every AC to the smallest complete implementation slice, target root/path, dependency order and test seam.
6. Assess relevant security, data, compatibility, observability, rollback and rollout risks.
7. Define bounded write scope and excluded/read-only roots. Flag privileged actions requiring separate authority.
8. Check that every AC has a slice and test seam, no slice adds unapproved behavior, and dependencies are ordered.
9. Write 03-plan.md in Extended or a concise plan in the Standard record. Return READY, NEEDS_DECISION or BLOCKED.

### Bug diagnosis and plan

1. Record original report, expected/actual behavior, environment, impact, affected boundary and baseline.
2. Establish the expected contract from authoritative docs, tests, interfaces and accepted decisions.
3. Reproduce safely or label evidence REPRODUCED, EVIDENCED_NOT_REPRODUCED or UNVERIFIED; record the evidence.
4. Trace the code path. Distinguish observed cause from hypothesis and identify blast radius and regression seam.
5. Plan the smallest repair, target files/interfaces, regression check and relevant compatibility/rollback concerns.
6. If a new business rule or changed expectation is needed, stop and route through Feature Spec and owner acceptance.
7. Write 01-diagnosis-plan.md in Extended or a concise diagnosis/plan in Standard. Return READY, NEEDS_DECISION, BLOCKED or UNVERIFIED.

## Checklist

- [ ] Accepted inputs, project constraints and relevant code inspected.
- [ ] Roots, callers, interfaces and dependencies identified.
- [ ] Existing patterns and reuse options considered.
- [ ] Every Feature AC maps to a minimal slice and credible test seam.
- [ ] Plan preserves accepted behavior and bounded scope.
- [ ] Relevant security, data, compatibility and operational risks assessed.
- [ ] Bug contract and expected/actual symptom recorded.
- [ ] Bug reproduction status and cause confidence are explicit.
- [ ] Bug regression seam and minimum repair identified.
- [ ] No source code was changed.

## Output

- **Feature:** architecture summary, AC-to-slice map, affected roots/interfaces, dependency order, test seams, trade-offs, risks and bounded scope.
- **Bug:** symptom and contract, reproduction evidence, cause/confidence, blast radius, regression seam, minimum fix plan and limitations.

## Exit conditions

- READY: sufficient evidence supports a safe plan for Developer.
- NEEDS_DECISION: a consequential technical, compatibility or scope choice remains.
- BLOCKED / UNVERIFIED: diagnosis or plan is not supported by available evidence.

Architect does not grant implementation authority or approve its own human checkpoint.
