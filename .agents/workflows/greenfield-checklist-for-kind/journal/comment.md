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
- **September 4, 2026, 00:00 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Conducted a status check on Greenfield Step 1 PR #11408 on GitHub. Confirmed that all CI check-runs are completely green and passing successfully with zero failures. Since the `overseer/stop` label remains active on the pull request, we strictly adhere to our safety guardrails, respect this stop label, and leave the PR paused on standby, making absolutely no modifications to its labels, its assignees, or its state.
- **September 3, 2026, 23:00 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Verified the live status of Greenfield Step 1 PR #11408 on GitHub. Confirmed that all CI check-runs continue to pass successfully with zero failures (all checks are completely green). Observed the references evaluation feedback posted by human reviewer `gemmahou` on parent issue #11349 (specifying reference mappings for `network` and `encryption_spec.kms_key_name`). Since the `overseer/stop` label remains active on the pull request, we strictly adhere to our safety guardrails, respect this stop label, and leave the PR paused on standby, making absolutely no modifications to its labels, its assignees, or its state.
- **September 3, 2026, 20:53 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Re-verified the live status of Greenfield Step 1 PR #11408 on GitHub. Confirmed that all CI check-runs continue to pass successfully with zero failures (all checks are completely green). Observed the references evaluation feedback posted by human reviewer `gemmahou` on parent issue #11349 (specifying reference mappings for `network` and `encryption_spec.kms_key_name`). Since the `overseer/stop` label remains active on the pull request, we strictly adhere to our safety guardrails, respect this stop label, and leave the PR paused on standby, making absolutely no modifications to its labels, its assignees, or its state.
