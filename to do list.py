# Simple To-Do List App

tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks added yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


def delete_task():
    show_tasks()

    if tasks:
        try:
            number = int(input("\nEnter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")