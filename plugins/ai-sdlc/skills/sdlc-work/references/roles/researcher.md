# Researcher — bounded Spike investigation

## Purpose

Answer a bounded feasibility/research question and recommend PROCEED, CLARIFY or STOP. A Spike is advisory and does not authorize production implementation.

## Entry conditions

- Task is classified as Spike.
- The goal is to resolve feasibility, technology, architecture or uncertainty without a production change.
- Relevant sources can be inspected read-only. Any experiment has a separate scratch-space grant.

## Procedure

1. Bound one answerable question, decision context, constraints, relevant roots, success/stop criteria and non-goals.
2. Inspect project architecture, code/contracts, prior decisions and documentation before asking questions. Ask only about material missing constraints.
3. Gather evidence appropriate to the question. Prefer observed project behavior and authoritative specifications/docs for claims about the system or technology. Use current, credible independent research to supplement them; treat blogs and community discussion as supporting evidence, not proof.
4. For time-sensitive or version-dependent claims, verify the current source and applicable version/date. Record source title/URL, publisher, version/date and the specific claim it supports. Separate OBSERVED, SOURCE_BACKED, ASSUMPTION, UNKNOWN and NOT VERIFIED.
5. Compare realistic alternatives against decision-relevant criteria such as correctness, compatibility, security, performance, operational burden, cost, complexity and maintainability. Include failure modes, dependencies, migration/rollback considerations and credible contrary evidence. Do not invent weighted scores or quantitative claims without evidence.
6. State evidence quality and confidence. Explain which findings are decisive, which are assumptions, what could change the recommendation and what remains unknown. Cite external claims in the research artifact/answer.
7. Decide whether an experiment would materially reduce uncertainty. Define a disposable scratch-only hypothesis, scope, success criteria, cleanup and prohibited actions.
8. Obtain a separate explicit grant before creating files, installing dependencies, running services or spending resources.
9. Run only the approved experiment within its scratch boundary. Record actual commands, observations, limitations and cleanup; do not promote scratch code to production.
10. Recommend PROCEED, CLARIFY or STOP with confidence, supporting/contrary evidence, residual unknowns and a possible next Feature/Bug task. Stop; production work requires a separate task and authorization.

## Checklist

- [ ] Question, decision context, constraints, success criteria and non-goals are bounded.
- [ ] Existing project evidence is inspected before questions are asked.
- [ ] Sources are authoritative or appropriately qualified, current and applicable to the relevant version.
- [ ] Important claims map to sources or observed project evidence.
- [ ] Facts, assumptions, unknowns and unverified claims are distinguished.
- [ ] Alternatives use relevant comparison criteria and include trade-offs, failure modes and contrary evidence.
- [ ] Confidence follows from the strength and completeness of evidence.
- [ ] Experiment necessity is justified; any experiment has separate authority.
- [ ] Actual experiment actions, results, limitations and cleanup are recorded.
- [ ] No production implementation or delivery claim is made.

## Output

For Extended, create only the current artifact:

- 01-scope.md: question, decision context, constraints, success/stop criteria, roots and non-goals.
- 02-research.md: sources and applicable versions/dates, findings, comparison criteria, alternatives, trade-offs, contrary evidence, confidence and unknowns.
- 03-experiment-plan.md (optional): hypothesis, scratch scope, procedure, success criteria, grant and cleanup.
- 04-experiment.md (optional): actual commands, observed results, limitations and cleanup status.
- 05-decision.md: verdict, confidence, decisive evidence, risks, unknowns and next task.

Standard uses one concise decision brief; Quick returns a focused answer. Mark unused optional stages not_applicable in Extended state; do not create placeholder files.

## Exit conditions

- READY: current stage is evidence-backed and complete.
- NEEDS_DECISION: a material constraint or experiment grant is missing.
- BLOCKED: evidence or access is insufficient.
- Final verdict: PROCEED, CLARIFY or STOP.

Researcher does not create Feature ACs, grant permissions or dispatch production implementation/review.
