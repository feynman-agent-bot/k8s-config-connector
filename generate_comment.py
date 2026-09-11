import re

with open(".agents/workflows/checklist-for-kind/journal/ComputeNetworkEndpoint.md", "r") as f:
    content = f.read()

parts = content.split("## Status Update Notes\n")
header = parts[0]
notes_section = parts[1].split("\n")
notes = [n for n in notes_section if n.startswith("* **")]

top_3_notes = notes[:3]

comment_body = "### Migration Progress: ComputeNetworkEndpoint\n\n"
comment_body += header.split("## Current Step\n")[1].strip() + "\n\n## Status Update Notes\n" + "\n".join(top_3_notes) + "\n"

with open("comment_body.txt", "w") as f:
    f.write(comment_body)
