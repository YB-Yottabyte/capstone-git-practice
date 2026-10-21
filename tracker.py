import csv
from collections import Counter
from pathlib import Path

project = Path(__file__).resolve().parent
with (project / "tasks.csv").open(newline="") as source:
    tasks = list(csv.DictReader(source))

print("CAPSTONE TASK TRACKER")
print(f"Total tasks: {len(tasks)}")
for status, count in sorted(Counter(task["status"] for task in tasks).items()):
    print(f"{status}: {count}")
print("High-priority unfinished tasks:")
for task in tasks:
    if task["priority"] == "high" and task["status"] != "done":
        print(f"- {task['task']}")
print("Workflow:", (project / "workflow.txt").read_text().strip())
