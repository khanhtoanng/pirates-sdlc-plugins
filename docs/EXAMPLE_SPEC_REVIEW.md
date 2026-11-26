# Example — human-readable Spec review without edge-case inflation

**Illustrative request:** "Allow a project owner to rename a project." A real coding agent must inspect the actual project rules and ticket before creating these ACs. The access and persistence contracts below are examples, not assumptions about every project.

## Discovery (no extra artifact required)

- **Intent — WHY:** distinguish a visible display name from an immutable identifier. Ask the owner only if accepted context cannot resolve the difference.
- **Spec — WHAT:** derive required behavior from the request and verified authorization. Boundary inputs are VERIFY examples, not automatic new ACs.
- **Architect — HOW:** inspect whether the existing update service supports the change. Do not choose an implementation in the Spec.
- **Human sees:** the proposed outcome, complete AC table, source/basis, scope and consequential decisions — not discarded brainstorm ideas.

## Example `02-spec.md`

> Revision: r2 · Source: owner-accepted rename request · Status: awaiting owner acceptance

### Outcome

A project owner can change a project's visible name without creating a new project or changing its identity.

### Acceptance criteria

| ID | Scenario and required behavior (Given / When / Then) | Source and basis |
|---|---|---|
| AC-01 | Given an authorized owner viewing an existing project, when they submit an accepted new name, then the name is persisted and appears on the next load without changing project identity. | OWNER_ACCEPTED — rename request, r2 |
| AC-02 | Given an actor without rename permission, when they attempt a rename through the supported interface, then the change is denied and the original name remains unchanged. | SOURCE_BACKED — existing authorization contract; confirm actual evidence before use |

AC-02 is only valid when the project actually has this verified authorization contract. If it is not evidenced, mark it PROPOSED and obtain an owner decision instead.

### Verification examples

| AC | Example to verify | Expected evidence |
|---|---|---|
| AC-01 | Reload the project after a successful rename. | New name is displayed; project identity is unchanged. |
| AC-02 | Attempt rename without permission. | Request is denied; persisted name is unchanged. |
| AC-01 | Try one representative invalid name under the existing verified naming rule. | Existing validation behavior is preserved. Do not invent a length or character rule. |

### Scope

| In scope | Out of scope |
|---|---|
| Change the visible project name | Bulk rename, automatic translation, offline rename queue, rename audit dashboard |

### Decisions needed

None, provided the sources above are verified and accepted.

**Human action:** accept the complete Spec revision r2 or request a correction. Acceptance is not a code-edit grant.

## Handoff

Developer receives the complete accepted ACs, source revision, actual repository paths from Architect, test seams and bounded edit scope. Reviewer receives the actual diff, tests and the same AC revision. Neither role should invent additional product rules.

## What is deliberately omitted

Do not produce a second AC summary repeating the full table, a standalone brainstorming artifact, speculative input permutations or routine implementation questions. The table above is the authoritative AC list.

Ponytail, when explicitly installed and opted in, may suggest reusing an existing endpoint/service. It cannot remove an accepted authorization rule or regression test.
