#!/usr/bin/env python3
"""Dependency-free package and workflow contract validation; not a host eval."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ai-sdlc"
SKILLS = PLUGIN / "skills"
REFS = SKILLS / "sdlc-work" / "references"
VERSION = "0.9.0"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: {exc}")
        return {}


for label, path in [
    ("portable", PLUGIN / "plugin.json"),
    ("Claude", PLUGIN / ".claude-plugin/plugin.json"),
    ("Cursor", PLUGIN / ".cursor-plugin/plugin.json"),
]:
    manifest = read_json(path)
    check(manifest.get("name") == "ai-sdlc", f"{label}: invalid name")
    check(manifest.get("version") == VERSION, f"{label}: invalid version")
    if label == "portable":
        check(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
              "portable: missing manifest schema")
    if label == "Cursor":
        check(manifest.get("skills") == "./skills/" and manifest.get("agents") == "./agents/",
              "Cursor: native component path mismatch")

for name in ("sdlc-work", "sdlc-setup", "sdlc-doctor"):
    path = SKILLS / name / "SKILL.md"
    check(path.is_file(), f"missing skill {name}")
    if path.is_file():
        txt = path.read_text(encoding="utf-8")
        parts = txt.split("---", 2)
        front = parts[1] if len(parts) >= 3 and txt.startswith("---\n") else ""
        check(bool(front) and f"name: {name}" in front, f"{name}: invalid frontmatter/name")
        check("description:" in front, f"{name}: missing description")

required_references = (
    "core/routing", "core/runtime", "core/modes",
    "workflows/feature", "workflows/bug", "workflows/spike",
    "roles/intent", "roles/spec", "roles/architect", "roles/developer",
    "roles/reviewer", "roles/researcher",
    "practices/coverage", "practices/workspace", "practices/review",
    "practices/tdd", "practices/delegation", "practices/integrations",
    "practices/smallest-change",
)
for name in required_references:
    check((REFS / f"{name}.md").is_file(), f"missing reference {name}.md")

for removed in ("core/human-gates.md", "roles/shared.md", "roles/verifier.md"):
    check(not (REFS / removed).exists(), f"obsolete role/reference still exists: {removed}")

for host in ("claude", "cursor", "codex", "copilot"):
    check((REFS / "hosts" / f"{host}.md").is_file(), f"missing host adapter {host}.md")
portable_manifest = read_json(PLUGIN / "plugin.json")
check(portable_manifest.get("agents") == "com.github.copilot/agents/" and portable_manifest.get("skills") == ["skills/"],
      "portable manifest must expose Copilot-native agents and shared skills")
check((PLUGIN / "agents/sdlc-reviewer.md").is_file(), "missing Claude/Cursor reviewer")
check((PLUGIN / "com.github.copilot/agents/sdlc-reviewer.agent.md").is_file(),
      "missing VS Code Copilot-native Reviewer agent")
copilot_agent = (PLUGIN / "com.github.copilot/agents/sdlc-reviewer.agent.md").read_text(encoding="utf-8")
check('target: github-copilot' in copilot_agent and 'tools: ["read", "search"]' in copilot_agent
      and "strict-tools-list: true" in copilot_agent,
      "Copilot Reviewer must target Copilot with a strict read-only tool list")

for marketplace, label in [
    (ROOT / ".claude-plugin/marketplace.json", "Claude"),
    (ROOT / ".agents/plugins/marketplace.json", "Codex"),
]:
    data = read_json(marketplace)
    try:
        entry = data["plugins"][0]
        source = entry["source"] if isinstance(entry["source"], str) else entry["source"]["path"]
        check(entry["name"] == "ai-sdlc" and source.startswith("./") and (ROOT / source).is_dir(),
              f"{label}: invalid local marketplace link")
    except Exception as exc:
        errors.append(f"{label} marketplace: {exc}")

skill = (PLUGIN / "skills/sdlc-work/SKILL.md").read_text(encoding="utf-8")
router = (REFS / "core/routing.md").read_text(encoding="utf-8")
runtime = (REFS / "core/runtime.md").read_text(encoding="utf-8")
modes = (REFS / "core/modes.md").read_text(encoding="utf-8")
for task in ("feature", "bug", "spike"):
    check(task in router, f"routing.md missing task type {task}")

for mode in ("Quick", "Standard", "Extended"):
    check(mode in modes, f"modes.md missing {mode} definition")
for phrase in ("awaiting_human_approval", "End the turn", "revision", "invalidate", "NOT DURABLE"):
    check(phrase.lower() in modes.lower(), f"modes.md missing Extended approval contract: {phrase}")
for phrase in ("references/core/routing.md", "references/core/modes.md",
               "references/core/runtime.md", "references/workflows/feature.md",
               "references/workflows/bug.md", "references/workflows/spike.md"):
    check(phrase in skill, f"SKILL.md missing load instruction {phrase}")
check("human-gates.md" not in skill and "roles/shared.md" not in skill,
      "Coordinator still loads a deleted reference")
check("Developer performs implementation plus verification" in skill,
      "Coordinator must assign verification to Developer")

roles = ("intent", "spec", "architect", "developer", "reviewer", "researcher")
for name in roles:
    path = REFS / "roles" / f"{name}.md"
    content = path.read_text(encoding="utf-8") if path.is_file() else ""
    for section in ("## Purpose", "## Entry conditions", "## Procedure",
                    "## Checklist", "## Output", "## Exit conditions"):
        check(section in content, f"roles/{name}.md missing section {section}")
    check("- [ ]" in content, f"roles/{name}.md has no mandatory checklist")

for task in ("feature", "bug", "spike"):
    content = (REFS / "workflows" / f"{task}.md").read_text(encoding="utf-8")
    check(all(mode in content for mode in ("Quick", "Standard", "Extended")),
          f"{task} workflow missing mode applicability")
    check("Extended" in content and ".md" in content,
          f"{task} workflow missing Extended artifact rules")

grade_text = (ROOT / "tests/evals/grade.py").read_text(encoding="utf-8")
route_section = grade_text.split("ROUTES = {", 1)[1].split("}", 1)[0]
check("verification" not in route_section,
      "evaluation grader still has standalone verification stage")
check("ARTIFACTS" in grade_text, "evaluation grader lacks role-to-artifact mapping")

suite = read_json(ROOT / "tests/evals/scenarios.json")
check(suite.get("schema_version") == 1, "eval suite schema_version mismatch")
cases = suite.get("scenarios", [])
check(isinstance(cases, list) and len(cases) >= 9, "too few behavioral evaluation scenarios")
if isinstance(cases, list):
    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    check(len(ids) == len(set(ids)), "duplicate evaluation scenario IDs")
    check({case.get("task_type") for case in cases if isinstance(case, dict)} == {"feature", "bug", "spike"},
          "evaluation scenarios do not cover exactly the 3 task types")
    for case in cases:
        if isinstance(case, dict):
            required = case.get("required")
            check(isinstance(required, list) and bool(required),
                  f"{case.get('id')}: missing expected checks")
            if isinstance(required, list):
                check(len(required) == len(set(required)),
                      f"{case.get('id')}: duplicate expected checks")

for path in PLUGIN.rglob("*.md"):
    txt = path.read_text(encoding="utf-8")
    check("ai-sdlc-bootstrap" not in txt,
          f"old bootstrap reference in {path.relative_to(ROOT)}")
check(not (PLUGIN / "hooks").exists(), "unexpected auto hooks directory")
check(not (PLUGIN / "mcp.json").exists(), "unexpected automatic MCP")
check((ROOT / "docs/TASK_ROUTES.md").is_file(), "human task routes missing")

# Practice ownership and role-to-practice references.
developer = (REFS / 'roles/developer.md').read_text(encoding='utf-8')
architect = (REFS / 'roles/architect.md').read_text(encoding='utf-8')
reviewer = (REFS / 'roles/reviewer.md').read_text(encoding='utf-8')
researcher = (REFS / 'roles/researcher.md').read_text(encoding='utf-8').lower()
coverage = (REFS / 'practices/coverage.md').read_text(encoding='utf-8')
delegation = (REFS / 'practices/delegation.md').read_text(encoding='utf-8').lower()
workspace = (REFS / 'practices/workspace.md').read_text(encoding='utf-8').lower()
smallest_change = (REFS / 'practices/smallest-change.md').read_text(encoding='utf-8')
check('practices/smallest-change.md' in skill,
      'Coordinator must load smallest-change for Architect and Developer')
check('practices/smallest-change.md' in architect and 'practices/smallest-change.md' in developer,
      'Architect and Developer must share the smallest-change practice')
for phrase in ('Does it need to exist?', 'Already in this codebase?', 'Standard library or platform',
               'Already-installed dependency?', 'smallest complete', 'all relevant callers'):
    check(phrase.lower() in smallest_change.lower(),
          f'smallest-change practice missing principle: {phrase}')
check('practices/tdd.md' in architect and 'practices/tdd.md' in developer and 'practices/tdd.md' in reviewer,
      'Architect, Developer and Reviewer must refer to the single TDD practice')
check('RED → GREEN → REFACTOR' not in developer and '**RED:**' not in developer,
      'Developer duplicates the normative TDD sequence')
check('independent AC' in developer and 'delegation.md' in developer,
      'Developer must define independent-slice parallelism and delegate to its practice')
check('operational' in architect.lower() and 'trade-off' in architect.lower(),
      'Architect is missing operational assessment or decision rationale')
check('confidence' in researcher and 'contrary evidence' in researcher,
      'Researcher is missing evidence confidence/contrary evidence')
check('## Finding severity' in reviewer, 'Reviewer is missing finding severity definitions')
check('callers/consumers' in reviewer and 'concrete input' in reviewer.lower()
      and 'expected load' in reviewer.lower(),
      'Reviewer must trace impacted code beyond the diff and validate concrete findings/operating context')
check('## Finding severity' in reviewer and 'Trigger and problem' in reviewer
      and 'Smallest safe fix' in reviewer and 'Impact if unchanged' in reviewer,
      'Reviewer findings must explain trigger, fix and impact in a consistent format')
check('REQUIRED' in coverage and 'VERIFY' in coverage,
      'Coverage must own requirement versus verification classification')
check('independent reviewer requirement' in delegation and 'parallel work' in delegation,
      'Delegation must own independent review and parallel execution rules')
check('actual worker dispatch' not in workspace and 'parallel/serial execution rules' not in workspace,
      'Workspace repeats delegation execution policy; link to delegation.md instead')
check('RED/GREEN' not in runtime and 'AI_PASS' in runtime,
      'Coordinator runtime contains detailed TDD procedure or lacks review invariant')
check('human-gates.md' not in runtime and 'human-gates.md' not in skill,
      'runtime/Coordinator references removed human-gates.md')

# Agent instructions must not depend on human-only docs/ pages.
for path in SKILLS.rglob('*.md'):
    check('docs/' not in path.read_text(encoding='utf-8'),
          f'agent skill must not depend on human-only docs/: {path.relative_to(ROOT)}')

# Validate local Markdown links throughout the repository. Ignore examples in fenced blocks.
link_pattern = r'(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)'
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    content = path.read_text(encoding='utf-8')
    content = re.sub(r'```.*?```|~~~.*?~~~', '', content, flags=re.DOTALL)
    for target in re.findall(link_pattern, content):
        target = target.strip('<>')
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        target_path = target.split('#', 1)[0].split('?', 1)[0]
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f'{path.relative_to(ROOT)}: link escapes repository: {target}')
            continue
        check(resolved.exists(), f'{path.relative_to(ROOT)}: broken local Markdown link: {target}')

check((ROOT / 'docs/TASK_RECORDS.md').is_file(), 'human task-record guide missing')
extended_guide = (ROOT / 'docs/EXTENDED.md').read_text(encoding='utf-8')
check('## Durable record' not in extended_guide, 'EXTENDED.md duplicates the durable-record guide')
check('TASK_RECORDS.md' in extended_guide, 'EXTENDED.md must point to the dedicated task-record guide')
for path in PLUGIN.rglob('*.md'):
    content = path.read_text(encoding='utf-8')
    check('core/human-gates.md' not in content,
          f'stale removed human-gates reference in {path.relative_to(ROOT)}')

required_ids = {case.get('id') for case in cases if isinstance(case, dict)}
for expected_id in ('research_evidence_quality', 'architect_tradeoffs_operational_risk',
                    'parallel_independent_ac_slices', 'parallel_dependent_slices_serial',
                    'review_findings_severity', 'smallest_complete_change',
                    'review_impact_beyond_diff'):
    check(expected_id in required_ids, f'missing behavioral eval {expected_id}')

if errors:
    print("\n".join("FAIL: " + error for error in errors))
    sys.exit(1)
print("PASS: manifests, routes, modes, role procedures/checklists, artifact mappings and eval schemas (static only)")
