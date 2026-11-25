# Bug workflow

A Bug repairs existing behavior that violates an established expectation. Normal responsibility order is Architect (assessment + diagnosis + minimal fix plan) → Developer (fix + verification) → independent Reviewer. Do not create fictional Feature Intent or Spec stages. If a repair requires a new business rule, stop and route that WHAT decision through Feature Spec and owner acceptance.

## Role sequence and mode applicability

| Order | Responsibility | Quick | Standard | Extended |
|---|---|---|---|---|
| 1 | Assess, diagnose and plan | Developer performs bounded symptom check and minimal triage; use Architect if cause/risk is not straightforward | Architect investigates symptom, reproduction, cause and minimal repair plan | One distinct Architect stage/artifact; approval required |
| 2 | Fix and verify | Developer fixes only with credible evidence and bounded authority, then verifies | Developer implements the minimal repair and verifies | One gated Developer stage combining fix, TDD and verification |
| 3 | Independent review | Fresh independent review after code changes | Fresh independent review after code changes | Separate gated Reviewer stage |

If the original symptom cannot be reproduced, distinguish REPRODUCED, EVIDENCED_NOT_REPRODUCED and UNVERIFIED. Do not guess root cause or claim a verified fix based only on correlation.

## Extended artifacts

- Architect: 01-diagnosis-plan.md (assessment, diagnosis, reproduction evidence and minimum fix plan)
- Developer: 02-implementation.md (fix and verification evidence)
- Reviewer: 03-review.md

Use stage IDs diagnosis_plan, implementation and review. Do not create intent.md, spec.md, separate assessment.md/diagnosis.md/plan.md files, or verification.md for the normal Bug route. Each artifact is created only when its stage runs.

## Bug-specific rules

1. Capture the original report, expected versus actual behavior, environment, occurrence, impact/severity and affected boundary. Preserve a useful baseline.
2. Inspect authoritative tests, interface/API contracts, documentation and accepted decisions to establish expected behavior.
3. Reproduce using observed failure/logs or exact trustworthy reporter evidence. Label reproduction status honestly and record exact evidence.
4. Trace a credible cause and distinguish observed cause from hypothesis. Identify a regression seam and blast radius.
5. Plan the smallest safe repair, target files/interfaces, regression check, relevant non-regressions and compatibility/rollback concerns when applicable.
6. After bounded edit authorization, Developer captures a failing regression first where feasible, implements minimally, and reruns the original symptom, targeted regression and relevant integrations.
7. Developer reports before/after observations, actual commands/results, affected roots, changed snapshot and missing checks.
8. Reviewer independently checks the original expected/actual symptom, reproduction/cause evidence, diff, test credibility, regression protection and completeness.

Use VERIFIED_FIX only when credible evidence shows the original symptom resolved, adequate regression evidence exists, required checks are observed and independent review is AI_PASS. Otherwise report PARTIAL or UNVERIFIED with the exact gap.

Extended: Architect, Developer and Reviewer each complete their own checklist and receive approval of the exact artifact revision before the next stage. A new code change requires Developer re-verification and fresh independent review.