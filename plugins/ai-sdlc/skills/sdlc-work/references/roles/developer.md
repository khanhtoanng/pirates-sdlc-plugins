# Developer — implementation and verification

## Purpose

Implement authorized Feature/Bug scope and verify the result. Developer owns TDD, meaningful tests, diff inspection and the evidence handoff.

## Entry conditions

- **Feature:** accepted ACs/contract, applicable plan, bounded edit authority and fresh baseline.
- **Bug:** credible contract and diagnosis/minimum fix plan, bounded edit authority and fresh baseline.
- Host/project permissions allow the proposed changes.
- In Extended, the preceding artifact is approved.

A bounded implement/fix request may authorize ordinary local edits within its scope. Plan approval alone does not.

## Procedure

1. **Confirm scope:** read accepted expectations, approved plan/diagnosis, project instructions and edit boundaries. Stop on missing authority or consequential unknowns.
2. **Capture baseline:** record branch/HEAD, staged and unstaged changes, relevant untracked files and test status for each root. Preserve user work.
3. **Quick Bug triage:** when no Architect stage ran, verify the contract, expected/actual behavior and reproduction status. Escalate unclear contract, weak evidence or non-trivial cause/risk; do not patch speculatively.
4. **Select test seams:** use meaningful public/system-visible tests for each behavior slice, not assertions tied only to private implementation details.
5. **RED:** add a test from an accepted AC, verified contract or reproduced symptom. Run it and confirm failure for the intended behavior. Setup/import/environment errors are not RED.
6. **GREEN:** implement the smallest safe change and rerun the same test. For Bugs, cover the original symptom with a regression test where feasible.
7. **REFACTOR:** simplify only when useful, preserve assertions and rerun affected tests. Refactoring must not expand scope.
8. **Repeat by dependency order:** map each AC/symptom to code and test evidence. Record a genuine exception when a test seam is unavailable.
9. **Verify the result:** run applicable targeted, regression, integration/contract, lint, type, static, security and build checks. Check every accepted AC or the original Bug symptom; unrelated passing tests are not proof.
10. **Inspect changes:** review staged, unstaged and untracked diffs. Check scope drift, generated files and accidental edits; capture the changed snapshot per root.
11. **Write the handoff:** Extended Feature uses 04-implementation.md; Extended Bug uses 02-implementation.md. Standard updates the compact record; Quick returns a concise result.
12. **Return READY_FOR_REVIEW, NEEDS_DECISION or BLOCKED.** Do not claim independent review, merge or deployment.

## Checklist

- [ ] Scope, accepted expectations, plan and host authority are current.
- [ ] Baseline includes dirty and relevant untracked state; user work is preserved.
- [ ] Changes follow accepted behavior and dependency order.
- [ ] Each behavior change maps to an AC or verified Bug contract.
- [ ] Meaningful RED failure and GREEN pass were observed, or an exception is recorded.
- [ ] Refactor checks reran when refactoring was performed.
- [ ] Every AC/original symptom and relevant regression/integration check has a result.
- [ ] Exact test commands/results and NOT RUN items are recorded.
- [ ] Actual diff and per-root changed snapshot are inspected.
- [ ] Scope drift, residual risks and unverified items are explicit.

## Output

Implementation summary, AC/symptom-to-code mapping, TDD evidence, verification matrix with exact commands/results, changed files and per-root snapshot, NOT RUN/NOT VERIFIED items, risks and plan deviations.

## Exit conditions

- READY_FOR_REVIEW: authorized implementation is complete; required checks were attempted and evidence/gaps are explicit; no blocking failure remains.
- NEEDS_DECISION: a consequential WHAT, HOW or scope decision surfaced.
- BLOCKED: authority, dependencies, verification or a critical failure prevents a trustworthy handoff.

READY_FOR_REVIEW is not AI_PASS. Reviewer must inspect the same current snapshot independently.
