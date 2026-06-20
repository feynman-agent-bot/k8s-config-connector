#!/usr/bin/env python3
import os
import re
import json
import subprocess
import sys

def main():
    COORDINATOR_ISSUE_NUMBER = 10588
    DATA_JSON_PATH = "dev/migration-tracker/data.json"
    STATIC_CONFIG_PATH = "pkg/controller/resourceconfig/static_config.go"

    if not os.path.exists(DATA_JSON_PATH):
        print(f"Error: {DATA_JSON_PATH} not found.")
        sys.exit(1)

    if not os.path.exists(STATIC_CONFIG_PATH):
        print(f"Error: {STATIC_CONFIG_PATH} not found.")
        sys.exit(1)

    # 1. Load data.json
    with open(DATA_JSON_PATH) as f:
        data = json.load(f)

    # Sort data by kind/group just in case, but let's keep original order unless we need to update
    kind_to_item = {item["kind"]: item for item in data}

    # 2. Parse direct controller registrations in static_config.go
    direct_registered_kinds = set()
    with open(STATIC_CONFIG_PATH) as f:
        for line in f:
            m = re.search(r"Kind:\s*\"([^\"]+)\"", line)
            if m and "ReconcilerTypeDirect" in line:
                direct_registered_kinds.add(m.group(1))

    print(f"Found {len(direct_registered_kinds)} kinds registered with Direct in static_config.go.")

    # Apply Step 2 (Audit Ground Reality)
    for item in data:
        kind = item["kind"]
        if kind in direct_registered_kinds:
            if item.get("state") != "Completed":
                print(f"Transitioning {kind} to Completed (registered in static_config.go)")
            item["state"] = "Completed"
            item["stage"] = "Completed"
            item["notes"] = "Registered in code"
            item["trackingIssue"] = ""
            item["external_tracking"] = ""
            item["assignee"] = ""
            item["steps"] = {
                "gen-types": True,
                "identity-reference": True,
                "mapper-fuzzer": True,
                "mocks": True,
                "controller": True,
                "tests": True
            }
        else:
            if item.get("state") == "Completed":
                print(f"Warning: {kind} is marked Completed but is NOT registered in static_config.go! Reverting to In Progress.")
                item["state"] = "In Progress"
                item["notes"] = "Reverted from Completed: not registered in static_config.go"
                item["stage"] = "Investigation/Setup"

    # 3. Scan GitHub for Active Migration Workflows (SET 1)
    print("Fetching overseer migration issues...")
    try:
        overseer_raw = subprocess.check_output([
            "gh", "issue", "list", "--state", "all", "--label", "overseer,workflow/migrate", "--json", "number,title,labels,assignees,createdAt,state,url"
        ])
        overseer_issues = json.loads(overseer_raw)
    except Exception as e:
        print("Error fetching overseer issues:", e)
        overseer_issues = []

    # Map overseer issues to Kinds
    for issue in overseer_issues:
        title = issue["title"]
        # Skip coordinator tracker issue itself
        if "TRACKER" in title or issue["number"] == COORDINATOR_ISSUE_NUMBER:
            continue
        
        # Find which uncompleted Kind matches this title
        matched_kind = None
        for item in data:
            kind = item["kind"]
            if re.search(rf"\b{kind}\b", title, re.IGNORECASE):
                matched_kind = kind
                break
        
        if matched_kind:
            item = kind_to_item[matched_kind]
            issue_url = issue["url"]
            issue_num = issue["number"]
            issue_link = f"[#{issue_num}]({issue_url})"
            
            # Fetch assignee
            assignee = ""
            if issue.get("assignees"):
                assignee = issue["assignees"][0].get("login", "")

            if issue["state"].upper() == "OPEN":
                if item["state"] == "Completed":
                    # Anomaly: overseer issue open but already completed in code!
                    pass
                else:
                    if item["state"] != "In Progress":
                        print(f"Setting {matched_kind} to In Progress (open overseer issue #{issue_num})")
                        item["state"] = "In Progress"
                    item["trackingIssue"] = issue_link
                    if assignee:
                        item["assignee"] = assignee
            else: # CLOSED overseer issue
                if item["state"] != "Completed":
                    print(f"Anomaly: Overseer issue #{issue_num} for {matched_kind} is CLOSED but direct controller is not registered in static_config.go!")
                    item["state"] = "In Progress"
                    # Add anomaly to notes if not already there
                    anomaly_note = f"Anomaly: Overseer issue #{issue_num} closed but controller not registered"
                    if anomaly_note not in item.get("notes", ""):
                        if item.get("notes") and item["notes"] != "N/A":
                            item["notes"] += f", {anomaly_note}"
                        else:
                            item["notes"] = anomaly_note

    # 4. Scan GitHub for Other/External Issues and PRs (SET 2)
    print("Fetching bulk open issues and PRs...")
    try:
        issues_raw = subprocess.check_output([
            "gh", "issue", "list", "--state", "open", "--limit", "500", "--json", "number,title,url,author"
        ])
        open_issues = json.loads(issues_raw)
    except Exception as e:
        print("Error fetching open issues:", e)
        open_issues = []

    try:
        prs_raw = subprocess.check_output([
            "gh", "pr", "list", "--state", "open", "--limit", "500", "--json", "number,title,url,author"
        ])
        open_prs = json.loads(prs_raw)
    except Exception as e:
        print("Error fetching open PRs:", e)
        open_prs = []

    for item in data:
        if item["state"] == "Completed":
            continue
        kind = item["kind"]
        
        # Build set of existing tracking urls/numbers to avoid duplication
        existing_notes = item.get("notes", "") or ""
        existing_tracking = item.get("external_tracking", "") or ""
        
        new_trackings = []
        new_notes = []

        # Check issues
        for issue in open_issues:
            if issue["number"] == COORDINATOR_ISSUE_NUMBER:
                continue
            title = issue["title"]
            if re.search(rf"\b{kind}\b", title, re.IGNORECASE):
                # Check author bot filter
                author = issue.get("author", {}).get("login", "") if issue.get("author") else ""
                if "bot" in author.lower() or "robot" in author.lower():
                    continue
                
                issue_url = issue["url"]
                issue_num = issue["number"]
                
                # Check if already tracked
                if f"#{issue_num}" not in existing_notes and f"#{issue_num}" not in existing_tracking and issue_url not in existing_tracking:
                    new_trackings.append(issue_url)
                    new_notes.append(f"External Work: #{issue_num}")

        # Check PRs
        for pr in open_prs:
            title = pr["title"]
            if re.search(rf"\b{kind}\b", title, re.IGNORECASE):
                author = pr.get("author", {}).get("login", "") if pr.get("author") else ""
                if "bot" in author.lower() or "robot" in author.lower():
                    continue
                
                pr_url = pr["url"]
                pr_num = pr["number"]
                
                if f"#{pr_num}" not in existing_notes and f"#{pr_num}" not in existing_tracking and pr_url not in existing_tracking:
                    new_trackings.append(pr_url)
                    new_notes.append(f"External Work: #{pr_num}")

        if new_trackings:
            print(f"Found active external work for {kind}: {new_notes}")
            # Merge with existing
            if existing_tracking and existing_tracking != "N/A":
                track_list = [t.strip() for f in existing_tracking.split(",") for t in f.split()]
                for nt in new_trackings:
                    if nt not in track_list:
                        track_list.append(nt)
                item["external_tracking"] = ", ".join(track_list)
            else:
                item["external_tracking"] = ", ".join(new_trackings)

            if existing_notes and existing_notes != "N/A" and existing_notes != "Registered in code":
                note_list = [n.strip() for n in existing_notes.split(",")]
                for nn in new_notes:
                    if nn not in note_list:
                        note_list.append(nn)
                item["notes"] = ", ".join(note_list)
            else:
                item["notes"] = ", ".join(new_notes)

            # Mark state to In Progress if it was Not Started
            if item["state"] == "Not Started":
                item["state"] = "In Progress"

    # 5. File System Stage Detector (Step 4)
    print("Scanning filesystem to determine development stages...")
    apis_files = []
    for root, dirs, files in os.walk("apis"):
        for file in files:
            if file.endswith(".go"):
                apis_files.append(os.path.join(root, file))

    direct_files = []
    for root, dirs, files in os.walk("pkg/controller/direct"):
        for file in files:
            if file.endswith(".go"):
                direct_files.append(os.path.join(root, file))

    mockgcp_dirs = sorted([d for d in os.listdir("mockgcp") if os.path.isdir(os.path.join("mockgcp", d))])

    basic_test_dirs = []
    for root, dirs, files in os.walk("pkg/test/resourcefixture/testdata/basic"):
        for d in dirs:
            basic_test_dirs.append(d.lower())

    for item in data:
        if item["state"] != "In Progress":
            continue
        group = item["group"]
        kind = item["kind"]
        group_lower = group.lower()
        kind_lower = kind.lower()

        # Case-insensitive prefix strip
        if kind.lower().startswith(group.lower()):
            short_kind = kind[len(group):]
        else:
            short_kind = kind

        if kind == "KMSKeyRingImportJob":
            short_kind = "ImportJob"
        short_kind_lower = short_kind.lower()

        # Step 1: gen-types
        gen_types = False
        for f in apis_files:
            f_dir = os.path.basename(os.path.dirname(os.path.dirname(f))).lower()
            if f_dir == group_lower:
                f_name = os.path.basename(f).lower()
                if f_name in (f"{kind_lower}_types.go", f"{short_kind_lower}_types.go", "types.go") or "types" in f_name:
                    try:
                        with open(f, errors="ignore") as file_obj:
                            content = file_obj.read()
                        if f"type {kind} struct" in content or f"type {short_kind} struct" in content:
                            gen_types = True
                            break
                    except Exception:
                        pass

        # Step 2: identity-reference
        identity_reference = False
        for f in apis_files:
            f_dir = os.path.basename(os.path.dirname(os.path.dirname(f))).lower()
            if f_dir == group_lower:
                f_name = os.path.basename(f).lower()
                if f_name in (f"{kind_lower}_identity.go", f"{short_kind_lower}_identity.go", f"{kind_lower}_reference.go", f"{short_kind_lower}_reference.go"):
                    identity_reference = True
                    break

        # Step 3: mapper-fuzzer
        mapper_fuzzer = False
        for f in direct_files:
            f_name = os.path.basename(f).lower()
            if f_name in (f"{kind_lower}_fuzzer.go", f"{short_kind_lower}_fuzzer.go"):
                mapper_fuzzer = True
                break

        # Step 4: mocks and tests
        mocks = False
        mock_dir = f"mock{group_lower}"
        if mock_dir in mockgcp_dirs:
            mocks = True

        tests = False
        if kind_lower in basic_test_dirs or short_kind_lower in basic_test_dirs:
            tests = True

        # Step 5: controller
        controller = False
        for f in direct_files:
            f_name = os.path.basename(f).lower()
            if f_name in (f"{kind_lower}_controller.go", f"{short_kind_lower}_controller.go", "adapter.go"):
                controller = True
                break
            try:
                with open(f, errors="ignore") as file_obj:
                    content = file_obj.read()
                if "RegisterModel(" in content and (kind in content or short_kind in content):
                    controller = True
                    break
            except Exception:
                pass

        # Map steps to stage
        if controller:
            stage = "Stage 5 (Controller Implemented)"
        elif mocks and tests:
            stage = "Stage 4 (MockGCP/E2E Fixtures)"
        elif mapper_fuzzer:
            stage = "Stage 3 (KRM Fuzzer)"
        elif identity_reference:
            stage = "Stage 2 (Identity & Reference Types)"
        elif gen_types:
            stage = "Stage 1 (Direct KRM Types)"
        else:
            stage = "Investigation/Setup"

        # Update steps dictionary
        item["steps"] = {
            "gen-types": gen_types,
            "identity-reference": identity_reference,
            "mapper-fuzzer": mapper_fuzzer,
            "mocks": mocks,
            "controller": controller,
            "tests": tests
        }
        item["stage"] = stage

    # 6. Save tracking data to disk
    with open(DATA_JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print("Saved updated dev/migration-tracker/data.json.")

    # 7. Identify Next Pending Resources (Step 5)
    completed_kinds = {item["kind"] for item in data if item["state"] == "Completed"}
    
    pending_candidates = []
    for item in data:
        if item["state"] == "Not Started" and item["defaultController"] in ("Terraform", "DCL"):
            deps = item.get("dependencies", [])
            all_deps_completed = True
            for dep in deps:
                # Resolve dep to Kind
                if dep not in completed_kinds:
                    all_deps_completed = False
                    break
            if all_deps_completed:
                pending_candidates.append(item)

    pending_candidates.sort(key=lambda x: x.get("sortOrder", 9999))
    print(f"Identified {len(pending_candidates)} pending & unblocked candidates.")

    # 8. Compute Counts for summary
    completed_count = sum(1 for item in data if item["state"] == "Completed")
    in_progress_count = sum(1 for item in data if item["state"] == "In Progress")
    pending_count = sum(1 for item in data if item["state"] == "Not Started")
    total_count = len(data)

    # 9. Format lists for markdown tables
    # In Progress Resources
    in_progress_list = [item for item in data if item["state"] == "In Progress"]
    # Sort In Progress by Kind name
    in_progress_list.sort(key=lambda x: x["kind"])

    in_progress_rows = []
    for item in in_progress_list:
        kind = item["kind"]
        stage = item.get("stage", "Investigation/Setup")
        tracking = item.get("trackingIssue", "N/A") or "N/A"
        assignee = item.get("assignee", "")
        notes = item.get("notes", "") or ""
        
        # If external tracking contains URLs but notes doesn't contain links, or just print notes
        in_progress_rows.append(f"| {kind} | {stage} | {tracking} | {assignee} | {notes} |")

    # Next Resources
    next_rows = []
    for item in pending_candidates[:30]: # Limit to next 30 to keep summary clean and focused
        kind = item["kind"]
        sort_order = item.get("sortOrder", "")
        controller = item.get("defaultController", "")
        deps = ", ".join(item.get("dependencies", []))
        notes = item.get("notes", "") or ""
        next_rows.append(f"| {kind} | {sort_order} | {controller} | {deps} | {notes} |")

    # Completed Resources
    completed_list = [item for item in data if item["state"] == "Completed"]
    completed_list.sort(key=lambda x: x["kind"])
    completed_rows = []
    for item in completed_list:
        kind = item["kind"]
        controller = item.get("defaultController", "")
        notes = item.get("notes", "Registered in code")
        completed_rows.append(f"| {kind} | {controller} | {notes} |")

    # Construct the final comment body
    summary_body = f"""### Migration Progress Tracker Summary

## High-Level Status
| State | Count |
|-------|-------|
| Completed | {completed_count} |
| In Progress | {in_progress_count} |
| Pending | {pending_count} |
| Total | {total_count} |

## In Progress Resources
| Kind | Current Stage | Tracking Issue/PR | Assignee | Notes |
|------|---------------|-------------------|----------|-------|
""" + "\n".join(in_progress_rows) + f"""

## Next Resources (Pending & Unblocked)
| Kind | Sort Order | Default Controller | Dependencies | Notes |
|------|------------|--------------------|--------------|-------|
""" + "\n".join(next_rows) + f"""

## Completed Resources
| Kind | Default Controller | Date Completed / Notes |
|------|--------------------|------------------------|
""" + "\n".join(completed_rows)

    # 10. Update or Create coordinator comment on issue 10588
    print("Scanning coordinator issue comments...")
    try:
        comments_raw = subprocess.check_output([
            "gh", "issue", "view", str(COORDINATOR_ISSUE_NUMBER), "--json", "comments"
        ])
        comments_data = json.loads(comments_raw)
        comments = comments_data.get("comments", [])
    except Exception as e:
        print("Error retrieving comments:", e)
        comments = []

    target_comment_id = None
    for comment in comments:
        body = comment.get("body", "")
        if "### Migration Progress Tracker Summary" in body:
            target_comment_id = comment.get("id")
            # If the ID starts with "IC_", gh CLI likes it
            break

    if target_comment_id:
        print(f"Found existing tracker comment with ID: {target_comment_id}. Updating it...")
        # Write comment body to temp file to avoid shell argument limit
        with open("temp_comment.md", "w") as f:
            f.write(summary_body)
        try:
            subprocess.check_call([
                "gh", "api", "graphql", "-F", f"id={target_comment_id}", "-F", "body=@temp_comment.md", "-f", "query=mutation($id: ID!, $body: String!) { updateIssueComment(input: {id: $id, body: $body}) { clientMutationId } }"
            ])
            print("Successfully updated existing comment.")
        except Exception as e:
            print("Error editing comment:", e)
        finally:
            if os.path.exists("temp_comment.md"):
                os.remove("temp_comment.md")
    else:
        print("No existing tracker comment found. Creating a new one...")
        with open("temp_comment.md", "w") as f:
            f.write(summary_body)
        try:
            subprocess.check_call([
                "gh", "issue", "comment", str(COORDINATOR_ISSUE_NUMBER), "--body-file", "temp_comment.md"
            ])
            print("Successfully created a new comment.")
        except Exception as e:
            print("Error creating comment:", e)
        finally:
            if os.path.exists("temp_comment.md"):
                os.remove("temp_comment.md")

if __name__ == "__main__":
    main()
