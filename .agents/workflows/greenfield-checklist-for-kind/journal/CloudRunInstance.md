# Greenfield Migration Journal: CloudRunInstance

## Current Step
Step 1: Direct API Types and Identity and Reference Types Pattern

## Migration Progress

| Step Number & Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|
| Step 1: Direct API Types, Identity, Reference | [#8718](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8718), [#9005](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9005) | [#9008](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9008) | PR Created | 2026-06-02 | |
| Step 2: Direct Controller, E2E fixtures & Fuzzer | | | Pending | | |
| Step 3: mockGCP generation | | | Pending | | |
| Step 4: MockGCP Alignment with RealGCP | | | Pending | | |

## Status Notes
- **2026-07-07**: Checked PR #9008 status. The latest commit (02fb32f) has completed 16 out of 21 checks, with all of them passing and no failures. The remaining 5 checks are currently in progress. The PR remains in "PR Created" status under Step 1.
- **2026-07-07**: Checked PR #9008 status. A new commit (02fb32f) was pushed by `codebot-robot`. Current CI checks are in progress with no failures reported.
- **2026-07-07**: Checked PR #9008 status. CI check `validate-generated-files` failed on the latest commit (d9a02f2). The PR was unassigned, so assigned it back to `codebot-robot` to investigate and resolve the code/file validation failures.
- **2026-07-07**: Checked PR #9008 status. Diagnosed the failure of `tests-e2e-fixtures-run` on commit `f9df077` and found it is due to `cloudruninstancebasic` fixture being executed before the direct controller config is registered in `static_config.go` (a Step 2 task). Since `codebot-robot` is already assigned, they will need to either defer the fixture files to Step 2 or exclude them from current test runs.
- **2026-07-07**: Checked PR #9008 status. CI check `tests-e2e-fixtures-run` failed on the latest commit (f9df077). The PR was unassigned, so assigned it back to `codebot-robot` to investigate and resolve the test failure in the run fixtures.
- **2026-07-07**: Checked PR #9008 status. All completed CI checks on the latest commit (f9df077) are passing successfully, with the remaining checks currently in progress. The PR remains in "PR Created" status under Step 1.
- **2026-07-07**: Checked PR #9008 status. The merge conflicts have been resolved by `codebot-robot` (commit `f9df077`), and the CI checks are currently running. No failures reported on the latest commit. The PR remains in "PR Created" status under Step 1.
- **2026-07-07**: Checked PR #9008 status. The PR is open and mergeable, but was unassigned with failing CI checks (`validate-generated-files` and `validations`). Assigned the PR to `codebot-robot` to address the failures and complete Step 1.
- **2026-07-07**: Checked PR #9008 status. The PR is still open but its mergeable state is 'dirty' (has merge conflicts) and it is currently unassigned. Assigning PR #9008 back to `codebot-robot` to resolve the conflicts.
- **2026-07-07**: Initialized journal for CloudRunInstance greenfield tracking. Step 1 types PR #8766 was closed, and follow-up PR #9008 (addressing issue #9005) is currently open. PR #9008 validations check is failing with client regeneration errors. Assigned PR #9008 to `codebot-robot` to regenerate Go clients and address validations.
