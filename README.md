# Capstone Task Tracker

A small command-line project for practicing Git version control while tracking work on hero-image quality checks for a capstone project.

Run `python3 tracker.py`. It reports task counts, the percentage of tasks completed, and unfinished high-priority tasks with their Taiga IDs. It also displays the development policy preserved during merge conflict resolution.

## Capstone task snapshot

The task names and statuses come from [Taiga user story #79](https://tree.taiga.io/project/tkandala-capstone/us/79), **Improve hero-image quality checks using original product photos**, and [task #80](https://tree.taiga.io/project/tkandala-capstone/task/80). The story concerns comparing generated hero images with original product photos while allowing authentic product lettering.

The snapshot was checked on October 20, 2026. Tasks #80, #81, #82, and #83 were all shown as **New**, mapped to `todo` in `tasks.csv`. Their `high` priority is inherited from the parent story; it is not a separately verified priority for each task. The source links identify where each task was observed.

This is a saved snapshot, not a live Taiga integration. Running the tracker does not fetch from or modify Taiga. Update `tasks.csv` manually when task progress changes. Supported statuses are `todo`, `in_progress`, and `done`.

## Completion percentage

Progress is calculated as `done tasks / total tasks * 100`. It measures task count, not effort or hours, and is printed to one decimal place. An empty task list reports 0.0% instead of dividing by zero. The current snapshot reports **0/4 tasks (0.0%)**, because all four tasks were New when checked.

This adapts the starter tracker to a specific capstone story by replacing generic examples with sourced tasks, preserving their IDs and links, and adding a progress summary.

## Git practice

Use two branches to make different edits to the same line in `workflow.txt`, merge them, resolve the conflict by retaining both policies, and inspect the resulting history.

The repository history records separate updates to `workflow.txt` on `main` and `feature/workflow`, followed by a merge commit that combines both policies. The repository includes a pull request template; that template alone is not evidence of opening or reviewing a pull request.
