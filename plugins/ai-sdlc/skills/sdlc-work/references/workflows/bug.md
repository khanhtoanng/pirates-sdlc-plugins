# Bug workflow

A Bug repairs existing behavior that violates an established expectation. Normal order is Architect (assessment, diagnosis and minimum repair plan) → Developer (fix and verify) → independent Reviewer. Quick may use bounded Developer triage for a clear, low-risk Bug.

## Role sequence by mode

| Responsibility | Quick | Standard | Extended |
|---|---|---|---|
| Assess/diagnose | Developer performs bounded symptom check and triage | Architect investigates symptom, reproduction and cause | Distinct Architect diagnosis/plan stage; approval required |
| Fix/verify | Developer fixes only with credible evidence and bounded authority | Developer implements the minimum repair and verifies | One gated fix, TDD and verification stage |
| Review | Fresh independent review after code changes | Fresh independent review after code changes | Separate gated Reviewer stage |

If reproduction is unavailable, report REPRODUCED, EVIDENCED_NOT_REPRODUCED or UNVERIFIED accurately. Do not infer cause from correlation or patch speculatively.

## Extended artifacts

1. Architect — 01-diagnosis-plan.md
2. Developer — 02-implementation.md (fix and verification)
3. Reviewer — 03-review.md

Use stage IDs diagnosis_plan, implementation and review. Create only the current artifact.

## Bug-specific rules

1. Preserve the original report, expected/actual behavior, environment, impact and baseline.
2. Establish the expected contract from authoritative tests, docs, interfaces and accepted decisions.
3. Record reproduction evidence and distinguish observed cause from hypothesis.
4. Identify blast radius, regression seam and smallest safe repair.
5. If a new business rule or changed expectation is required, stop and route through Feature Spec and owner acceptance.
6. After authorization, Developer adds a failing regression test where feasible, applies the minimum fix, then reruns the original symptom and relevant regressions/integrations.
7. Record before/after observations, exact commands/results, changed roots and missing checks.
8. Reviewer checks the original symptom, diagnosis evidence, diff, test credibility and completeness.

Use VERIFIED_FIX only when the original symptom is credibly resolved, regression evidence exists, required checks are observed and independent review is AI_PASS. Otherwise report PARTIAL or UNVERIFIED.
