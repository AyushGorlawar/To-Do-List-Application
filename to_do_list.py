import os
import json

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')
    save_tasks(tasks)

def view_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['task']} [{status}]")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as complete: ")) - 1
        tasks[task_number]["completed"] = True
        print(f'Task "{tasks[task_number]["task"]}" marked as complete.')
        save_tasks(tasks)
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: ")) - 1
        task = tasks.pop(task_number)
        print(f'Task "{task["task"]}" deleted.')
        save_tasks(tasks)
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
