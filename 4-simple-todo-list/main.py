# simple_todo.py

class SimpleTodoList:
    def __init__(self):
        self.tasks = []  # Each task is a dict: {'task': str, 'completed': bool}

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"\nTask '{task}' added!\n")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks in the list.\n")
            return
        print("\nYour Tasks:")
        for i, t in enumerate(self.tasks, 1):
            status = "✅" if t['completed'] else "❏"
            print(f"[{i}] {status} {t['task']}")
        print()

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"\nTask '{removed['task']}' deleted!\n")
        else:
            print("\nInvalid task number!\n")

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['completed'] = True
            print(f"\nTask marked as completed!\n")
        else:
            print("\nInvalid task number!\n")

    def run(self):
        print("🚀 Welcome to the Simple Todo List!")
        while True:
            print("Todo List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("\nChoose an option: ").strip()

            if choice == '1':
                task = input("Enter task: ").strip()
                if task:
                    self.add_task(task)
                else:
                    print("Task cannot be empty!\n")

            elif choice == '2':
                self.view_tasks()

            elif choice == '3':
                self.view_tasks()
                if self.tasks:
                    try:
                        num = int(input("Enter task number to mark as completed: "))
                        self.mark_completed(num)
                    except ValueError:
                        print("Please enter a valid number.\n")

            elif choice == '4':
                self.view_tasks()
                if self.tasks:
                    try:
                        num = int(input("Enter task number to delete: "))
                        self.delete_task(num)
                    except ValueError:
                        print("Please enter a valid number.\n")

            elif choice == '5':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    todo = SimpleTodoList()
    todo.run()