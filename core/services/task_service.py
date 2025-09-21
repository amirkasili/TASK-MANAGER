from core.models.task import Task
from core.utils.helpers import generate_unique_id

class TaskService:
    def __init__(self, file_service):
        self.file_service = file_service
        self.tasks = self.file_service.load_tasks()

    def add_task(self, title, description, due_date):
        """Add a new task."""
        existing_ids = [task["id"] for task in self.tasks]
        new_task = Task(
            id=generate_unique_id(existing_ids),  # Use the helper function
            title=title,
            description=description,
            due_date=due_date,
        )
        self.tasks.append(new_task.to_dict())
        self.file_service.save_tasks(self.tasks)

    def edit_task(self, task_id, **kwargs):
        """Edit an existing task."""
        for task in self.tasks:
            if task["id"] == task_id:
                for key, value in kwargs.items():
                    if key in task:
                        task[key] = value
                self.file_service.save_tasks(self.tasks)
                return

    def delete_task(self, task_id):
        """Delete a task."""
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.file_service.save_tasks(self.tasks)

    def filter_tasks(self, status=None):
        """Filter tasks by status."""
        if status:
            return [task for task in self.tasks if task["status"] == status]
        return self.tasks
    