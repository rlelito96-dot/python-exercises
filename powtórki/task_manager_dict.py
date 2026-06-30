import json

def load_file(filename="saved.json"):
    """Load tasks from a JSON file.

       Args:
           filename (str): Name of the file to load.

       Returns:
            list: List of tasks loaded from file. Returns empty list if file cannot be read or JSON is invalid.
    """
    try:
        with open(filename, "r", encoding="UTF-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except OSError:
        return []

def save_file(tasks, filename="saved.json"):
    """Saving tasks to JSON file.

       Args:
           tasks (list): List of strings to save.
           filename (str): Name of file where tasks will be saved.

       Returns:
            None

    """
    try:
        with open(filename, "w+", encoding="UTF-8") as f:
            json.dump(tasks, f, indent=4)
            print("File has been saved!")
    except OSError as e:
        print(f"Error saving file: {e}")

def display_tasks():
    """Displays tasks(list of strings)."""
    if not tasks:
        print("No tasks yet. Add something.")
        return

    print("\nTask list:")

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    """Adds task to tasks."""
    adds = input("Enter the task to add: ")
    tasks.append(adds)
    print(f"Task: {adds} has been added!")


OFFSET = 1

def delete_task():
    """Deletes task from tasks."""
    if not tasks:
        print("No tasks yet. Add something.")
        return

    print("\nTask list:")
    display_tasks()

    try:
        deletes = int(input("Enter the number of task to delete: "))
        if not 0 <= deletes <= len(tasks):
            print(f"Invalid number. Choose number from 1 to {len(tasks)}.")
            return

        removed = tasks.pop(deletes - OFFSET)
        print(f"Task: {removed} has been deleted!")

    except ValueError:
        print(f"Invalid number. Choose number from 1 to {len(tasks)}.")
        return

tasks = load_file()

print("Welcome in my program!")

while True:
    print()
    print("1.Display tasks")
    print("2.Add task")
    print("3.Delete task")
    print("4.Save file")
    print("0.Exit")

    try:
        user_choice = int(input("\nEnter an action(0-4): "))
        if not -1 <= user_choice <= 5:
            print("\nInvalid action! Please choose number from 0 to 4.")
            continue
    except ValueError:
        print("\nInvalid action! Please choose number from 0 to 4.")
        continue

    if user_choice == 0:
        print("Adios!")
        break

    elif user_choice == 1:
        display_tasks()
    elif user_choice == 2:
        add_task()
    elif user_choice == 3:
        delete_task()
    elif user_choice == 4:
        save_file(tasks)

