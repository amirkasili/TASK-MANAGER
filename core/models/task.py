class Task:
    def __init__(self, id, title, description, due_date, status="pending"):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_as_done(self):
        """Mark the task as done."""
        self.status = "done"

    def to_dict(self):
        """Convert the task object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }