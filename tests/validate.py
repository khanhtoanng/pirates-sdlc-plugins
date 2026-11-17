#!/usr/bin/env python3
"""Dependency-free static package/contract validation. NOT a host behavioral eval."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins' / 'ai-sdlc'
REFS = PLUGIN / 'skills' / 'sdlc-work' / 'references'
VERSION = '0.6.0'
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{path}: {exc}')
        return {}


for label, path in [
    ('portable', PLUGIN / 'plugin.json'),
    ('Claude', PLUGIN / '.claude-plugin/plugin.json'),
    ('Cursor', PLUGIN / '.cursor-plugin/plugin.json'),
]:
    manifest = read_json(path)
    check(manifest.get('name') == 'ai-sdlc', f'{label}: invalid name')
    check(manifest.get('version') == VERSION, f'{label}: invalid version')
    if label == 'portable':
        check(manifest.get('$schema') == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
              'portable: missing manifest schema')
    if label == 'Cursor':
        check(manifest.get('skills') == './skills/' and manifest.get('agents') == './agents/',
              'Cursor: native component path mismatch')

for name in ('sdlc-work', 'sdlc-setup', 'sdlc-doctor'):
    path = PLUGIN / 'skills' / name / 'SKILL.md'
    check(path.is_file(), f'missing skill {name}')
    if path.is_file():
        txt = path.read_text(encoding='utf-8')
        parts = txt.split('---', 2)
        front = parts[1] if len(parts) >= 3 and txt.startswith('---\n') else ''
        check(bool(front) and f'name: {name}' in front, f'{name}: invalid frontmatter/name')
        check('description:' in front, f'{name}: missing description')

for name in ('routing', 'runtime', 'roles', 'coverage', 'workspace', 'review', 'tdd', 'delegation', 'integrations'):
    check((REFS / f'{name}.md').is_file(), f'missing reference {name}.md')
for name in ('claude', 'cursor', 'codex'):
    check((REFS / 'hosts' / f'{name}.md').is_file(), f'missing host adapter {name}.md')
check((PLUGIN / 'agents/sdlc-reviewer.md').is_file(), 'missing native reviewer')

for cat, label in [('.claude-plugin/marketplace.json', 'Claude'), ('.agents/plugins/marketplace.json', 'Codex')]:
    data = read_json(ROOT / cat)
    try:
        entry = data['plugins'][0]
        source = entry['source'] if isinstance(entry['source'], str) else entry['source']['path']
        check(entry['name'] == 'ai-sdlc' and source.startswith('./') and (ROOT / source).is_dir(),
              f'{label}: invalid local marketplace link')
    except Exception as exc:
        errors.append(f'{label} marketplace: {exc}')

# Behavior and loading contracts must exist and remain distinct.
router = (REFS / 'routing.md').read_text(encoding='utf-8')
runtime = (REFS / 'runtime.md').read_text(encoding='utf-8')
skill = (PLUGIN / 'skills/sdlc-work/SKILL.md').read_text(encoding='utf-8')
found_types = re.findall(r'^\| `(feature|bug|spike)` \|', router, flags=re.MULTILINE)
check(found_types == ['feature', 'bug', 'spike'], f'expected exactly 3 task routing entries, got {found_types}')
for mode in ('auto', 'quick', 'standard', 'extended'):
    check(mode in router and mode in skill, f'missing mode {mode}')
check('`spike` as a risk mode' in router, 'mode/type separation not explicit')
for term in ('<transition-gates>', '<verify-and-converge>', 'changed_snapshot', 'NOT DURABLE', 'EDIT_APPROVED'):
    check(term in runtime, f'runtime missing contract {term}')
for phrase in ('<feature-route>', '<bug-route>', '<spike-route>'):
    check(phrase in router, f'route missing {phrase}')
for phrase in ('references/routing.md', 'references/runtime.md'):
    check(phrase in skill, f'skill not loading {phrase}')
for rel in re.findall(r'`references/([\w./-]+\.md)`', skill):
    check((REFS / rel).is_file(), f'broken skill reference {rel}')

suite = read_json(ROOT / 'tests/evals/scenarios.json')
check(suite.get('schema_version') == 1, 'eval suite schema_version mismatch')
cases = suite.get('scenarios', [])
check(isinstance(cases, list) and len(cases) >= 9, 'too few behavioral scenarios')
if isinstance(cases, list):
    ids = [c.get('id') for c in cases if isinstance(c, dict)]
    check(len(ids) == len(set(ids)), 'duplicate evaluation scenario IDs')
    check({c.get('task_type') for c in cases if isinstance(c, dict)} == {'feature', 'bug', 'spike'},
          'evaluation scenarios do not cover exact 3 task types')
    for c in cases:
        if isinstance(c, dict):
            req = c.get('required')
            check(isinstance(req, list) and bool(req), f"{c.get('id')}: missing expected checks")
            if isinstance(req, list):
                check(len(req) == len(set(req)), f"{c.get('id')}: duplicate expected checks")
check((ROOT / 'tests/evals/score.py').is_file(), 'evaluation scorer missing')

for path in PLUGIN.rglob('*.md'):
    txt = path.read_text(encoding='utf-8')
    check('ai-sdlc-bootstrap' not in txt, f'old bootstrap reference in {path.relative_to(ROOT)}')
check(not (PLUGIN / 'hooks').exists(), 'unexpected auto hooks directory')
check(not (PLUGIN / 'mcp.json').exists(), 'unexpected automatic MCP')
check((ROOT / 'docs/TASK_ROUTES.md').is_file(), 'human task routes missing')

if errors:
    print('\n'.join('FAIL: ' + error for error in errors))
    sys.exit(1)
print('PASS: v0.6.0 manifests, three routes, gates, progressive skill refs, eval schemas, no automatic hooks/MCP (static only)')
