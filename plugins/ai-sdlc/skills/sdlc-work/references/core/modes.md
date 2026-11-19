# Mode selection (independent of task type)

`auto` is the default selector, not an execution mode. After proportionate read-only inspection, choose the smallest justified mode. A user may request more rigor; never downgrade an explicit higher mode. Never lower a mode during a run without explicit human agreement and resolved risk.

| Dimension | Quick (all relevant criteria) | Standard (default otherwise) | Extended (any material trigger) |
|---|---|---|---|
| Requirements | Known, bounded, unambiguous | Focused clarification | Consequential new business rules or unresolved high-impact choices |
| Design | Existing pattern, reversible | Moderate changes | Significant architecture or critical dependency changes |
| Data | No sensitive changes | Compatible/reversible | Irreversible data loss, destructive migration, sensitive data |
| Security | No sensitive impact | Routine safeguards | Material auth, privacy, security or compliance risk |
| Interfaces | Predictable | Multiple components, compatible | Breaking contract, critical integration or complex rollout |
| Operations | Low impact, ordinary local edits | Normal risk | High production/availability impact or irreversible infrastructure |

1. Record observed risk drivers and relevant unknowns. Explicit Extended always wins. Any evidenced material high-risk trigger sets Extended, even if Quick requested. If a consequential risk is unknown, investigate or ask before editing; never presume low risk.
2. Quick only if all relevant criteria are low-risk and the desired behavior is established. Otherwise Standard unless Extended warranted. Multiple repositories alone do not imply Extended. Respect requested Standard as a minimum.
3. Announce requested_mode, mode, reason, risk drivers and scope. Reassess at each stage and on new information; if escalation occurs, suspend downstream work and present all prior applicable outputs for approval in sequence, beginning with the earliest unapproved stage. Preserve earlier evidence but do not retroactively claim approval.
4. For Spike, classify research effort and decision impact, not permission to implement; high-risk experiments require separate approval. Never silently transition to implementation.

| Mode | Documents | Human checkpoints |
|---|---|---|
| quick | Compact chat/result; existing ticket when useful | Material unknowns and actual authority only |
| standard | Existing ticket/PR or one approved compact record for continuity | Material WHAT/HOW/scope decisions and actual authority |
| extended | Durable stage artifacts and state or equivalent existing tracker sections | Mandatory explicit human review and approval after EVERY applicable stage, in order (human-gates.md) |

Examples: label/quick; customer status feature/standard; payment security bug/extended; compare logging libraries/quick; investigate production database migration/extended. Do not choose based on guessed file counts or arbitrary point scores.
