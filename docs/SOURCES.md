# Official platform references (checked November 2026)

- Agent Plugins portable manifest: https://agent-plugins.org/specification
- Agent Skills specification: https://agentskills.io/specification
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Claude Code additional directories/instructions: https://code.claude.com/docs/en/settings
- Cursor plugin development and local testing: https://cursor.com/docs/plugins
- Cursor native plugin reference: https://cursor.com/docs/reference/plugins
- Codex plugin packaging and local marketplace: https://developers.openai.com/plugins/build/plugins
- Codex CLI developer commands (`codex plugin ...`): https://learn.chatgpt.com/docs/developer-commands
- Codex local skills and AGENTS.md: https://learn.chatgpt.com/docs/build-skills
- Codex subagents and inherited sandbox constraints: https://learn.chatgpt.com/docs/agent-configuration/subagents

Product/host behavior changes; re-check actual installed version and host outcomes before treating a reference as enforcement.


## Workflow research for v0.6.0 (November 2026)

- GitHub Spec Kit — independent SDD/bug/assessment routes and convergence: https://github.com/github/spec-kit and https://github.github.com/spec-kit/guides/bugfix.html and https://github.github.com/spec-kit/guides/assessment.html
- OpenAI — test agent skills with outcomes/process/efficiency traces: https://developers.openai.com/blog/eval-skills
- OpenAI — progressive disclosure, minimal skills and less instruction bloat: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- Cursor — skill loading and when isolated subagents help: https://cursor.com/docs/skills and https://cursor.com/docs/subagents
- Cursor — hooks are a host-level enforcement option, not an automatic install: https://cursor.com/docs/hooks

These sources informed design principles; this plugin does not claim identical functionality or guaranteed host capabilities.

## Additional references for v0.7.0

- Spec Kit's agentic SDLC and human handoffs: https://github.github.com/spec-kit/guides/agentic-sdlc.html
- Superpowers workflow, TDD and independent review: https://github.com/obra/superpowers
- OpenSpec change artifacts: https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md
- Agent Skills evaluation: https://agentskills.io/skill-creation/evaluating-skills
- Claude native plugin evals: https://code.claude.com/docs/en/plugin-evals
- Cursor structured CLI output: https://cursor.com/docs/cli/using
