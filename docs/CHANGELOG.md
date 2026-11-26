# Changelog

## Unreleased

- Added GitHub Copilot support for VS Code and Copilot CLI using the portable Agent Plugins 1.0 skill package and Copilot-native Reviewer agent.
- Extended opt-in host smoke runs and offline grader tests to recognize Copilot CLI JSONL output.
- Structured Architect planning from accepted ACs through evidence-backed technical choices, tracer-bullet slices, blocker-first dependencies, proposed parallel groups and verification seams.
- Clarified planning ownership: Architect owns the logical delivery graph; Developer validates current execution feasibility and owns actual dispatch, implementation and verification.
- Added a human-facing Architect plan review card covering task granularity, blocking edges, execution order, approach and scope decisions.
- Aligned Feature/Bug workflows and architecture guides with the revised Architect/Developer handoff.

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
- Added multi-repository coordination, host adapters, local installation guidance and static validation.
