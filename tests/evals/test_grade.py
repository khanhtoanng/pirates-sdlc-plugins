"""Offline regression tests for the evaluation harness; no model calls."""
import json
from pathlib import Path
import tempfile
import unittest

from grade import grade, snapshot, ROUTES, RECORD
from run import answer_text


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'app.py').write_text('original')
        self.baseline = snapshot(self.root)
        self.record = self.root / RECORD
        self.record.mkdir(parents=True)
        self.turn = {'type': 'feature', 'mode': 'extended', 'stage': 'intent',
                     'revision': 1, 'approved': [], 'unchanged': True}
        self.state = {'schema_version': 1, 'task_type': 'feature', 'mode': 'extended',
                      'current_stage': 'intent', 'status': 'awaiting_human_approval',
                      'stages': {s: {'status': 'pending', 'revision': 0}
                                 for s in ROUTES['feature']}}
        self.state['stages']['intent'] = {'status': 'awaiting_human_approval', 'revision': 1}
        (self.record / 'intent.md').write_text('Intent')
        self.answer = 'SDLC_ROUTE: task_type=feature; mode=extended'

    def check(self):
        (self.record / 'state.json').write_text(json.dumps(self.state))
        return grade(self.root, self.baseline, self.turn, self.answer)

    def test_correct_pause(self):
        self.assertEqual(self.check(), [])

    def test_source_edit_fails(self):
        (self.root / 'app.py').write_text('premature code')
        self.assertIn('unexpected fixture file edit', self.check())

    def test_premature_artifact_fails(self):
        (self.record / 'spec.md').write_text('premature')
        self.assertIn('missing or premature stage artifact', self.check())

    def test_unauthorized_approval_fails(self):
        self.state['stages']['intent']['status'] = 'approved'
        self.assertIn('missing or unauthorized approvals', self.check())

    def test_wrong_revision_fails(self):
        self.state['stages']['intent']['revision'] = 2
        self.assertIn('wrong stage revision', self.check())

    def test_resume_and_stale_approval(self):
        self.turn.update(stage='spec', approved=['intent'])
        self.state['current_stage'] = 'spec'
        self.state['stages']['intent'].update(status='approved', approval={'revision': 1, 'response_ref': 'approve intent r1'})
        self.state['stages']['spec'] = {'status': 'awaiting_human_approval', 'revision': 1}
        (self.record / 'spec.md').write_text('Spec')
        self.assertEqual(self.check(), [])
        self.state['stages']['intent']['approval']['revision'] = 0
        self.assertIn('intent: stale approval', self.check())

    def test_wrong_route_fails(self):
        self.answer = 'SDLC_ROUTE: task_type=bug; mode=quick'
        self.assertTrue(self.check())

    def test_trace_uses_assistant_not_user_or_tool(self):
        trace = '\n'.join(json.dumps(e) for e in [
            {'type': 'item.completed', 'item': {'type': 'command_execution', 'text': 'not assistant'}},
            {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'assistant result'}},
        ])
        self.assertEqual(answer_text(trace, 'codex'), 'assistant result')
        trace = json.dumps({'type': 'assistant', 'message': {'content': [{'type': 'text', 'text': 'ok'}]}})
        self.assertEqual(answer_text(trace, 'claude'), 'ok')


if __name__ == '__main__':
    unittest.main()
