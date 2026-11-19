# Migrating from v0.4/v0.5 to v0.6 runtime

## From v0.6.0 to v0.7.0

- Update/reload the plugin; invocation and host manifests remain compatible.
- Extended now pauses at every applicable stage. Reuse prior evidence but never assume an earlier v0.6 record contains a human checkpoint approval.
- Existing project rules remain yours; do not copy the new runtime into projects. Approve a task record location only when needed.
- Run offline tests and the selected opt-in host evaluation scenarios before treating behavior as verified.

The v0.4 package generated a standalone repo skill (`.claude/skills/sdlc-work` or `.cursor/skills/sdlc-work`) and possibly a reviewer agent. This version ships SDLC at plugin runtime. Installing it does NOT automatically delete or supersede old project files.

1. Install v0.5 local plugin in one selected host; verify its `sdlc-work` skill without editing the project.
2. Run `sdlc-doctor` to discover old skills in `.claude/skills`, `.cursor/skills`, `.agents/skills`, and old reviewer definitions. Inspect local Git changes; preserve edits.
3. Compare old project-specific additions against current project instruction sources. Move only owner-approved project-specific rules into appropriate existing `CLAUDE.md`, `AGENTS.md`, `.cursor/rules` or optional workspace profile. Do not paste runtime role policies across hosts.
4. Present an exact `KEEP/MERGE/RETIRE` diff. Obtain approval before removing old generated skill/agent files. If cannot resolve conflicts, leave both and warn explicitly about ambiguous skill discovery; do not claim it is migrated.
5. Run one read-only exercise (setup inspect) and one dry-run Standard plan. Test actual reviewer dispatch before marking verification complete.

Use absolute plugin invocation for Claude (`/ai-sdlc:sdlc-work`) to avoid ambiguity; Cursor and Codex may show names under their native skill selectors.

## From v0.5.0 to v0.6.0

- Replace installed plugin and reload each host; do not modify project files automatically.
- `spike` is now a task type, **not** a risk mode. `sdlc-work spike <question>` remains a legacy alias; new preferred input is `sdlc-work spike auto <question>`.
- `feature` and `bug` can be specified explicitly before `auto|quick|standard|extended`; no type specified means Coordinator derives it from the task.
- A scoped explicit `implement/fix` request can authorize ordinary local edits unless stricter host/project policy demands permission; it never authorizes privileged/external operations.
- No new required project config; `routing.md` and `tests/evals` are plugin-owned files only.
- Run `python3 tests/validate.py`, `python3 tests/evals/score.py --self-test`, then real host discovery and behavioral scenarios; static and synthetic results are not host proof.
