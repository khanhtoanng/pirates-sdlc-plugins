# Host installation and support

The plugin provides one workflow across Claude Code, Cursor, Codex and GitHub Copilot. Host integration determines how skills, agents and tools are discovered; it does not change SDLC permissions or grant project edit authority. Commands below are Linux examples; use the installed host's help when CLI behavior differs by version.

## Host capability overview

| Host | Plugin integration | Automated runner coverage | Reviewer integration |
|---|---|---|---|
| Claude Code | Native plugin directory / marketplace | CLI loads the native plugin | Bundled Reviewer agent; verify fresh dispatch |
| Cursor | Cursor-native local plugin | Runner copies skills into a fixture project | Native Reviewer agent; verify discovery and dispatch |
| Codex | Local plugin marketplace / plugin manager | Runner copies skills into a fixture project | Fresh subagent; verify independence and inherited sandbox |
| GitHub Copilot CLI | Portable Agent Plugins package | CLI loads native plugin and captures JSONL | Copilot custom agent |
| GitHub Copilot in VS Code | Agent Plugins through Chat Customizations | Manual GUI discovery/workflow check | Copilot custom agent |

Plugin support does not mean every host capability is exercised by automated evaluation. Cursor and Codex runner paths test project-local skill snapshots; VS Code Copilot requires manual GUI checks. See [Evaluation](EVALUATION.md).

## Claude Code

Run from a project repository:

```bash
claude --plugin-dir /absolute/path/to/pirates-sdlc-plugins/plugins/ai-sdlc
```

Verify `/ai-sdlc:sdlc-work`, `/ai-sdlc:sdlc-setup`, `/ai-sdlc:sdlc-doctor` and the Reviewer are discoverable. Add only required additional roots with `--add-dir`, and verify access and project instructions. Added directories are not approval to edit them.

The optional local marketplace catalog is `.claude-plugin/marketplace.json`. Check persistent-install commands with `claude plugin --help`.

## Cursor

```bash
mkdir -p ~/.cursor/plugins/local
cp -R /absolute/path/to/pirates-sdlc-plugins/plugins/ai-sdlc ~/.cursor/plugins/local/ai-sdlc
```

Inspect an existing copy before replacing it. Restart/reload Cursor, open Customize → Plugins and confirm skills and Reviewer discovery. Open required repositories in a multi-root workspace. Cloud agents may not have the same access as the local editor.

## Codex

From the repository root:

```bash
codex plugin marketplace add /absolute/path/to/pirates-sdlc-plugins
codex plugin marketplace list
codex plugin add ai-sdlc@ai-sdlc-local
codex plugin list
```

If the installed version uses a GUI or `/plugins`, install `ai-sdlc` from `ai-sdlc-local`. The catalog at `.agents/plugins/marketplace.json` points to `./plugins/ai-sdlc`.

For multi-root CLI work, grant only the required additional directories:

```bash
cd /path/to/project/backend
codex --sandbox workspace-write --ask-for-approval on-request --add-dir ../frontend --add-dir ../flyway
```

Host access is not SDLC approval to edit each root. Codex subagents inherit the parent sandbox and approval mode; a Reviewer instruction alone does not enforce OS-level read-only isolation.

## GitHub Copilot CLI

```bash
copilot plugin install /absolute/path/to/pirates-sdlc-plugins/plugins/ai-sdlc
copilot plugin list
```

Start a new session and verify `/skills list` and `/agent`. Invoke a workflow:

```bash
copilot -p "Use /sdlc-work feature standard Add customer status" --plugin-dir /absolute/path/to/pirates-sdlc-plugins/plugins/ai-sdlc
```

The manifest exposes shared skills and the Copilot-specific `sdlc-reviewer` agent. Reinstall the local path after changing the checkout so the installed cache is refreshed.

## GitHub Copilot in VS Code

Select the Copilot harness and open Chat: Open Customizations → Plugins. Install from a local folder or Git repository, or use the plugin installed through Copilot CLI. Verify the `sdlc-work` skill and `sdlc-reviewer` agent in the UI.

For development, VS Code also supports the experimental `chat.pluginLocations` setting with the plugin directory mapped to `true`. This is not the same as a CLI eval.

## Fallback skill snapshots

When native plugin installation is unavailable, copy skills into `~/.agents/skills/` or a project `.agents/skills/`. This is a snapshot and must be copied again after updates. It does not install native Reviewer agents. Prefer native plugin installation when available.

## Verify the actual workflow

Plugin discovery is only the first check. Verify skill discovery/invocation, route and mode selection, available tools and repository roots, actual Developer/Reviewer handoffs, Reviewer independence, and durable records under the selected `.sdlc/changes/<task-id>/` task home.

The Markdown adapters under `plugins/ai-sdlc/skills/sdlc-work/references/hosts/` are runtime instructions for the Coordinator, not installation guides.
