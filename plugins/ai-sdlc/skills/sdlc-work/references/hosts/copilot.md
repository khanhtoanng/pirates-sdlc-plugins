# GitHub Copilot host notes

This adapter covers GitHub Copilot CLI and the Copilot harness in VS Code. It does not describe inline code completions or the deprecated VS Code Local harness.

## Package and discovery

- The plugin uses the portable Agent Plugins 1.0 package: the root `plugin.json` points to shared `skills/` and the Copilot-specific `com.github.copilot/agents/` directory.
- **Copilot CLI:** the plugin manifest explicitly points to `com.github.copilot/agents/`; use its `sdlc-reviewer.agent.md` (`sdlc-reviewer`) as the Copilot-native read-only Reviewer.
- **VS Code:** `com.github.copilot/agents/sdlc-reviewer.agent.md` is the Copilot-specific Reviewer profile, named `sdlc-reviewer`. Select the Copilot harness and enable agent plugins (`chat.plugins.enabled`).
- Do not copy the plugin into a target repository or generate project harness files. Install the plugin itself.
- **Copilot CLI:** install from the plugin directory with `copilot plugin install /absolute/path/to/plugins/ai-sdlc`. Verify with `copilot plugin list`, then start a new session and inspect `/skills list` and `/agent`.
- **VS Code:** open Chat: Open Customizations → Plugins and install the plugin from a local folder or Git repository. VS Code also discovers plugins installed through Copilot CLI. A development checkout can be registered with the experimental `chat.pluginLocations` setting.

## Workflow invocation

- In Copilot CLI, invoke the skill by name in the prompt, for example: `Use /sdlc-work feature extended Add customer status`.
- In VS Code Chat with the Copilot harness selected, invoke `/sdlc-work feature extended Add customer status`.
- A skill being loaded does not prove that the Coordinator followed its workflow. Inspect the route, stage records, tool activity, approvals and resulting files.

## Delegation and review

- Copilot custom agents run in their own subagent context. Explicitly request `sdlc-reviewer` for the fresh post-implementation review.
- Verify the actual agent handoff and returned Reviewer result in the Copilot session trace. Merely discovering the custom agent or mentioning its name is not evidence of dispatch or independence.
- The Reviewer profile is restricted to read/search tools. This does not by itself create a separate worktree or OS sandbox. Use host worktree isolation when parallel writes are proposed; otherwise run implementation serially.
- Tool permissions, approval prompts, organization policy and available tools remain host-controlled. Instructions do not override those controls.

## Evaluation

- The opt-in runner targets Copilot CLI because it supports non-interactive prompts and JSONL output. It passes the plugin directory explicitly, suppresses ambient plugin discovery with `COPILOT_PLUGIN_DIR_ONLY=true`, and grants only fixture-required read/write plus scoped shell tools.
- Run representative VS Code discovery and workflow checks manually. The CLI runner is not evidence of VS Code GUI behavior.
- Use disposable repositories and accounts. Never use `--allow-all` for routine evals or run the fixture against production workspaces.
