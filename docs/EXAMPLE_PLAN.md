# Example — actionable, human-readable implementation plan

This is an illustrative plan for an imaginary customer-status feature. The paths are examples, not a recommended project structure. A real Architect must inspect the target repositories and use their actual paths and symbols.

## Example `03-plan.md`

> Revision: r1 · Spec: r2 · Status: awaiting human approval

### Summary

| Item | Decision |
|---|---|
| Outcome | An authorized user can update customer status; the existing API returns it and the frontend displays it. |
| Recommended approach | Extend the existing customer update and display flows; do not add a second service. |
| Scope | Backend API and frontend. Infrastructure is read-only. |
| Delivery | Three complete slices with API and UI dependencies. |

### Implementation tasks

| Task | Action / outcome | File operation and path | Specific code change | ACs | Blocked by |
|---|---|---|---|---|---|
| T1 | Persist customer status and return it in the existing customer representation. | UPDATE `backend/src/customers/customer_service.py` | Extend the existing update mapping and response construction to preserve the accepted status value. | AC-01 | None |
| T1 | Prove persistence and response mapping. | UPDATE `backend/tests/customers/test_customer_service.py` | Add a service-level test that updates a customer, reloads it and asserts the returned status. | AC-01 | None |
| T2 | Expose the status through the existing customer update endpoint. | UPDATE `backend/src/customers/customer_controller.py` | Pass the status through the existing request/response contract; preserve existing authorization and error handling. | AC-01, AC-02 | T1 — the controller must use the status mapping introduced by T1. |
| T2 | Verify endpoint behavior and authorization. | UPDATE `backend/tests/customers/test_customer_api.py` | Add API tests for a successful status update and the accepted unauthorized behavior. | AC-01, AC-02 | T1 — endpoint evidence depends on the persisted status contract. |
| T3 | Display and update customer status in the existing UI. | UPDATE `frontend/src/features/customers/CustomerForm.tsx` | Bind the status control to the API field and existing update action; preserve current loading and error states. | AC-01, AC-03 | T2 — the UI consumes the updated API contract. |
| T3 | Verify the user-visible status flow. | UPDATE `frontend/src/features/customers/CustomerForm.test.tsx` | Add a component test that loads, changes and displays the accepted status value. | AC-03 | T2 — test the UI against the agreed API response shape. |

### Design decision

| Constraint | Options considered | Recommendation and reason |
|---|---|---|
| Existing customer update flow already owns persistence and authorization | Add a new status service; extend the existing service | Extend the existing flow because it preserves current ownership and avoids duplicate validation/authorization paths. |

### Verification

| AC / task | Test seam | Expected evidence |
|---|---|---|
| AC-01 / T1 | Customer service test | Status survives persistence and appears in the customer representation. |
| AC-01, AC-02 / T2 | Customer API integration test | Accepted status is returned; unauthorized updates follow the existing contract. |
| AC-03 / T3 | Customer form component test | UI displays and submits the status correctly. |

**Integration checks:** run backend contract/API checks before frontend integration; verify the frontend consumes the actual API response shape.

### Risks and boundaries

| Risk / dependency | Impact | Mitigation or decision |
|---|---|---|
| Existing customers may not have a status value | Existing reads or UI rendering may fail | Inspect the current data contract and preserve its established absence/default behavior; ask the owner if a new default is required. |

**Included roots:** backend and frontend, limited to customer status behavior.
**Excluded / read-only roots:** infrastructure; no infrastructure edits are proposed.
**Separate authorization:** database migration, deployment or production data changes require separate approval.

### Handoff

READY — human reviews the task/file mapping, code responsibilities, AC coverage and T1 → T2 → T3 dependencies. After plan approval, Developer revalidates every path and test seam against the current checkout before editing.

## Reading the table

- A task can have several file rows. Repeating the task ID keeps its implementation and test changes together.
- Use actual paths and mark each operation `CREATE` or `UPDATE`; do not list files merely inspected.
- The code-change column should say which existing method, mapping, route or component responsibility changes. It should not contain speculative code snippets.
- If the repository does not reveal a reliable path, write `UNKNOWN — locate <capability> before editing`. Never invent filenames or symbols.
- `Blocked by` records a genuine prerequisite and why it gates the task. Task numbering or preferred order alone is not a dependency.
- Every accepted AC must map to a task and verification seam. The full AC text remains in the Spec, not repeated here.
