# Delegation and safe parallel work

Roles are instruction contracts, not native subagent declarations. The Coordinator normally invokes each stage role in the current context; the role owner may choose bounded subdelegation when it adds meaningful isolation, expertise or throughput. The Coordinator must not create one subagent per SDLC stage merely to follow the workflow. A claimed dispatch is not evidence: verify that the host actually started the requested worker and returned its result.

## Role-owned delegation decision

Each role owner decides whether to perform its work directly or delegate bounded subtasks. Delegation is an available technique, not a stage requirement or a measure of productivity. Make the decision when the work reveals separable investigation or execution; do not spawn workers merely because the host offers them.

**Delegate when** a subtask has a clear, independently useful result and at least one material benefit:
- It needs a distinct specialist perspective or independent evidence gathering.
- It spans separate modules, repositories, sources or alternatives that can be explored without shared mutable state.
- It can make useful progress in parallel without depending on another unfinished result.
- A genuinely fresh context is needed for an independent assessment.

**Stay in the current context when** the work is small, sequential, tightly coupled, depends on substantial shared context, has no safe write boundary, or would cost more to delegate and reconcile than to perform directly.

Before dispatch, confirm that the active host exposes a real worker/subagent capability and that its scope and permissions are sufficient. If it does not, continue inline; do not simulate a dispatch, assume an agent exists, or claim isolation that the host has not provided.

The parent role remains accountable for:
- The assigned stage's complete result and exit conditions.
- Synthesizing and checking worker findings against the source, current repository state and accepted decisions.
- The canonical artifact, decision, and handoff to the Coordinator.
- Staying within the same approval, authority and scope boundaries as non-delegated work.

Delegate **investigation or bounded execution**, not ownership of the stage. Workers may return evidence, alternatives, candidate scenarios or an explicitly assigned implementation slice. They may not change accepted requirements, independently approve an artifact, alter task scope/dependencies, grant permissions or replace the role owner's final judgment.

Use a compact worker contract appropriate to the task: **objective, context/revision, allowed roots and paths, permissions, dependencies, expected output, constraints and handoff**. For implementation workers, also specify the accepted task/AC IDs, write boundary, baseline, test seam and evidence expected. Record actual dispatch and returned results when delegation materially affects the work; never report a proposed or failed dispatch as completed.

### Role-specific ownership

- **Coordinator:** may delegate bounded read-only discovery when it materially reduces context or broadens independent evidence. It retains task classification, risk/mode selection, authority, canonical state, stage order, approval gates and transition decisions. It does not delegate an entire stage just to create a worker per role.
- **Intent:** may delegate separate read-only investigation of users, workflows or source context. Intent owns the final problem, outcome, scope and non-goals.
- **Spec:** may delegate independent inspection of contracts, flows or existing tests. Spec owns classification and the single canonical AC set; workers must not create competing requirement inventories.
- **Architect:** may delegate read-only module tracing, caller/consumer discovery, alternatives or risk research. Architect owns the recommended approach, AC-to-task mapping, file-level plan and logical dependency graph.
- **Developer:** may delegate bounded implementation slices or independent failure investigation only after checking approved scope, dependencies, write ownership, host capability and isolation. Developer owns integration and final verification.
- **Researcher:** may delegate independent source/alternative research. Researcher owns evidence quality, synthesis, confidence and the final Spike decision.
- **Reviewer:** is the mandatory fresh independent review context, not a workstream coordinator. It must inspect the actual integrated snapshot itself and must not delegate or outsource its verdict. Its host-defined read-only restrictions and independence must remain intact.

The Coordinator still validates each role handoff. A delegated worker result is input to the role owner, not a new SDLC stage or an approval event.

## Planning ownership and execution validation

- **Architect owns the logical delivery graph:** accepted AC-to-slice mapping, task outcomes, genuine prerequisite/blocking edges and proposed independent groups.
- **Developer owns execution feasibility and actual dispatch:** validate current write ownership, worktree/host isolation, shared resources and dispatch capability before starting parallel workers.
- A logically independent task is not automatically safe to run in parallel. The plan's parallel groups are candidates, not permission or proof of isolation.
- If Developer discovers a material missing dependency, shared resource or infeasible task boundary, stop the affected dispatch and return the issue to the Coordinator. Revise the plan through Architect; do not silently rewrite approved task outcomes or blocker relationships. In Extended, obtain approval for the revised plan before implementation resumes.

## When parallel work is safe

Use the Architect's approved dependency graph as the starting point. Developer confirms operational independence at execution time.

- Prefer isolated worktrees/workspaces for parallel code changes when the host supports them.
- In a shared worktree, parallel edits are allowed only when write paths and shared resources are demonstrably disjoint and workers cannot race on Git/index or generated state. Otherwise run serially.
- Do not parallelize slices that depend on one another, change the same files, share a migration/schema/API contract still being decided, modify common fixtures/configuration, or require another slice's generated output.
- Give each worker an explicit task contract: approved plan revision, assigned task and AC IDs, expected end-to-end outcome, allowed roots/paths, relevant baseline, genuine blockers, test seam and expected handoff. Workers cannot alter ACs, task outcomes, dependencies, expand scope or grant themselves authority.
- Each implementation worker follows `practices/tdd.md` for its own behavior slice and records exact test evidence. Do not let parallelism bypass RED/GREEN evidence.
- Integrate completed slices deliberately. Resolve conflicts, capture the integrated snapshot and run cross-slice, regression and integration checks before Reviewer dispatch.
- If isolation, ownership or independence cannot be established, prefer serial execution. Do not parallelize merely to increase agent count.

Parallel implementation does not replace the single canonical AC set, Developer's final integration verification or the independent whole-change Reviewer.

## Independent Reviewer requirement

After any authorized Feature/Bug project-code change, `AI_PASS` requires a genuinely fresh Reviewer context that did not implement the changed code and inspected the current identified snapshot. Do not dispatch an independent Reviewer for a read-only Spike or scratch-only POC.

- Verify actual host dispatch and fresh context; a role prompt or a second message in the implementer's context is not independence.
- Give the Reviewer accepted expectations, approved plan/diagnosis, current per-root snapshot identity, actual diff (including relevant untracked files), and observed test evidence.
- Do not give the Reviewer source-edit authority merely to collect evidence.
- Reviewer findings and verdict format are defined in `roles/reviewer.md`. Any repair invalidates affected evidence and requires Developer re-verification plus a fresh review. Escalate after at most three AI repair/review cycles.

## Host capabilities

- **Claude Code:** use actual Agent/subagent tools when present. The bundled `agents/sdlc-reviewer.md` prefers read/grep/glob. If the Reviewer cannot run shell, supply exact Git diff and test output plus relevant new/untracked contents. Validate the subagent truly ran.
- **Cursor:** use the actual subagent/Task workflow when available, with the bundled Reviewer agent. Confirm native Reviewer discovery and actual invocation; do not assume `readonly` instructions enforce filesystem isolation.
- **Codex:** use actual subagents for a fresh Reviewer context when supported. Custom `.codex/agents/*.toml` is optional project-owned configuration and is not generated by default. Codex subagents inherit parent sandbox/approval settings; a Reviewer prompt alone is not a read-only sandbox. A dedicated `codex review` on an exact snapshot may provide additional evidence but is not an independent subagent unless actual isolation is observed.
- **GitHub Copilot:** use the Copilot-native `com.github.copilot/agents/sdlc-reviewer.agent.md` (`sdlc-reviewer`) in Copilot CLI and the VS Code Copilot harness. Explicitly dispatch the named Reviewer as a fresh subagent after implementation; agent discovery or a model's claim is not proof of dispatch. Inspect the Copilot session trace for the actual handoff and returned result. The Reviewer profile is read-only, but a separate context is not automatically a separate worktree or OS sandbox. Use host worktree isolation when parallel writes are proposed; otherwise run implementation serially.
- If a separate independent Reviewer is unavailable, report `REVIEW: NOT VERIFIED` and `INDEPENDENCE: NOT VERIFIED`; do not emit `AI_PASS`.
