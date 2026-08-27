# Greenfield Migration Progress: APIHubDependency

This journal tracks the progress of migrating the `APIHubDependency` resource to a production-ready direct controller.

## Current Status
- **Current Step:** Step 1: Direct API Types and Identity and Reference Types Pattern
- **Status:** Issue #8398 is open. Previous PR #8410 was closed without merge. A new PR/run is required to implement the direct KRM types for `APIHubDependency`.

## Migration Steps Tracking

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types & Identity | [#8398](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/8398) | [#8410](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8410) (Closed) | Open | 2026-05-19 | |
| 2 | Direct Controller & Fuzzer | TBD | TBD | Pending | | |
| 3 | mockGCP Generation | TBD | TBD | Pending | | |
| 4 | MockGCP Alignment with RealGCP | TBD | TBD | Pending | | |

## Progress Journal Notes
- **2026-08-27:** Initiated migration tracking for `APIHubDependency`. Found existing open issue #8398 representing Step 1. Noticed that the previous PR #8410 was closed. Updating the title, body, and labels of issue #8398 to align with Step 1 and triggering the coder bot by ensuring the labels and unassigned status are correct.
