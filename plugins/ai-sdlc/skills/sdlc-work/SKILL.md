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

## Task records

Follow references/core/modes.md for mode-specific persistence. Every durable plugin-generated record must use one canonical task directory under `.sdlc/changes/<task-id>/` in a selected task-home root. External tickets, issues, PRs and ADRs are source references, not alternate state stores. The Coordinator selects and creates the directory, checks write authorization, and passes its path to every role. Do not create duplicate records in participating repositories.

Quick creates no record by default; Standard creates a compact `task.md` when continuity is needed; Extended requires `state.json` and applicable stage artifacts before the first stage. If required storage is unavailable, report `HANDOFF: NOT DURABLE`; do not silently fall back.

## Execute

1. Follow the workflow's order and mode applicability.
2. For Extended, follow the approval and resume protocol in references/core/modes.md. Run only the current stage.
3. Load practices by responsibility: coverage.md when classifying candidate rules versus verification examples; tdd.md for Architect test-seam planning, Developer test execution and Reviewer evidence checks; delegation.md for actual dispatch, safe parallel work and Reviewer isolation; review.md for human decisions/cards; workspace.md for multi-root work; integrations.md for optional add-ons. Load host adapters only when host capabilities matter.
4. Treat each practice as the single owner of its detailed procedure. Role files define role-specific responsibilities and point to practices rather than copying their procedures.
5. Return each role's result to the Coordinator. The Coordinator checks evidence and prerequisites before handing off.
6. Reassess risk, authority, source freshness and scope at each transition. A local edit grant does not authorize privileged operations or excluded roots.

## Resume

Resolve the supplied task ID or record path to the canonical task directory under the selected task home. Reload its state and pending artifact. Verify its exact revision, approval, scope, project instructions and source/Git snapshot freshness before continuing. Follow the resume protocol in references/core/modes.md.

Do not silently relocate legacy task records. Continue an existing record in its original location only when its identity and prior approvals can be verified; otherwise ask the owner to migrate it explicitly.

## Guardrails

- Never invent approvals, test results, reproduction evidence, reviewer independence or host capabilities.
- Developer performs implementation plus verification and may parallelize only independent, bounded AC slices under references/practices/delegation.md.
- Reviewer independently inspects the actual changes and evidence. The Reviewer role owns the review method and verdict.
- If a fresh independent Reviewer cannot be dispatched, report `INDEPENDENCE: NOT VERIFIED` and `REVIEW: PENDING`.
- A stale snapshot cannot be reviewed as current. Relevant changes require re-verification and fresh review.
- A Spike ends with a decision. Any POC needs a separate bounded scratch grant; production delivery requires a new Feature/Bug task.
- Host and operating-system permissions remain authoritative; Markdown instructions are not an enforcement boundary.
