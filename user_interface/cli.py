from .get_input import (
    get_string_input,
    get_date_input,
    get_task_id_input,
    get_status
)
from typing import List
from .erorrs import display_error
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class CLI:
    def __init__(self, task_service):
        self.task_service = task_service
        self.valid_statuses : List = ['done','pending']

    def display_welcome_banner(self):
        """Display a welcome banner with 'KASILI'."""
        print(Fore.CYAN + r"""
                     _        _  __         _ _ _ 
     /\             (_)      | |/ /        (_) (_)
    /  \   _ __ ___  _ _ __  | ' / __ _ ___ _| |_ 
   / /\ \ | '_ ` _ \| | '__| |  < / _` / __| | | |
  / ____ \| | | | | | | |    | . \ (_| \__ \ | | |
 /_/    \_\_| |_| |_|_|_|    |_|\_\__,_|___/_|_|_|
                                                  
        """)
        print(Fore.YELLOW + "Welcome to the Amir Kasili Task Manager CLI!\n")

    def display_tasks(self, tasks):
        """Display a list of tasks."""
        if not tasks:
            print(Fore.YELLOW + "\nNo tasks found.")
            return
        for task in tasks:
            status_color = Fore.GREEN if task['status'] == 'DONE' else Fore.RED
            print(
                f"ID: {Fore.CYAN}{task['id']}{Style.RESET_ALL}, "
                f"Title: {Fore.BLUE}{task['title']}{Style.RESET_ALL}, "
                f"Due Date: {Fore.MAGENTA}{task['due_date']}{Style.RESET_ALL}, "
                f"Status: {status_color}{task['status']}{Style.RESET_ALL},\n"
                f"discription: {Fore.CYAN}{task['description']}{Style.RESET_ALL}\n"
            )

    def run(self):
        """Run the CLI."""
        self.display_welcome_banner()  # Display the banner at the start
        while True:
            print(Fore.YELLOW + "\n===== Task Manager =====")
            print(Fore.CYAN + "1. Add Task\n2. Edit Task\n3. Delete Task\n4. Filter Tasks\n5. Exit")
            choice = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)

            if choice == "1":
                try:
                    title = get_string_input("Enter title: ")
                    description = get_string_input("Enter description: ")
                    due_date = get_date_input("Enter due date or 'ENTER' for today's date (YYYY-MM-DD): ")
                    self.task_service.add_task(title, description, due_date)
                    print(Fore.GREEN + "Task added successfully!")
                except Exception as e:
                    display_error(str(e))

            elif choice == "2":
                try:
                    task_id = get_task_id_input("Enter task ID to edit: ", self.task_service)
                    status = get_status("Enter new status ('P' or 'PENDING' / 'D' or 'DONE'): ", self.valid_statuses)
                    updates = {}
                    if status:
                        updates["status"] = status
                    self.task_service.edit_task(task_id, **updates)
                    print(Fore.GREEN + "Task updated successfully!")
                except Exception as e:
                    display_error(str(e))

            elif choice == "3":
                try:
                    task_id = get_task_id_input("Enter task ID to delete: ", self.task_service)
                    self.task_service.delete_task(task_id)
                    print(Fore.GREEN + "Task deleted successfully!")
                except Exception as e:
                    display_error(str(e))

            elif choice == "4":
                status = get_status("Filter by status ('P' or 'PENDING' / 'D' or 'DONE'), leave blank for all): ", self.valid_statuses)
                tasks = self.task_service.filter_tasks(status)
                self.display_tasks(tasks)

            elif choice == "5":
                print(Fore.YELLOW + "Exiting...")
                break

            else:
                display_error("Invalid choice. Please try again.")
                