# advanced_todo.py

class AdvancedTodoList:
    def __init__(self):
        self.tasks = []
        self.priorities = {'high': 3, 'medium': 2, 'low': 1}  # For sorting

    def add_task(self, task, priority='medium', due_date=None):
        priority = priority.lower()
        if priority not in self.priorities:
            print("Invalid priority! Using 'medium'.")
            priority = 'medium'
        self.tasks.append({
            'task': task,
            'completed': False,
            'priority': priority,
            'due_date': due_date
        })
        due_msg = f" [Due: {due_date}]" if due_date else ""
        print(f"\nTask '{task}' (Priority: {priority.capitalize()}){due_msg} added!\n")

    def view_tasks(self, filter_by=None):
        filtered_tasks = self.tasks.copy()

        if filter_by == 'completed':
            filtered_tasks = [t for t in filtered_tasks if t['completed']]
        elif filter_by == 'pending':
            filtered_tasks = [t for t in filtered_tasks if not t['completed']]
        elif filter_by and filter_by.startswith('priority:'):
            prio = filter_by.split(':')[1]
            filtered_tasks = [t for t in filtered_tasks if t['priority'] == prio]

        if not filtered_tasks:
            print(f"\nNo tasks to show ({filter_by.replace(':', ' ')}).\n")
            return

        print(f"\nTasks ({filter_by.replace(':', ' ') if filter_by else 'All'}):")
        for i, t in enumerate(filtered_tasks, 1):
            status = "✅" if t['completed'] else "❏"
            due_msg = f" [Due: {t['due_date']}]" if t['due_date'] else ""
            print(f"[{i}] {status} ({t['priority'].capitalize()}) {t['task']}{due_msg}")
        print()

    def search_tasks(self, keyword):
        found = [t for t in self.tasks if keyword.lower() in t['task'].lower()]
        if not found:
            print(f"\nNo tasks found containing '{keyword}'.\n")
            return
        print(f"\nSearch Results for '{keyword}':")
        for i, t in enumerate(found, 1):
            status = "✅" if t['completed'] else "❏"
            due_msg = f" [Due: {t['due_date']}]" if t['due_date'] else ""
            print(f"[{i}] {status} ({t['priority'].capitalize()}) {t['task']}{due_msg}")
        print()

    def mark_completed(self, index):
        available_tasks = [t for t in self.tasks]
        if 1 <= index <= len(available_tasks):
            task = available_tasks[index - 1]
            task['completed'] = True
            print(f"\nTask marked as completed!\n")
        else:
            print("\nInvalid task number!\n")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"\nTask '{removed['task']}' deleted!\n")
        else:
            print("\nInvalid task number!\n")

    def sort_tasks(self, by):
        if by == 'priority':
            self.tasks.sort(key=lambda t: self.priorities[t['priority']], reverse=True)
        elif by == 'due_date':
            # Sort by due date (assuming YYYY-MM-DD format)
            self.tasks.sort(key=lambda t: (t['due_date'] or '9999-99-99'))
        elif by == 'status':
            self.tasks.sort(key=lambda t: t['completed'])  # Incomplete first
        else:
            print("Invalid sort option!\n")
            return
        print(f"\nTasks sorted by {by}.\n")

    def run(self):
        print("🚀 Welcome to the Full Todo List!")
        while True:
            print("Full Todo List Menu:")
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. View Pending Tasks")
            print("4. View Completed Tasks")
            print("5. Search Task")
            print("6. Sort Tasks")
            print("7. Mark Completed")
            print("8. Delete Task")
            print("9. Exit")
            choice = input("\nChoose an option: ").strip()

            if choice == '1':
                task = input("Enter task: ").strip()
                if not task:
                    print("Task cannot be empty!\n")
                    continue
                priority = input("Enter priority (high/medium/low) [default: medium]: ").strip() or 'medium'
                due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()
                due_date = due_date if due_date else None
                self.add_task(task, priority, due_date)

            elif choice == '2':
                self.view_tasks()

            elif choice == '3':
                self.view_tasks('pending')

            elif choice == '4':
                self.view_tasks('completed')

            elif choice == '5':
                keyword = input("Enter keyword to search: ").strip()
                if keyword:
                    self.search_tasks(keyword)
                else:
                    print("Search cannot be empty!\n")

            elif choice == '6':
                sort_by = input("Sort by (priority/due_date/status): ").strip().lower()
                self.sort_tasks(sort_by)

            elif choice == '7':
                self.view_tasks()
                if self.tasks:
                    try:
                        num = int(input("Enter task number to mark as completed: "))
                        self.mark_completed(num)
                    except ValueError:
                        print("Please enter a valid number.\n")

            elif choice == '8':
                self.view_tasks()
                if self.tasks:
                    try:
                        num = int(input("Enter task number to delete: "))
                        self.delete_task(num)
                    except ValueError:
                        print("Please enter a valid number.\n")

            elif choice == '9':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    todo = AdvancedTodoList()
    todo.run()