# Bug workflow

1. Record symptom, expected vs actual, occurrence, environment, severity, affected boundaries and original report reference. Preserve a useful baseline and current changes.
2. Reproduce with observed failure/log or trustworthy exact reporter evidence. Separate `REPRODUCED`, `EVIDENCED_NOT_REPRODUCED` and `UNVERIFIED`. Do not claim root cause from correlation. If evidence is inadequate for a safe fix, return diagnosis and the smallest missing reproduction request; no speculative patch.
3. Investigate cause, compare plausible causes only as needed, identify regression seam and blast radius. Build a minimum fix plan and check it preserves established behavior; a new business choice returns to Feature Spec/human gate.
4. After bounded edit authorization, capture a failing regression first where feasible; implement minimal repair and rerun original reproduction, targeted test and affected regressions. Report before/after observations, remaining gaps and affected roots.
5. Verify & Converge against **the original symptom, root-cause hypothesis, regression protection, and compatibility**, then independent review on current changed snapshot. `VERIFIED_FIX` requires credible original symptom resolution, regression evidence, required checks and independent `AI_PASS`; else return `PARTIAL`/`UNVERIFIED` explicitly.

In Extended, follow the exact stage sequence in core/human-gates.md, with a mandatory approval after each applicable stage; do not combine stages or prepare downstream outputs before approval.
