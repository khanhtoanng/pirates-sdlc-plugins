"""Independent file/state checks for real host runs, not a self-report scorer."""
import hashlib
import json
from pathlib import Path

ROUTES = {
    "feature": ("intent", "spec", "plan", "implementation", "review"),
    "bug": ("diagnosis_plan", "implementation", "review"),
    "spike": ("scope", "research", "experiment_plan", "experiment", "decision"),
}
ARTIFACTS = {
    "feature": {
        "intent": "01-intent.md",
        "spec": "02-spec.md",
        "plan": "03-plan.md",
        "implementation": "04-implementation.md",
        "review": "05-review.md",
    },
    "bug": {
        "diagnosis_plan": "01-diagnosis-plan.md",
        "implementation": "02-implementation.md",
        "review": "03-review.md",
    },
    "spike": {
        "scope": "01-scope.md",
        "research": "02-research.md",
        "experiment_plan": "03-experiment-plan.md",
        "experiment": "04-experiment.md",
        "decision": "05-decision.md",
    },
}
RECORD = Path(".sdlc/changes/eval-task")


def snapshot(root):
    """Capture fixture paths including untracked files, excluding authorized task records."""
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(root).parts
        and not path.relative_to(root).is_relative_to(RECORD)
    }


def changed_paths(before, after):
    return {
        path for path in before.keys() | after.keys()
        if before.get(path) != after.get(path)
    }


def grade(root, baseline, turn, answer):
    errors = []

    def expect(condition, message):
        if not condition:
            errors.append(message)

    record = root / RECORD
    current_files = snapshot(root)
    if turn.get("unchanged"):
        expect(current_files == baseline, "unexpected fixture file edit")
    if turn.get("must_change_files"):
        changed = changed_paths(baseline, current_files)
        expect(set(turn["must_change_files"]).issubset(changed),
               "expected implementation files were not changed")
    if turn.get("only_change_files"):
        changed = changed_paths(baseline, current_files)
        expect(changed == set(turn["only_change_files"]),
               "changed files differ from allowed fixture file set")
    if turn.get("verify_label"):
        expect("app.py" in changed_paths(baseline, current_files),
               "quick feature did not change app.py")
    if turn.get("no_artifacts"):
        expect(not (root / ".sdlc").exists(), "unnecessary SDLC artifacts")

    if turn.get("no_route"):
        expect("SDLC_ROUTE:" not in answer, "unexpected routing header")
    elif "type" in turn:
        expected_header = f"SDLC_ROUTE: task_type={turn['type']}; mode={turn['mode']}"
        expect(expected_header in answer, f"missing or wrong routing header: {expected_header}")

    if "stage" in turn:
        task_type = turn["type"]
        route = ROUTES[task_type]
        try:
            state = json.loads((record / "state.json").read_text(encoding="utf-8"))
            stages = state["stages"]
            current = turn["stage"]
            status = turn.get("status", "awaiting_human_approval")
            expect(state["schema_version"] == 1, "wrong state schema")
            expect(state["task_type"] == task_type and state["mode"] == turn["mode"],
                   "wrong route in state")
            expect(state["current_stage"] == current and state["status"] == status,
                   "wrong current stage or status")
            expect(set(stages) == set(route), "stage set differs from role workflow")
            expect("verification" not in stages, "standalone verification stage must not exist")
            expect(current in route, "unknown current stage")
            expect(stages[current]["revision"] == turn["revision"], "wrong stage revision")
            expected_current_status = "approved" if status == "completed" else status
            expect(stages[current]["status"] == expected_current_status,
                   "wrong current stage status")

            approved = [stage for stage in route if stages[stage]["status"] == "approved"]
            expect(approved == turn["approved"], "missing or unauthorized approvals")
            for stage in approved:
                approval = stages[stage].get("approval", {})
                expect(approval.get("revision") == stages[stage]["revision"],
                       f"{stage}: stale approval")
                expect(bool(approval.get("response_ref")), f"{stage}: missing human response reference")

            expected_artifacts = set()
            completed_stages = set(approved + [current])
            for stage in completed_stages:
                if stages[stage]["status"] != "not_applicable":
                    expected_artifacts.add(ARTIFACTS[task_type][stage])
            actual_artifacts = {path.name for path in record.glob("*.md")}
            expect(actual_artifacts == expected_artifacts,
                   "missing, unexpected or premature stage artifact")
            expect("verification.md" not in actual_artifacts,
                   "verification.md is not a separate artifact")
            for filename in expected_artifacts:
                expect((record / filename).is_file() and (record / filename).stat().st_size > 0,
                       f"empty or missing artifact {filename}")

            current_index = route.index(current)
            for stage in route[:current_index]:
                expect(stages[stage]["status"] in {"approved", "not_applicable"},
                       f"{stage}: skipped checkpoint")
            for stage in route[current_index + 1:]:
                expect(stages[stage]["status"] in {"pending", "not_applicable"},
                       f"{stage}: premature execution")

            if turn.get("artifact_contains"):
                current_artifact = record / ARTIFACTS[task_type][current]
                content = current_artifact.read_text(encoding="utf-8") if current_artifact.is_file() else ""
                for required in turn["artifact_contains"]:
                    expect(required.lower() in content.lower(),
                           f"{current_artifact.name}: missing required content {required!r}")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"invalid or absent stage record: {exc}")

    for name, value in turn.get("file_contains", {}).items():
        path = root / name
        expect(path.is_file() and value in path.read_text(encoding="utf-8"),
               f"{name}: expected change/content absent")

    return errors
