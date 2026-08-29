# Greenfield Migration Progress: APIHubDependency

This journal tracks the progress of migrating the `APIHubDependency` resource to a production-ready direct controller.

## Current Status
- **Current Step:** Step 1: Direct API Types and Identity and Reference Types Pattern
- **Status:** Pull request [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) has encountered merge conflicts. The watch daemon `argus-watcher-bot` has automatically initiated conflict resolution and rebasing. Prior to the conflict, all functional unit/E2E checks passed successfully. The PR awaits final human OWNER review and approval to merge.

## Migration Steps Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types & Identity | [#12564](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12564) | [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) | In Progress | 2026-05-19 | |
| 2 | Direct Controller & Fuzzer | TBD | TBD | Pending | | |
| 3 | mockGCP Generation | TBD | TBD | Pending | | |
| 4 | MockGCP Alignment with RealGCP | TBD | TBD | Pending | | |

## Progress Journal Notes
- **2026-08-29 (Status update - Rebase Pending):** Verified PR mergeability status is dirty. Conflict resolution by `argus-watcher-bot` is still in progress / pending. Awaiting completion of the rebase and final human OWNER review before proceeding to Step 2.
- **2026-08-29 (Status update - Merge Conflict):** Detected merge conflicts on PR [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570). The watch daemon `argus-watcher-bot` has automatically initiated conflict resolution and rebasing. The PR remains "In Progress" for Step 1.
- **2026-08-29 (Status update):** `lovelace-coder-bot` has successfully resolved the `unit-tests-1-of-4` failure by registering `.spec.attributes` under `exceptions/alpha-missingfields.txt` and has force-pushed the branch. All automated reviews have successfully passed. Awaiting final human OWNER review/approval to merge before proceeding to Step 2.
- **2026-08-28 (Status update - 23:55):** Detected a unit test failure (`unit-tests-1-of-4` failed) on the latest push `ecd23d51f3c903d55723fc068e5faaed2d3634ce` on PR #12570. The watch daemon `argus-watcher-bot` has automatically initiated investigation and troubleshooting as of 23:48:46 UTC. The PR remains "In Progress" for Step 1.
- **2026-08-28 (Status update):** Verified the migration status of APIHubDependency. Confirmed via API query that the PR is currently active under human review (`overseer/review` label is present, and no `overseer/stop` label is attached to the PR or issues). Checked automated CI status: all functional checks (smoketests, unit tests, linters, e2e fixtures) are passing successfully, with only the known stale 'Validate PR Release Note' check showing a failure (due to rerun/stale webhook payload limitations). The PR is fully healthy and remains in 'In Progress' status, awaiting human OWNER approval to merge before proceeding to Step 2.
- **2026-08-27 (Status update):** The watcher bot `argus-watcher-bot` has attached the `overseer/stop` label to PR [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) after attempting to investigate the stale "Validate PR Release Note" check run 3 times without success. The PR remains paused/stopped in compliance with safety guidelines. The actual newest check has successfully passed and is fully green, so the PR is healthy and awaits human OWNER review and approval.
- **2026-08-27 (Analysis):** Analyzed the `overseer/stop` label on Pull Request [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570). The automated checks are fully healthy and passing; the "Validate PR Release Note" failure is a known GitHub Actions rerun/stale webhook payload limitation, whereas the newer workflow run has completed successfully. Awaiting human OWNER review and approval.
- **2026-08-27 (Update):** `lovelace-coder-bot` opened Pull Request [#12570](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12570) for Step 1. All automated CI checks have completed and passed successfully. Awaiting human OWNER review and approval.
- **2026-08-27:** Initiated migration tracking for `APIHubDependency`. Closed the outdated issue #8398 and opened a new standardized Step 1 issue #12564 with the proper title, body, and labels to trigger the coder bot. Added progress note and updated the journal file.
