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

Use stage IDs diagnosis_plan, implementation and review. Persist these artifacts and `state.json` in the canonical `.sdlc/changes/<task-id>/` directory selected by the Coordinator. Link the issue or PR as a source reference; do not use it as an alternate artifact/state store. Create only the current stage.

## Bug workflow constraints

- Preserve the original report and established expected contract; distinguish observed behavior from hypotheses.
- Report reproduction as REPRODUCED, EVIDENCED_NOT_REPRODUCED or UNVERIFIED. Do not infer cause from correlation.
- If the expected behavior itself must change, stop and route the new rule through Feature Spec and owner acceptance.
- A fix is VERIFIED_FIX only when the original symptom is credibly resolved, regression evidence exists, required checks are observed and independent review is AI_PASS. Otherwise report PARTIAL or UNVERIFIED.

The Architect and Developer roles own diagnosis, repair and verification procedures. This workflow owns route order, stage applicability and artifact names.
