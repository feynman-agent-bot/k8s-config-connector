# ComputeDiskResourcePolicyAttachment Migration Journal

## Current Step
Step 6: Validate Direct Promotion

## Progress Tracking

| Step Number & Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|
| Step 1: Direct API Types | [#9968](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9968) | [#10657](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10657) | Merged | 2026-06-13 | 2026-06-21 |
| Step 2: Identity & Reference Types | [#10665](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10665) | [#10666](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10666) | Merged | 2026-06-21 | 2026-06-22 |
| Step 3: Round-Trip KRM Fuzzer | [#10673](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10673) | [#10674](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10674) | Merged | 2026-06-22 | 2026-06-22 |
| Step 4: Ensure MockGCP matches real gcp behavior | [#10676](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10676) | [#10678](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10678) | Merged | 2026-06-22 | 2026-06-23 |
| Step 5: Implement Direct Controller & E2E Fixtures | [#10739](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10739) | [#10740](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10740) | Merged | 2026-06-23 | 2026-06-24 |
| Step 6: Validate Direct Promotion | [#12079](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12079) | [#12099](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12099) | PR Green | 2026-07-30 | - |

## Status Update Notes
* **2026-07-31**: Monitored the progress of PR #12099. All CI checks are passing and the PR is green, awaiting human OWNER review and merge.
* **2026-07-30**: Checked progress of PR #12099 for Step 6. All CI checks have successfully passed! The PR is now fully green and awaiting human/OWNER review and merge.
* **2026-07-30**: Checked progress of PR #12099 for Step 6. Author bot (lovelace-coder-bot) has successfully pushed a new commit to resolve the previous test failures. All completed CI checks have passed, and the remaining checks are currently running. Leaving the PR to run to completion.
* **2026-07-30**: Identified open PR #12099 for Step 6 (Validate Direct Promotion) with failing checks (presubmit-gatekeeper, tests-e2e-fixtures-compute, unit-tests). Assigned PR back to its author bot (lovelace-coder-bot) to resolve the failures.
* **2026-07-30**: Steps 1 to 5 have been fully resolved and merged in past runs. Created Issue #12079 to track Step 6 (Validate Direct Promotion).
* **2026-06-13**: Initiated tracking for ComputeDiskResourcePolicyAttachment. Found in-flight Step 1 PR #10021 (fixing Issue #9968). PR is currently open but failing `unit-tests` check.
