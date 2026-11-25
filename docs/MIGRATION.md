# Migration guide

## From 0.7.0 to 0.8.0

This release consolidates mode policy and role ownership without changing host packaging.

- Extended approval, pause/resume, revision and invalidation policy is consolidated in core/modes.md.
- Each role instruction owns its procedure, checklist, output and exit conditions.
- Feature Extended uses 01-intent.md, 02-spec.md, 03-plan.md, 04-implementation.md and 05-review.md. Developer's artifact includes verification evidence.
- Bug Extended uses 01-diagnosis-plan.md, 02-implementation.md and 03-review.md.
- Spike keeps Researcher-owned scope, research, optional scratch experiment and decision stages.

Replace the installed plugin and reload the host. Existing project files are not rewritten automatically.

## Existing Extended task records

Do not silently rename old stage IDs or treat an earlier approval as approval of a different artifact. When resuming an older task, continue with its original record under an explicit legacy mapping or ask the owner to migrate it.

Run `python3 tests/validate.py`, `python3 tests/evals/score.py --self-test` and `python3 tests/evals/test_grade.py`, then run opt-in host evaluations. Static validation does not prove host behavior.
