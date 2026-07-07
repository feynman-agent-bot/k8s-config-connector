# Greenfield Migration Journal: NetworkSecurityAuthzPolicy

## Current Step
Step 1: Direct API Types and Identity and Reference Types Pattern

## Migration Progress Tracking

| Step | Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Direct API Types, Identity, Reference | [#8721](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8721) | [#9195](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9195) | PR Created | 2026-06-04 | |
| 2 | Direct Controller, E2E fixtures and Fuzzer | | | Pending | | |
| 3 | mockGCP generation | | | Pending | | |
| 4 | MockGCP Alignment with RealGCP | | | Pending | | |

## Status Update Notes

### 2026-07-07
- Created a "take over" issue for `codebot-robot` to take over PR [#9195](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9195) to resolve its merge conflicts, rebase, and run tests.
- Re-verified PR [#9195](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9195) status: The PR remains open but is blocked by merge conflicts (`mergeable_state: dirty`). All 140+ CI checks are passing and the PR has approval and LGTM. Re-confirmed that we must wait for these conflicts to be resolved and the PR to be merged before we can trigger Step 2.
- Initialized Greenfield migration tracking journal for `NetworkSecurityAuthzPolicy`.
- Identified that Step 1 is currently in progress: GitHub Issue [#8721](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8721) is open, and a corresponding Pull Request [#9195](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9195) has been created.
- Pull Request [#9195](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9195) has been approved and LGTM'd by human maintainers, and all CI checks are passing.
- Checked the PR mergeability status and found it is currently blocked by merge conflicts (`mergeable_state: dirty`).
- Waiting for the merge conflicts on PR [#9195](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9195) to be resolved and the PR to be merged before moving to Step 2.
