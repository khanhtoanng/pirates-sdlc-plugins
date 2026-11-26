# Intent — problem and outcome

## Purpose

Define the Feature's WHY, WHO, expected outcome, scope and non-goals. Intent does not define detailed behavior or technical design.

## Entry conditions

- The task is a Feature.
- Existing requests, decisions and project context have been inspected.
- The problem, user, outcome or scope needs definition, or Extended requires the stage.

## Procedure

1. Inspect the request, ticket, current behavior and accepted decisions. Reuse known facts.
2. Describe the problem independently from the proposed solution.
3. Identify the affected user/stakeholder and intended outcome. Mark unsupported details unknown.
4. Define scope, non-goals and important exclusions.
5. Separate observed facts, sources, assumptions and unknowns. Ask the Coordinator to raise the most consequential unresolved question.
6. Write 01-intent.md in Extended, a concise Intent section in Standard, or a short context summary in Quick.
7. Return READY, NEEDS_DECISION or BLOCKED to the Coordinator.

## Checklist

- [ ] Problem and desired outcome are distinct from the proposed solution.
- [ ] User, outcome, scope and non-goals are grounded or marked unknown.
- [ ] Sources, facts, assumptions and unknowns are distinguishable.
- [ ] Consequential decisions are surfaced for the Coordinator.
- [ ] No detailed ACs or technical design were invented.

## Output

Problem, target user, intended outcome, success signal when known, scope, non-goals, sources, assumptions and unresolved decisions.

## Exit conditions

- READY: problem and outcome are clear enough for Spec.
- NEEDS_DECISION: a consequential WHY/WHO/scope decision remains.
- BLOCKED: required context or authority is unavailable.

Intent does not create ACs, edit source or grant implementation authority.
