# Capstone Task Tracker

A small command-line project for practicing Git version control while tracking work on hero-image quality checks for a capstone project.

Run `python3 tracker.py`. It reports the sprint, task counts, the percentage of tasks completed, and unfinished high-priority tasks with their Taiga IDs. It also displays the development policy preserved during merge conflict resolution.

## Capstone task snapshot

The task names come from [Taiga user story #79](https://tree.taiga.io/project/tkandala-capstone/us/79), **Improve hero-image quality checks using original product photos**, and [task #80](https://tree.taiga.io/project/tkandala-capstone/task/80). The story concerns comparing generated hero images with original product photos while allowing authentic product lettering.

The board was checked on October 20, 2026, when all four tasks were shown as **New**. The project owner subsequently confirmed that **#80 and #81 are complete** and requested the **Sprint 3** label. The tracker records those two tasks as `done`; #82 and #83 remain `todo`. The completion updates and sprint label are owner-reported, rather than synchronized from the board, which had not yet been updated. Their `high` priority is inherited from the parent story; it is not a separately verified priority for each task. The source links identify where each task was observed.

This is a saved snapshot, not a live Taiga integration. Running the tracker does not fetch from or modify Taiga. Update `tasks.csv` manually when task progress changes. Supported statuses are `todo`, `in_progress`, and `done`.

## Completion percentage

Progress is calculated as `done tasks / total tasks * 100`. It measures task count, not effort or hours, and is printed to one decimal place. An empty task list reports 0.0% instead of dividing by zero. The current Sprint 3 snapshot reports **2/4 tasks (50.0%)**, based on the owner's completion update for #80 and #81.

This adapts the starter tracker to a specific capstone story by replacing generic examples with sourced tasks, preserving their IDs and links, and adding a progress summary.

## Git practice

Use two branches to make different edits to the same line in `workflow.txt`, merge them, resolve the conflict by retaining both policies, and inspect the resulting history.

The repository history records separate updates to `workflow.txt` on `main` and `feature/workflow`, followed by a merge commit that combines both policies. The repository includes a pull request template; that template alone is not evidence of opening or reviewing a pull request.
