import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    due_date = due_date_entry.get()
    priority = priority_combobox.get()
    category = category_entry.get()
    
    if task and due_date and priority and category:
        tasks.append({"task": task, "due_date": due_date, "priority": priority, "category": category, "completed": False})
        update_task_listbox()
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "All fields must be filled.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index[0])
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_task_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
        update_task_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "You must select a task to mark as complete.")

def search_tasks():
    search_term = search_entry.get()
    filtered_tasks = [task for task in tasks if search_term.lower() in task["task"].lower()]
    update_task_listbox(filtered_tasks)

def update_task_listbox(filtered_tasks=None):
    task_listbox.delete(0, tk.END)
    for task in (filtered_tasks or tasks):
        status = "✓" if task["completed"] else "✗"
        task_listbox.insert(tk.END, f"{task['task']} [{status}] (Due: {task['due_date']}, Priority: {task['priority']}, Category: {task['category']})")

app = tk.Tk()
app.title("Advanced To-Do List")

tasks = load_tasks()

# Frame for adding tasks
add_frame = tk.Frame(app)
add_frame.pack(pady=10)

tk.Label(add_frame, text="Task:").pack(side=tk.LEFT, padx=5)
task_entry = tk.Entry(add_frame, width=20)
task_entry.pack(side=tk.LEFT, padx=5)

tk.Label(add_frame, text="Due Date (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
due_date_entry = tk.Entry(add_frame, width=15)
due_date_entry.pack(side=tk.LEFT, padx=5)

tk.Label(add_frame, text="Priority:").pack(side=tk.LEFT, padx=5)
priority_combobox = ttk.Combobox(add_frame, values=["Low", "Medium", "High"], width=10)
priority_combobox.pack(side=tk.LEFT, padx=5)

tk.Label(add_frame, text="Category:").pack(side=tk.LEFT, padx=5)
category_entry = tk.Entry(add_frame, width=15)
category_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(add_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

# Frame for searching tasks
search_frame = tk.Frame(app)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", command=search_tasks)
search_button.pack(side=tk.LEFT, padx=5)

# Listbox for displaying tasks
task_listbox = tk.Listbox(app, width=100, height=10)
task_listbox.pack(pady=10)

# Frame for task action buttons
task_button_frame = tk.Frame(app)
task_button_frame.pack(pady=5)

complete_button = tk.Button(task_button_frame, text="Mark Completed", command=mark_task_completed)
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(task_button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

update_task_listbox()

app.mainloop()
