# Spike workflow

A Spike answers a bounded feasibility, research or architecture question without committing to production implementation. Researcher owns Scope → Research → optional Experiment Plan → optional Experiment → Decision.

## Role sequence and mode applicability

| Order | Researcher stage | Quick | Standard | Extended |
|---|---|---|---|---|
| 1 | Scope | Bound the question in the answer | Define question, constraints and success/stop criteria | Create and approve 01-scope.md |
| 2 | Research | Focused evidence and recommendation | Compare viable options and contrary evidence | Create and approve 02-research.md |
| 3 | Experiment Plan | Skip unless research shows a POC is necessary | Optional; separate scratch grant required | Optional 03-experiment-plan.md, approved before execution |
| 4 | Experiment | Optional, separately authorized | Optional, separately authorized | Optional 04-experiment.md; execute only after plan approval/grant |
| 5 | Decision | Concise PROCEED, CLARIFY or STOP | Decision brief and recommended next task | Create and approve 05-decision.md |

A mode never grants permission to modify production code or run an experiment. If production implementation is recommended, end the Spike and request a new Feature/Bug task with its own scope and authority.

## Extended artifacts

- 01-scope.md
- 02-research.md
- 03-experiment-plan.md (optional)
- 04-experiment.md (optional)
- 05-decision.md

Use stage IDs scope, research, experiment_plan, experiment and decision. If no experiment is needed or authorized, mark both optional stages not_applicable in state with a reason and do not create placeholder artifacts. Each applicable stage follows the Extended approval protocol in core/modes.md.

## Researcher procedure

1. Bound one answerable question, context, constraints, relevant roots, success/exit evidence, effort budget if supplied and explicit non-goals.
2. Inspect current architecture, code contracts, project docs and prior decisions before asking questions. Ask only about material missing constraints.
3. Research reliable sources and practical options. Compare costs, trade-offs, dependencies, failure modes and contrary evidence.
4. Label OBSERVED, SOURCE_BACKED, ASSUMPTION, UNKNOWN and NOT VERIFIED correctly. Cite fresh sources for current/niche external claims.
5. Decide whether an experiment would materially reduce uncertainty. If useful, propose a disposable scratch-only experiment with hypothesis, scope, success criteria, cleanup and prohibited actions.
6. Obtain a separate explicit grant before creating files, installing dependencies, running services or spending resources.
7. Run only an approved experiment inside its scratch boundary. Record actual commands, observations, outputs, limitations and cleanup; never promote scratch code to production.
8. Recommend PROCEED, CLARIFY or STOP with confidence, supporting/contrary evidence, residual unknowns and a possible next Feature/Bug task.
9. Stop. PROCEED is advisory, not implementation authorization; no automatic Developer or Reviewer chain.

For Quick/Standard, return one focused answer/decision brief rather than separate stage files.