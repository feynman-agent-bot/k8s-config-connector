# DiscoveryEngineWidgetConfig Greenfield Migration Journal

**Current Step:** Step 1: Direct API Types and Identity and Reference Types Pattern

| Step Number & Name | GitHub Issue | GitHub Pull Request | Status | Date Started | Date Completed |
|---|---|---|---|---|---|
| Step 1: Direct API Types and Identity | [#12025](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/12025) | [#12049](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12049) | CI Failed | 2026-07-29 | - |
| Step 2: Direct Controller, E2E fixtures and Fuzzer | - | - | Pending | - | - |
| Step 3: mockGCP generation | - | - | Pending | - | - |
| Step 4: MockGCP Alignment with RealGCP | - | - | Pending | - | - |

## Step Logs & Updates
* **2026-07-29**: Deep-dived into failed CI logs for PR [#12049](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12049). Identified that `TestCRDFieldPresenceInTestsForAlpha` failed because multiple fields are missing from unstructured test objects (such as `.spec.uiSettings.enableQualityFeedback`), and `TestCRDObjectTypes` failed because `status.observedState` lacks structural schema definitions (missing properties or x-kubernetes-preserve-unknown-fields) in the generated CRD. Confirmed `ada-coder-bot` remains assigned to investigate and apply fixes.
* **2026-07-29**: Monitored Step 1 progress. Checked PR [#12049](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12049). CI checks failed (`presubmit-gatekeeper`, `unit-tests`, and `validate-generated-files` failed). Assigned the PR back to `ada-coder-bot` for resolution.
* **2026-07-29**: Monitored Step 1 progress. Checked PR [#12049](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12049). CI checks are in-progress, with key validations and test suites (such as mockgcp, e2e fixtures, preview, etc.) passing successfully.
* **2026-07-29**: Monitored Step 1 progress. Pull Request [#12049](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12049) has been created. CI checks are in progress, and no failures have been reported.
* **2026-07-29**: Monitored Step 1 progress. Issue #12025 remains Open and assigned to ada-coder-bot; no pull request has been created yet.
* **2026-07-29**: Monitored Step 1 progress. Issue #12025 is Open and assigned to ada-coder-bot; no pull request has been created yet.
* **2026-07-29**: Monitored Step 1 progress. Issue #12025 is still Open; AI Factory sandbox is active, but no pull request has been submitted yet.
* **2026-07-29**: Monitored Step 1 progress. Issue #12025 remains Open. No pull request has been created yet.
* **2026-07-29**: Monitored Step 1 progress. Issue #12025 remains Open. No pull request has been created yet; the AI Factory is still active in the sandbox.
* **2026-07-29**: Monitored Step 1 progress. Issue #12025 is still Open, and AI Factory is active in the sandbox. No pull requests have been created yet.
* **2026-07-29**: Started Step 1: Direct API Types and Identity. Created tracking issue #12025.
