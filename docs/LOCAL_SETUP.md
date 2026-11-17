# Local installation & verification (Linux)

All paths below assume you extracted this ZIP at `/home/you/AI_SDLC_Local_Plugin_v0.6.0`. Substitute the real absolute directory. Plugin root is `plugins/ai-sdlc/`, while repository root contains local marketplace catalogs.

## Claude Code — fastest interactive development

```bash
cd /home/you/project/backend
claude --plugin-dir /home/you/AI_SDLC_Local_Plugin_v0.6.0/plugins/ai-sdlc
```

In Claude, inspect skills for `/ai-sdlc:sdlc-work`, `/ai-sdlc:sdlc-setup`, `/ai-sdlc:sdlc-doctor`; invoke one and verify the reviewer is actually discoverable. No permanent install needed. For cross-repo access use `--add-dir` for FE/DB/infra and inspect actual permission and instruction loading. E.g.:

```bash
cd /home/you/project/backend
claude --plugin-dir /home/you/AI_SDLC_Local_Plugin_v0.6.0/plugins/ai-sdlc \
  --add-dir ../frontend --add-dir ../flyway --add-dir ../terraform
```

Optional persistent local marketplace setup: register extracted root as a local Claude marketplace (its `.claude-plugin/marketplace.json`) and install `ai-sdlc@ai-sdlc-local` through the host plugin manager. Check current CLI command options with `claude plugin --help` rather than assuming user or project scope.

## Cursor — local plugin directory

```bash
mkdir -p ~/.cursor/plugins/local
cp -R /home/you/AI_SDLC_Local_Plugin_v0.6.0/plugins/ai-sdlc ~/.cursor/plugins/local/ai-sdlc
```

If a previous copy exists, inspect its contents and deliberately replace it rather than using an unsafe overwrite. Cursor local plugin symlinks that point outside `~/.cursor/plugins/local` may be skipped. Restart Cursor (or Developer: Reload Window), open Customize → Plugins and confirm `sdlc-work`, `sdlc-setup`, `sdlc-doctor` and reviewer; test actual invocation. Open the four Git repos using a multi-root workspace. Cursor cloud agents may not support the same multi-root access as the local editor.

## Codex — local marketplace (CLI / local plugin manager)

```bash
codex plugin marketplace add /home/you/AI_SDLC_Local_Plugin_v0.6.0
codex plugin marketplace list
codex plugin add ai-sdlc@ai-sdlc-local
codex plugin list
```

If your Codex version uses a GUI or `/plugins` for installation, open that manager and install `ai-sdlc` from `ai-sdlc-local`. Local repo marketplace file is `.agents/plugins/marketplace.json`; it points to `./plugins/ai-sdlc` **relative to the marketplace root**. Restart the session / refresh local plugins after editing. Codex reads project `.codex/config.toml` only for trusted projects; a local plugin may also be toggled using `[plugins."ai-sdlc@ai-sdlc-local"] enabled = true` if needed. For a four-repository workspace in local Codex CLI, use explicit additional directories rather than broad sandbox bypass:

```bash
cd /home/you/project/backend
codex --sandbox workspace-write --ask-for-approval on-request \
  --add-dir ../frontend --add-dir ../flyway --add-dir ../terraform
```

`--add-dir` grants additional host-level directory write access, **not an SDLC workflow authorization** to edit every directory. The coordinator must still verify the bounded edit scope; an explicit scoped implement/fix request may grant ordinary local edits, but not protected operations. Confirm the selected working directory and required sibling-root access under the current sandbox.

**Fallback, only if your host does not support plugin installation:** manually copy `plugins/ai-sdlc/skills/sdlc-*` into `~/.agents/skills/` (global) or `.agents/skills/` (project), then restart Codex. This is a *snapshot*; re-copy after plugin updates. It does not include the native reviewer agent; use actual Codex subagents for independent review.

## Try all three task routes

After confirming discovery in the selected host, invoke one scope-limited route at a time:

```text
sdlc-work feature standard Add a customer status; first inspect accepted ACs, then implement only authorized roots.
sdlc-work bug quick Fix a reproduced endpoint 500 regression and verify the original expected response.
sdlc-work spike standard Research whether offline sync is feasible, compare contrary evidence, and STOP without implementation.
```

These are invocation examples, not evidence any host has executed them. The five logical roles are invoked proportionally; Bug and Spike must not be forced through every Feature stage. See `TASK_ROUTES.md` for expected evidence and `../tests/SCENARIOS.md` for evaluation.

## Test one task

Ask: `Use sdlc-setup inspect to map the visible FE, BE, Flyway and Terraform roots. Read only. Show instruction conflicts, available tests and suggested write scope. Do not generate files.`

Then: `Use sdlc-work standard to plan adding customer status across FE, BE and Flyway. Terraform is read-only. Do not edit until I approve exact paths. Show one AC set and release dependencies.`

When local edits are authorized by the bounded user request or a further explicit grant, run actual tests and confirm a genuine fresh reviewer was invoked. If the host cannot dispatch a reviewer, status must be `NOT VERIFIED` rather than `AI_PASS`.
