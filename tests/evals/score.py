#!/usr/bin/env python3
"""Score manually collected host observations against declared scenario expectations.

A PASS is self-reported by the evaluator and requires a trace/evidence pointer;
this script cannot validate agent independence, actual environment, or truth of claims.
Run with --self-test to verify scorer behavior without a host.
"""
import argparse
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SCENARIOS = HERE / 'scenarios.json'


def load_cases():
    raw = json.loads(SCENARIOS.read_text(encoding='utf-8'))
    assert raw['schema_version'] == 1
    ids = [c['id'] for c in raw['scenarios']]
    assert len(ids) == len(set(ids)), 'duplicate scenario IDs'
    for c in raw['scenarios']:
        assert c['task_type'] in {'feature', 'bug', 'spike'}
        assert c['required'] and len(c['required']) == len(set(c['required']))
    return {c['id']: c for c in raw['scenarios']}


def evaluate(observation, cases):
    errors = []
    case = cases.get(observation.get('scenario'))
    if not case:
        return False, ['unknown scenario']
    if observation.get('host') not in {'claude', 'cursor', 'codex', 'copilot'}:
        errors.append('host must be claude, cursor, codex or copilot')
    if not isinstance(observation.get('run_id'), str) or not observation['run_id'].strip():
        errors.append('missing run_id for evidence trace')
    observations = observation.get('observations')
    if not isinstance(observations, dict):
        return False, errors + ['observations must be an object']
    for check in case['required']:
        o = observations.get(check)
        if not isinstance(o, dict):
            errors.append(f'{check}: missing observation')
            continue
        if o.get('status') != 'pass':
            errors.append(f"{check}: {o.get('status', 'no status')}")
        if not isinstance(o.get('evidence'), str) or len(o['evidence'].strip()) < 8:
            errors.append(f'{check}: missing concrete trace/artifact evidence')
    unknown = sorted(set(observations) - set(case['required']))
    if unknown:
        errors.append('unexpected check IDs: ' + ', '.join(unknown))
    return not errors, errors


def self_test(cases):
    c = cases['spike_research_only']
    good = {'scenario': c['id'], 'host': 'claude', 'run_id': 'trace-001',
            'observations': {k: {'status': 'pass', 'evidence': f'trace-001 lines 10-20: {k}'} for k in c['required']}}
    ok, errs = evaluate(good, cases)
    assert ok, errs
    good['observations'][c['required'][0]]['status'] = 'fail'
    ok, errs = evaluate(good, cases)
    assert not ok and errs
    good['observations'][c['required'][0]]['status'] = 'pass'
    good['observations'][c['required'][0]]['evidence'] = ''
    ok, errs = evaluate(good, cases)
    assert not ok and errs
    print('PASS: eval scorer self-test (synthetic data only; no agent runs)')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('observation_json', nargs='?', help='JSON with scenario, host, run_id and concrete per-check evidence')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    cases = load_cases()
    if args.self_test:
        self_test(cases)
        return 0
    if not args.observation_json:
        parser.error('provide observation_json or --self-test')
    o = json.loads(Path(args.observation_json).read_text(encoding='utf-8'))
    ok, errors = evaluate(o, cases)
    if ok:
        print(f"PASS (reported evidence present; human verification required): {o['scenario']} on {o['host']}")
        return 0
    print('FAIL: ' + '\nFAIL: '.join(errors))
    return 1


if __name__ == '__main__':
    sys.exit(main())
