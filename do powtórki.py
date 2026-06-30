
print()
print("   Welcome in my list project!".strip())




tasks = []
tasks.append("Throw trash")



def show_tasks():
    """Showing list with number and strings"""
    try:
        if not tasks:
            print("No tasks yet.Add tasks.")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
    except FileNotFoundError:
        return []

def add_task(where = "coś.txt"):
    """Adding a string to list"""
    task = input("Write your task: ")
    tasks.append(task + "\n".strip())
    save_file(tasks, where)
    print("\nTask added!")

def delete_task(tasks):
    """Deleting string from list"""
    if not tasks:
        print("No tasks yet.Add tasks.")
        return
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

    task = int(input("What number ot task do you want to delete?: "))
    index = task -1
    if 0 <= index < len(tasks):
        delete = tasks.pop(index)
        print(f"The task {delete} has been deleted!")
    else:
        print("This number does not exist!Try again.")
        return

def save_file(tasks, where = "coś.txt"):
    """Saving strings list to .txt file"""
    try:

        with open(where, "w", encoding = "utf-8") as f:
            f.write("\n".join(str(task) for task in tasks))
        print("\nFile has been saved!")
    except Exception as  e:
        print(f"Error saving file! {e}")

def load_file(where = "coś.txt"):
    """Loading strings list from .txt file"""
    try:
        with open(where, "r", encoding = "utf-8") as f:
            return(line.strip() for line in f.readlines())
    except FileNotFoundError:
        return []


tasks = list(load_file())

while True:



    print()
    print("1.Show tasks")
    print("2.Add task")
    print("3.Delete task")
    print("4.Save")
    print("5.Exit")

    try:
        user_choice = int(input("Enter your choice 1 - 5: "))
    except ValueError:
        print("Invalid input.Choose number 1-5.")
        continue

    if user_choice == 5:
        print("Goodbye!")
        break

    if user_choice == 1:
        show_tasks()
    elif user_choice == 2:
        add_task()
    elif user_choice == 3:
        delete_task(tasks)
    elif user_choice == 4:
        save_file(tasks)



