# Local installation & verification (Linux)

Examples use the extracted directory `/home/you/AI_SDLC_Local_Plugin_v0.8.0`. Substitute your actual path. The plugin root is `plugins/ai-sdlc/`; marketplace catalogs are in the repository root.

## Claude Code

```bash
cd /home/you/project/backend
claude --plugin-dir /home/you/AI_SDLC_Local_Plugin_v0.8.0/plugins/ai-sdlc
```

Verify discovery of `/ai-sdlc:sdlc-work`, `/ai-sdlc:sdlc-setup`, `/ai-sdlc:sdlc-doctor` and the Reviewer. Use `--add-dir` for additional repository roots, then verify actual access and permissions. For persistent local installation, register the extracted root as a marketplace using `.claude-plugin/marketplace.json`; check current CLI options with `claude plugin --help`.

## Cursor

```bash
mkdir -p ~/.cursor/plugins/local
cp -R /home/you/AI_SDLC_Local_Plugin_v0.8.0/plugins/ai-sdlc ~/.cursor/plugins/local/ai-sdlc
```

Inspect an existing copy before replacing it. Restart Cursor or reload the window, open Customize → Plugins, and confirm the skills and Reviewer are discoverable. Open required repositories in a multi-root workspace. Cloud agents may not have the same multi-root access as the local editor.

## Codex

```bash
codex plugin marketplace add /home/you/AI_SDLC_Local_Plugin_v0.8.0
codex plugin marketplace list
codex plugin add ai-sdlc@ai-sdlc-local
codex plugin list
```

If your Codex version uses a GUI or `/plugins`, install `ai-sdlc` from `ai-sdlc-local`. The catalog at `.agents/plugins/marketplace.json` points to `./plugins/ai-sdlc` relative to the marketplace root.

For multi-root CLI work, grant only the additional directories required:

```bash
cd /home/you/project/backend
codex --sandbox workspace-write --ask-for-approval on-request \
  --add-dir ../frontend --add-dir ../flyway --add-dir ../terraform
```

Host directory access is not SDLC approval to edit every root. The Coordinator still checks the task's bounded scope.

## GitHub Copilot (VS Code and CLI)

The plugin uses the portable Agent Plugins 1.0 manifest, shared `skills/` directory and Copilot-specific `com.github.copilot/agents/sdlc-reviewer.agent.md` Reviewer. The portable manifest points Copilot CLI at that same directory, so both Copilot clients use the `sdlc-reviewer` agent.

For Copilot CLI, install the plugin from the local checkout:

```bash
copilot plugin install /home/you/AI_SDLC_Local_Plugin_v0.8.0/plugins/ai-sdlc
copilot plugin list
```

Start a new CLI session and verify `/skills list` and `/agent`. Invoke a workflow directly:

```bash
copilot -p "Use /sdlc-work feature standard Add customer status" \
  --plugin-dir /home/you/AI_SDLC_Local_Plugin_v0.8.0/plugins/ai-sdlc
```

For persistent installation, use `copilot plugin install` once and start a new session. Reinstall the local path after changing the checkout so the installed cache is refreshed. VS Code automatically discovers plugins installed through Copilot CLI. Select the Copilot harness and verify the plugin and its skills/agent under Chat: Open Customizations → Plugins. For a development checkout, VS Code also supports the experimental `chat.pluginLocations` setting with the plugin directory mapped to `true`.

**Fallback:** when native plugin installation is unavailable, copy `plugins/ai-sdlc/skills/sdlc-*` into `~/.agents/skills/` or project `.agents/skills/`. This is a snapshot; copy again after updates. It does not install the native Reviewer agent.

## Try the three task routes

```text
sdlc-work feature standard Add customer status; inspect accepted ACs and edit only authorized roots.
sdlc-work bug quick Fix a reproduced endpoint 500 and verify the original response contract.
sdlc-work spike standard Research offline sync feasibility; compare contrary evidence and stop before implementation.
```

These examples do not prove host execution. See `tests/SCENARIOS.md` for host evaluation.

## Verify a task

Start with read-only setup inspection. Then plan a bounded Feature, confirm accepted ACs and write scope, authorize implementation, run tests, and confirm a genuinely fresh Reviewer was dispatched. If independent dispatch cannot be verified, report `NOT VERIFIED`, not `AI_PASS`.
