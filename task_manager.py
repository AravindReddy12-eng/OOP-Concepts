class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "Pending"

    def __str__(self):
        return f"{self.title} - {self.description} [{self.status}]"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed.")
                return
        print(f"Task '{title}' not found.")

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)


task_list = TaskList()
task_list.add_task("Interview prep", "aptitude, coding, hr questions")
task_list.add_task("project", "cache application")
task_list.list_tasks()
task_list.mark_complete("project")
task_list.list_tasks()
task_list.remove_task("Interview prep")
task_list.list_tasks()