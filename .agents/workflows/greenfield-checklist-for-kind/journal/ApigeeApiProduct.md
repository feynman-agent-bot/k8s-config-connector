# Migration Journal: ApigeeApiProduct

Current Step: Step 2: Direct Controller, E2E fixtures and Fuzzer

## Progress Tracking

| Step Number & Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Step 1: Direct API Types & Identity | [#8061](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8061) | [#10607](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10607) | Merged | 2026-06-24 | 2026-06-24 |
| Step 2: Direct Controller, E2E Fixtures & Fuzzer | [#12289](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12289) | [#12298](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12298) | Open | 2026-08-09 | - |
| Step 3: mockGCP Generation | - | - | Pending | - | - |
| Step 4: MockGCP Alignment with RealGCP | - | - | Pending | - | - |

## Status Update Notes

- **2026-08-24**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-23**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-22**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-21**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-20**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-19**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-18**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-17**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-16**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-15**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains paused with the `overseer/stop` label while human reviewers triage the Apigee connect agent precondition requirements.
- **2026-08-14**: Human reviewer @barney-s noted that GCP requests are failing with Apigee connect agent errors ("no connections available from the Apigee connect agent(s)"), and highlighted the need to investigate preconditions. The PR currently has the `overseer/stop` label, pausing automation while the preconditions are triaged. All CI check-runs continue to pass successfully.
- **2026-08-13**: Verified all CI check-runs on PR #12298 continue to pass successfully. All 180+ tests are green. The PR remains open, awaiting final human review and merge.
- **2026-08-12**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR remains open, awaiting final human review and merge.
- **2026-08-11**: Verified all CI check-runs on PR #12298 continue to pass successfully. The PR is awaiting final human owner approval and merge.
- **2026-08-10**: Verified all CI presubmit checks on PR #12298 have successfully completed and passed. The PR remains open, awaiting final human review and merge.
- **2026-08-09**: `ada-coder-bot` successfully resolved the `unit-tests-3-of-4` test failure and addressed all review comments on PR #12298. Active CI checks are currently passing or in progress. PR is awaiting final human owner approval.
- **2026-08-09**: PR #12298 opened for Step 2. Identified `unit-tests-3-of-4` check failure in `TestRegisteredTemplatesMatchCAI` due to missing `ApigeeApiProduct` template exception in `pkg/gcpurls/registry_test.go`. Assigning PR back to `ada-coder-bot` to resolve the test failure.
- **2026-08-09**: Verified Step 1 is merged (PR #10607). Created GitHub Issue #12289 for Step 2.
