# VertexAIExtension Greenfield Migration Journal

**Current Step**: Step 2: Direct Controller, E2E fixtures and Fuzzer

| Step | Step Name | GitHub Issue | GitHub PR | Status | Date Started | Date Completed |
|------|-----------|--------------|-----------|--------|--------------|----------------|
| 1 | Direct KRM Types & Identity | [#12027](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12027) | [#12036](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12036) | Merged | 2026-07-29 | 2026-08-05 |
| 2 | Direct Controller & E2E | [#12201](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12201) | [#12205](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12205) | PR Created | 2026-08-06 | - |
| 3 | mockGCP Generation | - | - | Pending | - | - |
| 4 | MockGCP Alignment | - | - | Pending | - | - |

## Recent Status Updates
* **2026-08-06**: Detected that PR [#12205](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12205) has been created for Step 2. However, the CI checks failed (specifically `unit-tests-1-of-4`). Assigning the PR back to `hopper-coder-bot` to triage and fix.
* **2026-08-06**: Re-verified the status of Issue #12201. Coder bots are still actively working in the AI Factory sandbox, and no Pull Request has been created yet. Continuing to monitor.
* **2026-08-06**: Checked progress on Step 2 (Direct Controller & E2E). Issue #12201 is open and assigned to coder bots `hopper-coder-bot` and `neumann-coder-bot`. AI Factory sandbox execution has been initiated. Awaiting creation of the Step 2 Pull Request.
* **2026-08-06**: Assigned `neumann-coder-bot` to Issue #12201 to initiate the implementation of the Direct Controller and E2E fixtures.
* **2026-08-06**: Step 1 (Direct KRM Types & Identity) is verified merged (PR #12036). Created Issue #12201 for Step 2 (Direct Controller & E2E fixtures) and initiated the next step of the migration.
