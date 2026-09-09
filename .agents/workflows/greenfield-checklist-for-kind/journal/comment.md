This issue is to track the Greenfield implementation of VertexAIPersistentResource.

Workflow: https://raw.githubusercontent.com/gke-labs/gemini-for-kubernetes-development/main/.agents/workflows/kcc-greenfield.txt

## Migration Progress

### Current Step
**Step 1: Direct API Types and Identity and Reference Types Pattern** (Paused - Respecting Stop Label)

### Progress Tracking Table

| Step Number and Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|
| Step 1: Direct API Types and Identity | [#9245](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9245) | [#11408](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11408) | Paused - Respecting Stop Label | July 6, 2026 | - |
| Step 2: Direct Controller and E2E Fixtures | - | - | Pending | - | - |
| Step 3: MockGCP Generation | - | - | Pending | - | - |
| Step 4: MockGCP Alignment | - | - | Pending | - | - |

### Recent Status Updates
- **September 9, 2026, 04:37 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Conducted a status check on Greenfield Step 1 PR #11408 on GitHub. Confirmed that all CI checks continue to pass successfully with zero failures (all checks are green). Since the `overseer/stop` label remains active on the pull request, we strictly respect this stop label and leave the PR paused on standby, making absolutely no modifications to its labels, its assignees, or its state.
- **September 9, 2026, 02:28 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Checked the live status of Greenfield Step 1 PR #11408 on GitHub. Confirmed that the `overseer/stop` label remains active, and a merge conflict (`CONFLICTING`) is present on the PR. Observed the `References Evaluation` feedback comment on parent issue #11349. In accordance with our strict safety guardrails and system rules, we respect the active stop label, treat the PR as paused, and leave it untouched on standby, making absolutely no modifications to its labels, its assignees, or its state.
- **September 9, 2026, 00:17 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Verified the live status of Greenfield Step 1 PR #11408 on GitHub. Confirmed that the `overseer/stop` label remains active, and a merge conflict (`CONFLICTING`) is present on the PR. Observed the `References Evaluation` feedback comment on parent issue #11349. In accordance with our strict safety guardrails and explicit system rules, we respect the active stop label, treat the PR as paused, and leave it untouched on standby, making absolutely no modifications to its labels, its assignees, or its state.
