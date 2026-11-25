# Spec — observable WHAT and acceptance criteria

## Purpose

Define exactly what observable behavior is required. Spec owns creation, classification, source mapping and consistency validation of Feature acceptance criteria (ACs). It does not choose technical implementation.

## Entry conditions

- The task is a Feature, or an existing Bug contract is discovered to be materially ambiguous/new and must be routed through Feature.
- Intent and existing accepted contracts have been inspected.
- A separate Spec stage is needed because changed behavior lacks a complete, accepted AC set, or Extended requires the stage.

## Procedure

1. **Inspect accepted intent and sources:** read the accepted Intent, original request, tickets, current behavior, API/UI contracts, documentation and relevant existing tests. Reuse accepted requirements.
2. **Extract expected behavior:** identify externally observable outcomes and business rules. Do not derive new product behavior from implementation convenience.
3. **Create ACs:** assign stable unique IDs (AC-01, AC-02, ...). Write each criterion in Given/When/Then or an equally testable form. Each AC must describe one meaningful observable rule.
4. **Classify requirement candidates:** use practices/coverage.md to separate REQUIRED ACs from VERIFY examples, DECISION questions, DEFER items and REJECT speculation. Negative/boundary cases are normally VERIFY examples, not extra ACs.
5. **Map every AC to its source:** record the originating accepted intent, ticket, authoritative contract or explicit owner decision. Distinguish an existing accepted rule from a proposed rule awaiting acceptance.
6. **Check completeness:** ensure every part of the accepted outcome is represented and every material path, actor or state is covered where required. Avoid speculative permutations and document sprawl.
7. **Check consistency and testability:** detect contradictions, ambiguity, unverifiable wording, missing preconditions, unsupported assumptions and accidental scope expansion.
8. **Resolve material WHAT decisions:** send the Coordinator the single most consequential unresolved question at a time. Do not silently turn a proposal into an accepted requirement.
9. **Create the AC coverage map:** show every AC ID, short meaning, authoritative source/decision and a pointer to the complete AC text. The human summary must not omit any AC.
10. **Write the output:** Extended creates 02-spec.md; Standard adds a concise complete Spec/AC section to the agreed record; Quick reuses an existing accepted AC set and does not create a file.
11. **Return to Coordinator:** report READY, NEEDS_DECISION or BLOCKED. Do not design architecture, implement code or start Developer.

## Checklist

- [ ] Accepted Intent, request and existing contracts inspected.
- [ ] Every AC has a stable unique ID.
- [ ] Each AC describes observable, testable behavior.
- [ ] Every AC maps to an authoritative source or explicit owner decision.
- [ ] Proposed behavior is distinguished from accepted behavior.
- [ ] REQUIRED rules are separated from VERIFY examples.
- [ ] DECISION, DEFER and REJECT candidates are handled explicitly.
- [ ] ACs are complete for the accepted outcome without speculative scope.
- [ ] ACs are mutually consistent and testable.
- [ ] Material WHAT decisions are resolved or explicitly block readiness.
- [ ] Human summary maps to every AC ID.
- [ ] Full AC text and source/provenance are accessible.

## Output

02-spec.md (Extended) or a concise complete Spec section (Standard): revision, context, full AC list, source/provenance per AC, REQUIRED/VERIFY classification, decision log, non-goals, exclusions, consistency/testability checks and complete AC ID summary.

## Exit conditions

- READY: complete, consistent, source-backed AC proposal is ready for owner acceptance/Architect.
- NEEDS_DECISION: consequential expected behavior remains unresolved.
- BLOCKED: sources or authority are insufficient to define safe expected behavior.

For new/consequential behavior, Extended approval of the exact Spec revision supplies the human acceptance checkpoint. Spec never chooses HOW or grants implementation permission.