# Migration Journal: ComputeInstanceGroupNamedPort

This journal tracks the migration progress of the `ComputeInstanceGroupNamedPort` resource to a direct controller.

## Current Step
**Step 1: Direct API Types** — The PR is currently open with all CI checks passing, but a merge conflict is present (`mergeable: CONFLICTING`). We have unassigned and re-assigned the author bot `codebot-robot` via the GitHub REST API to trigger the automated system to rebase and resolve the merge conflict.

## Progress Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types | [#9988](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9988) | [#10078](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10078) | PR Created | 2026-06-13 | |
| 2 | Identity and Reference Types | | | Not Started | | |
| 3 | Round-Trip KRM Fuzzer | | | Not Started | | |
| 4 | MockGCP Alignment | | | Not Started | | |
| 5 | Direct Controller & E2E Fixtures | | | Not Started | | |
| 6 | Validate Direct Promotion | | | Not Started | | |

## Status Updates
* **2026-07-30**: Re-triggered the automated rebase and conflict resolution by unassigning and re-assigning the author bot `codebot-robot` via the GitHub REST API. PR status remains open and all CI checks are passing.
* **2026-07-30**: Re-verified PR #10078 status. Confirmed the merge conflict persists (`mergeable: CONFLICTING`). Successfully re-assigned `codebot-robot` via the GitHub REST API to trigger the automated rebase and conflict resolution daemon.
* **2026-07-30**: Identified a merge conflict (`mergeable: CONFLICTING`) on PR #10078, despite all CI checks passing. Explicitly re-assigned `codebot-robot` via GitHub REST API to trigger the automated daemon to perform a rebase/conflict resolution.
* **2026-07-29**: Started migration tracking. Identified that Step 1 is currently in progress via issue #9988 and PR #10078. PR is open with all CI checks passing. The `/hold` placed by `justinsb` for `ComputeInstanceGroupRef` is now resolved since #10074 is merged. Re-assigned to `codebot-robot` to trigger automated follow-up.
