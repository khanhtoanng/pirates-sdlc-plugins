# Feature workflow

1. Inspect existing ticket/contracts and relevant roots. Intent asks WHY/WHO only if consequential ambiguity remains; no speculative brainstorming transcript.
2. Spec reuses the accepted AC revision or drafts full observable source-linked ACs. Separate REQUIRED acceptance rules from VERIFY examples (`practices/coverage.md`). **Spec gate:** all changed ACs are testable, mutually consistent, authority-backed and accepted where consequential; open material decisions block build.
3. Architect maps AC→vertical slice→root/interface/test seam, compatibility, rollback and rollout where implicated. **Plan gate:** impact and verification plan are credible; sensitive technical trade-offs resolved.
4. Confirm authorized edit scope, build slices test-first where applicable, verify and converge ACs plus dependencies, then independent review on the current snapshot. Any code change invalidates prior review.
5. Report `READY_FOR_MERGE_REVIEW` only if required evidence and independent verdict support it; this does not authorize merging, deploying or running migrations.

In Extended, follow the exact stage sequence in core/human-gates.md, with a mandatory approval after each applicable stage; do not combine stages or prepare downstream outputs before approval.
