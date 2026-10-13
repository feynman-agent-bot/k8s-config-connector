# SQLSSLCert Migration Journal

## Current Step
Step 4: Ensure MockGCP matches real gcp behavior

## Progress Tracking

| Step | Name | Issue | Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types | [#13819](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13819) | [#13832](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13832) | Merged | 2026-10-08 | 2026-10-09 |
| 2 | Identity and Reference Types Pattern | [#13877](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13877) | [#13885](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13885) | Merged | 2026-10-09 | 2026-10-12 |
| 3 | Create a Round-Trip KRM Fuzzer | [#13942](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13942) | [#13946](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/13946) | Merged | 2026-10-12 | 2026-10-13 |
| 4 | Ensure MockGCP matches real gcp behavior | [#13967](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/13967) | - | Open | 2026-10-13 | - |
| 5 | Implement Direct Controller & E2E Fixtures | - | - | Pending | - | - |
| 6 | Validate Direct Promotion | - | - | Pending | - | - |

## Status Updates
- **2026-10-13**: Created issue #13967 for Step 4: Match real gcp behavior in MockGCP for SQLSSLCert.
- **2026-10-13**: Step 3 completed. PR #13946 merged into master.
- **2026-10-12**: Created issue #13942 for Step 3: Implement round-trip KRM fuzzer for SQLSSLCert.
- **2026-10-12**: Step 2 completed. PR #13885 merged into master.
- **2026-10-09**: Created issue #13877 for Step 2: Move SQLSSLCert to identity and refs pattern.
- **2026-10-09**: Step 1 completed. PR #13832 merged into master.
- **2026-10-08**: Created issue #13819 for Step 1: Implement direct KRM types and generate.sh for SQLSSLCert.
