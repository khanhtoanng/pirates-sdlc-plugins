# Bug workflow

A Bug repairs existing behavior that violates an established expectation. Normal order is Architect (assessment, diagnosis and minimum repair plan) → Developer (fix and verify) → independent Reviewer. Quick may use bounded Developer triage for a clear, low-risk Bug.

## Role sequence by mode

| Responsibility | Quick | Standard | Extended |
|---|---|---|---|
| Assess/diagnose | Developer performs bounded symptom check and triage | Architect investigates symptom, reproduction and cause | Distinct Architect diagnosis/plan stage; approval required |
| Fix/verify | Developer fixes only with credible evidence and bounded authority | Developer validates and executes the minimum repair plan | One gated fix, TDD and verification stage against the approved diagnosis plan |
| Review | Fresh independent review after code changes | Fresh independent review after code changes | Separate gated Reviewer stage |

If reproduction is unavailable, report REPRODUCED, EVIDENCED_NOT_REPRODUCED or UNVERIFIED accurately. Do not infer cause from correlation or patch speculatively.

## Extended artifacts

1. Architect — 01-diagnosis-plan.md
2. Developer — 02-implementation.md (fix and verification)
3. Reviewer — 03-review.md

Use stage IDs diagnosis_plan, implementation and review. Create only the current stage.

## Bug-specific rules

1. Preserve the original report, expected/actual behavior, environment, impact and baseline.
2. Establish the expected contract from authoritative tests, docs, interfaces and accepted decisions.
3. Record reproduction evidence and distinguish observed cause from hypothesis.
4. Identify blast radius, regression seam and smallest safe repair.
5. Architect owns the diagnosis and proposed minimum repair plan, including genuine prerequisites and verification seams. Developer validates feasibility against the current baseline and executes it; material plan changes return through the Coordinator.
6. If a new business rule or changed expectation is required, stop and route it through Feature Spec and owner acceptance.
7. After authorization, Developer follows practices/tdd.md for a failing regression, minimum fix, GREEN evidence and justified exceptions.
8. Record before/after observations, exact commands/results, changed roots and missing checks.
9. Reviewer checks the original symptom, diagnosis evidence, diff, test credibility and completeness.

Use VERIFIED_FIX only when the original symptom is credibly resolved, regression evidence exists, required checks are observed and independent review is AI_PASS. Otherwise report PARTIAL or UNVERIFIED.
