# Intent — WHY, WHO and outcome

## Purpose

Establish the product problem and intended outcome for a Feature. Intent does not define detailed behavior or technical implementation. It is not a mandatory separate responsibility for every Quick/Standard task; Extended Feature always presents an Intent stage, even when it summarizes already accepted evidence.

## Entry conditions

- The task is classified as Feature.
- Relevant request, ticket, source and project instructions have been inspected.
- There is a need to establish or explicitly review WHY, WHO, outcome, scope or non-goals.

## Procedure

1. **Inspect context:** read the original request, existing ticket/decisions, current behavior and relevant documentation before asking questions. Reuse accepted decisions.
2. **Identify the problem:** describe the user/business problem without jumping to a solution.
3. **Identify the user:** establish who experiences the problem or receives the benefit. Do not invent personas unsupported by the request/source.
4. **Define the outcome:** describe the observable business/user outcome and a suitable success signal where one is known or can be grounded.
5. **Set boundaries:** state in-scope outcomes, explicit non-goals and important exclusions.
6. **Surface uncertainty:** separate observed facts, source-backed facts, assumptions and unknowns. Ask the Coordinator to raise only the highest-impact unresolved question.
7. **Write the output:** for Extended, create 01-intent.md; for Standard, contribute a concise Intent section to the agreed record; for Quick, provide the minimum understanding in context without creating a file.
8. **Return to Coordinator:** report READY, NEEDS_DECISION or BLOCKED. Do not write ACs, design architecture, edit source or start Spec.

## Checklist

- [ ] Original request and relevant existing decisions inspected.
- [ ] Problem is stated independently from the proposed solution.
- [ ] Target user/stakeholder is identified or marked unknown.
- [ ] Intended outcome and success signal are grounded.
- [ ] Scope, non-goals and exclusions are explicit.
- [ ] Facts, assumptions and unknowns are distinguished.
- [ ] Material unresolved questions are surfaced, not hidden in the artifact.
- [ ] No detailed ACs or technical design were invented.
- [ ] Output is concise and traceable to source material.

## Output

01-intent.md (Extended) or a concise Intent section (Standard): Problem, target user, intended outcome, success signal, scope, non-goals, sources, assumptions and unresolved decisions.

## Exit conditions

- READY: problem/outcome/scope are sufficiently grounded for Spec.
- NEEDS_DECISION: a consequential WHY/WHO/scope decision remains.
- BLOCKED: necessary context or authority is unavailable.

Intent never approves the next role or grants implementation permission.