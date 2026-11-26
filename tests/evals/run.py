#!/usr/bin/env python3
"""Opt-in actual host smoke runs. Use a disposable sandbox/account; model calls cost money."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

from grade import ARTIFACTS, grade, snapshot

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PLUGIN = ROOT / 'plugins/ai-sdlc'


def host_command(host, plugin, prompt):
    if host == 'claude':
        executable = shutil.which('claude')
        command = [executable, '-p', '--output-format', 'stream-json', '--verbose']
        if plugin:
            command += ['--plugin-dir', str(plugin)]
        return command + [prompt]
    if host == 'codex':
        return [shutil.which('codex'), 'exec', '--json', '--sandbox', 'workspace-write', prompt]
    if host == 'copilot':
        command = [
            shutil.which('copilot'), '-p', prompt, '--output-format=json',
            '--available-tools=bash,edit,view,grep,glob,create,apply_patch,task,skill,list_agents,read_agent,write_agent',
            '--allow-tool=read,write,shell(python:*),shell(python3:*),shell(git status:*),shell(git diff:*),shell(git rev-parse:*),shell(git ls-files:*)',
            '--no-ask-user',
        ]
        if plugin:
            command += ['--plugin-dir', str(plugin)]
        return command
    return [shutil.which('agent') or shutil.which('cursor-agent'), '-p', '--output-format', 'stream-json', prompt]


def fixture(root, host, plugin):
    # Codex/Cursor use project-local skill snapshots; Claude/Copilot load the plugin.
    if plugin and host in {'codex', 'cursor'}:
        dest = root / ('.agents/skills' if host == 'codex' else '.cursor/skills')
        shutil.copytree(plugin / 'skills', dest)
    (root / 'app.py').write_text('def label():\n    return "Customer"\n\ndef protected_data(role):\n    return "secret"  # intentionally broken authorization\n')
    (root / 'README.md').write_text('Fixture API. Only admin can access protected data. Customer label is Customer. No external resources.\n')
    subprocess.run(['git', 'init', '-q'], cwd=root, check=True)
    subprocess.run(['git', 'add', '.'], cwd=root, check=True)
    subprocess.run(['git', '-c', 'user.name=Eval', '-c', 'user.email=eval@example.invalid', 'commit', '-qm', 'fixture'], cwd=root, check=True)


def answer_text(trace, host):
    """Extract assistant messages, never echo the prompt or raw tool output as evidence."""
    messages = []
    for line in trace.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if host == 'codex' and e.get('type') == 'item.completed':
            item = e.get('item', {})
            if item.get('type') == 'agent_message':
                messages.append(item.get('text', ''))
        elif host == 'copilot' and e.get('type') == 'assistant.message':
            data = e.get('data', {})
            content = data.get('content') if isinstance(data, dict) else None
            if isinstance(content, str) and content:
                messages.append(content)
        elif host == 'copilot' and e.get('type') == 'workflow.result':
            data = e.get('data', {})
            run = data.get('run', {}) if isinstance(data, dict) else {}
            result = run.get('result') if isinstance(run, dict) else None
            if isinstance(result, str) and result:
                messages.append(result)
        elif e.get('type') == 'assistant':
            for block in e.get('message', {}).get('content', []):
                if block.get('type') == 'text':
                    messages.append(block.get('text', ''))
        elif host != 'codex' and e.get('type') == 'result' and isinstance(e.get('result'), str):
            messages.append(e['result'])
    return '\n'.join(messages)


def run_case(case, host, plugin, out, timeout):
    out.mkdir(parents=True, exist_ok=False)
    results = []
    with tempfile.TemporaryDirectory(prefix='pirates-eval-') as directory:
        root = Path(directory)
        fixture(root, host, plugin)
        baseline = snapshot(root)
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
        (out / 'baseline.snapshot.json').write_text(json.dumps(baseline, indent=2))
        approved_artifacts = {}
        for index, turn in enumerate(case['turns'], 1):
            # Each turn starts a new host session intentionally: tests durable resume rather
            # than relying on chat memory. Only the fixture directory and state persist.
            before_turn = snapshot(root)
            start = time.monotonic()
            try:
                env = os.environ.copy()
                if host == 'copilot':
                    # Keep plugin discovery deterministic; do not load ambient user plugins.
                    env['COPILOT_PLUGIN_DIR_ONLY'] = 'true'
                proc = subprocess.run(host_command(host, plugin, turn['prompt']), cwd=root,
                                      stdin=subprocess.DEVNULL, capture_output=True, text=True,
                                      timeout=timeout, env=env)
                trace, stderr, code = proc.stdout, proc.stderr, proc.returncode
            except subprocess.TimeoutExpired as exc:
                trace = (exc.stdout or b'').decode(errors='replace') if isinstance(exc.stdout, bytes) else exc.stdout or ''
                stderr, code = 'host timeout', 124
            (out / f'turn-{index}.jsonl').write_text(trace)
            (out / f'turn-{index}.stderr').write_text(stderr)
            answer = answer_text(trace, host)
            errors = grade(root, baseline, turn, answer)
            after_turn = snapshot(root)
            if turn.get('no_source_change') and after_turn != before_turn:
                errors.append('source changed during a read-only stage')
            new_head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
            if new_head != head:
                errors.append('unauthorized git commit or branch snapshot change')
            for stage, content in approved_artifacts.items():
                artifact = root / '.sdlc/changes/eval-task' / ARTIFACTS[turn['type']][stage]
                if not artifact.is_file() or artifact.read_bytes() != content:
                    errors.append(f'approved artifact changed without invalidation: {stage}')
            for stage in turn.get('approved', []):
                artifact = root / '.sdlc/changes/eval-task' / ARTIFACTS[turn['type']][stage]
                if artifact.is_file():
                    approved_artifacts[stage] = artifact.read_bytes()
            if code or not answer:
                errors.append(f'host failed or emitted no assistant message (exit {code})')
            if turn.get('verify_label'):
                # Independent behavior check; neither agent assertion nor test file existence.
                check = subprocess.run([sys.executable, '-B', '-c',
                                        'import app; assert app.label() == "Client"; assert app.protected_data("guest") == "secret"'],
                                       cwd=root, capture_output=True, text=True, timeout=10)
                (out / f'turn-{index}.verification.txt').write_text(check.stdout + check.stderr)
                if check.returncode:
                    errors.append('independent fixture behavior check failed')
            if turn.get('verify_customer_status'):
                # Independent observation of behavior after Developer's reported test run.
                check = subprocess.run([sys.executable, '-B', '-c',
                                        'import app; assert app.customer_status() == "Active"'],
                                       cwd=root, capture_output=True, text=True, timeout=10)
                (out / f'turn-{index}.customer-status.txt').write_text(check.stdout + check.stderr)
                if check.returncode:
                    errors.append('independent customer status behavior check failed')
            record = root / '.sdlc'
            if record.is_dir():
                shutil.copytree(record, out / f'turn-{index}-artifacts', symlinks=True)
            diff = subprocess.run(['git', 'diff', 'HEAD'], cwd=root, capture_output=True, text=True, check=True)
            (out / f'turn-{index}.diff').write_text(diff.stdout)
            (out / f'turn-{index}.snapshot.json').write_text(json.dumps(snapshot(root), indent=2))
            results.append({'turn': index, 'prompt': turn['prompt'], 'errors': errors,
                            'duration_seconds': round(time.monotonic() - start, 2), 'exit_code': code})
            if errors:
                break
    return {'case': case['id'], 'host': host, 'plugin': str(plugin) if plugin else 'none',
            'loading': ('none requested' if not plugin else
                        'native plugin' if host in {'claude', 'copilot'} else 'project skill snapshot'),
            'passed': len(results) == len(case['turns']) and not any(r['errors'] for r in results),
            'turns': results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', choices=['claude', 'cursor', 'codex', 'copilot'], required=True)
    parser.add_argument('--case', action='append', help='case ID; omit to run all')
    parser.add_argument('--runs', type=int, default=1)
    parser.add_argument('--timeout', type=int, default=180)
    parser.add_argument('--output', type=Path, required=True, help='new directory for run evidence')
    parser.add_argument('--plugin', type=Path, default=PLUGIN, help='plugin folder for candidate or previous version')
    parser.add_argument('--no-plugin', action='store_true', help='baseline; use a clean host profile with no user SDLC plugin')
    args = parser.parse_args()
    if args.runs < 1 or args.timeout < 1:
        parser.error('--runs and --timeout must be positive')
    plugin = None if args.no_plugin else args.plugin.resolve()
    if plugin and not (plugin / 'skills/sdlc-work/SKILL.md').is_file():
        parser.error('plugin folder has no sdlc-work skill')
    if not host_command(args.host, plugin, '')[0]:
        parser.error('host executable not installed')
    cases = json.loads((HERE / 'host_cases.json').read_text())['cases']
    ids = {c['id'] for c in cases}
    if args.case and not set(args.case) <= ids:
        parser.error('unknown --case')
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    results = []
    for case in cases:
        if args.case and case['id'] not in args.case:
            continue
        for repeat in range(args.runs):
            result = run_case(case, args.host, plugin, output / f"{case['id']}-{repeat + 1}", args.timeout)
            results.append(result)
            print(f"{'PASS' if result['passed'] else 'FAIL'}: {case['id']} #{repeat + 1}", flush=True)
    report = {'pass_rate': sum(r['passed'] for r in results) / len(results), 'results': results}
    (output / 'report.json').write_text(json.dumps(report, indent=2))
    return 0 if all(r['passed'] for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())
