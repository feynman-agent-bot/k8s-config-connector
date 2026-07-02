import subprocess
import sys
import json

def run_command(args):
    result = subprocess.run(args, capture_output=True, text=True)
    return result

def main():
    body_file = "/workspaces/k8s-config-connector/.agents/workflows/greenfield-checklist-for-kind/journal/temp_issue_body.md"
    
    # Try editing the parent issue first
    print("Attempting to edit parent issue 11138 description...")
    res = run_command(["gh", "issue", "edit", "11138", "-F", body_file])
    
    if res.returncode == 0:
        print("Successfully updated issue description!")
        return
        
    print(f"Failed to edit description (code {res.returncode}): {res.stderr.strip()}")
    print("Falling back to updating or creating a comment...")
    
    # Query comments to see if one already exists
    res = run_command(["gh", "api", "repos/GoogleCloudPlatform/k8s-config-connector/issues/11138/comments"])
    if res.returncode != 0:
        print(f"Error querying comments: {res.stderr}")
        sys.exit(1)
        
    comments = json.loads(res.stdout)
    existing_comment_id = None
    for comment in comments:
        if comment.get("user", {}).get("login") == "feynman-agent-bot" and "Migration Progress" in comment.get("body", ""):
            existing_comment_id = comment.get("id")
            break
            
    if existing_comment_id:
        print(f"Found existing comment {existing_comment_id}. Updating it...")
        res = run_command(["gh", "api", "-X", "PATCH", f"repos/GoogleCloudPlatform/k8s-config-connector/issues/comments/{existing_comment_id}", "-F", f"body=@{body_file}"])
    else:
        print("No existing comment found. Creating a new one...")
        res = run_command(["gh", "issue", "comment", "11138", "-F", body_file])
        
    if res.returncode == 0:
        print("Successfully updated GitHub via comment fallback!")
    else:
        print(f"Failed to update GitHub comment (code {res.returncode}): {res.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    main()
