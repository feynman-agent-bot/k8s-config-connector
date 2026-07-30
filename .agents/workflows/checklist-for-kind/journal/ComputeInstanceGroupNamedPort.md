# Migration Journal: ComputeInstanceGroupNamedPort

This journal tracks the migration progress of the `ComputeInstanceGroupNamedPort` resource to a direct controller.

## Current Step
**Step 1: Direct API Types** — The PR is currently open and has successfully passed all CI checks. It was held blocked by `ComputeInstanceGroup` (#10074), which has since been merged. The PR is currently awaiting final merge/unhold, and we have assigned the author bot `codebot-robot` to resume.

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
* **2026-07-30**: Verified all CI checks are passing on PR #10078. Assigned/added `codebot-robot` as an assignee to PR #10078 to trigger the automated system to process the hold resolution since the blocking PR #10074 has been merged.
* **2026-07-29**: Started migration tracking. Identified that Step 1 is currently in progress via issue #9988 and PR #10078. PR is open with all CI checks passing. The `/hold` placed by `justinsb` for `ComputeInstanceGroupRef` is now resolved since #10074 is merged. Re-assigned to `codebot-robot` to trigger automated follow-up.
