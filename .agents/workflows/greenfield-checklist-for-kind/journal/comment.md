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
- **September 2, 2026, 20:26 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Conducted a status check on Greenfield Step 1 PR #11408 on GitHub. Confirmed that all CI check-runs continue to pass successfully with zero failures (all checks are completely green). Since the `overseer/stop` label remains active on the pull request, we strictly adhere to our safety guardrails, respect this stop label, and leave the PR paused on standby, making absolutely no modifications to its labels, its assignees, or its state.
- **September 2, 2026, 18:20 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Verified the live status of Greenfield Step 1 PR #11408 on GitHub. Confirmed that all 300+ CI checks continue to pass successfully with zero failures (all checks are completely green). Observed that the `overseer/stop` label remains active on the pull request. Adhering strictly to the safety guardrails, we respect this stop label and keep the PR paused on standby, making absolutely no modifications to its labels, its assignees, or its state.
- **September 2, 2026, 16:05 UTC (Greenfield Monitoring; PR #11408 Live Monitored, Status: Paused, Respecting Stop Label)**: Evaluated the references comment posted by human reviewer `gemmahou` on parent issue #11349 (recommending reference mapping for field `network` to `ComputeNetwork` and `encryption_spec.kms_key_name` to `KMSCryptoKey`). Confirmed that all CI check-runs for PR #11408 continue to pass successfully with zero failures (all checks are completely green). Since the `overseer/stop` label remains active on the pull request, we strictly adhere to our safety guardrails, respect this stop label, and leave the PR paused on standby, making absolutely no modifications to its labels, its assignees, or its state.
