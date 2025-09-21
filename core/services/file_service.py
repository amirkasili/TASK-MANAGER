import json
from config import TASKS_FILE_PATH

class FileService:
    def __init__(self, file_path=TASKS_FILE_PATH):
        self.file_path = file_path

    def load_tasks(self):
        """Load tasks from the JSON file."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        """Save tasks to the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(tasks, file, indent=4)
            