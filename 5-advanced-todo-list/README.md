# Advanced Todo List

## 📌 Requirements
Enhance the todo list with more advanced features:

- Add task with priority (`high`, `medium`, `low`)
- Set due date (as string, e.g., "2025-04-01")
- Filter tasks by status (completed / pending)
- Filter by priority
- Search tasks by keyword
- Sort tasks (by due date, priority, or completion status)

## 🧩 Required Functions (via Class)
Create a class FullTodoList with:

- `add_task(task: str, priority: str = 'medium', due_date: str = None)`
- `view_tasks(filter_by: str = None)` – filter_by can be 'completed', 'pending', 'priority:high', etc.
- `search_tasks(keyword: str)`
- `mark_completed(index: int)`
- `delete_task(index: int)`
- `sort_tasks(by: str) – Sort by 'priority', 'due_date', 'status'`
- `run()` – Interactive menu with more options

## 📝 Input & Output Examples

```shell
Full Todo List Menu:
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Search Task
6. Sort Tasks
7. Mark Completed
8. Delete Task
9. Exit

Choose an option: 1
Enter task: Prepare presentation
Enter priority (high/medium/low): high
Enter due date (YYYY-MM-DD): 2025-03-15

Task added!

Choose an option: 2
[1] ❏ (High) Prepare presentation [Due: 2025-03-15]

Choose an option: 5
Enter keyword to search: presentation
[1] ❏ (High) Prepare presentation [Due: 2025-03-15]

Choose an option: 6
Sort by (priority/due_date/status): due_date
Tasks sorted by due date.

Choose an option: 9
Goodbye!
```