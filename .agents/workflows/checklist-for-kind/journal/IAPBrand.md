# Migration Journal: IAPBrand

**Current Step:** Step 1: Direct API Types

| Step | Name | Issue | Pull Request | Status | Date Started | Date Completed |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Direct API Types | [Issue #10375](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/10375) | [PR #10379](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10379), [PR #10381](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10381), [PR #10385](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10385) | PR Created | 2026-06-16 | - |
| 2 | Identity and Reference Types Pattern | - | - | - | - | - |
| 3 | Create a Round-Trip KRM Fuzzer | - | - | - | - | - |
| 4 | Implement Direct Controller & E2E Fixtures | - | - | - | - | - |

## Status Updates
- **2026-06-17**: Checked progress on Step 1. Pull Request #10381 remains open with failing CI checks (`unit-tests` and `validations`). Commented `/assign factorybot-robot` on the parent issue #9737 to request automated correction. Step 1 remains in progress.
- **2026-06-17**: Checked progress. Pull Request #10385 remains open with failing CI checks (validate-generated-files, validations). Assigned `factorybot-robot` to PR #10385 via the GitHub CLI to trigger automated correction and re-trigger CI. Step 1 remains in progress.
- **2026-06-17**: Checked progress. Pull Requests #10379 and #10381 remain open and are blocked by failing CI checks on the same commit 79f48c70c9. The PRs are currently assigned to `factorybot-robot` and we are waiting for the automated watch daemon to correct the failed checks (`unit-tests`, `validate-generated-files`, `validations`). Step 1 remains in progress.
- **2026-06-17**: Checked progress. Both PR #10379 and PR #10381 remain open and are blocked by failing CI checks (unit-tests, validate-generated-files, validations). Commented `/assign factorybot-robot` on both PRs to request automated correction. Step 1 remains in progress.
- **2026-06-17**: Checked progress. Pull Requests #10379 and #10381 remain open with failing CI checks (validations, unit-tests, validate-generated-files). Attempted direct REST API assignment to `factorybot-robot` on the child PRs but received permission 404s. Requesting automated correction by commenting `/assign factorybot-robot` on the parent issue. Step 1 remains in progress.
- **2026-06-17**: Checked progress on Step 1. Both Pull Requests #10379 and #10381 remain open and are blocked by failing CI checks (validations, unit-tests, validate-generated-files) on commit 79f48c70c9. Re-assigned the PRs to `factorybot-robot` using the GitHub API to re-trigger automated correction of the failed checks. Step 1 remains in progress.
- **2026-06-17**: Checked progress. Pull Request #10379 and #10381 are both open but currently blocked by failing CI checks (unit-tests, validations, validate-generated-files) on commit 79f48c70c9. Step 1 remains in progress.
- **2026-06-17**: Checked progress. Pull Request #10381 has been opened with the `overseer` label to address Issue #10375. Both PR #10379 and PR #10381 are currently failing CI checks. Investigation of GHA run 27657392037 shows that `validate-generated-files` is failing due to an out-of-date generated file (`apis/cloudbuild/v1alpha1/types.generated.go`), and `unit-tests` is failing due to a runner infrastructure `gcloud` CLI authentication issue. The code compiles and passes local validation checks. Step 1 remains in progress.
- **2026-06-17**: Checked progress. Pull Request #10379 remains open with failing CI checks (validations, unit-tests, validate-generated-files). Re-assigned the PR to `factorybot-robot` to trigger automated correction of the failed checks.
- **2026-06-17**: Checked progress on Pull Request #10379. Analyzed failed CI check-runs:
  1. `validate-generated-files` failed because the reference documentation (`iapbrand.md` and `iapsettings.md`) is out-of-date and needs to be regenerated via `make resource-docs`.
  2. `unit-tests` failed (`TestCRDFieldPresenceInTests`) because newly introduced fields on `IAPSettings` / `IAPBrand` are not yet covered in tests and must be added to the exceptions list in `tests/apichecks/testdata/exceptions/missingfields.txt` (which is typically updated automatically by running the unit tests check script).
  Step 1 remains in progress while the watch daemon / automated correction processes these fixes.
- **2026-06-17**: Checked progress. Pull Request #10379 has been opened by `lovelace-coder-bot` to address Issue #10375. CI checks were previously failing on `validate-generated-files` and `unit-tests`, but a new CI run has been triggered and is currently in progress.
- **2026-06-16**: Checked progress. No PR has been opened yet. Step 1 remains in progress.
- **2026-06-16**: AI Factory (argus-watcher-bot) started fixing Issue #10375 in a sandbox.
- **2026-06-16**: Assigned Issue #10375 to codebot-robot to begin implementation of Step 1.
- **2026-06-16**: Added the `overseer` label to Issue #10375 to trigger the AI Factory (argus-watcher-bot) for Step 1 implementation.
- **2026-06-16**: Started migration for IAPBrand. Opened Issue #10375 to implement direct KRM types and generate.sh for IAPBrand.
