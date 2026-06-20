#!/usr/bin/env python3
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import re
import os
import sys
import subprocess

def get_implemented_types(apis_dir="apis"):
    implemented_kinds = {}
    struct_regex = re.compile(r"type\s+([A-Za-z0-9_]+)\s+struct\s*\{")
    if not os.path.exists(apis_dir):
        return implemented_kinds

    for root, _, files in os.walk(apis_dir):
        for file in files:
            if file.endswith("_types.go"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = struct_regex.findall(content)
                    for kind in matches:
                        if kind.endswith("Spec") or kind.endswith("Status") or kind.endswith("List") or kind.endswith("ObservedState"):
                            continue
                        if kind not in implemented_kinds:
                            implemented_kinds[kind] = []
                        implemented_kinds[kind].append(filepath)
    return implemented_kinds

def parse_static_config(config_file_path):
    # Map of Kind -> {defaultController, supportedControllers}
    configs = {}
    if not os.path.exists(config_file_path):
        print(f"Error: {config_file_path} not found.")
        return configs

    with open(config_file_path, 'r', encoding='utf-8') as f:
        config_lines = f.readlines()
        
    for line in config_lines:
        line = line.strip()
        if not line.startswith('{Group: '):
            continue
            
        group_match = re.search(r'Group:\s*"([^"]+)"', line)
        kind_match = re.search(r'Kind:\s*"([^"]+)"', line)
        default_ctrl_match = re.search(r'DefaultController:\s*k8s\.ReconcilerType([A-Za-z]+)', line)
        supported_ctrls_match = re.search(r'SupportedControllers:\s*\[\]k8s\.ReconcilerType\{(.*?)\}', line)
        
        if group_match and kind_match:
            group_full = group_match.group(1)
            group = group_full.split('.')[0]
            kind = kind_match.group(1)
            
            supported = []
            if supported_ctrls_match:
                ctrls_raw = supported_ctrls_match.group(1)
                supported = re.findall(r'k8s\.ReconcilerType([A-Za-z]+)', ctrls_raw)
            
            default_ctrl = "Unknown"
            if default_ctrl_match:
                default_ctrl = default_ctrl_match.group(1)

            configs[kind] = {
                "group": group,
                "defaultController": default_ctrl,
                "supportedControllers": supported
            }
    return configs

def determine_stage(kind, group, service, implemented_kinds):
    # Check Stage 1 & 2
    types_files = implemented_kinds.get(kind, [])
    has_stage1 = len(types_files) > 0
    has_stage2 = False
    has_stage3 = False
    has_stage4 = False
    has_stage5 = False
    
    if has_stage1:
        for tf in types_files:
            dirpath = os.path.dirname(tf)
            filename = os.path.basename(tf)
            prefix = filename.replace("_types.go", "")
            
            possible_ref_names = [
                f"{prefix}_reference.go",
                f"{prefix}_identity.go",
                f"{kind.lower()}_reference.go",
                f"{kind.lower()}_identity.go",
            ]
            for pr in possible_ref_names:
                if os.path.exists(os.path.join(dirpath, pr)):
                    has_stage2 = True
                    break
            if has_stage2:
                break
                
    # Check Stage 3 & 5
    direct_service_dir = os.path.join("pkg/controller/direct", service)
    if os.path.exists(direct_service_dir):
        kind_without_service = kind
        if kind.lower().startswith(service.lower()):
            kind_without_service = kind[len(service):]
            
        possible_fuzz_prefixes = [kind.lower(), kind_without_service.lower()]
        if has_stage1:
            for tf in types_files:
                possible_fuzz_prefixes.append(os.path.basename(tf).replace("_types.go", ""))
                
        # Check if fuzzer exists (Stage 3)
        for root, _, files in os.walk(direct_service_dir):
            for f in files:
                if f.endswith("_fuzzer.go"):
                    f_prefix = f.replace("_fuzzer.go", "").lower()
                    if f_prefix in possible_fuzz_prefixes or f_prefix == kind.lower() or f_prefix == kind_without_service.lower():
                        has_stage3 = True
                        break
            if has_stage3:
                break
                
        # Check if controller exists (Stage 5)
        for root, _, files in os.walk(direct_service_dir):
            for f in files:
                if f.endswith("_controller.go"):
                    f_prefix = f.replace("_controller.go", "").lower()
                    if f_prefix in possible_fuzz_prefixes or f_prefix == kind.lower() or f_prefix == kind_without_service.lower():
                        has_stage5 = True
                        break
                elif f == "adapter.go":
                    has_stage5 = True
                    break
            if has_stage5:
                break
                
    # Check Stage 4
    testdata_basic = "pkg/test/resourcefixture/testdata/basic"
    if os.path.exists(testdata_basic):
        for root, dirs, _ in os.walk(testdata_basic):
            for d in dirs:
                if kind.lower() in d.lower():
                    has_stage4 = True
                    break
            if has_stage4:
                break
                
    # Check mockgcp files
    mock_service_dir = os.path.join("mockgcp", "mock" + service)
    if os.path.exists(mock_service_dir):
        kind_without_service = kind
        if kind.lower().startswith(service.lower()):
            kind_without_service = kind[len(service):]
        for root, _, files in os.walk(mock_service_dir):
            for f in files:
                if f.endswith(".go") and (kind.lower() in f.lower() or kind_without_service.lower() in f.lower()):
                    has_stage4 = True
                    break
            if has_stage4:
                break
                
    if has_stage5:
        return "Stage 5 (Controller Implemented)"
    elif has_stage4:
        return "Stage 4 (MockGCP/E2E Fixtures)"
    elif has_stage3:
        return "Stage 3 (KRM Fuzzer)"
    elif has_stage2:
        return "Stage 2 (Identity & Reference Types)"
    elif has_stage1:
        return "Stage 1 (Direct KRM Types)"
    else:
        return "Investigation/Setup"

def main():
    print("Starting tracker update script...")
    
    # 1. Load static config
    static_configs = parse_static_config("pkg/controller/resourceconfig/static_config.go")
    print(f"Loaded {len(static_configs)} configurations from static_config.go.")
    
    # 2. Get implemented types from apis/
    implemented_kinds = get_implemented_types("apis")
    print(f"Detected {len(implemented_kinds)} kinds with types defined in apis/.")
    
    # 3. Load existing data.json
    data_json_path = "dev/migration-tracker/data.json"
    if not os.path.exists(data_json_path):
        print(f"Error: {data_json_path} not found.")
        sys.exit(1)
        
    with open(data_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Loaded {len(data)} resources from data.json.")
    
    # 4. Fetch GitHub Overseer/Migrate Issues (SET 1)
    print("Fetching active overseer/migrate issues from GitHub...")
    cmd_set1 = [
        "gh", "issue", "list", 
        "--state", "all", 
        "--label", "overseer", 
        "--label", "workflow/migrate", 
        "--limit", "1000", 
        "--json", "number,title,state,url,assignees"
    ]
    res_set1 = subprocess.run(cmd_set1, capture_output=True, text=True, check=True)
    set1_issues = json.loads(res_set1.stdout)
    print(f"Found {len(set1_issues)} migration tracker issues.")
    
    # 5. Fetch other open issues and open PRs (SET 2)
    print("Fetching other open issues and PRs from GitHub...")
    cmd_issues = ["gh", "issue", "list", "--state", "open", "--limit", "1000", "--json", "number,title,url,author,state"]
    res_issues = subprocess.run(cmd_issues, capture_output=True, text=True, check=True)
    open_issues = json.loads(res_issues.stdout)
    
    cmd_prs = ["gh", "pr", "list", "--state", "open", "--limit", "1000", "--json", "number,title,url,author,state"]
    res_prs = subprocess.run(cmd_prs, capture_output=True, text=True, check=True)
    open_prs = json.loads(res_prs.stdout)
    print(f"Found {len(open_issues)} open issues and {len(open_prs)} open PRs.")
    
    # Pre-build list of kind patterns sorted by length descending to match issues accurately
    all_kinds = [res['kind'] for res in data]
    sorted_kinds = sorted(all_kinds, key=len, reverse=True)
    
    # Match SET 1 issues to Kind
    set1_by_kind = {}
    for issue in set1_issues:
        title = issue['title']
        if "TRACKER: Direct Controller Migration" in title:
            continue
        # Find which Kind is mentioned in the title
        matched_kind = None
        for k in sorted_kinds:
            if re.search(rf"\b{k}\b", title):
                matched_kind = k
                break
        if matched_kind:
            if matched_kind not in set1_by_kind:
                set1_by_kind[matched_kind] = []
            set1_by_kind[matched_kind].append(issue)
            
    # Process each resource in data.json
    for res in data:
        kind = res['kind']
        group = res['group']
        service = group.split('.')[0]
        
        # Look up static config
        sc = static_configs.get(kind, {})
        supported = sc.get("supportedControllers", res.get("supportedControllers", []))
        default_ctrl = sc.get("defaultController", res.get("defaultController", "Unknown"))
        
        res['supportedControllers'] = supported
        res['defaultController'] = default_ctrl
        res['controllerType'] = default_ctrl
        
        is_direct_registered = 'Direct' in supported
        
        # Determine the current stage on disk
        stage = determine_stage(kind, group, service, implemented_kinds)
        
        if is_direct_registered:
            res['state'] = "Completed"
            res['stage'] = "Completed"
            res['steps'] = {
                "gen-types": True,
                "identity-reference": True,
                "mapper-fuzzer": True,
                "mocks": True,
                "controller": True,
                "tests": True
            }
            # Regenerate if reference file actually missing (e.g. for completed resources without references)
            types_files = implemented_kinds.get(kind, [])
            has_reference = False
            if len(types_files) > 0:
                for tf in types_files:
                    dirpath = os.path.dirname(tf)
                    filename = os.path.basename(tf)
                    prefix = filename.replace("_types.go", "")
                    possible_names = [
                        f"{prefix}_reference.go",
                        f"{kind.lower()}_reference.go",
                    ]
                    for name in possible_names:
                        if os.path.exists(os.path.join(dirpath, name)):
                            has_reference = True
                            break
                    if has_reference:
                        break
            if not has_reference:
                res['steps']['identity-reference'] = False
                res['notes'] = "Missing _reference.go" if res.get('notes') != 'Registered in code' else "Registered in code"
            else:
                res['steps']['identity-reference'] = True
                res['notes'] = "Registered in code"
                
            res['trackingIssue'] = ""
            res['external_tracking'] = ""
            res['assignee'] = ""
        else:
            # Not completed in static_config.go
            res['stage'] = stage
            
            # Reset notes and external tracking
            notes_parts = []
            external_urls = []
            tracking_issue_str = "N/A"
            assignee_str = ""
            
            # Check SET 1 active/closed tracker issues
            issues_set1 = set1_by_kind.get(kind, [])
            active_issue = None
            closed_issue = None
            for issue in issues_set1:
                if issue['state'].upper() == "OPEN":
                    active_issue = issue
                    break
                elif issue['state'].upper() == "CLOSED":
                    closed_issue = issue
            
            if active_issue:
                tracking_issue_str = f"[#{active_issue['number']}]({active_issue['url']})"
                res['state'] = "In Progress"
                if active_issue.get('assignees'):
                    assignee_str = active_issue['assignees'][0]['login']
            elif closed_issue:
                # Closed issue, but not completed!
                notes_parts.append("Anomaly: tracking issue closed but controller not registered")
                res['state'] = "In Progress" if stage != "Investigation/Setup" else "Not Started"
            else:
                # No tracker issue
                res['state'] = "In Progress" if stage != "Investigation/Setup" else "Not Started"
                
            # Scan SET 2: external open issues and PRs containing Kind
            external_items = []
            for item in open_issues + open_prs:
                title = item['title']
                number = item['number']
                # Skip if already tracked as tracking issue
                if active_issue and number == active_issue['number']:
                    continue
                # Skip if author is a bot/robot
                author = item.get('author', {}).get('login', '') if item.get('author') else ''
                if 'bot' in author.lower() or 'robot' in author.lower():
                    continue
                # Match Kind as word in title
                if re.search(rf"\b{kind}\b", title):
                    external_items.append(item)
                    
            if external_items:
                res['state'] = "In Progress"
                for item in external_items:
                    notes_parts.append(f"External Work: #{item['number']}")
                    external_urls.append(item['url'])
                    
            res['trackingIssue'] = tracking_issue_str
            res['assignee'] = assignee_str
            res['external_tracking'] = ", ".join(external_urls)
            res['notes'] = ", ".join(notes_parts)
            
            # Map steps based on stage
            stage_num = 0
            if stage.startswith("Stage 1"): stage_num = 1
            elif stage.startswith("Stage 2"): stage_num = 2
            elif stage.startswith("Stage 3"): stage_num = 3
            elif stage.startswith("Stage 4"): stage_num = 4
            elif stage.startswith("Stage 5"): stage_num = 5
            
            res['steps'] = {
                "gen-types": stage_num >= 1,
                "identity-reference": stage_num >= 2,
                "mapper-fuzzer": stage_num >= 3,
                "mocks": stage_num >= 4,
                "controller": stage_num >= 5,
                "tests": stage_num >= 4 # tests can run on Stage 4 or 5
            }
            
    # Save the updated data back to disk
    with open(data_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Saved updated data to {data_json_path}.")
    
    # 6. Step 5: Identify next pending resources
    pending_candidates = []
    completed_kinds = {res['kind'] for res in data if res['state'] == 'Completed'}
    # Also add standard Completed built-in parent kinds just in case
    completed_kinds.add("Project")
    completed_kinds.add("Folder")
    completed_kinds.add("Organization")
    completed_kinds.add("BillingAccount")
    
    for res in data:
        if res['state'] == 'Not Started' and res['defaultController'] in ('Terraform', 'DCL'):
            # Check if all dependencies are completed
            deps = res.get('dependencies', [])
            all_deps_completed = True
            for dep in deps:
                if dep not in completed_kinds:
                    all_deps_completed = False
                    break
            if all_deps_completed:
                pending_candidates.append(res)
                
    pending_candidates.sort(key=lambda x: x.get('sortOrder', 9999))
    print(f"Identified {len(pending_candidates)} pending & unblocked candidates.")
    
    # 7. Generate markdown tables and totals
    completed_count = sum(1 for res in data if res['state'] == 'Completed')
    in_progress_count = sum(1 for res in data if res['state'] == 'In Progress')
    not_started_count = sum(1 for res in data if res['state'] == 'Not Started')
    total_count = len(data)
    
    # Construct in-progress rows
    in_progress_rows = []
    # Sort in-progress by Kind
    in_progress_data = sorted([res for res in data if res['state'] == 'In Progress'], key=lambda x: x['kind'])
    for res in in_progress_data:
        tracking_issue = res['trackingIssue'] if res['trackingIssue'] else "N/A"
        assignee = res['assignee'] if res['assignee'] else ""
        in_progress_rows.append(
            f"| {res['kind']} | {res['stage']} | {tracking_issue} | {assignee} | {res['notes']} |"
        )
        
    # Construct next pending rows
    next_rows = []
    for res in pending_candidates[:30]: # limit to top 30 next candidates to keep comment size reasonable
        deps_str = ", ".join(res.get('dependencies', []))
        next_rows.append(
            f"| {res['kind']} | {res['sortOrder']} | {res['defaultController']} | {deps_str} | {res['notes']} |"
        )
        
    # Construct completed rows
    completed_rows = []
    completed_data = sorted([res for res in data if res['state'] == 'Completed'], key=lambda x: x['kind'])
    for res in completed_data:
        completed_rows.append(
            f"| {res['kind']} | {res['defaultController']} | Registered in code |"
        )
        
    # Build complete summary body
    summary_body = f"""### Migration Progress Tracker Summary

## High-Level Status
| State | Count |
|-------|-------|
| Completed | {completed_count} |
| In Progress | {in_progress_count} |
| Pending | {not_started_count} |
| Total | {total_count} |

## In Progress Resources
| Kind | Current Stage | Tracking Issue/PR | Assignee | Notes |
|------|---------------|-------------------|----------|-------|
""" + "\n".join(in_progress_rows) + """

## Next Resources (Pending & Unblocked)
| Kind | Sort Order | Default Controller | Dependencies | Notes |
|------|------------|--------------------|--------------|-------|
""" + "\n".join(next_rows) + f"""

## Completed Resources
| Kind | Default Controller | Date Completed / Notes |
|------|--------------------|------------------------|
""" + "\n".join(completed_rows)

    # 8. Post or edit comment on Coordinator Issue 10588
    coordinator_issue = "10588"
    print(f"Finding existing comment on issue {coordinator_issue}...")
    cmd_view = ["gh", "issue", "view", coordinator_issue, "--comments", "--json", "comments"]
    res_view = subprocess.run(cmd_view, capture_output=True, text=True, check=True)
    comments_data = json.loads(res_view.stdout)
    
    comment_id = None
    for comment in comments_data.get('comments', []):
        if "### Migration Progress Tracker Summary" in comment.get('body', ''):
            # Extract numeric comment ID from the URL (e.g., #issuecomment-4758933141)
            comment_url = comment.get('url', '')
            match_db_id = re.search(r'#issuecomment-(\d+)', comment_url)
            if match_db_id:
                comment_id = match_db_id.group(1)
            break
            
    if comment_id:
        print(f"Found existing comment DB ID {comment_id}. Updating via gh api...")
        payload = {"body": summary_body}
        cmd_edit = [
            "gh", "api", "-X", "PATCH", 
            f"/repos/GoogleCloudPlatform/k8s-config-connector/issues/comments/{comment_id}", 
            "--input", "-"
        ]
        subprocess.run(cmd_edit, input=json.dumps(payload), text=True, check=True)
        print("Existing comment updated successfully!")
    else:
        print("No existing comment found. Posting new comment via gh api...")
        payload = {"body": summary_body}
        cmd_create = [
            "gh", "api", "-X", "POST", 
            f"/repos/GoogleCloudPlatform/k8s-config-connector/issues/{coordinator_issue}/comments", 
            "--input", "-"
        ]
        subprocess.run(cmd_create, input=json.dumps(payload), text=True, check=True)
        print("New comment posted successfully!")

if __name__ == "__main__":
    main()
