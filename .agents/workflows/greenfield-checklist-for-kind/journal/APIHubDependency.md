# Greenfield Migration Progress: APIHubDependency

This journal tracks the progress of migrating the `APIHubDependency` resource to a production-ready direct controller.

## Current Status
- **Current Step:** Step 1: Direct API Types and Identity and Reference Types Pattern
- **Status:** Pull request [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) is paused (`overseer/stop` attached) after consecutive investigations of the stale rerun failure. The newer workflow check is fully green. Awaiting human OWNER review/approval.

## Migration Steps Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types & Identity | [#12564](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12564) | [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) | In Progress | 2026-05-19 | |
| 2 | Direct Controller & Fuzzer | TBD | TBD | Pending | | |
| 3 | mockGCP Generation | TBD | TBD | Pending | | |
| 4 | MockGCP Alignment with RealGCP | TBD | TBD | Pending | | |

## Progress Journal Notes
- **2026-08-27 (Status update):** The watcher bot `argus-watcher-bot` has attached the `overseer/stop` label to PR [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) after attempting to investigate the stale "Validate PR Release Note" check run 3 times without success. The PR remains paused/stopped in compliance with safety guidelines. The actual newest check has successfully passed and is fully green, so the PR is healthy and awaits human OWNER review and approval.
- **2026-08-27 (Analysis):** Analyzed the `overseer/stop` label on Pull Request [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570). The automated checks are fully healthy and passing; the "Validate PR Release Note" failure is a known GitHub Actions rerun/stale webhook payload limitation, whereas the newer workflow run has completed successfully. Awaiting human OWNER review and approval.
- **2026-08-27 (Update):** `lovelace-coder-bot` opened Pull Request [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) for Step 1. All automated CI checks have completed and passed successfully. Awaiting human OWNER review and approval.
- **2026-08-27:** Initiated migration tracking for `APIHubDependency`. Closed the outdated issue #8398 and opened a new standardized Step 1 issue #12564 with the proper title, body, and labels to trigger the coder bot. Added progress note and updated the journal file.
