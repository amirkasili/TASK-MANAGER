class InvalidInputError(Exception):
    """Raised when the user provides invalid input."""
    pass

class TaskNotFoundError(Exception):
    """Raised when a task with the given ID is not found."""
    pass

def display_error(message):
    """Display an error message to the user."""
    print(f"Error: {message}")