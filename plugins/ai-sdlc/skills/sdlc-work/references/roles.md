# Role contracts — one Coordinator, five logical responsibilities

`routing.md` decides which roles apply. Roles are responsibilities, not automatically five subagents, five Markdown files, or five user approvals. Workers return to Coordinator; they never approve owner decisions, grant edit scope or invoke downstream agents autonomously. `runtime.md` owns transition gates and current-snapshot semantics.

<discovery-brainstorming>
1. Inspect request, existing source, accepted contracts, project instructions and prior decisions **before asking**. Do not debate settled matters.
2. Responsibility boundary: **Intent asks WHY/WHO**, **Spec asks WHAT**, **Architect asks HOW**. Bug assessment starts at symptom/cause; Spike focuses on a bounded feasibility question. Do not make every role repeat the same brainstorm.
3. When no material uncertainty exists, state `NO_MATERIAL_UNCERTAINTY` or proceed without extra narrative. When genuine alternatives remain, compare only grounded options (often 2–3), impacts and counterevidence; no fabricated option matrix.
4. Distinguish `OBSERVED`, `SOURCE_BACKED`, `OWNER_ACCEPTED`, `PROPOSED`, `ASSUMPTION`, `UNKNOWN` and `DECISION`. Only meaningful WHAT/security/data/scope/reversibility decisions reach the Coordinator; ask one highest-impact question at a time. Never smuggle an open choice into an accepted AC.
5. Close with the result, source, scope exclusions and blockers. No brainstorm transcript or separate artifact by default. Quick = evidence check; Standard = focused uncertainty; Extended = consequential alternatives, recovery and human gating.
</discovery-brainstorming>

## Intent — product outcome / feature only when needed

**Entry:** Feature outcome/actor/scope is unsettled or risk requires explicit recheck; not a mandatory Bug or Spike phase. Inspect the actual request and existing behavior; identify WHY, WHO, outcome, success signal, material scope boundary and non-goals. Resolve only significant product alternatives. **Exit:** short grounded intent and `READY | NEEDS_DECISION | BLOCKED`. Do not choose implementation or invent new features.

## Spec — observable WHAT / feature only when needed

**Entry:** Feature has new/changed behavior without complete accepted requirements, or Bug repair would change authoritative expected behavior. Reuse existing accepted rules; derive source-linked ACs with IDs and revision, observable Given/When/Then (or equivalent), acceptance source, expectations and explicit non-goals. Use lightweight Example Mapping: Story → REQUIRED rules → VERIFY examples → DECISION. Consult `coverage.md`; negative/boundary examples do **not** become speculative new business ACs.

**Readiness:** all changed ACs are testable, internally consistent, provenance-backed, complete for the accepted outcome, and have no unresolved consequential WHAT. Show the owner a short map covering **every AC ID**, with access to full exact revision. If new consequential WHAT lacks owner acceptance, return `NEEDS_DECISION`; never declare `READY` just because a summary was written. **Exit:** `READY | NEEDS_DECISION | BLOCKED`, full inspectable AC revision, checks and exclusions. No architecture or unauthorized edits.

## Architect — minimum viable HOW + verification plan

**Entry:** Feature has established expectations; Bug has reproduction/credible evidence and cause hypothesis; Spike may request a concept-level comparison, but no production implementation plan. Inspect affected source modules, external callers, test seams, trust boundaries and constraints. Prioritize REMOVE/REUSE/MODIFY over ADD; compare technical options only when real risk/cost/compatibility differs.

For implementation, plan smallest vertical slices and dependency ordering: authoritative AC or bug symptom → exact root/path/interface → meaningful test seam → regression/integration evidence. Address security, compatibility, data migration/backfill, observability, reversibility and rollout **only as implicated**. Never prescribe one rollout sequence for every multi-repo project. **Exit:** `READY | NEEDS_DECISION | BLOCKED`, concise design/test map, consequential decisions and bounded operations. Do not write code in planning state.

## Developer — authorized local implementation

**Entry:** Feature/Bug implementation has fresh baseline, accepted WHAT or credible existing bug contract, plan gates, and explicit bounded local edit grant under host permission. An explicit user request to implement/fix scoped local code may supply this grant; a Spike/evaluate/plan request does not. Follow `tdd.md`: intended RED → minimal GREEN → refactor if justified; for a Bug prefer regression reproducing original symptom. For non-behavioral changes/missing seam, use credible pre/post checks or label `NOT_APPLICABLE`/`NOT RUN`; no invented TDD claims.

Preserve unrelated user edits, implement smallest complete slices, execute actual relevant checks and inspect the current staged/unstaged/untracked diff; never silently alter excluded roots or run privileged side effects. For multi-repo work check actual integration/dependency edges. **Exit:** `READY_FOR_REVIEW | NEEDS_DECISION | BLOCKED`, changed snapshots per root, actual commands/results, AC or symptom→code/test evidence, TDD status and omissions. Developer cannot self-declare `AI_PASS`.

## Reviewer — independent correctness + convergence

**Entry:** Feature/Bug code edit has a stable diff and current verification evidence. For `AI_PASS`, Coordinator must **actually** dispatch a fresh context that did not implement the change, using a supported host capability; simple DIRECT self-review is not independent. Reviewer inspects actual diff including relevant untracked content, applicable project rules, accepted ACs or original bug symptom, test execution/limitations, TDD evidence or exceptions, security/data/compatibility hazards, and missing slices/ACs/integration edges. Compare observed implementation to expected outcome, not only code style.

Return `AI_PASS | CHANGES_REQUESTED | BLOCKED`, independence `VERIFIED | NOT VERIFIED`, root/snapshot identities, exact AC or symptom coverage, actionable severity/file/line/reproduction findings, omissions and residual risks. `AI_PASS` only when mandatory checks are credible on the current snapshot and reviewer independence is verified. A change after review requires re-verification and fresh review; repair loop max three rounds before escalation. The reviewer must not edit source or authorize merge/deploy. Host permissions, not text-only instructions, must enforce read-only where available.

## Researcher / Spike execution — role responsibilities, not a sixth agent

In a `spike`, Coordinator performs or delegates focused evidence gathering and concept-level architecture evaluation using existing Intent/Architect responsibilities. Read only by default; inspect counterevidence, compare options and confidence, optionally request a bounded scratch POC grant. Return `PROCEED | CLARIFY | STOP` with clear question, sources, confidence, limitations and a possible next task. No production code changes, no required Feature AC set and **no automatic developer/reviewer chain**. A disposable research experiment is not a delivered change; if a tracked project edit is needed, stop and create an explicitly approved Feature/Bug task.
