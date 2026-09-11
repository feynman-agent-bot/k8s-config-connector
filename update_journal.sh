#!/bin/bash
JOURNAL=".agents/workflows/greenfield-checklist-for-kind/journal/DiscoveryEngineSitemap.md"

awk -v today="2026-09-11" '
/^## Notes & Updates/ {
    print $0
    print "- **" today "**: Monitored Step 1 Pull Request [#12032](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12032). Confirmed via `gh pr view` that the PR remains OPEN with merge conflicts (state: `DIRTY` / `CONFLICTING`). Verified that all CI checks continue to pass successfully. The PR remains paused with the `overseer/stop` label applied, awaiting human action to resolve conflicts and proceed."
    next
}
{ print $0 }
' "$JOURNAL" > temp.md && mv temp.md "$JOURNAL"
