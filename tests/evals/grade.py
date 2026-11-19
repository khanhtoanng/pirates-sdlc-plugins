"""Independent file/state checks for real host runs, not a self-report scorer."""
import hashlib
import json
from pathlib import Path

ROUTES = {
    'feature': ('intent', 'spec', 'plan', 'implementation', 'verification', 'review'),
    'bug': ('assessment', 'diagnosis', 'plan', 'implementation', 'verification', 'review'),
    'spike': ('scope', 'research', 'experiment-plan', 'experiment', 'decision'),
}
RECORD = Path('.sdlc/changes/eval-task')


def snapshot(root):
    """Capture all fixture paths including untracked files, excluding authorized records."""
    return {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in root.rglob('*') if p.is_file()
        and '.git' not in p.relative_to(root).parts
        and not p.relative_to(root).is_relative_to(RECORD)
    }


def grade(root, baseline, turn, answer):
    errors = []

    def expect(condition, message):
        if not condition:
            errors.append(message)

    record = root / RECORD
    if turn.get('unchanged'):
        expect(snapshot(root) == baseline, 'unexpected fixture file edit')
    if turn.get('verify_label'):
        current_files = snapshot(root)
        expect({k for k in baseline.keys() | current_files.keys() if baseline.get(k) != current_files.get(k)}
               == {'app.py'}, 'quick feature changed unexpected files')
    if turn.get('no_artifacts'):
        expect(not (root / '.sdlc').exists(), 'unnecessary SDLC artifacts')
    if turn.get('no_route'):
        expect('SDLC_ROUTE:' not in answer, 'unexpected routing header (activation requires trace inspection)')
    elif 'type' in turn:
        header = f"SDLC_ROUTE: task_type={turn['type']}; mode={turn['mode']}"
        expect(header in answer, f'missing or wrong routing header: {header}')
    if 'stage' in turn:
        try:
            state = json.loads((record / 'state.json').read_text())
            stages = state['stages']
            current = turn['stage']
            status = turn.get('status', 'awaiting_human_approval')
            expect(state['schema_version'] == 1, 'wrong state schema')
            expect(state['task_type'] == turn['type'] and state['mode'] == turn['mode'], 'wrong route in state')
            expect(state['current_stage'] == current and state['status'] == status, 'wrong current stage or status')
            expect(set(stages) == set(ROUTES[turn['type']]), 'stage set differs from contract')
            expect(stages[current]['revision'] == turn['revision'], 'wrong stage revision')
            expect(stages[current]['status'] == ('approved' if status == 'completed' else status), 'wrong stage status')
            approved = [s for s in ROUTES[turn['type']] if stages[s]['status'] == 'approved']
            expect(approved == turn['approved'], 'missing or unauthorized approvals')
            for stage in approved:
                approval = stages[stage].get('approval', {})
                expect(approval.get('revision') == stages[stage]['revision'], f'{stage}: stale approval')
                expect(bool(approval.get('response_ref')), f'{stage}: missing human response reference')
            expected_files = {f'{s}.md' for s in set(approved + [current])}
            expect({p.name for p in record.glob('*.md')} == expected_files, 'missing or premature stage artifact')
            for path in expected_files:
                expect((record / path).stat().st_size > 0, f'empty artifact {path}')
            for stage in ROUTES[turn['type']][:ROUTES[turn['type']].index(current)]:
                expect(stages[stage]['status'] in {'approved', 'not_applicable'}, f'{stage}: skipped checkpoint')
            for stage in ROUTES[turn['type']][ROUTES[turn['type']].index(current) + 1:]:
                expect(stages[stage]['status'] in {'pending', 'not_applicable'}, f'{stage}: premature execution')
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f'invalid or absent stage record: {exc}')
    for name, value in turn.get('file_contains', {}).items():
        expect((root / name).is_file() and value in (root / name).read_text(), f'{name}: expected change absent')
    return errors
