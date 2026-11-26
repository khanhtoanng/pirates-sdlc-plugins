# Execution modes

Task type (Feature, Bug or Spike) selects the workflow. Mode (Quick, Standard or Extended) selects its depth and human approval. Auto selects a mode; it is not a mode itself.

All modes retain the same permissions, verification and independent-review requirements.

## 1. Select a mode

After proportionate read-only inspection, choose the smallest mode justified by the evidence. Record requested/effective mode, reason, risk drivers and material unknowns.

| Signal | Quick | Standard | Extended |
|---|---|---|---|
| Requirements | Established and bounded | Focused clarification or AC work | New consequential rules or unresolved high-impact choices |
| Design | Existing pattern, reversible | Moderate design or several components | Critical dependencies, breaking contracts or complex rollout |
| Data/security | No material impact | Routine safeguards | Irreversible data, privacy, compliance or security risk |
| Operations | Ordinary local change | Multi-component delivery | High production or infrastructure impact |
| Human review | Material questions only | Consequential decisions | Approval after every applicable artifact stage |

Selection rules:

1. Explicit Extended always wins.
2. Escalate when evidence shows material high risk, even if Quick or Standard was requested. Explain why and pause at a new consequential decision or permission boundary.
3. Quick requires low risk, established expected behavior and no substantial design decision.
4. Otherwise choose Standard unless Extended is warranted.
5. Multiple repositories alone do not imply Extended; assess actual integration and rollout risk.
6. A consequential unknown is not low risk. Investigate read-only or ask the most important question before editing.
7. Do not downgrade a run without human agreement and resolved risk.
8. For Spike, assess research and experiment risk separately; mode never grants production-edit or experiment authority.

## 2. Quick — minimum safe path

Use for clear, low-risk work with an established approach.

- Follow the minimum role path in the selected workflow; reuse accepted requirements and contracts.
- Skip separate Intent, Spec or Architect work only when its decisions are already clear.
- Create no stage files or per-role approvals by default; return a concise result.
- Ask only about material unknowns, scope, authority or blockers.
- Developer still implements and verifies. Apply TDD where a meaningful test seam exists; record exceptions.
- Feature/Bug code changes still need a genuinely independent Reviewer before AI_PASS.

Typical paths:
- Feature: Developer → Reviewer.
- Bug: Developer triage, fix and verify → Reviewer; escalate unclear reproduction, cause or risk.
- Spike: Researcher scope, research and decision. No production edits; experiments need a separate scratch grant.

Any durable record explicitly requested for a Quick task must use the canonical task directory in section 6.

Less ceremony does not mean less correctness.

## 3. Standard — structured delivery

Use for normal engineering work that needs analysis or coordination but not approval after every role.

- Run each applicable workflow responsibility in order; reuse accepted Intent and Spec material.
- Perform Intent when problem, user, outcome or scope is unclear.
- Perform Spec when accepted ACs are incomplete or a Bug fix needs a new business rule.
- Perform Architect for meaningful design, dependency mapping or non-trivial Bug diagnosis. Small established changes may use a lightweight design check within Developer.
- Developer implements and verifies; Reviewer independently checks code and evidence.
- Create one compact `task.md` under the canonical task directory when continuity is needed, including multi-repository coordination, cross-session resume or an explicit user request.
- Ask for consequential WHAT, HOW, scope, risk or authority decisions. Routine handoffs do not need approval.
- Plan, research and review requests are read-only. A bounded implement/fix request may authorize ordinary local edits within scope and host policy.

Typical paths:
- Feature: Intent? → Spec? → Architect? → Developer → Reviewer.
- Bug: Architect → Developer → Reviewer; clear low-risk Bugs may use the Quick path.
- Spike: Researcher scope → research → decision; experiment requires a separate scratch grant.

## 4. Extended — approval at every stage

Run the complete applicable workflow. Each stage completes its role checklist, writes one artifact and pauses for approval of that exact revision.

- Create the task directory and `state.json` under `.sdlc/changes/<task-id>/` in one selected, authorized task-home root before beginning the first stage.
- Create only the current stage artifact, using the filename in the workflow table.
- Validate source references and exit conditions before presenting the artifact.
- Persist stage state and revision in `state.json` before every human handoff.
- Present a review card with stage, revision, artifact path, decisions, evidence, checklist result, risks and the next human action.
- End the turn. Do not start downstream work, poll or interpret silence as consent.
- Continue only after explicit approval of the current stage and revision.
- A material upstream change invalidates affected downstream approvals/evidence; return to the earliest affected stage.
- Developer's implementation and verification are one stage. Reviewer is a separate independent stage.

The task-record permission is separate from source-code edit permission. If the selected task home is not writable or record creation is not authorized, ask for an authorized task home/write grant or report `HANDOFF: NOT DURABLE`. Do not use an external tracker, host state or another folder as a silent fallback.

### Stage and artifact map

| Task | Stage | Owner | Artifact |
|---|---|---|---|
| Feature | intent | Intent | 01-intent.md |
| Feature | spec | Spec | 02-spec.md |
| Feature | plan | Architect | 03-plan.md |
| Feature | implementation | Developer | 04-implementation.md |
| Feature | review | Reviewer | 05-review.md |
| Bug | diagnosis_plan | Architect | 01-diagnosis-plan.md |
| Bug | implementation | Developer | 02-implementation.md |
| Bug | review | Reviewer | 03-review.md |
| Spike | scope | Researcher | 01-scope.md |
| Spike | research | Researcher | 02-research.md |
| Spike | experiment_plan (optional) | Researcher | 03-experiment-plan.md |
| Spike | experiment (optional) | Researcher | 04-experiment.md |
| Spike | decision | Researcher | 05-decision.md |

For a Spike without an experiment, mark both optional stages not_applicable with a reason. Do not create placeholders.

### Approval and resume protocol

1. Run only the current stage and follow its role instructions.
2. Complete the role checklist. An essential unmet item is BLOCKED or NEEDS_DECISION.
3. Create/update only the current artifact and increment its revision when changed.
4. Persist state as awaiting_human_approval with the stage, revision, artifact path and source/snapshot references.
5. Present the review card and end the turn.
6. On the next turn, reload the exact state and artifact. Recheck revision, sources, scope, permissions and snapshot freshness.
7. Accept approval only for the current stage and exact revision (for example, “approve spec r1”). Record the response/reference and time when available.
8. For requested changes, revise the same artifact, increment revision, rerun the checklist and request approval again. Rejection cancels the task; ambiguity requires clarification.
9. After approval, run only the next applicable stage. Plan approval does not grant extra edit or privileged-operation authority.
10. A material change to source, requirements, scope, plan or code invalidates affected downstream evidence. Do not reapprove unaffected stages.
11. Developer verification failure blocks the stage. A repair requires Developer re-verification and fresh independent review. Escalate after at most three repair/review cycles.
12. Final Reviewer approval completes workflow evidence; it does not authorize merge, production migration or deployment.

### Durable state and canonical location

All durable plugin-generated task records use this location relative to one selected task-home root:

```text
.sdlc/changes/<task-id>/
```

- Quick: no record by default; if one is explicitly requested, use this path.
- Standard: one compact `task.md` in this path when continuity is needed.
- Extended: mandatory `state.json` and applicable stage artifacts in this path.

External issues, tickets, PRs and ADRs may be recorded as source references. They must not replace the local record or hold a competing copy of its state. Multi-repository work has one task directory in one selected workspace/primary root, not a copy in every repository.

Use a short, lowercase, filesystem-safe task ID with hyphens. Check for collisions before creating the directory; never overwrite an existing task. The Coordinator creates the directory and passes its canonical path to all roles.

The `state.json` schema (v1) records:
- `schema_version`, `task_id`, `task_type`, `requested_mode`, `mode` and `mode_reason`.
- `current_stage`, top-level `status` and a `stages` map keyed by the selected route's stage IDs.
- Each stage's `status`, integer `revision`, artifact path/section, evidence and approval record.
- `request_ref`, source references, repository roots, edit scope, baseline/changed snapshots and material decisions.
- Each approval's exact stage/revision, human response or reference, and timestamp when available.

Stage status is one of: pending, in_progress, awaiting_human_approval, approved, blocked, needs_decision, cancelled, invalidated or not_applicable. Keep top-level and stage status consistent. Update state before handoff. If persistence fails, report HANDOFF: NOT DURABLE and provide a pasteable handoff; do not claim reliable resume.

## 5. Cross-mode safety

Follow the state, permission and evidence invariants in references/core/runtime.md. Mode selection never expands edit scope, grants privileged actions or allows a Spike to become production implementation.
