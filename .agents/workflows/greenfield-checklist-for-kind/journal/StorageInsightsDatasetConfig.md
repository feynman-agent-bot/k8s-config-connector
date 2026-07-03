# StorageInsightsDatasetConfig Greenfield Migration Journal

Current Step: Step 1 (Direct API Types and Identity and Reference Types Pattern)

## Migration Progress

| Step | Step Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|---|
| 1 | Direct API Types & Identity | [#11243](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11243) | [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) | PR Created | 2026-07-02 | |
| 2 | Direct Controller & E2E Fixtures | N/A | N/A | Pending | | |
| 3 | mockGCP Generation | N/A | N/A | Pending | | |
| 4 | mockGCP Alignment | N/A | N/A | Pending | | |

## Status Updates
* **2026-07-03**: Monitored the migration progress. Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) remains open, and all 194 CI checks have successfully passed. The PR is ready and awaiting human OWNER review and merge.
* **2026-07-03**: Re-checked the migration progress. Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) remains open, and all 150+ CI checks continue to pass successfully. The PR is awaiting human OWNER review and merge to proceed to Step 2.
* **2026-07-03**: Re-verified the status of Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252). All 150+ CI checks remain 100% green and successfully passing. The PR is awaiting human OWNER review and merge before we can proceed to Step 2.
* **2026-07-03**: Monitored the migration progress. Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) remains open and is fully green with all 150+ CI checks successfully passing. Awaiting human OWNER review and merge before proceeding to Step 2.
* **2026-07-03**: Verified that all 150+ CI checks on Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) are 100% green and successfully passing. The PR remains open and is awaiting human OWNER review and merge.
* **2026-07-03**: Re-checked the status of Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) again. All CI checks are still 100% green and passing. The PR remains open and is awaiting human OWNER review and merge.
* **2026-07-03**: Re-verified the status of Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252). All CI checks are 100% green and passing. Ready for human OWNER review and merge.
* **2026-07-03**: Checked the migration progress. Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) remains open and fully green. Awaiting human OWNER review and merge before we can proceed to Step 2.
* **2026-07-03**: Verified that all CI checks on Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) have completed successfully with no failures. The PR is awaiting human OWNER review and merge.
* **2026-07-03**: Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) CI checks are green (all major checks including validations and unit-tests have successfully passed). PR is awaiting human OWNER review and merge.
* **2026-07-03**: Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) failed the `validations` CI check due to unregenerated Go clients (`ERROR: Resource Go Clients must be regenerated. Please run 'make ready-pr'`). Assigned the PR back to `lovelace-coder-bot` to resolve and regenerate.
* **2026-07-03**: `lovelace-coder-bot` resolved all previous CI failures (`unit-tests`, `unit-tests-operator`, `validate-generated-files`, and schema/exclusion issues for `validations`) and successfully pushed the fixes. Updated CI checks are currently running with no failures so far.
* **2026-07-03**: Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) remains open with failing CI checks (`unit-tests`, `unit-tests-operator`, `validate-generated-files`, `validations`). lovelace-coder-bot remains assigned for fixes.
* **2026-07-02**: Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) CI checks have failed (`unit-tests`, `unit-tests-operator`, `validate-generated-files`, `validations`). Assigned the PR to lovelace-coder-bot for fixes.
* **2026-07-02**: Step 1 Pull Request [#11252](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11252) has been created by lovelace-coder-bot and is currently under review with CI checks in progress.
* **2026-07-02**: Initialized Greenfield Migration Checklist orchestration. Created Step 1 GitHub issue [#11243](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/11243) for generating direct KRM types and identity.
