---
name: sdlc-work
description: Coordinate feature delivery, bug diagnosis/fix, or bounded technical research across one or more repositories. Select Quick, Standard or Extended; Extended requires approval after each applicable artifact stage. Use for engineering work, not general Q&A.
argument-hint: "[feature|bug|spike] [auto|quick|standard|extended] <request> [selected roots] | resume <task-id or record>"
---

# AI SDLC work — Coordinator

Execute the workflow from this installed plugin. Do not generate project harness files. The Coordinator owns routing, mode selection, task state, permissions and handoffs.

## Route

1. Read references/core/routing.md, references/core/modes.md and references/core/runtime.md.
2. Inspect the request, ticket/source, project instructions, relevant roots, risk and Git state.
3. Classify task type and requested/effective mode independently. Report the route, reason, scope and risk; emit `SDLC_ROUTE: task_type=<feature|bug|spike>; mode=<quick|standard|extended>`.
4. Read only the selected workflow: references/workflows/feature.md, references/workflows/bug.md or references/workflows/spike.md.
5. Load the role files named by that workflow. Each role owns its procedure, checklist, output and exit conditions.

## Execute

1. Follow the workflow's order and mode applicability.
2. For Extended, follow the approval and resume protocol in references/core/modes.md. Run only the current stage.
3. Load supporting practices when relevant: coverage.md for AC/regression classification, tdd.md for Feature/Bug changes, workspace.md for multi-root work, review.md for review decisions, delegation.md for independent review, and integrations.md for optional add-ons. Load host adapters only when host capabilities matter.
4. Return each role's result to the Coordinator. The Coordinator checks evidence and prerequisites before handing off.
5. Reassess risk, authority, source freshness and scope at each transition. A local edit grant does not authorize privileged operations or excluded roots.

## Resume

Reload the task state and pending artifact. Verify its exact revision, approval, scope, project instructions and source/Git snapshot freshness before continuing. Follow the resume protocol in references/core/modes.md.

## Guardrails

- Never invent approvals, test results, reproduction evidence, reviewer independence or host capabilities.
- Developer performs implementation plus verification. Reviewer independently inspects the actual changes and evidence.
- If a fresh independent Reviewer cannot be dispatched, report `INDEPENDENCE: NOT VERIFIED` and `REVIEW: PENDING`.
- A stale snapshot cannot be reviewed as current. Relevant changes require re-verification and fresh review.
- A Spike ends with a decision. Any POC needs a separate bounded scratch grant; production delivery requires a new Feature/Bug task.
- Host and operating-system permissions remain authoritative; Markdown instructions are not an enforcement boundary.
