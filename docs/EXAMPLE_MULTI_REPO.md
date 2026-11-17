# Example: one feature across FE, BE, Flyway and Terraform

Illustrative workspace (not part of the plugin install):

```text
product/
  frontend/       # independent Git repository
  backend/        # independent Git repository
  flyway/         # independent Git repository
  terraform/      # independent Git repository
```

**Request:** Add a customer status field, return it from an API, and display it in FE. Inspect Terraform only; no assumed infra change.

**Coordinator intake:** discover all actual roots, instruction files, access and revisions. Proposed `RELEVANT = FE, BE, Flyway, Terraform (read-only)`; `EDIT_APPROVED = none` in this **planning-only** example; a later explicit scoped implement request may grant ordinary local edits to named roots under host policy. Inspect code/contracts before deciding which repos need edits.

**One Spec revision (example only; do not invent actual business rules):**
- `AC-01`: accepted status is persisted/retrieved and returned through the existing customer API.
- `AC-02`: FE shows the status from the API and handles the supported absence/compatibility behavior.
- `AC-03`: existing customers remain readable through the rollout.
All ACs must be traced to actual requirements/contracts before acceptance. Boundary examples are VERIFY, not independent product rules.

| Repo | Candidate implementation | Evidence |
|---|---|---|
| Flyway | New backward-compatible migration, only if schema inspection requires it | Migration in test DB; existing rows checked |
| Backend | DTO/mapping/business behavior | Unit/integration + contract tests |
| Frontend | UI field and API consumption | Component/E2E tests |
| Terraform | READ-ONLY impact inspection | No change needed, or escalate if discovered |

**Architect:** derive actual dependency graph. Possible sequence is schema expand → compatible BE → FE; check whether CI/deployment makes other order necessary. `terraform plan`/`apply` are not automatically authorized. Keep one AC set, per-repo test evidence and separate PRs.

**Developer:** use test-first RED/GREEN where a real seam exists, record commands and outcomes per root; never invent successful tests.

**Reviewer:** independently review current diffs from each modified root and cross-repo compatibility. If a required integration test is unavailable, report `NOT RUN`; incomplete critical evidence blocks `AI_PASS` even if each individual repo passes unit tests.

**Human handoff:** one concise card with accepted AC revision, changed root/branch/snapshot list, AC→repo→test coverage, release dependency order, outstanding risks and separate merge/deploy gates. No mandatory four separate SDLC documents.
