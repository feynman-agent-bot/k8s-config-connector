# Greenfield Migration Progress: APIHubDependency

This journal tracks the progress of migrating the `APIHubDependency` resource to a production-ready direct controller.

## Current Status
- **Current Step:** Step 1: Direct API Types and Identity and Reference Types Pattern
- **Status:** Outdated issue #8398 has been closed, and a new standardized Step 1 issue #12564 is open to implement the direct KRM types, identity, and generate.sh for `APIHubDependency`.

## Migration Steps Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types & Identity | [#12564](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12564) | [#8410](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8410) (Closed) | Open | 2026-05-19 | |
| 2 | Direct Controller & Fuzzer | TBD | TBD | Pending | | |
| 3 | mockGCP Generation | TBD | TBD | Pending | | |
| 4 | MockGCP Alignment with RealGCP | TBD | TBD | Pending | | |

## Progress Journal Notes
- **2026-08-27:** Initiated migration tracking for `APIHubDependency`. Closed the outdated issue #8398 and opened a new standardized Step 1 issue #12564 with the proper title, body, and labels to trigger the coder bot. Added progress note and updated the journal file.
