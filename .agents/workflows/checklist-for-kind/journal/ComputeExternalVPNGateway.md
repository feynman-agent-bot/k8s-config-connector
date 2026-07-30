# Migration Journal: ComputeExternalVPNGateway

## Current Step
Step 6: Validate Direct Promotion (Issue [#12080](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12080))

| Step Number and Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|
| Step 1: Direct API Types | [#9970](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9970) | [#10032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10032) | Completed | 2026-06-13 | 2026-06-30 |
| Step 2: Identity and Reference Types Pattern | [#11110](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11110) | [#11111](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11111) | Completed | 2026-07-01 | 2026-07-01 |
| Step 3: Create a Round-Trip KRM Fuzzer | [#11124](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11124) | [#11125](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11125) | Completed | 2026-07-01 | 2026-07-01 |
| Step 4: Ensure MockGCP matches real gcp behavior | | [#3927](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/3927) | Completed | | |
| Step 5: Implement Direct Controller & E2E Fixtures | [#11310](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11310) | [#11311](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11311) | Completed | 2026-07-03 | 2026-07-06 |
| Step 6: Validate Direct Promotion | [#12080](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12080) | [#12092](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12092) | PR Created | 2026-07-30 | |

## Recent Status Update Notes
- **2026-07-30**: Verified that Steps 1 to 5 are completed and merged successfully. Opened Step 6 GitHub issue #12080 to validate direct promotion of `ComputeExternalVPNGateway`.
- **2026-07-30**: Discovered in-flight PR #12092 implementing Step 6. All CI checks are passing successfully. Waiting for human approval and merge.
