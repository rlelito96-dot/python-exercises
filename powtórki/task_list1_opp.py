
class Task:
    """Represents a single task to be performed"""
    def __init__(self, task_name, due_date):
        """Creates a task.

           Args:
               task_name (str): Name of the task.
               due_date (str): Deadline for completing the task.
        """
        self.task_name = task_name
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, due_date):
        """Adds task to list(tasks).

           Args:
               task_name (str): Name of the task.
               due_date (str): Deadline for completing the task.

           Returns:
                 None
        """
        task = Task(task_name, due_date)
        self.tasks.append(task)
        print(f"Task: {task.task_name} has been added to list!")

    def remove_task(self, task_name):
        """Removes task from list.

           Args:
               task_name (str): Name of task.

           Returns:
                None

        """

        task_exists = False

        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                task_exists = True
                print(f"Task: {task.task_name} has been deleted!")
                break

        if not task_exists:
            print(f"Task: {task_name} does not exist!")

    def display_tasks(self):
        """Displays list of tasks.

           Returns:
                None

        """
        if not self.tasks:
            print("Task list is empty! Add something.")
        else:
            print("\nTask list:")

            for task in self.tasks:
                print(f"Name: {task.task_name} | Due date: {task.due_date}")

    def change_due_date(self, task_name, new_due_date):
        """Changes due date of single task.

           Args:
               task_name (str): Name of the task.
               new_due_date (str): Changed due date.

           Returns:
                 None
        """
        task_exists = False
        for task in self.tasks:
            if task.task_name == task_name:
                old_due_date = task.due_date
                task.due_date = new_due_date
                task_exists = True
                print(f"Due date of task: {task.task_name} has been changed from: {old_due_date} to {new_due_date}")
                break

        if not task_exists:
            print(f"Task: {task_name} does not exist!")


taskmanager = TaskManager()
taskmanager.add_task("Umyj naczynia", "11-07-2026")
taskmanager.add_task("Wyrzuć śmieci", "12-07-2026")
taskmanager.add_task("Zrób zakupy", "13-07-2026")
print("-------------------------------------------------------")

taskmanager.display_tasks()
print("-------------------------------------------------------")
taskmanager.remove_task("Wyrzuć śmieci")
