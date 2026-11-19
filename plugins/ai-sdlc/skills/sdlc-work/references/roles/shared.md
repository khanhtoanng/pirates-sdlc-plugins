# Role contracts — one Coordinator, five logical responsibilities

`core/routing.md` and `workflows/` decide which roles apply. Roles are responsibilities, not automatically native subagents. Extended requires each applicable stage's separately reviewable artifact and approval; Quick/Standard avoid sprawl. Workers return to Coordinator; they never approve owner decisions, grant edit scope or invoke downstream agents autonomously. `core/runtime.md` owns transition gates and current-snapshot semantics.

<discovery-brainstorming>
1. Inspect request, existing source, accepted contracts, project instructions and prior decisions **before asking**. Do not debate settled matters.
2. Responsibility boundary: **Intent asks WHY/WHO**, **Spec asks WHAT**, **Architect asks HOW**. Bug assessment starts at symptom/cause; Spike focuses on a bounded feasibility question. Do not make every role repeat the same brainstorm.
3. When no material uncertainty exists, state `NO_MATERIAL_UNCERTAINTY` or proceed without extra narrative. When genuine alternatives remain, compare only grounded options (often 2–3), impacts and counterevidence; no fabricated option matrix.
4. Distinguish `OBSERVED`, `SOURCE_BACKED`, `OWNER_ACCEPTED`, `PROPOSED`, `ASSUMPTION`, `UNKNOWN` and `DECISION`. Only meaningful WHAT/security/data/scope/reversibility decisions reach the Coordinator; ask one highest-impact question at a time. Never smuggle an open choice into an accepted AC.
5. Close with the result, source, scope exclusions and blockers. No brainstorm transcript; follow mode-specific artifact policy. Quick = evidence check; Standard = focused uncertainty; Extended = consequential alternatives, recovery and human gating.
</discovery-brainstorming>
