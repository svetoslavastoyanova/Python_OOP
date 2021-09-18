class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            filtered_task = [t for t in self.tasks if t.name == task_name][0]
            filtered_task.completed = True
            return f"Completed task {filtered_task.name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        uncompleted = [t for t in self.tasks if not t.completed]
        count = len(self.tasks) - len(uncompleted)
        self.tasks = uncompleted
        return f"Cleared {count} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for t in self.tasks:
            result += f"{t.details()}\n"
        return result