This issue is to track the Greenfield implementation of DiscoveryEngineSitemap.

Workflow: https://raw.githubusercontent.com/gke-labs/gemini-for-kubernetes-development/main/.agents/workflows/kcc-greenfield.txt

## Migration Progress

### Current Step
Step 1: Direct API Types and Identity and Reference Types Pattern

| Step | Step Name | Issue | Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types and Identity | [#12028](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12028) | [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032) | PR Created | 2026-07-29 | - |
| 2 | Direct Controller, E2E fixtures and Fuzzer | - | - | Pending | - | - |
| 3 | mockGCP generation | - | - | Pending | - | - |
| 4 | MockGCP Alignment with RealGCP | - | - | Pending | - | - |

### Status Updates
- **2026-09-10 (Current Run)**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Confirmed that the PR remains OPEN with merge conflicts (state: `DIRTY`). Checked the latest CI status and verified that all 246 CI checks continue to pass successfully. The PR remains paused with the `overseer/stop` label applied, awaiting human action (such as conflict resolution or label removal) to proceed.
- **2026-09-10**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Confirmed that the PR remains OPEN with merge conflicts (state: `CONFLICTING` / `DIRTY`). Checked the latest CI status and verified that all 246 CI checks continue to pass successfully. The PR remains paused with the `overseer/stop` label applied, awaiting human action (such as conflict resolution or label removal) to proceed.
- **2026-09-09**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Confirmed that the PR remains OPEN with merge conflicts (state: `CONFLICTING` / `DIRTY`). Checked the latest CI status and verified that all 246 CI checks continue to pass successfully. The PR remains paused with the `overseer/stop` label applied, awaiting human action (such as conflict resolution or label removal) to proceed.
