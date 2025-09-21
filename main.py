from user_interface.cli import CLI
from core.services.file_service import FileService
from core.services.task_service import TaskService
def main():
    # Initialize services
    file_service = FileService()
    task_service = TaskService(file_service)
    # Start the CLI
    cli = CLI(task_service)
    cli.run()

if __name__ == "__main__":
    main()

