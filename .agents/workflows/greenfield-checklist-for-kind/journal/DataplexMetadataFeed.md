# Greenfield Migration Progress: DataplexMetadataFeed

This journal tracks the progress of migrating the `DataplexMetadataFeed` resource to a direct KCC controller.

## Current Step
**Step 1: Direct API Types and Identity and Reference Types Pattern**
The types-only PR [#10820](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10820) remains open with failing checks (`validate-generated-files`, `validations`). It has been assigned back to `hopper-coder-bot` for troubleshooting and resolution.

## Progress Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Direct API Types & Identity | [#9280](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9280) | [#10820](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10820) | PR Created (Failing Checks) | 2026-06-25 | - |
| 2 | Direct Controller & E2E Fixtures | - | - | Not Started | - | - |
| 3 | MockGCP Generation & Alignment | - | - | Not Started | - | - |
| 4 | MockGCP Log Alignment | - | - | Not Started | - | - |

## Status Updates
* **2026-06-25**: Checked PR #10820 and verified that checks `unit-tests`, `validate-generated-files`, and `validations` remain in a failing state. Confirmed the PR was unassigned. Assigned the PR back to the author bot (`hopper-coder-bot`) via the GitHub REST API to re-trigger its troubleshooting workflow.
* **2026-06-25**: Checked the status of PR #10820 and found that the `validate-generated-files` and `validations` checks are still failing, and the PR had no assignee. Successfully assigned the PR back to `hopper-coder-bot` via the GitHub REST API to re-trigger its troubleshooting workflow.
* **2026-06-25**: Monitored PR #10820 checks and found that 'validate-generated-files', 'unit-tests', and 'validations' continue to fail. Since the PR was unassigned, assigned the PR back to 'hopper-coder-bot' via the REST API to re-trigger troubleshooting.
* **2026-06-25**: Checked the CI check runs on PR #10820 and verified that `unit-tests`, `validate-generated-files`, and `validations` checks remain in a failing state. Since there were no active runs on GitHub Actions, unassigned and re-assigned `hopper-coder-bot` via the REST API to re-trigger its troubleshooting workflow.
* **2026-06-25**: Checked PR #10820 status and verified that checks `validate-generated-files`, `unit-tests`, and `validations` are failing. Confirmed PR has no assignee. Successfully assigned the PR back to the author bot `hopper-coder-bot` to trigger troubleshooting and resolve the failures.
* **2026-06-25**: Monitored the progress of the types-only PR #10820. The PR remains open and assigned to `hopper-coder-bot` with failing checks (`validate-generated-files`, `unit-tests`, `validations`). Continuing to monitor the PR for fixes.
* **2026-06-25**: Successfully added `hopper-coder-bot` as the assignee on PR #10820 via GitHub REST API to trigger troubleshooting and resolve the failing `unit-tests`, `validate-generated-files`, and `validations` checks.
* **2026-06-25**: Observed that although `hopper-coder-bot` force-pushed a new commit to address the previous compile errors, the latest CI checks still fail on `unit-tests`, `validate-generated-files`, and `validations`. Re-assigning the PR back to `hopper-coder-bot` to trigger further investigation and resolution.
* **2026-06-25**: Confirmed the validations check-run failure. Assigned the PR back to the author bot (`hopper-coder-bot`) for troubleshooting and resolution.
* **2026-06-25**: Initiated the Greenfield checklist workflow. Found that the types-only PR [#10820](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10820) is open but has failing CI checks. Assigning it back to the PR author bot (`hopper-coder-bot`) to fix the checks.
