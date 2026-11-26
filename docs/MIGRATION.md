# Migration guide

## From 0.8.0 to the canonical task-record layout

New durable plugin-generated records use one canonical location:

```text
.sdlc/changes/<task-id>/
```

Quick creates no record by default. Standard uses one compact `task.md` when continuity is needed. Extended requires `state.json` and applicable stage artifacts.

External issues, tickets, PRs and ADRs remain request/source references. They are no longer alternate locations for plugin state or stage artifacts.

### Existing tasks

Do not automatically move, rename or rewrite an existing task record. Do not treat an approval for an earlier artifact revision as approval of a moved or changed artifact.

When resuming a task created before this policy:

1. Identify its existing record and verify task identity, artifact revisions, approval references and source/snapshot context.
2. Continue in the original location only when the record is unambiguous and its state can be safely verified.
3. Otherwise ask the owner to explicitly migrate it to `.sdlc/changes/<task-id>/`.
4. Preserve the old record until the owner confirms the new record is complete. Do not maintain two active state stores.

### Updating the plugin

Replace the installed plugin and reload the host. Existing project files are not rewritten automatically. The plugin does not generate project harness files or change host settings by default.

For installation, see [Hosts](HOSTS.md). For the new layout and resume behavior, see [Task records](TASK_RECORDS.md).
