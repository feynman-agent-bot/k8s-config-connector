# Greenfield Migration Journal: SecurityCenterBigQueryExport

This journal tracks the progress of migrating `SecurityCenterBigQueryExport` to a direct controller at `v1alpha1`.

## Current Step
Step 3: MockGCP generation

## Progress Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Direct API Types and Identity | [#8714](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8714) | [#8762](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8762) | Merged | 2026-05-27 | 2026-05-28 |
| 2 | Direct Controller, E2E fixtures and Fuzzer | [#8811](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8811) | [#8833](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8833) | Merged | 2026-05-29 | 2026-06-04 |
| 3 | MockGCP generation | [#11101](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11101) | [#11399](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11399) | PR Created | 2026-07-07 | - |
| 4 | MockGCP Alignment with RealGCP | - | - | Not Started | - | - |

## Status Updates
- **2026-08-09**: Initialized the migration journal. Noticed that Step 1 and Step 2 are already merged successfully. Step 3 PR (#11399) is open but currently marked with `overseer/stop` due to a transient, unrelated CI failure in `tests-e2e-fixtures-privateca` (infrastructure issue where etcd was missing from runner path). Since there is no `overseer/giving-up` label, assigning PR back to `hopper-coder-bot` to trigger retry.
