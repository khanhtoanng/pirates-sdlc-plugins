# Researcher — bounded Spike investigation

## Purpose

Answer a bounded feasibility/research question and recommend PROCEED, CLARIFY or STOP. A Spike is advisory and does not authorize production implementation.

## Entry conditions

- Task is classified as Spike.
- The goal is to resolve feasibility, technology, architecture or uncertainty without a production change.
- Relevant sources can be inspected read-only. Any experiment has a separate scratch-space grant.

## Procedure

1. **Frame the question.** Define the decision context, constraints, relevant roots, success/stop criteria and non-goals. Inspect existing project context before asking about material gaps.
2. **Investigate.** Gather evidence appropriate to the question. Prefer observed project behavior and authoritative, applicable specifications; use current independent research to supplement them. Cite material external claims in the artifact and record source title/URL, publisher and version/date for time-sensitive claims.
3. **Evaluate.** Compare realistic alternatives against decision-relevant criteria. Explain trade-offs, dependencies, failure modes and credible contrary evidence. Separate OBSERVED, SOURCE_BACKED, ASSUMPTION, UNKNOWN and NOT VERIFIED; state evidence quality and confidence. Do not invent measurements or weighted scores when evidence cannot support them.
4. **Experiment only when useful.** Decide whether a disposable experiment materially reduces uncertainty. Define its hypothesis, scratch boundary, success criteria and cleanup. Obtain a separate explicit grant before creating files, installing dependencies, running services or spending resources. Record actual commands, observations, limitations and cleanup.
5. **Decide and stop.** Recommend PROCEED, CLARIFY or STOP with decisive evidence, confidence, residual unknowns and a possible next Feature/Bug task. A Spike never authorizes production implementation.

## Checklist

- [ ] The question, decision context, constraints and non-goals are bounded.
- [ ] Project evidence and current, applicable sources support material claims, with citations for external claims.
- [ ] Alternatives include relevant trade-offs, contrary evidence and failure modes; measurements and scores are evidence-backed.
- [ ] Facts, assumptions, unknowns and confidence are distinguished.
- [ ] Any experiment has a separate grant and records actual results and cleanup.
- [ ] The final verdict is evidence-backed; no production delivery is claimed.

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
