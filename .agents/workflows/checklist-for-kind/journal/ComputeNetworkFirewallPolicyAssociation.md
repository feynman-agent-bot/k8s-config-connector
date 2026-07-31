<!--
Copyright 2026 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Migration Journal: ComputeNetworkFirewallPolicyAssociation

## Current Step
**Step 1: Direct API Types**

PR #10083 is open with changes requested. The PR is currently failing the `zizmor-output` CI check and has been re-assigned to its author bot `codebot-robot` via the GitHub REST API to investigate and resolve the failure, while awaiting final human review and merge by human OWNERs to proceed to Step 2.

## Migration Progress

| Step Number & Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| --- | --- | --- | --- | --- | --- |
| 1. Direct API Types | [#9998](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9998) | [#10083](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10083) | `PR Created` | 2026-07-29 | |
| 2. Identity and Reference Types Pattern | | | `Not Started` | | |
| 3. Create a Round-Trip KRM Fuzzer | | | `Not Started` | | |
| 4. Ensure MockGCP matches real gcp behavior | | | `Not Started` | | |
| 5. Implement Direct Controller & E2E Fixtures | | | `Not Started` | | |
| 6. Validate Direct Promotion | | | `Not Started` | | |

## Update Logs

### 2026-07-31
- Verified that PR #10083 (Step 1) is still open and currently under review with changes requested.
- Detected that the PR was unassigned and failing the `zizmor-output` check.
- Assigned the PR back to its author bot `codebot-robot` via the GitHub REST API to investigate and resolve the CI failure, ensuring active tracking remains enabled.

### 2026-07-30
- Verified all CI checks for PR #10083 have successfully passed and are fully green.
- Re-assigned PR #10083 to its author bot `codebot-robot` via REST API after verifying that the assignee list was empty, ensuring active automated tracking remains enabled.

### 2026-07-29
- Initiated tracking of `ComputeNetworkFirewallPolicyAssociation` migration.
- Detected active in-flight PR #10083 for Step 1 (Issue #9998).
- Assigned PR #10083 to author bot `codebot-robot` to trigger rebasing and address failures.
