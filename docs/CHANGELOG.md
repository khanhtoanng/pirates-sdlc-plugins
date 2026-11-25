# Local change notes

## 0.7.0 — Extended human gates and executable evals

- Separate routing, mode policy, runtime, human gates, workflows, roles and practices; preserve host adapters and optional integrations.
- Mandatory revision-aware review at each applicable Extended stage, with durable state and explicit resume; dynamic risk escalation.
- Opt-in host execution with independent file/state checks, trace retention, multi-turn checkpoint fixtures and offline grader unit tests.
- Offline validation in GitHub Actions; no automatic paid model calls, hooks or MCPs.

## 0.6.0 — Feature / Bug / Spike routing and stage contracts

- Separated task type (`feature | bug | spike`) from risk mode (`auto | quick | standard | extended`), preserving the positional `spike` alias.
- Added route-specific entry/exit evidence: Feature AC acceptance, Bug original-symptom reproduction and regression, Spike recommendation with explicit STOP/no auto-build.
- Introduced concise stage transition gates, verification and convergence, per-root dirty-worktree snapshot freshness, and scope/authority semantics.
- Preserved five **logical** roles, loading instructions progressively; research-only Spike avoids mandatory Developer/Reviewer and product artifacts.
- Clarified ordinary scoped implement/fix requests vs separate privileged side-effect permissions; no silent approvals.
- Strengthened multi-session durable handoffs without generating five per-stage files; reviewer rechecks stale snapshots and completeness.
- Added documented Feature/Bug/Spike examples, twelve behavioral eval scenarios and an evidence-pointer scoring helper. Static passes are not live host validation.


## 0.5.0 — rewrite from bootstrap to runtime

- Removed the separate bootstrap generator plugin and generation of project-native SDLC files.
- Kept one plugin, with `sdlc-work`, optional `sdlc-setup`, `sdlc-doctor`.
- Preserved v0.4's detailed `roles.md`, `coverage.md`, `review.md`, and TDD rules with targeted language updates.
- Added multi-repository Coordinator, separate visibility/relevance/edit sets, shared ACs, integration evidence and per-repository snapshots.
- Changed Extended mode from automatic for any cross-repo write to actual risk-driven escalation.
- Added native Cursor and Claude reviewer discovery, and Codex local marketplace/subagent instructions.
- Added local-only installation guide and static integrity validator; no publication workflow, bundled MCP, hook, or external integration installation.


## Unreleased — consolidated modes and role workflows

- Make Quick, Standard and Extended operationally distinct in core/modes.md, including Extended approval/resume/revision behavior.
- Remove the separate human-gates and shared-role references; each role owns a numbered procedure and checklist.
- Make Developer own implementation plus verification; retain Reviewer as independent evidence/code review.
- Align Feature, Bug and Spike role sequences, ordinal artifact paths and behavioral evaluation fixtures.
