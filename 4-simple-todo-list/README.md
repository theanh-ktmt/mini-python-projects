# Simple Todo List

## 📌 Requirements
Build a simple todo list manager that allows users to:

- Add a new task
- View all tasks
- Delete a task by index
- Mark a task as completed
- Exit the program

## 🧩 Required Functions (via Class)
Create a class SimpleTodoList with the following methods:

- `add_task(task: str)` – Adds a new task (initially not completed)
- `view_tasks()` – Displays all tasks with index and status
- `delete_task(index: int)` – Deletes a task by its number (1-based index from user)
- `mark_completed(index: int)` – Marks a task as completed
- `run()` – Runs the main loop for user interaction

## 📝 Input & Output Examples

```shell
Todo List Menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Choose an option: 1
Enter task: Buy groceries

Task added!

Choose an option: 2
[1] ❏ Buy groceries

Choose an option: 3
Enter task number to mark as completed: 1

Task marked as completed!

Choose an option: 2
[1] ✅ Buy groceries

Choose an option: 4
Enter task number to delete: 1

Task deleted!

Choose an option: 5
Goodbye!
```