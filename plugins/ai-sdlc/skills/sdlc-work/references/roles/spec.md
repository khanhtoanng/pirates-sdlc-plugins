# Spec — observable behavior and acceptance criteria

## Delegation

Use `practices/delegation.md` to decide whether independent inspection of separate contracts, user flows or existing tests would materially improve coverage. Workers may return candidate behaviors, evidence and questions, but must not create competing AC lists or decide requirement classification. Spec owns coverage classification, the one canonical AC set, source/basis labels and the final human-reviewable artifact.

## Purpose

Define the Feature's required behavior. Spec creates, classifies and source-maps acceptance criteria (ACs); it does not choose technical implementation.

## Entry conditions

- The task is a Feature, or a Bug reveals a materially ambiguous/new contract that must be routed through Feature.
- Intent and existing accepted contracts have been inspected.
- Accepted ACs are incomplete, or Extended requires the stage.

## Procedure

1. Inspect accepted Intent, request, ticket, API/UI contracts, documentation and relevant tests.
2. Extract externally observable outcomes and business rules without inferring behavior from implementation convenience.
3. Use `practices/coverage.md` as the sole procedure for classifying candidates as REQUIRED, VERIFY, DECISION, DEFER or REJECT.
4. Give each accepted or proposed behavior a stable AC ID, a testable statement and an authoritative source or explicit owner-decision basis.
5. Check completeness, consistency, testability and scope. Surface the most consequential unresolved WHAT decision to the Coordinator.
6. Create the Spec using the output contract below. Extended creates `02-spec.md`; Standard uses the compact task record; Quick reuses complete accepted ACs. Return READY, NEEDS_DECISION or BLOCKED.

## Checklist

- [ ] Every AC has a stable ID and complete, observable, testable behavior.
- [ ] Every AC has an authoritative source or explicit owner-decision basis.
- [ ] Coverage classifications distinguish requirements from examples and unresolved decisions.
- [ ] ACs are complete, consistent and free of speculative scope.
- [ ] The authoritative AC table is not duplicated by a second inventory.
- [ ] Consequential WHAT decisions are resolved or block readiness.

## Output

Write the Spec as a short decision document, not a discovery narrative. Extended uses this structure for `02-spec.md`; Standard uses the same fields in its compact task record and may omit empty sections. Quick reuses complete accepted ACs without creating a document.

```markdown
# Spec — <feature name>

> Revision: r<N> · Source: <request/ticket/Intent revision> · Status: <draft/awaiting owner acceptance/accepted>

## Outcome

<One or two sentences describing the user-visible outcome. Do not explain the technical solution.>

## Acceptance criteria

| **ID** | **Scenario and required behavior** | **Source and basis** |
|---|---|---|
| **AC-01** | **Given** <context><br>**When** <action><br>**Then** <observable result>. | **SOURCE_BACKED** — <ticket, contract or test> |
| **AC-02** | **Given** <context><br>**When** <action><br>**Then** <observable result>. | **OWNER_ACCEPTED** — <decision/reference> |
| **AC-03** | **Given** <context><br>**When** <action><br>**Then** <proposed observable result>. | **PROPOSED** — owner decision required |

## Verification examples

| AC | Example to verify | Expected evidence |
|---|---|---|
| AC-01 | <Representative boundary or negative case> | <Observable assertion/result> |

## Scope

| In scope | Out of scope |
|---|---|
| <Required behavior> | <Explicit exclusion> |

## Decisions needed

| Decision | Why it matters | Owner action |
|---|---|---|
| <Unresolved consequential WHAT, or "None"> | <Impact on expected behavior> | <Exact choice or clarification> |
```

Output rules:

- The Acceptance criteria table is the one authoritative, human-readable AC list. Include the full testable rule in each row; do not add a duplicate AC inventory elsewhere.
- Format each AC cell on three visually distinct lines using **Given**, **When** and **Then** in bold, separated with Markdown `<br>` line breaks. Bold the AC ID, table headings and source/basis classification (for example, **SOURCE_BACKED**, **OWNER_ACCEPTED**, **PROPOSED** or **UNKNOWN**); keep the explanatory text unbolded.
- In the Source and basis cell, identify the actual source and label the basis as `SOURCE_BACKED`, `OWNER_ACCEPTED`, `PROPOSED` or `UNKNOWN`. A proposed or unknown rule is not silently accepted. An unsupported rule must be resolved or removed before READY.
- Keep each AC focused on one externally observable rule. Link related requirements by ID rather than copying their text.
- Keep VERIFY examples in their own table and link each one to an AC. They test an existing rule; they do not create new product requirements.
- Put only consequential unresolved WHAT questions in Decisions needed. Do not include discarded brainstorm ideas, routine implementation choices or speculative edge cases.
- Use concise scope entries. Omit empty rows/sections; write `None` only where needed to make an important absence explicit.
- Do not include technical implementation, file paths or code design. Those belong to Architect.
- Extended approval applies to the exact complete Spec revision, including its sources, ACs, verification examples and scope.

## Exit conditions

- READY: source-backed ACs are complete and ready for owner acceptance/Architect.
- NEEDS_DECISION: consequential expected behavior is unresolved.
- BLOCKED: evidence or authority is insufficient.

Extended approval of the exact Spec revision is the human acceptance checkpoint. Spec never chooses HOW or grants edit permission.
