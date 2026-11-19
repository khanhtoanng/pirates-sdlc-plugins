# Spike workflow

1. Define one answerable question, context, constraints, success/exit evidence, in-scope roots, time/effort budget if supplied, and what is explicitly NOT being implemented.
2. Investigate existing code, available documentation, options, costs, failure cases and disconfirming evidence. Label `OBSERVED`, `SOURCE_BACKED`, `ASSUMPTION`, `UNKNOWN`. Use external citations only when accessible; do not invent up-to-date facts.
3. A POC is optional and must have a separate bounded scratch/experiment grant. A disposable unmerged scratch POC is NOT production implementation or feature acceptance; if actual production/repository code changes are proposed, end the spike and ask for a new Feature/Bug invocation plus normal change gates.
4. Return concise decision brief: question; evidence and confidence; viable options/trade-offs; recommendation `PROCEED | CLARIFY | STOP`; unanswered risks; recommended next task (if any). **STOP** without creating acceptance criteria, starting a build, or granting itself approval to proceed.

In Extended, follow the exact stage sequence in core/human-gates.md, with a mandatory approval after each applicable stage; do not combine stages or prepare downstream outputs before approval.
