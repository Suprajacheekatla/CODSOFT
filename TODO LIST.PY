import json
import os
import datetime
from termcolor import colored
from pyfiglet import figlet_format

TASKS_FILE = "tasks.json"

# Stylized banner
def print_banner():
    print(colored(figlet_format("To-Do List", font="slant"), "cyan"))

# Load tasks from file safely
def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(colored(f"Error loading tasks: {e}", "red"))
            return []
    return []

# Save tasks to file safely
def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(colored(f"Error saving tasks: {e}", "red"))

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print(colored("No tasks to display.", "yellow"))
    else:
        print(colored("\nYour Tasks:", "green", attrs=["bold"]))
        for i, task in enumerate(tasks):
            status = "✔️" if task["done"] else "❌"
            created = task.get("created", "N/A")
            print(colored(f"{i + 1}. [{status}] {task['title']} (Added: {created})", "blue"))

# Add new task
def add_task(tasks):
    title = input(colored("Enter task: ", "cyan"))
    created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    tasks.append({"title": title, "done": False, "created": created_time})
    print(colored("Task added successfully!", "green"))

# Mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input(colored("Enter task number to mark as done: ", "cyan"))) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(colored("Task marked as done!", "green"))
        else:
            print(colored("Invalid task number.", "red"))
    except ValueError:
        print(colored("Please enter a valid number.", "red"))

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input(colored("Enter task number to delete: ", "cyan"))) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print(colored("Task deleted.", "green"))
        else:
            print(colored("Invalid task number.", "red"))
    except ValueError:
        print(colored("Please enter a valid number.", "red"))

# Main loop
def main():
    print_banner()
    tasks = load_tasks()
    while True:
        print(colored("\nMenu:", "magenta", attrs=["bold"]))
        print(colored("1. View Tasks", "white"))
        print(colored("2. Add Task", "white"))
        print(colored("3. Mark Task Done", "white"))
        print(colored("4. Delete Task", "white"))
        print(colored("5. Exit", "white"))

        choice = input(colored("Choose an option: ", "cyan"))
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(colored("Goodbye!", "yellow"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == "__main__":
    main()