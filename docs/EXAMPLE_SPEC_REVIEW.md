# Example — human-readable Spec review without edge-case inflation

**Illustrative request:** "Allow a project owner to rename a project." A real coding agent MUST inspect the actual project rules and ticket before creating these ACs. The following access and persistence contracts are only examples, not assumed universal requirements.

## Discovery and brainstorming (illustrative, no extra artifact required)

- **Intent — WHY:** inspect the actual request first. If “rename” could mean changing a **visible display name** or an immutable **identifier**, ask the owner via Coordinator only if the existing accepted context cannot distinguish them. Otherwise record `NO_MATERIAL_UNCERTAINTY` and proceed.
- **Spec — WHAT:** derive business rules from accepted behavior and verified authorization; a successful rename and denied unauthorized rename are candidate source-backed rules. Boundary input variants are VERIFY checks, not automatic new rules. Do not ask about arbitrary character length or bulk rename without a material reason.
- **Architect — HOW:** check whether the existing update service already supports name changes; reuse it if appropriate. Compare a new endpoint only if real compatibility/test seam/trust-boundary trade-offs make it consequential.
- **Human sees:** the concrete behavioral decisions to approve, not the agent's discarded brainstorm ideas. No separate `brainstorm.md` is generated.

## Human review card (example if both rules are source-backed)

**Outcome:** The owner can change a project's visible name without creating a new project.

**Behavior to approve** (linked to **full proposed Spec revision r2**):

| AC | What a human needs to know | Full source |
|---|---|---|
| AC-01 | Renaming saves the new name and it is shown after reopening the project | Ticket requirement, AC-01 r2 |
| AC-02 | Only an authorized project owner can rename the project | Verified existing access policy, AC-02 r2 |

**Not changing:** This work does not bulk-rename projects or translate existing names.

**Material risk:** Prevent unauthorized renames; verify that other project data is unchanged.

**Action requested:** Accept **AC-01 and AC-02, complete Spec r2**, or correct an inaccurate expected result. **This is not a code-edit grant.**

## Detail: normative ACs (in the existing ticket/authorized record)

- **AC-01 r2** — Given an authorized owner viewing an existing project, when they submit an accepted new name, then the project name is persisted and appears on the next load without changing its identity. **Source:** the owner-accepted rename request; independent acceptance is required for any additional validation rule.
- **AC-02 r2** — Given an actor without rename permission, when they attempt a rename through the supported interface, then the change is denied and the original name remains unchanged. **Source:** verified existing project authorization contract (only if actually evidenced).

## VERIFY tests, not additional ACs

- Successful change appears after reload (AC-01).
- Unauthorized request cannot mutate persisted name (AC-02).
- One known invalid-name representative for the **existing verified** naming rule, if one exists; otherwise don't invent a "must be 3–20 characters" requirement.
- Other callers or name references only if actual code and contracts show a meaningful compatibility risk.

## What is explicitly NOT generated

"Rename multiple projects", "automatically translate names", "offline rename queue", and "rename audit dashboard" are not new ACs just because an agent can imagine them. Any new business rule needs credible authority and, when consequential, an owner decision.

## Role handoff that human need not read

Developer receives AC-01/AC-02 complete text + accepted source r2 + actual repo paths + available test seam + bounded local edit authority (which an explicit scoped implement request may provide). Reviewer receives real current diff + tests + AC revision, and must verify both ACs and meaningful risks. Internal test details can be long; the human-facing card stays small.

## Test-first evidence (illustrative; not a claim that commands were run)

For a change to a profile-name endpoint, Developer chooses the existing endpoint integration seam. The first accepted AC requires persistence of the new name.

- RED: `pytest tests/test_profiles.py::test_update_name_persists -q` → FAIL: returned old name after update (expected mismatch).
- GREEN: the same command → PASS after a minimal authorized change.
- REFACTOR: only if necessary; same test and relevant regression pass.
- Reviewer separately verifies actual current source snapshot, AC proof, real TDD evidence and meaningful authorization checks. Do **not** mark these sample commands as actually run.

Ponytail, when explicitly installed and opted in, can suggest simpler reuse of an existing endpoint/service rather than a new abstraction. It cannot remove the accepted access-control check or regression test. When not selected, no Ponytail configuration is generated.
