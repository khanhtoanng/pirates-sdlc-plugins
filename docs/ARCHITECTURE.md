# Architecture decisions — AI SDLC v0.7.0

## Single plugin, minimal host adapter

One `ai-sdlc` runtime holds three task routes and five logical role contracts. Host-native manifests/catalogs expose the same installed skills to Claude Code, Cursor and Codex. Project-specific instructions/config remain project-owned. Do not generate a second kit or per-repo harness by default. Setup and Doctor are optional skills.

## Two independent axes

- **Task type** (`routing.md`): `Feature` (new or intentionally changed observable behavior), `Bug` (repair proven violated behavior), `Spike` (bounded research/feasibility decision, no automatic implementation).
- **Execution mode** (`auto`/`quick`/`standard`/`extended`): evidence and human-gate depth based on real risk; multi-repo count alone is not Extended. The old `spike` mode is now a supported legacy alias for the Spike task type.

Each route has stage entry/exit evidence and explicit block conditions (`core/runtime.md`). `core/routing.md` classifies, `core/modes.md` selects rigor, `workflows/` contains the routes, `roles/` specifies responsibilities, and `practices/` holds shared rules. Intent (WHY), Spec (WHAT), Architect (HOW), Developer (BUILD), Reviewer (independent VERIFY) are *logical* responsibilities. Reviewer dispatch uses a fresh independent context.

## Verify and converge, not just run a test

- **Feature:** accepted AC revision → planned slice and root → actual diff → meaningful observed test; check completeness, compatibility and rollout dependencies.
- **Bug:** original expected/actual symptom → reproduction evidence → root cause/fix → observed after-state → regression protection; no `VERIFIED_FIX` on weak or stale evidence.
- **Spike:** bounded question → credible supporting and disconfirming evidence → confidence/options/verdict → STOP; a POC requires a separate scratch grant and never becomes implementation silently.
- All code-change verification is tied to actual per-root branch/HEAD **plus dirty patch/untracked state**. Repairs/rebases can invalidate old proof or a previous review.

## Authority and human review

A bounded user **implement/fix** request can authorize local source edits within that scope if host/project policy permits. Approval of new business behavior remains separate. A request to analyze/plan/spike does not grant source edits; any broadened paths or privileged/external operations need explicit permission. Nothing in prompt text overrides OS/host permission, protected environments or CI controls.

Human sees concise changed decisions/AC mapping, not every brainstorming thought. Extended requires explicit approval after every applicable stage, even when there is no new material decision. `core/human-gates.md` owns mandatory pause/resume/revision invalidation; see [Extended](EXTENDED.md). An independent `AI_PASS` is not merge/deploy authority.

## Multi-repo and continuation

Treat independent Git roots separately: `VISIBLE`, `RELEVANT`, `EDIT_APPROVED`, `EXCLUDED`. Share one accepted Feature AC set, maintain a per-root impact/test map and dependency-aware release order. Quick/Standard use concise records; Extended requires distinct stage artifacts and state in one authorized location or tracker. Resume refreshes source, permissions, approvals and snapshots.

## Upgrades

Replace the plugin package and reload the host. Do not automatically change project files or pin runtime version in project instructions. Optional workspace profile `schemaVersion` is a schema identifier, not an installed plugin version. Doctor detects legacy per-repo skills before any approved retirement.
