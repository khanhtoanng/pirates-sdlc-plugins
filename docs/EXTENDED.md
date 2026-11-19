# Extended mode — review every stage

Run e.g. `/ai-sdlc:sdlc-work feature extended Add customer status` (Claude), or `Use sdlc-work feature extended ...` (Cursor/Codex). For high-risk tasks the coordinator escalates even if Quick was requested.

| Feature | Bug | Spike |
|---|---|---|
| Intent | Assessment | Scope |
| Spec | Diagnosis | Research |
| Plan | Plan | Optional experiment plan |
| Implementation | Implementation | Optional experiment |
| Verification | Verification | Decision |
| Review | Review | — |

The agent validates each output, presents a concise summary and **ends its turn while awaiting explicit approval**. It does not start the next role, create its artifact, or poll. Reply to the current checkpoint:

- `approve intent r1` — approve this artifact, not future stages.
- `request changes to spec r1: ...` — revise and request approval again.
- `reject plan r2` — stop.
- `Use sdlc-work resume .sdlc/changes/add-customer-status` — recover pending state; approve the correct revision separately.

An accepted requirement can be reused without re-litigating it, but Extended still presents the stage for review. Approval of a plan does not authorize unrelated edits or privileged operations. Spike completion never authorizes production code.

## Artifacts

Use the existing ticket/PR if it has revisioned stage sections. Otherwise approve one task directory in a selected writable repository:

```text
.sdlc/changes/add-customer-status/
  state.json
  intent.md
  spec.md
  plan.md
  implementation.md
  verification.md
  review.md
```

Each file is created **only when its stage runs**. A review card identifies artifact and revision, outcome, risk and evidence; Spec maps every AC ID to the full inspectable requirement. State records pending stage, approval history, sources and scope. Material changes invalidate affected approvals and evidence; resume rechecks them. Do not commit artifacts without separate approval. If persistence isn't allowed, the agent stops with a pasteable handoff and marks durability unverified.

These are workflow instructions, not a security boundary; independent evaluation measures compliance. Real mandatory tool restrictions require host permissions or an external controller.
