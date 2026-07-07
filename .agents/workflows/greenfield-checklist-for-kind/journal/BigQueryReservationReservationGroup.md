# Migration Journal: BigQueryReservationReservationGroup

Current Step: Step 1 (Direct API Types and Identity and Reference Types Pattern)

## Progress Tracking

| Step Number & Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| --- | --- | --- | --- | --- | --- |
| 1. Direct API Types, Identity & Reference Types | [#9022](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9022) | [#11391](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11391) | In Progress (All completed checks passing) | 2026-07-06 | - |
| 2. Direct Controller, E2E fixtures & Fuzzer | - | - | Pending | - | - |
| 3. mockGCP Generation | - | - | Pending | - | - |
| 4. MockGCP Alignment with RealGCP | - | - | Pending | - | - |

## Updates

- **2026-07-07**: Monitored Step 1 PR #11391. All completed CI checks are passing successfully (including `unit-tests`, `test-mockgcp`, `smoketest-with-kind`, `run-linters`, `golangci-lint`, `fuzz-roundtrippers`, `validations`, and `build-images`). Only three remaining integration check runs (`compute`, `dataflow`, and `bigquery` fixture tests) are currently in progress. We will continue monitoring the PR for merge.
- **2026-07-07**: Monitored Step 1 PR #11391. Verified that a new commit `a10e0988` was pushed, fixing the previous errors. All completed CI checks (including `validate-generated-files`, `unit-tests`, `test-mockgcp`, `smoketest-with-kind`, `golangci-lint`, and `fuzz-roundtrippers`) are now passing successfully. Other checks are currently running. No active failures were found. We will continue monitoring the PR for merge.
- **2026-07-07**: Monitored Step 1 PR #11391. Verified the PR remains open and assigned to `hopper-coder-bot` with failing CI checks (`validations`, `unit-tests`, `validate-generated-files`). We will continue waiting for the fixes to be applied.
- **2026-07-07**: Monitored Step 1 PR #11391. Verified the PR is still open with failing checks (`unit-tests`, `validate-generated-files`, `validations`) and remains assigned to `hopper-coder-bot`. We will continue waiting for the fixes.
- **2026-07-07**: Monitored Step 1 PR #11391. The PR remains open with failing CI checks (`unit-tests`, `validate-generated-files`, `validations`) and is currently assigned to the author bot `hopper-coder-bot`. We will continue waiting for the fixes to be applied.
- **2026-07-07**: Step 1 PR #11391 is open but CI checks are failing. Assigned the PR back to `hopper-coder-bot` for automated fixes.
- **2026-07-07**: Confirmed Step 1 PR #11391 is still open with failing CI checks. The PR remains assigned to `hopper-coder-bot`, and `argus-watcher-bot` has started investigating the failures.
- **2026-07-07**: Monitored PR #11391 status. Verified `argus-watcher-bot` has initiated its investigation of the failing checks, and the PR is assigned to the author bot for remediation.
- **2026-07-07**: Continued monitoring Step 1 PR #11391. Confirmed the PR is still open with failing checks, remains assigned to `hopper-coder-bot`, and `argus-watcher-bot` is actively triaging the failures. We will continue waiting for the fixes.
- **2026-07-07**: Verified Step 1 PR #11391 remains open with failing checks (`unit-tests`, `validate-generated-files`, `validations`). It is assigned to `hopper-coder-bot` for resolution, and we will continue monitoring for progress.
- **2026-07-07**: Monitored Step 1 PR #11391. The PR is still open with failing checks (`unit-tests`, `validate-generated-files`, `validations`). It remains assigned to `hopper-coder-bot` for remediation. We will continue monitoring for progress.
- **2026-07-07**: Monitored Step 1 PR #11391. Verified the PR is open with failing CI checks and no active assignees. Assigned the PR back to `hopper-coder-bot` via the GitHub REST API to trigger automated remediation of the failing checks.
- **2026-07-07**: Monitored Step 1 PR #11391. Confirmed the `validations` check failed while others passed. Re-assigned the PR to the author bot `hopper-coder-bot` via the REST API to trigger automated remediation.
