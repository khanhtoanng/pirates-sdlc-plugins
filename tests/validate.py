#!/usr/bin/env python3
"""Dependency-free package and workflow contract validation; not a host eval."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ai-sdlc"
REFS = PLUGIN / "skills" / "sdlc-work" / "references"
VERSION = "0.7.0"
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
    path = PLUGIN / "skills" / name / "SKILL.md"
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
)
for name in required_references:
    check((REFS / f"{name}.md").is_file(), f"missing reference {name}.md")

for removed in ("core/human-gates.md", "roles/shared.md", "roles/verifier.md"):
    check(not (REFS / removed).exists(), f"obsolete role/reference still exists: {removed}")

for host in ("claude", "cursor", "codex"):
    check((REFS / "hosts" / f"{host}.md").is_file(), f"missing host adapter {host}.md")
check((PLUGIN / "agents/sdlc-reviewer.md").is_file(), "missing native reviewer")

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

if errors:
    print("\n".join("FAIL: " + error for error in errors))
    sys.exit(1)
print("PASS: manifests, routes, modes, role procedures/checklists, artifact mappings and eval schemas (static only)")
