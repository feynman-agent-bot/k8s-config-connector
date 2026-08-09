# Greenfield Migration Journal: SecurityCenterBigQueryExport

This journal tracks the progress of migrating `SecurityCenterBigQueryExport` to a direct controller at `v1alpha1`.

## Current Step
Step 3: MockGCP generation

## Progress Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Direct API Types and Identity | [#8714](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8714) | [#8762](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8762) | Merged | 2026-05-27 | 2026-05-28 |
| 2 | Direct Controller, E2E fixtures and Fuzzer | [#8811](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8811) | [#8833](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8833) | Merged | 2026-05-29 | 2026-06-04 |
| 3 | MockGCP generation | [#11101](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11101) | [#11399](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11399) | CI Passed | 2026-07-07 | - |
| 4 | MockGCP Alignment with RealGCP | - | - | Not Started | - | - |

## Status Updates
- **2026-08-09**: All CI checks on PR #11399 have passed successfully! The PR is now mergeable and awaiting human owner review/approval for merging.
- **2026-08-09**: Successfully removed the `overseer/stop` label from PR #11399 to trigger a retry of the CI checks. The previous run failed due to a transient, unrelated infrastructure issue in `tests-e2e-fixtures-privateca` (missing etcd on runner). Since no `overseer/giving-up` label is present, the PR is unblocked for automatic retry.
