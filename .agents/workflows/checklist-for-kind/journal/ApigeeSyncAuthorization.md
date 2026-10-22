# ApigeeSyncAuthorization Migration Journal

## Current Step
Step 3: Create a Round-Trip KRM Fuzzer

## Migration Progress: ApigeeSyncAuthorization

| Step | Name | Issue | Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types | [#14104](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14104) | [#14116](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14116) | Completed | 2026-10-19 | 2026-10-21 |
| 2 | Identity and Reference Types Pattern | [#14216](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14216) | [#14220](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14220) | Completed | 2026-10-21 | 2026-10-21 |
| 3 | Create a Round-Trip KRM Fuzzer | [#14254](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/14254) | [#14261](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14261) | PR Created | 2026-10-21 | - |
| 4 | Ensure MockGCP matches real gcp behavior | - | - | Not Started | - | - |
| 5 | Implement Direct Controller & E2E Fixtures | - | - | Not Started | - | - |
| 6 | Validate Direct Promotion | - | - | Not Started | - | - |

### Status Updates
- **2026-10-21**: PR #14261 created for Step 3. All presubmit CI checks passed and PR is marked ready-for-human.
- **2026-10-21**: PR #14220 merged. Completed Step 2. Created issue #14254 for Step 3: Implement round-trip KRM fuzzer for ApigeeSyncAuthorization.
- **2026-10-21**: PR #14220 created for Step 2. All CI checks passed and reviewed by reviewbot.
- **2026-10-21**: PR #14116 merged. Completed Step 1. Created issue #14216 for Step 2: Move ApigeeSyncAuthorization to identity and refs pattern.
- **2026-10-20**: PR #14116 created for Step 1.
- **2026-10-19**: Started migration for ApigeeSyncAuthorization. Created issue #14104 for Step 1: Implement direct KRM types and generate.sh.
