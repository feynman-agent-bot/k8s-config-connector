# Migration Journal: SaaSServiceMgmtRollout

**Current Step**: Step 2: Direct Controller, E2E fixtures and Fuzzer

## Progress Tracking

| Step Number & Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|
| Step 1: Direct API Types and Identity | [#13599](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13599) | [#13793](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13793) | Completed | 2026-10-01 | 2026-10-14 |
| Step 2: Direct Controller, E2E fixtures and Fuzzer | [#13974](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13974) | TBD | Open | 2026-10-14 | - |
| Step 3: mockGCP generation | TBD | TBD | Not Started | - | - |
| Step 4: MockGCP Alignment with RealGCP | TBD | TBD | Not Started | - | - |

## Status Updates
- **2026-10-14**: PR [#13793](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13793) was merged. Completed Step 1. Created Step 2 tracking issue [#13974](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13974) to implement direct controller, E2E fixtures, and fuzzer.
- **2026-10-08**: PR [#13793](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13793) was created for Step 1 replacing closed PR [#13628](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13628). All presubmit checks passed. Status is `PR Created`.
- **2026-10-02**: PR [#13628](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13628) was created for Step 1. Updated status to `PR Created`.
- **2026-10-01**: Initiated Greenfield migration for `SaaSServiceMgmtRollout`. Created Step 1 tracking issue [#13599](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13599) to implement direct KRM types, identity, and generate.sh.
