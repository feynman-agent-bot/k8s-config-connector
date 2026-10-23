# Migration Journal: ComputeOrganizationSecurityPolicyAssociation

**Current Step:** Step 2: Identity and Reference Types Pattern

| Step | Name | Issue | Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types | #10007 | [#14256](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14256) | Merged | 2026-06-13 | 2026-10-23 |
| 2 | Identity and Reference Types Pattern | #14313 | [#14318](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/14318) | PR Created | 2026-10-23 | - |
| 3 | Create a Round-Trip KRM Fuzzer | - | - | Pending | - | - |
| 4 | Ensure MockGCP matches real gcp behavior | - | - | Pending | - | - |
| 5 | Implement Direct Controller & E2E Fixtures | - | - | Pending | - | - |
| 6 | Validate Direct Promotion | - | - | Pending | - | - |

## Status Updates
- **2026-10-21**: Resumed tracking under issue #14252. Added `overseer` and `overseer/review` labels to child issue #10007.
- **2026-10-22**: PR #14256 created for Step 1. All CI checks passed and PR is labeled `overseer/ready-for-human`.
- **2026-10-23**: Step 1 PR #14256 merged and Issue #10007 closed. Started Step 2: created child issue #14313 for Identity and Reference Types Pattern.
- **2026-10-23**: PR #14318 created for Step 2. All CI checks passed (257/257).
