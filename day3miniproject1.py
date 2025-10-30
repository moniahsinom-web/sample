# Command-line To-Do List Program

def display_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️ Completed" if task["completed"] else "❌ Pending"
            print(f"{i}. {task['name']} - {status}")

def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!")

def mark_task_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter the task number to mark complete: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["completed"] = True
            print(f"Task '{tasks[task_no - 1]['name']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()
