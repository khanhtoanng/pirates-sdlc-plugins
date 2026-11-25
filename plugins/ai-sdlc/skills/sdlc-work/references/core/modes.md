# Execution modes — Quick, Standard and Extended

Task type (Feature, Bug, Spike) determines **what workflow** runs. Mode (Quick, Standard, Extended) determines **how much process, evidence and human involvement** the workflow uses. Auto selects an effective mode; it is not an execution mode.

The same safety and correctness requirements apply to all modes. Modes change role depth, artifact detail and approval behavior. They never relax permissions, required verification or independent review.

## 1. Mode selection

After proportionate read-only inspection, choose the smallest mode justified by observed requirements and risk. Record requested mode, effective mode, reason, evidence and material unknowns.

| Dimension | Quick | Standard | Extended |
|---|---|---|---|
| Requirements | Known, bounded and source-backed | Some focused clarification or AC work is useful | Consequential new business rules, unresolved high-impact choices or owner requests full review |
| Design | Existing pattern; small and reversible | Moderate feature design or several components/interfaces | Significant architecture, critical dependency, breaking contract or complex rollout |
| Data | No material data risk | Compatible/reversible change | Destructive/irreversible migration, loss, privacy-sensitive data or recovery risk |
| Security | No material security impact | Routine safeguards | Authorization, privacy, compliance or security-critical behavior |
| Operations | Ordinary local changes | Multi-component delivery or normal coordination | High production/availability impact, privileged operation or irreversible infrastructure impact |
| Human involvement | Material questions and authority boundaries only | Consequential WHAT/HOW/scope decisions | Explicit approval after every applicable artifact stage |

Selection rules:

1. Explicit Extended always wins. Never downgrade it.
2. Escalate to Extended when any material high-risk trigger is evidenced, even if Quick or Standard was requested. Explain the trigger and pause before crossing a newly discovered consequential decision or permission boundary.
3. Quick is allowed only when all relevant risk dimensions are low, expected behavior is established and no substantial design decision is needed.
4. Standard is the default when Quick's criteria are not all met and Extended is not warranted.
5. Multiple repositories alone do not imply Extended. Assess actual contracts, risk and rollout complexity.
6. A consequential unknown is not low risk. Investigate read-only or ask the single most important question before editing.
7. Never lower the effective mode during a run without explicit human agreement and resolved risk.
8. For Spike, assess research/experiment risk separately. Mode selection never grants permission to edit production code or run an experiment.

## 2. Quick — minimum safe path

**Purpose:** Finish a small, clear, low-risk task with minimum ceremony.

- Run the minimum role path defined by the selected workflow.
- Reuse accepted requirements, existing contracts and established implementation patterns.
- Skip separate Intent, Spec or Architect work only when their decisions are already clear and no new analysis is needed.
- Do not create role-stage files by default. Return a concise chat result; use an existing ticket when useful.
- Do not stop after each role for approval.
- Ask only about material unknowns, scope changes, missing authority or blockers.
- Developer still implements and performs all applicable verification. TDD applies to behavior changes where a meaningful test seam exists; exceptions must be honest.
- Feature/Bug code changes still require a genuinely independent Reviewer before claiming AI_PASS.

Typical paths:
- Feature: Developer (understand established behavior → implement → verify) → Reviewer.
- Bug: Developer (bounded symptom check → straightforward diagnosis → fix → verify) → Reviewer. Escalate when reproduction, cause or risk is not simple.
- Spike: Researcher (bound question → focused research → decision); no production edits. Experiment requires a separate scratch grant.

Quick means less ceremony, not less correctness.

## 3. Standard — structured delivery, selective decisions

**Purpose:** Handle normal engineering work with clear reasoning, role ownership and evidence, without mandatory approval after every role.

- Run every applicable responsibility in the selected workflow, in order.
- Reuse accepted Intent/Spec material. Do not regenerate documents just to fill a role.
- Perform Intent when WHY, WHO, outcome or scope is materially unclear.
- Perform Spec when changed behavior lacks complete accepted ACs, or a Bug fix would introduce a new business rule. A new business rule must be accepted before implementation.
- Perform Architect for meaningful technical design, dependency mapping or non-trivial Bug diagnosis/plan. A small established change may use a lightweight design check within Developer.
- Developer implements and verifies. Reviewer independently checks code and evidence.
- Prefer an existing ticket/PR/ADR. Otherwise use one compact task record when continuity is needed. Do not create a file for every role by default.
- Ask for human decisions only for consequential WHAT/HOW/scope/risk/authority choices. Routine handoffs continue without approval.
- Plan/investigate/review requests are read-only. A bounded implement/fix request may authorize ordinary local edits only within its scope and subject to host/project policy.

Typical paths:
- Feature: Intent (if needed) → Spec (if needed) → Architect (if needed) → Developer → Reviewer.
- Bug: Architect (assessment + diagnosis + minimal fix plan) → Developer → Reviewer. A clearly reproduced, low-risk Bug may use the Quick Developer path.
- Spike: Researcher (scope + research + decision); optional experiment only with a separate explicit scratch grant.

## 4. Extended — full human-in-the-loop workflow

**Purpose:** Handle complex, consequential or explicitly human-supervised work. Every applicable artifact-producing stage is reviewed and approved before the next stage starts.

- Execute the complete applicable route in its defined order.
- Each role owns its numbered procedure and mandatory checklist. Complete the checklist before presenting the artifact.
- Generate only the current stage artifact with the exact ordinal filename defined by the selected workflow.
- Validate source/decision references and exit conditions. AI validation is not human approval.
- Persist state and artifact revision in one authorized task directory or existing tracker.
- Present a review card with task, stage, revision, artifact path, summary, decisions, risks, exclusions, evidence, checklist result and limitations.
- End the turn after presenting the card. Do not create downstream artifacts, start downstream work, poll or interpret silence as consent.
- Continue only after explicit approval of the exact current stage and revision.
- Material changes invalidate affected downstream approvals/evidence. Return to the earliest affected stage.
- Developer's implementation and verification are one stage and one artifact. Reviewer is a separate independent stage and artifact.

### Extended stage and artifact order

| Task | Stage ID | Owner | Artifact |
|---|---|---|---|
| Feature | intent | Intent | 01-intent.md |
| Feature | spec | Spec | 02-spec.md |
| Feature | plan | Architect | 03-plan.md |
| Feature | implementation | Developer (build + verify) | 04-implementation.md |
| Feature | review | Reviewer | 05-review.md |
| Bug | diagnosis_plan | Architect (assess + diagnose + plan) | 01-diagnosis-plan.md |
| Bug | implementation | Developer (fix + verify) | 02-implementation.md |
| Bug | review | Reviewer | 03-review.md |
| Spike | scope | Researcher | 01-scope.md |
| Spike | research | Researcher | 02-research.md |
| Spike | experiment_plan (optional) | Researcher | 03-experiment-plan.md |
| Spike | experiment (optional) | Researcher | 04-experiment.md |
| Spike | decision | Researcher | 05-decision.md |

For Spike without an experiment, mark both optional stages not_applicable with a reason. Do not create placeholder artifacts.

### Extended approval protocol

1. Run only the current stage. Load its role instructions and follow its numbered procedure.
2. Complete the role's mandatory checklist. An essential unmet item means BLOCKED or NEEDS_DECISION, not READY.
3. Create/update only the current stage artifact. Never create future-stage placeholders.
4. Persist state with current_stage, status awaiting_human_approval, artifact path, integer revision and relevant source/snapshot references.
5. Present a compact review card. The full artifact must be accessible.
6. End the turn. Do not begin the next stage, wait/poll or seek simulated approval from a worker.
7. On the next user turn, reload the exact state/artifact. Recheck revision, sources, permission scope and snapshot freshness.
8. Accept approval only for the current stage and exact revision (for example, approve spec r1). Record the human response/reference and time when available.
9. Request changes: revise the same stage, increment revision, rerun its checklist and request approval again. Reject: stop as cancelled. Ambiguous response: clarify; do not advance.
10. After approval, start only the next applicable stage. Plan approval does not grant extra edit or privileged-operation authority.
11. Material changes to source, requirements, scope, plan or code invalidate affected downstream approvals/evidence. Return to the earliest affected stage. Do not reapprove unchanged unaffected artifacts.
12. Developer verification failure blocks the Developer stage. Reviewer findings block review completion. Any material repair requires Developer re-verification and fresh independent review. Escalate after at most three AI repair/review cycles.
13. Final Reviewer approval completes workflow evidence; it does not authorize merge, production migration or deployment.

### State and durable records

Prefer an existing authorized issue, PR, ADR or tracker with revisioned stage sections. Otherwise ask once for permission to use one task directory in one selected writable root. The exact files depend on the route:

Feature: state.json, 01-intent.md, 02-spec.md, 03-plan.md, 04-implementation.md, 05-review.md.
Bug: state.json, 01-diagnosis-plan.md, 02-implementation.md, 03-review.md.
Spike: state.json, 01-scope.md, 02-research.md, optional 03-experiment-plan.md and 04-experiment.md, 05-decision.md.

state.json must include:
- schema_version, task_id, task_type, requested_mode, mode and mode_reason;
- current_stage, top-level status and stages map keyed by the stage IDs for the selected route;
- each stage status, integer revision, artifact path/section, evidence and approval reference;
- request/source references, repository roots, edit scope, baseline/changed snapshots and material decisions;
- approval record containing exact stage revision, human response/reference and timestamp when available.

Allowed stage statuses: pending, in_progress, awaiting_human_approval, approved, blocked, needs_decision, cancelled, invalidated, not_applicable. State and stage statuses must agree. Update state before returning control. If durable persistence fails, report HANDOFF: NOT DURABLE with a pasteable handoff; do not claim reliable resume. On resume, refresh sources, permissions and Git snapshots before continuing.

## 5. Safety and evidence invariants across all modes

- Never equate visible repositories with approved edit roots. Distinguish VISIBLE, RELEVANT, EDIT_APPROVED and EXCLUDED.
- Preserve staged, unstaged and untracked user work. A snapshot must account for dirty changes, not HEAD alone.
- Distinguish OBSERVED, SOURCE_BACKED, OWNER_ACCEPTED, PROPOSED, ASSUMPTION, UNKNOWN, NOT RUN and NOT VERIFIED.
- No role approves a human decision, grants its own authority or invokes a downstream role autonomously.
- Do not fabricate test output, reproduction, approval, reviewer independence or host capabilities.
- An explicit implement/fix request may authorize ordinary local edits within its bounded scope, subject to project and host permissions. It does not authorize destructive operations, installs, secrets access, remote/cloud changes, commit/push/merge, production migrations or deployment.
- Spike is research/advisory by default. Any POC needs an explicit bounded scratch grant. Never convert a Spike into production implementation without a new Feature/Bug task and authorization.