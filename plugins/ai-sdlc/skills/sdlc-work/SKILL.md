---
name: sdlc-work
description: Coordinate SDLC feature delivery, bug diagnosis/fix, or bounded technical feasibility research in one or multiple repositories. Auto-select Quick, Standard or Extended; Extended requires approval after every applicable artifact stage. Use for scoped engineering work, not unrelated explanations or general Q&A.
argument-hint: "[feature|bug|spike] [auto|quick|standard|extended] <request> [selected roots] | resume <task-id or record>"
---

# AI SDLC work — router and coordinator

## Purpose

Execute the SDLC from this installed plugin. Do not bootstrap or duplicate agent/role files in the project. One Coordinator owns routing, mode selection, task state, permissions and handoffs.

Roles are logical responsibilities, not automatically separate native subagents:
- Feature: Intent, Spec, Architect, Developer, Reviewer.
- Bug: Architect, Developer, Reviewer.
- Spike: Researcher.

Developer owns implementation and verification. There is no separate Verifier role or Verification stage. Reviewer independently checks code and Developer's verification evidence.

## Start and route

1. Read references/core/routing.md, references/core/modes.md and references/core/runtime.md.
2. Inspect the request, source/ticket, relevant repository roots, project instructions, risk and Git state proportionately. Classify task type and requested/effective mode independently. Auto is a selector, not an execution mode.
3. State task type, requested/effective mode, reason, scope and relevant risk drivers. Emit SDLC_ROUTE: task_type=<feature|bug|spike>; mode=<quick|standard|extended> for an activated SDLC task.
4. Read only the selected workflow: references/workflows/feature.md, bug.md or spike.md.
5. Load the role files named by that workflow. Every role file is self-contained: purpose, entry conditions, numbered procedure, checklist, output and exit conditions.

## Execute

1. Follow the selected workflow's exact responsibility order and mode applicability rules.
2. Extended approval, pause, resume, revision and invalidation rules are owned by references/core/modes.md. Do not load a separate human-gates file.
3. Load practices/coverage.md for AC/regression classification; practices/tdd.md before executable Feature/Bug changes; practices/workspace.md for multi-root work; practices/review.md for human decisions and handoffs; practices/delegation.md for independent review; practices/integrations.md for selected add-ons. Load host adapters only when actual host capabilities matter.
4. Complete the current role checklist and return its output to Coordinator. A role never approves a human gate, grants new scope or starts a downstream role autonomously.
5. Developer performs implementation plus verification. Reviewer independently inspects the code changes and Developer's evidence. Do not create/invoke a separate Verifier stage.
6. Reassess risk, authority, source freshness and scope at every transition. A user-authorized local implementation does not authorize excluded roots, destructive operations, installs, commits, pushes, merges, production migrations, cloud changes or deployment.

## Resume

Reload the existing task state and pending artifact. Verify exact revision, prior human approval, repository scope, project instructions and source/Git snapshot freshness. Do not restart completed work or infer approval from silence. Resume protocol is in references/core/modes.md.

## Guardrails

- Do not manufacture approvals, test outputs, reviewer isolation or implementation status.
- Developer self-check is not independent review and cannot yield AI_PASS.
- A stale snapshot cannot be reviewed as current. Relevant edits require re-verification and fresh review.
- If a fresh independent Reviewer cannot actually be dispatched, report INDEPENDENCE: NOT VERIFIED and REVIEW: PENDING.
- Spike never enters production implementation or code review. A POC requires a separate bounded scratch-space grant and ends with a decision, not a delivered feature.
- Markdown instructions do not enforce filesystem/runtime permissions; actual host and operating-system controls remain authoritative.