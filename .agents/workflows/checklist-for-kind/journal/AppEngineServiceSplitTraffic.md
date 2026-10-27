# Migration Progress: AppEngineServiceSplitTraffic

## Current Step
Step 3: Create a Round-Trip KRM Fuzzer

## Progress Tracking

| Step | Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Direct API Types | [#14340](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14340) | [#14361](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14361) | Completed | 2026-10-23 | 2026-10-27 |
| 2 | Identity and Reference Types Pattern | [#14340](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14340) | [#14361](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14361) | Completed | 2026-10-23 | 2026-10-27 |
| 3 | Create a Round-Trip KRM Fuzzer | [#14472](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14472) | [#14475](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14475) | PR Created | 2026-10-27 | - |
| 4 | Ensure MockGCP matches real gcp behavior | - | - | Pending | - | - |
| 5 | Implement Direct Controller & E2E Fixtures | - | - | Pending | - | - |
| 6 | Validate Direct Promotion | - | - | Pending | - | - |

## Status Update Notes
- **2026-10-27**: Pull Request [#14475](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14475) created for Step 3. All CI checks passed; awaiting review and merge.
- **2026-10-27**: Created Step 3 issue [#14472](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14472) to implement round-trip KRM fuzzer.
- **2026-10-27**: Pull Request [#14361](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14361) for Step 1 was merged. Step 2 (Identity and Reference Types Pattern) was verified as already completed in the same PR.
- **2026-10-24**: Pull Request [#14361](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14361) created for Step 1. Awaiting review and merge.
- **2026-10-23**: Initialized migration tracking for `AppEngineServiceSplitTraffic`. Created Step 1 issue [#14340](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14340) to implement direct KRM types and update `generate.sh`.
