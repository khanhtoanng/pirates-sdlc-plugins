"""Offline regression tests for the evaluation harness; no model calls."""
import json
from pathlib import Path
import tempfile
import unittest

from grade import ARTIFACTS, grade, snapshot, ROUTES
from run import answer_text


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "app.py").write_text("original", encoding="utf-8")
        self.baseline = snapshot(self.root)
        self.record = self.root / ".sdlc/changes/eval-task"
        self.record.mkdir(parents=True)
        self.turn = {
            "type": "feature", "mode": "extended", "stage": "intent",
            "revision": 1, "approved": [], "unchanged": True,
        }
        self.state = {
            "schema_version": 1, "task_type": "feature", "mode": "extended",
            "current_stage": "intent", "status": "awaiting_human_approval",
            "stages": {stage: {"status": "pending", "revision": 0}
                       for stage in ROUTES["feature"]},
        }
        self.state["stages"]["intent"] = {
            "status": "awaiting_human_approval", "revision": 1,
        }
        (self.record / ARTIFACTS["feature"]["intent"]).write_text("Intent", encoding="utf-8")
        self.answer = "SDLC_ROUTE: task_type=feature; mode=extended"

    def check(self):
        (self.record / "state.json").write_text(json.dumps(self.state), encoding="utf-8")
        return grade(self.root, self.baseline, self.turn, self.answer)

    def test_correct_pause(self):
        self.assertEqual(self.check(), [])

    def test_source_edit_fails_before_implementation(self):
        (self.root / "app.py").write_text("premature code", encoding="utf-8")
        self.assertIn("unexpected fixture file edit", self.check())

    def test_premature_artifact_fails(self):
        (self.record / ARTIFACTS["feature"]["spec"]).write_text("premature", encoding="utf-8")
        self.assertIn("premature stage artifact", " ".join(self.check()))

    def test_unauthorized_approval_fails(self):
        self.state["stages"]["intent"]["status"] = "approved"
        self.assertIn("missing or unauthorized approvals", self.check())

    def test_wrong_revision_fails(self):
        self.state["stages"]["intent"]["revision"] = 2
        self.assertIn("wrong stage revision", self.check())

    def test_resume_and_stale_approval(self):
        self.turn.update(stage="spec", approved=["intent"])
        self.state["current_stage"] = "spec"
        self.state["stages"]["intent"].update(
            status="approved",
            approval={"revision": 1, "response_ref": "approve intent r1"},
        )
        self.state["stages"]["spec"] = {
            "status": "awaiting_human_approval", "revision": 1,
        }
        (self.record / ARTIFACTS["feature"]["spec"]).write_text("Spec", encoding="utf-8")
        self.assertEqual(self.check(), [])
        self.state["stages"]["intent"]["approval"]["revision"] = 0
        self.assertIn("intent: stale approval", self.check())

    def test_standalone_verification_stage_is_rejected(self):
        self.state["stages"]["verification"] = {"status": "pending", "revision": 0}
        errors = self.check()
        self.assertTrue(any("stage set differs" in error or "standalone verification" in error
                            for error in errors))

    def test_wrong_route_fails(self):
        self.answer = "SDLC_ROUTE: task_type=bug; mode=quick"
        self.assertTrue(self.check())

    def test_implementation_artifact_must_include_verification_evidence(self):
        self.turn.update(stage="implementation", approved=["intent", "spec", "plan"],
                         unchanged=False, must_change_files=["app.py"],
                         artifact_contains=["AC-01", "verification results", "python -m unittest"])
        self.state["current_stage"] = "implementation"
        for stage in ("intent", "spec", "plan"):
            self.state["stages"][stage] = {
                "status": "approved", "revision": 1,
                "approval": {"revision": 1, "response_ref": f"approve {stage} r1"},
            }
            (self.record / ARTIFACTS["feature"][stage]).write_text(stage, encoding="utf-8")
        self.state["stages"]["implementation"] = {
            "status": "awaiting_human_approval", "revision": 1,
        }
        (self.record / ARTIFACTS["feature"]["implementation"]).write_text(
            "AC-01. Verification results. python -m unittest", encoding="utf-8")
        (self.root / "app.py").write_text("implemented", encoding="utf-8")
        self.assertEqual(self.check(), [])

    def test_trace_uses_assistant_not_user_or_tool(self):
        trace = "\n".join(json.dumps(event) for event in [
            {"type": "item.completed", "item": {"type": "command_execution", "text": "not assistant"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "assistant result"}},
        ])
        self.assertEqual(answer_text(trace, "codex"), "assistant result")
        trace = json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": "ok"}]}})
        self.assertEqual(answer_text(trace, "claude"), "ok")

    def test_copilot_jsonl_extracts_assistant_messages_only(self):
        trace = "\n".join(json.dumps(event) for event in [
            {"type": "tool.execution_complete", "data": {"result": {"content": "not assistant output"}}},
            {"type": "assistant.message", "data": {"content": "Copilot final response"}},
        ])
        self.assertEqual(answer_text(trace, "copilot"), "Copilot final response")


if __name__ == "__main__":
    unittest.main()
