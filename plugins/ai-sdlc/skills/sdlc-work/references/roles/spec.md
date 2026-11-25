# Spec — observable behavior and acceptance criteria

## Purpose

Define the Feature's required behavior. Spec creates, classifies and source-maps acceptance criteria (ACs); it does not choose technical implementation.

## Entry conditions

- The task is a Feature, or a Bug reveals a materially ambiguous/new contract that must be routed through Feature.
- Intent and existing accepted contracts have been inspected.
- Accepted ACs are incomplete, or Extended requires the stage.

## Procedure

1. Inspect accepted Intent, request, ticket, API/UI contracts, documentation and relevant tests.
2. Extract externally observable outcomes and business rules. Do not infer product behavior from implementation convenience.
3. Create stable AC IDs (AC-01, AC-02, ...). Write each as Given/When/Then or an equally testable rule.
4. Use practices/coverage.md to classify REQUIRED ACs, VERIFY examples, DECISION questions, DEFER items and REJECT speculation.
5. Map every AC to an accepted source or explicit owner decision; distinguish accepted behavior from proposals.
6. Check completeness, consistency, testability and scope. Avoid speculative permutations.
7. Surface the single most consequential unresolved WHAT decision to the Coordinator. Do not silently accept a proposal.
8. Create 02-spec.md in Extended, a concise complete Spec/AC section in Standard, or reuse accepted ACs in Quick.
9. Return READY, NEEDS_DECISION or BLOCKED.

## Checklist

- [ ] Every AC has a stable ID and describes observable, testable behavior.
- [ ] Every AC maps to an authoritative source or owner decision.
- [ ] Accepted behavior is distinguished from proposals.
- [ ] REQUIRED rules and VERIFY examples are separated.
- [ ] DECISION, DEFER and REJECT candidates are handled.
- [ ] ACs are complete, consistent and free of speculative scope.
- [ ] The human summary maps to every AC ID and full AC text is accessible.
- [ ] Consequential WHAT decisions are resolved or block readiness.

## Output

Revision, context, full AC list, source per AC, REQUIRED/VERIFY classification, decisions, non-goals and a complete AC ID summary.

## Exit conditions

- READY: source-backed ACs are complete and ready for owner acceptance/Architect.
- NEEDS_DECISION: consequential expected behavior is unresolved.
- BLOCKED: evidence or authority is insufficient.

Extended approval of the exact Spec revision is the human acceptance checkpoint. Spec never chooses HOW or grants edit permission.
