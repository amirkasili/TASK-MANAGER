from datetime import datetime
from .erorrs import (
    TaskNotFoundError,
    display_error
)
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_error(message):
    """Display error messages in red."""
    print(Fore.RED + f"⛔ {message}")

def get_string_input(prompt, allow_skip=False):
    """
    Get a non-empty string input from the user with validation.
    
    :param prompt: The prompt to display to the user.
    :return: The user's input as a string.
    """
    while True:
        user_input = input(Fore.CYAN + prompt + Style.RESET_ALL).strip()

        if not allow_skip:
            # Check if the input is empty
            if not user_input:
                display_error("Input cannot be empty. Please try again.")
                continue

            # Check if the input length is less than 4
            elif len(user_input) < 4:
                display_error("The input must be at least 4 characters long. Please try again.")
                continue

        # Check if the input starts with a number
        if user_input[0].isnumeric():
            display_error("The input cannot start with a number. Please try again.")
            continue

        # If all checks pass, return the validated input
        return user_input

def get_date_input(prompt, allow_defult=True):
    """
    Get a valid date input from the user in the format YYYY-MM-DD.
    
    :param prompt: The prompt to display to the user.
    :return: The user's input as a string in the format YYYY-MM-DD.
    """
    while True:
        user_input = input(Fore.CYAN + prompt + Style.RESET_ALL).strip()
        try:
            if not allow_defult:
                datetime.strptime(user_input, "%Y-%m-%d")
                return user_input
            else:
                return datetime.now().strftime("%Y-%m-%d")
        except ValueError:
            display_error("Invalid date format. Please use YYYY-MM-DD.")

def get_task_id_input(prompt, task_service):
    """
    Get a valid task ID input from the user.
    
    :param prompt: The prompt to display to the user.
    :param task_service: An instance of TaskService to validate the task ID.
    :return: The validated task ID as an integer.
    """
    while True:
        try:
            task_id = int(input(Fore.CYAN + prompt + Style.RESET_ALL).strip())
            if not any(task["id"] == task_id for task in task_service.tasks):
                raise TaskNotFoundError(f"Task with ID {task_id} not found.")
            return task_id
        except ValueError:
            display_error("Invalid input. Please enter a valid integer.")
        except TaskNotFoundError as e:
            display_error(str(e))

def get_status(prompt,valid_status):
    """
    Get a valid status DONE or PENDING.

    :param prompt: The prompt to get the input from the user.
    :return: The valid status DONE or PENDING.
    """
    while True:
        
        status = input(Fore.CYAN + prompt + Style.RESET_ALL).strip().lower()
        if status == 'd' or status == 'done':
            return valid_status[0]
        elif status == 'p' or status == 'pending':
            return valid_status[1]
        elif not status:
            return None 
        else:
            display_error('Invalid status. Enter "DONE"/"PENDING" or "P"/"D".')
            continue