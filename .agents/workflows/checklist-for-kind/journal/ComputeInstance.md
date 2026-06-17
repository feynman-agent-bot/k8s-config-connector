# Migration Progress: ComputeInstance

## Current Step
- **Step 1: Direct API Types** - Currently in progress. PR #10059 has been created but has failing CI checks.

## Progress Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Direct API Types | [#9985](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9985) | [#10059](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10059) | `PR Created` | 2026-06-13 | |
| 2 | Identity and Reference Types Pattern | | | | | |
| 3 | Create a Round-Trip KRM Fuzzer | | | | | |
| 4 | Implement Direct Controller & E2E Fixtures | | | | | |

## Status Update Notes
- **2026-06-17**: Overseer checked PR #10059. It is open, but currently in a `CONFLICTING` merge state (`dirty`) with failing CI checks (`unit-tests`, `fuzz-roundtrippers`). Under strict guardrails, no comments were posted directly to the child PR. Attempting to assign `factorybot-robot` via `gh` CLI returned a scope/permission error. Awaiting automated watch daemon or author action to resolve conflicts and failing checks before proceeding to Step 2.
- **2026-06-16**: Overseer checked PR #10059. The PR remains open with failing CI checks on `unit-tests` and `fuzz-roundtrippers`. Commented `/assign factorybot-robot` on the PR to request assistance and trigger automatic fixes/re-runs. Awaiting PR fix and merge before moving to Step 2.
