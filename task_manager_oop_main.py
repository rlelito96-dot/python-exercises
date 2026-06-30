class Task:
    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, due_date):
        zadanie = Task(task_name, due_date)
        self.tasks.append(zadanie)

    def remove_task(self, task_name):
        task_exists = False
        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                print("Zadanie", task.task_name, "zostało usuniete")
                task_exists = True
                break
        if not task_exists:
            print("Nie mozna odnalezc zadania o podanej nazwie")

    def display_task(self):
        if not self.tasks:
            print("Lista jest pusta")
        else:
            print("lista zadań:")

            for task in self.tasks:
                print(task.task_name, "| termin", task.due_date)

    def change_due_date(self,task_name, new_due_date):
        task_exists = False
        for task in self.tasks:
            if task.task_name == task_name:
                task.due_date = new_due_date
                print("Termin dla zadania", task.task_name, "został zmieniony na:", new_due_date)
                task_exists = True
                break

        if not task_exists:
            print("Nie mozna odnalezc zadania o nazwie:", task_name)

task_manager = TaskManager()
task_manager.add_task("Umyj naczynia", "27.07.2025")
task_manager.add_task("Wynies smieci", "29.07.2025")

task_manager.display_task()

print("--------------------")


task_manager.change_due_date("Umyj naczynia", "30.07.2025")

print("--------------------")


task_manager.remove_task("Wynies smieci")

print("--------------------")

task_manager.display_task()
