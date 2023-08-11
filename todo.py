class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def remove_task(self, index):
        if index >= 0 and index < len(self.tasks):
            del self.tasks[index]
            return True
        return False
