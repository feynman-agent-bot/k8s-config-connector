# Greenfield Migration: SecurityCenterManagementEventThreatDetectionCustomModule

## Current Step
**Step 1: Direct API Types and Identity and Reference Types Pattern**

## Progress Tracking

| Step | Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types and Identity and Reference Types Pattern | [#8716](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8716) | [#11432](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11432) | PR Created | 2026-07-07 | - |
| 2 | Direct Controller, E2E fixtures and Fuzzer | - | - | - | - | - |
| 3 | mockGCP generation | - | - | - | - | - |
| 4 | MockGCP Alignment with RealGCP | - | - | - | - | - |

## Notes / Status Updates

- **2026-07-07**: Core CI checks (including `unit-tests`, `unit-tests-operator`, and linters/static analyses) have successfully passed on head commit `1fa36e3`. A few `tests-e2e-fixtures` checks are still in progress.
- **2026-07-07**: `codebot-robot` pushed a new fixup commit (`1fa36e3`) to address the `unit-tests` check failure. The CI check-runs have been re-triggered and are currently in progress.
- **2026-07-07**: Pull Request [#11432](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11432) is failing the `unit-tests` check in `tests/apichecks` due to missing `alpha-missingfields.txt` entries. Assigned `codebot-robot` to the PR to run with `WRITE_GOLDEN_OUTPUT=1` and resolve the linter check failure.
- **2026-07-07**: Pull Request [#11432](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11432) has been opened by `codebot-robot` for Step 1. Identified `unit-tests-operator` CI failure. Assigned `codebot-robot` to the PR to investigate and fix the check failure.
- **2026-07-07**: Initialized Greenfield Migration Checklist. Step 1 issue is already open (#8716). Re-assigning to the agent bot to trigger development, as the previous PR (#8777) was closed without merging.
