import csv
from collections import Counter
from pathlib import Path

project = Path(__file__).resolve().parent
with (project / "tasks.csv").open(newline="") as source:
    tasks = list(csv.DictReader(source))

print("CAPSTONE TASK TRACKER")
print(f"Total tasks: {len(tasks)}")
status_counts = Counter(task["status"] for task in tasks)
completed = status_counts["done"]
completion_percentage = 100 * completed / len(tasks) if tasks else 0
print(f"Completion: {completed}/{len(tasks)} tasks ({completion_percentage:.1f}%)")
for status, count in sorted(status_counts.items()):
    print(f"{status}: {count}")
print("High-priority unfinished tasks:")
for task in tasks:
    if task["priority"] == "high" and task["status"] != "done":
        task_id = task.get("taiga_id", "")
        prefix = f"#{task_id} " if task_id else ""
        print(f"- {prefix}{task['task']}")
print("Workflow:", (project / "workflow.txt").read_text().strip())
