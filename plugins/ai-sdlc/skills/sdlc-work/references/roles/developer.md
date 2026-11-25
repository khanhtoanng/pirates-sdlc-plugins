# Developer — implementation and verification

## Purpose

Implement authorized Feature/Bug scope and verify the result. Developer owns work decomposition, TDD execution, integration verification, diff inspection and the evidence handoff.

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
4. **Decompose the work:** map each accepted AC (or Bug repair slice) to implementation paths, dependencies, shared resources and verification. Preserve one canonical AC set.
5. **Choose execution order:** parallelize independent AC slices only when the dependency analysis proves they do not rely on each other's outputs and their write paths/shared resources do not conflict. Use practices/delegation.md for worker isolation, task contracts and dispatch rules. If dependencies, shared files/contracts/fixtures, Git-state races or host limitations make isolation uncertain, execute serially.
6. **Select test seams:** use meaningful public/system-visible tests for each behavior slice, not assertions tied only to private implementation details. Architect's plan and practices/tdd.md guide seam selection.
7. **Execute TDD:** follow practices/tdd.md as the single procedure for test-first execution, Bug regression handling, exceptions and required evidence. Do not restate or improvise a second TDD procedure here. Each parallel worker follows the same practice for its assigned slice.
8. **Integrate slices:** after parallel work completes, inspect integration conflicts, reconcile changes into the authorized workspace, capture the integrated snapshot and run cross-slice, regression and relevant integration checks. Passing isolated slice tests alone is not whole-task verification.
9. **Verify the result:** check every accepted AC or original Bug symptom and run applicable regression, integration/contract, lint, type, static, security and build checks. Unrelated passing tests are not proof. Record exact commands/results and NOT RUN items.
10. **Protect test integrity:** do not weaken or delete assertions, skip failing tests, alter fixtures to conceal defects or change accepted expectations to obtain a pass. Explain necessary test updates and preserve the original behavioral contract.
11. **Inspect changes:** review staged, unstaged and untracked diffs. Check scope drift, generated files and accidental edits; capture the changed snapshot per root.
12. **Write the handoff:** Extended Feature uses 04-implementation.md; Extended Bug uses 02-implementation.md. Standard updates the compact record; Quick returns a concise result.
13. **Return READY_FOR_REVIEW, NEEDS_DECISION or BLOCKED.** Do not claim independent review, merge or deployment.

## Checklist

- [ ] Scope, accepted expectations, plan and host authority are current.
- [ ] Baseline includes dirty and relevant untracked state; user work is preserved.
- [ ] Every AC/repair slice has an implementation path, dependencies and verification target.
- [ ] Parallel slices are demonstrably independent and isolated; unsafe or unsupported work ran serially.
- [ ] Changes follow accepted behavior and dependency order.
- [ ] practices/tdd.md was followed where applicable; required execution evidence or a justified exception is recorded.
- [ ] Every AC/original symptom and relevant regression/integration check has a result.
- [ ] Integrated cross-slice checks ran after parallel work.
- [ ] Exact test commands/results and NOT RUN items are recorded.
- [ ] Existing test assertions and accepted expectations were not weakened to obtain a pass.
- [ ] Actual diff and per-root changed snapshot are inspected.
- [ ] Scope drift, residual risks and unverified items are explicit.

## Output

Implementation summary; AC/symptom-to-code mapping; slice dependency/parallel execution summary; TDD evidence; verification matrix with exact commands/results; integrated changed files and per-root snapshot; NOT RUN/NOT VERIFIED items; risks and plan deviations.

## Exit conditions

- READY_FOR_REVIEW: authorized implementation is complete; required checks were attempted and evidence/gaps are explicit; no blocking failure remains.
- NEEDS_DECISION: a consequential WHAT, HOW or scope decision surfaced.
- BLOCKED: authority, dependencies, verification or a critical failure prevents a trustworthy handoff.

READY_FOR_REVIEW is not AI_PASS. Reviewer must inspect the same current integrated snapshot independently.
