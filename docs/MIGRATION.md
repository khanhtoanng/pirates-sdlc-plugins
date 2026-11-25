# Migration guide

## From v0.7.0 to consolidated mode/role layout

This change simplifies workflow ownership without changing host packaging or requiring project-level harness files.

- Extended approval, pause/resume, revision and invalidation rules move from core/human-gates.md into core/modes.md.
- Generic role rules move out of roles/shared.md. Each role file becomes self-contained with its own purpose, entry conditions, numbered procedure, checklist, output and exit conditions.
- Feature Extended changes from six artifacts to five: 01-intent.md, 02-spec.md, 03-plan.md, 04-implementation.md, 05-review.md. Developer's artifact includes verification evidence; verification.md and the standalone Verification stage are removed.
- Bug uses Architect's 01-diagnosis-plan.md, Developer's 02-implementation.md (fix + verification), then Reviewer 03-review.md.
- Spike retains Researcher-owned scope, research, optional scratch experiment plan/experiment and decision.
- No Verifier role is introduced. Developer verifies; Reviewer independently inspects code and evidence.

Replace the installed plugin and reload each host. Do not automatically rewrite existing project files.

### Existing Extended task records

Prior task directories may contain stage IDs and filenames from the previous layout. Do not rename or reinterpret approvals silently. When resuming an older task, detect the old stage schema and either continue using its original record under an explicit legacy mapping or ask the owner to migrate it. A previous approval is never approval of a different artifact/revision.

Update the validator and eval harness with the new stage/artifact maps. Run python3 tests/validate.py, python3 tests/evals/score.py --self-test and python3 tests/evals/test_grade.py, then run actual host evaluations. Static validation is not proof of host behavior.