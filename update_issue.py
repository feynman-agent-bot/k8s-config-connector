import subprocess
import json
import sys

def main():
    with open('comment_body.txt', 'r') as f:
        body = f.read()

    # Try editing issue description
    result = subprocess.run(['gh', 'issue', 'edit', '10121', '--body', body], capture_output=True, text=True)
    if result.returncode == 0:
        print("Issue description updated.")
        return
    
    print("Failed to edit issue, falling back to comment:", result.stderr)

    # Get comment ID
    result = subprocess.run(['gh', 'issue', 'view', '10121', '--json', 'comments'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to get comments:", result.stderr)
        return
    
    comments = json.loads(result.stdout).get('comments', [])
    comment_id = None
    for c in comments:
        if 'Migration Progress' in c.get('body', ''):
            comment_id = c.get('id')
            
    if comment_id:
        print(f"Updating comment {comment_id}")
        result = subprocess.run(['gh', 'api', '--method', 'PATCH', f'repos/GoogleCloudPlatform/k8s-config-connector/issues/comments/{comment_id}', '-f', f'body={body}'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Comment updated.")
        else:
            print("Failed to update comment:", result.stderr)
    else:
        print("Creating new comment")
        result = subprocess.run(['gh', 'issue', 'comment', '10121', '--body', body], capture_output=True, text=True)
        if result.returncode == 0:
            print("Comment created.")
        else:
            print("Failed to create comment:", result.stderr)

if __name__ == '__main__':
    main()
