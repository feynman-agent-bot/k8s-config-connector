# DiscoveryEngineSitemap Greenfield Migration Journal

## Current Step
Step 1: Direct API Types and Identity and Reference Types Pattern

## Migration Progress

| Step | Step Name | Issue | Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types and Identity | [#12028](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12028) | [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032) | PR Created | 2026-07-29 | - |
| 2 | Direct Controller, E2E fixtures and Fuzzer | - | - | Pending | - | - |
| 3 | mockGCP generation | - | - | Pending | - | - |
| 4 | MockGCP Alignment with RealGCP | - | - | Pending | - | - |

## Notes & Updates
- **2026-07-29**: Re-checked Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Confirmed that all CI checks continue to pass successfully. The PR remains open, pending human OWNER review and merge.
- **2026-07-29**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Verified all CI checks are successfully passing (188/188 checks green). The PR is open, awaiting human OWNER review and merge.
- **2026-07-29**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Verified that all 158 CI checks have passed successfully and no failing runs were found. The PR remains open, awaiting human OWNER review and merge.
- **2026-07-29**: Checked the status of Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). All 158 CI checks are successfully passing. The PR is fully green, awaiting human OWNER review and merge.
- **2026-07-29**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Verified that all 158 CI checks are fully passing. The PR is green and pending human OWNER review and merge.
- **2026-07-29**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Re-verified that all 158 CI checks are still fully green and passing. The PR is open, awaiting human OWNER review and merge.
- **2026-07-29**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). All 158 CI checks have passed successfully. The PR is still open, pending human OWNER review and merge.
- **2026-07-29**: Re-checked the status of Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). All 158 CI checks are passing. The PR remains open, awaiting human OWNER review and merge.
- **2026-07-29**: Checked again. Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032) remains open with all 158 CI checks passing, awaiting human OWNER review and merge.
- **2026-07-29**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). All 158 CI checks have passed successfully. The PR remains open, pending human OWNER review and merge.
- **2026-07-29**: Re-verified the status of Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). The pull request remains open, with all CI checks fully passing, and is pending human OWNER review and merge.
- **2026-07-29**: Checked the status of Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). All core CI checks (including `unit-tests`, `validate-generated-files`, `golangci-lint`, and `test-mockgcp`) have passed successfully. The PR is now fully green and awaiting human OWNER review and merge.
- **2026-07-29**: Detected Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032) created for Step 1. Checked the CI check runs: `unit-tests` failed due to missing fields in `TestCRDFieldPresenceInTestsForAlpha` exception list (`.spec.dataStoreRef` and `.spec.uri` on `discoveryenginesitemaps`). Assigned the PR back to `ada-coder-bot` for troubleshooting and fix.
- **2026-07-29**: Checked progress on [#12028](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12028). Verified that the issue remains open and is assigned to `ada-coder-bot` for implementing types, identity, and generation. No Pull Request has been created yet. Waiting for the PR to be opened and merged.
- **2026-07-29**: Initialized the migration checklist. Created the step 1 tracking issue [#12028](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12028).
