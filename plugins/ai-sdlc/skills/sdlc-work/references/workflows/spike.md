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

Researcher owns the investigation, evidence evaluation, optional experiment and decision procedures in `roles/researcher.md`. This workflow owns stage order, mode applicability and artifact names; it does not restate the role procedure.

Experiment planning and execution are optional. Both require a separate explicit grant before creating files, installing dependencies, running services or spending resources. A Spike ends with PROCEED, CLARIFY or STOP and never dispatches Developer/Reviewer for production delivery.
