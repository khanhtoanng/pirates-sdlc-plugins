# Spike workflow

A Spike answers a bounded feasibility, research or architecture question without committing to production implementation. Researcher owns Scope → Research → optional Experiment Plan → optional Experiment → Decision.

## Role sequence by mode

| Stage | Quick | Standard | Extended |
|---|---|---|---|
| Scope | Bound the question in the answer | Define question, constraints and success/stop criteria | Create and approve 01-scope.md |
| Research | Focused evidence and recommendation | Compare options and contrary evidence | Create and approve 02-research.md |
| Experiment plan | Skip unless a POC is useful | Optional; separate scratch grant | Optional 03-experiment-plan.md; approve before execution |
| Experiment | Optional; separately authorized | Optional; separately authorized | Optional 04-experiment.md; run after approval/grant |
| Decision | PROCEED, CLARIFY or STOP | Decision brief and next task | Create and approve 05-decision.md |

Mode never grants permission to edit production code or run an experiment. Production implementation requires a separate Feature/Bug task.

## Extended artifacts

- 01-scope.md
- 02-research.md
- 03-experiment-plan.md (optional)
- 04-experiment.md (optional)
- 05-decision.md

Use stage IDs scope, research, experiment_plan, experiment and decision. Persist `state.json` and applicable artifacts in the canonical `.sdlc/changes/<task-id>/` directory selected by the Coordinator. Link external issues or ADRs as source references rather than alternate plugin-state stores. Mark unused optional stages not_applicable in state with a reason; do not create placeholders.

## Researcher handoff

1. Bound the question, constraints, roots, success criteria and non-goals.
2. Inspect current architecture, code contracts and prior decisions before asking questions.
3. Compare realistic options, costs, trade-offs, dependencies, failure modes and contrary evidence.
4. Label facts, assumptions and unknowns; cite current sources for fresh external claims.
5. Propose a disposable scratch experiment only when it materially reduces uncertainty. Define hypothesis, scope, success criteria and cleanup.
6. Obtain a separate grant before creating files, installing dependencies, running services or spending resources.
7. Record actual experiment commands, results, limitations and cleanup.
8. Return PROCEED, CLARIFY or STOP with confidence, evidence, residual unknowns and a possible next task.

PROCEED is advisory. A Spike ends with a decision, not production delivery or an automatic Developer/Reviewer chain.
