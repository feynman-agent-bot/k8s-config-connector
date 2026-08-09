# Greenfield Resource Migration: DataLabelingInstruction

Current Step: Step 3: mockGCP generation

## Migration Progress

| Step | Name | Issue | PR | Status | Date Started | Date Completed |
|------|------|-------|----|--------|--------------|----------------|
| 1 | Direct KRM types, identity, and generate.sh | [#9270](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9270) | [#9347](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9347) | Merged | 2026-08-09 | 2026-08-09 |
| 2 | Direct Controller, E2E fixtures and Fuzzer | [#11479](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11479) | [#11485](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11485) | Merged | 2026-08-09 | 2026-08-09 |
| 3 | mockGCP generation | [#12285](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12285) | [#12291](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12291) | PR Created | 2026-08-09 | - |
| 4 | MockGCP Alignment with RealGCP | - | - | Not Started | - | - |

## Status Updates
- **2026-08-09**: Re-verified check-runs for PR [#12291](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12291). Confirmed `tests-e2e-fixtures-datalabeling` is still failing, and explicitly assigned the PR back to `neumann-coder-bot` via the GitHub REST API to continue fixing the E2E check-run.
- **2026-08-09**: Monitored Step 3 (mockGCP generation). Pull Request [#12291](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12291) has been created but has a failing E2E fixtures check. Assigned the PR back to its author bot `neumann-coder-bot` for resolution.
- **2026-08-09**: Initialized checklist. Step 1 (Types) and Step 2 (Controller) are already completed and merged. Initiating Step 3 by opening a new GitHub issue [#12285](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12285) for MockGCP generation.
