# Changelog

## Unreleased

- Made Spec output human-first: one authoritative acceptance-criteria table with full observable rules, per-AC source/basis labels, separate verification examples, concise scope and consequential decisions.
- Made Architect Feature plans actionable: summary-first implementation table mapping each task to actual file operations/paths, specific code responsibilities, ACs and genuine blockers; added explicit unknown-path behavior and a compact Bug repair-plan format.
- Aligned human review handoffs with the Spec and plan tables and added illustrative Spec and Architect plan examples.

## 0.9.0 — smallest complete change

- Added a shared smallest-complete-solution decision ladder to Architect and Developer, preferring removal, existing project capabilities, platform/standard-library features and installed dependencies before adding the minimum necessary code.
- Required concrete justification for new dependencies, abstractions, wrappers, options and configuration; preserved safety and accepted behavior over minimizing line count.
- Strengthened caller/consumer impact tracing and evidence-based Bug root-cause repair, including verification of affected callers.
- Clarified that Developer may simplify implementation within approved outcomes and boundaries, while material design or plan changes still return through Architect and the Coordinator.
- Reorganized human documentation around a documentation index, user guide, host guide, task-record guide and evaluation guide; retained compatibility links for older pages.
- Made `.sdlc/changes/<task-id>/` the canonical location for all durable plugin-generated task records. External tickets, PRs and ADRs are source references, not alternate plugin-state stores.
- Defined Quick, Standard and Extended persistence behavior and one task home for multi-repository work.
- Clarified host plugin discovery, installation, automated runner coverage and actual Reviewer delegation.
- Added migration guidance for tasks created before the canonical task-record policy.

## 0.8.0 — consolidated modes and role workflows

- Clarified Quick, Standard and Extended behavior, including revision-aware Extended approval, pause/resume and invalidation.
- Standardized Feature, Bug and Spike role sequences and Extended artifact maps.
- Made each role instruction self-contained with its own procedure, checklist, output and exit conditions.
- Combined Developer implementation and verification; kept Reviewer independent and evidence-based.
- Expanded workflow, artifact-path and host-behavior evaluation coverage.

## 0.7.0 — Extended approvals and executable evaluations

- Added approval at every applicable Extended stage, with durable state and resume checks.
- Added opt-in host execution, independent file/state checks and multi-turn fixtures.
- Added offline validation and grader tests; no automatic paid model calls, hooks or MCP installation.

## 0.6.0 — task routing and stage contracts

- Separated task type (`feature | bug | spike`) from mode (`auto | quick | standard | extended`).
- Added Feature AC, Bug reproduction/regression and Spike decision/STOP contracts.
- Added verification, snapshot freshness, scope/authority and multi-repository rules.
- Added route examples, behavioral eval scenarios and evidence scoring.

## 0.5.0 — local-first plugin runtime

- Replaced project-harness generation with one plugin and the `sdlc-work`, `sdlc-setup` and `sdlc-doctor` skills.
- Added multi-repository coordination, host adapters, local installation guidance and evaluation tooling.
