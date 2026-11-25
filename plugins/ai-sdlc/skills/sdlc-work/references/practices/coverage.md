# Requirement and verification coverage

Use this practice when deciding whether a candidate is a new accepted behavior rule, a verification example, a question for the owner, or unnecessary scope. It applies to Feature requirements and credible Bug regression checks. A Spike uses a bounded research question and decision, not a Feature AC inventory.

## Classification

| Class | Destination | Decision test |
|---|---|---|
| `REQUIRED` | Source-linked observable Feature AC or mandatory existing contract | Owner-accepted behavior, verified existing contract or applicable mandatory safeguard. A proposed new rule requires owner acceptance. |
| `VERIFY` | Test/example/check under an accepted AC or Bug symptom | An input, boundary, negative path, state or credible failure that tests an existing rule; it is not a new AC by default. |
| `DECISION` | Coordinator asks the owner | A consequential unresolved WHAT, data/rights, compatibility or scope choice changes the expected result. |
| `DEFER` | Brief out-of-scope note | Useful adjacent behavior is not needed for the accepted outcome. |
| `REJECT` | Omit | Unsupported speculation, redundant variants or irrelevant scenarios. |

For a Bug, the original symptom and expected-versus-actual contract are the primary target. Do not turn every discovered edge case into a Feature AC. Investigate unknown existing behavior; do not label it verified. Do not defer a discovered vulnerability, data-loss hazard, mandatory safeguard or serious broken contract for brevity.

## Decision filter

1. **Grounded:** Which accepted owner decision, ticket, observed interface/code, documented contract or mandatory control requires it?
2. **Material:** Could failure significantly affect the outcome, rights, privacy, integrity, compatibility, accessibility, security, availability or recovery?
3. **Distinct:** Is this a different externally observable rule, or another input that exercises the same rule?
4. **Actionable:** Would documenting it change implementation, verification, a human decision or review?
5. **Sufficient:** Are all accepted rules testable and credible high-impact hazards considered, with no further distinct rule or meaningful defect-detection value?

Use Example Mapping lightly: **Story → business Rules (ACs) → representative Examples (VERIFY) → consequential Questions (DECISION)**. Group related ACs by user outcome. Avoid speculative combinations and fake precision.

## Traceability

Keep one authoritative AC set. Every accepted AC has a stable ID, source/owner decision and observable expected result. The downstream plan maps each AC to implementation slices and test seams; Developer maps each AC to actual code and verification evidence; Reviewer checks the same complete AC set. These later mappings are owned by Architect, Developer and Reviewer respectively, not duplicated here.

The human-facing summary must identify every AC ID and its meaning. Keep the full AC text and provenance accessible in the authoritative ticket/PR or current authorized record.

Apply this classification consistently in Quick, Standard and Extended. Mode-specific workflow depth and approvals are defined only in `core/modes.md`.
