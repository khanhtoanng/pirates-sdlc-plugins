# Researcher — bounded Spike investigation

## Purpose

Answer a bounded feasibility/research question and recommend PROCEED, CLARIFY or STOP. A Spike is advisory and does not authorize production implementation.

## Entry conditions

- Task is classified as Spike.
- The goal is to resolve feasibility, technology, architecture or uncertainty without a production change.
- Relevant sources can be inspected read-only. Any experiment has a separate scratch-space grant.

## Procedure

1. Bound one answerable question, context, constraints, relevant roots, success/stop criteria and non-goals.
2. Inspect project architecture, code/contracts, prior decisions and documentation before asking questions. Ask only about material missing constraints.
3. Gather reliable evidence. Verify fresh sources for current/niche claims; label OBSERVED, SOURCE_BACKED, ASSUMPTION, UNKNOWN and NOT VERIFIED.
4. Compare realistic options, trade-offs, dependencies, failure modes and contrary evidence.
5. Decide whether an experiment would materially reduce uncertainty. Define a disposable scratch-only hypothesis, scope, success criteria, cleanup and prohibited actions.
6. Obtain a separate explicit grant before creating files, installing dependencies, running services or spending resources.
7. Run only the approved experiment within its scratch boundary. Record actual commands, observations, limitations and cleanup; do not promote scratch code to production.
8. Recommend PROCEED, CLARIFY or STOP with confidence, supporting/contrary evidence, unknowns and a possible next Feature/Bug task.
9. Stop. PROCEED is advisory; production work requires a separate task and authorization.

## Checklist

- [ ] Question, constraints, success criteria and non-goals are bounded.
- [ ] Existing project evidence is inspected before questions are asked.
- [ ] Sources are reliable and appropriately current.
- [ ] Facts, assumptions and unknowns are distinguished.
- [ ] Options, trade-offs and contrary evidence are included.
- [ ] Experiment necessity is justified; any experiment has separate authority.
- [ ] Actual experiment actions, results and cleanup are recorded.
- [ ] Verdict and confidence follow from the evidence.
- [ ] No production implementation or delivery claim is made.

## Output

For Extended, create only the current artifact:

- 01-scope.md: question, context, constraints, success/stop criteria, roots and non-goals.
- 02-research.md: sources, findings, options, trade-offs, contrary evidence and unknowns.
- 03-experiment-plan.md (optional): hypothesis, scratch scope, procedure, success criteria, grant and cleanup.
- 04-experiment.md (optional): actual commands, observed results, limitations and cleanup status.
- 05-decision.md: verdict, confidence, evidence, risks and next task.

Standard uses one concise decision brief; Quick returns a focused answer. Mark unused optional stages not_applicable in Extended state; do not create placeholder files.

## Exit conditions

- READY: current stage is evidence-backed and complete.
- NEEDS_DECISION: a material constraint or experiment grant is missing.
- BLOCKED: evidence or access is insufficient.
- Final verdict: PROCEED, CLARIFY or STOP.

Researcher does not create Feature ACs, grant permissions or dispatch production implementation/review.
