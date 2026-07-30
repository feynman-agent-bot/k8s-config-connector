# ComputeDisk Migration Progress Journal

This journal tracks the migration of the `ComputeDisk` resource kind to a production-ready direct controller.

## Current Step
**Step 6: Validate Direct Promotion** - Issue #12077 has been created and is currently open for execution.

## Progress Tracking

| Step | Name | Issue | PR | Status | Date Started | Date Completed |
|------|------|-------|----|--------|--------------|----------------|
| 1 | Direct API Types | [#9965](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/9965) | [#10045](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10045) | Completed | 2026-06-13 | 2026-06-13 |
| 2 | Identity and Reference Types Pattern | [#10188](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10188) | [#10189](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10189) | Completed | 2026-06-13 | 2026-06-13 |
| 3 | Create a Round-Trip KRM Fuzzer | [#10437](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10437) | [#10438](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10438) | Completed | 2026-06-18 | 2026-06-18 |
| 4 | Ensure MockGCP matches real gcp behavior | - | - | Completed | - | - |
| 5 | Implement Direct Controller & E2E Fixtures | [#10508](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10508) | [#10511](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10511) | Completed | 2026-06-19 | 2026-06-23 |
| 6 | Validate Direct Promotion | [#12077](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12077) | - | Open | 2026-07-29 | - |

## Status Updates
- **2026-07-30**: Verified that the AI Factory has picked up the validation task for ComputeDisk. Issue #12077 is currently assigned to `neumann-coder-bot`, and a sandbox run has been initiated to perform the promotion validation and record/verify the HTTP cassettes. Monitoring for the creation of the corresponding pull request.
- **2026-07-29**: Resumed orchestration of the ComputeDisk migration. Checked historical PRs and verified that all previous steps (Steps 1, 2, 3, 4, 5) have been successfully implemented and merged.
- **2026-07-29**: Initiated Step 6. Created GitHub Issue #12077 to track the validation of direct promotion for ComputeDisk. Assigned the issue to the overseer/reviewer pool.
