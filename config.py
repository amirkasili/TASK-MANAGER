import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the path to the tasks.json file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE_PATH = os.getenv("TASKS_FILE_PATH", os.path.join(BASE_DIR, "tasks.json"))
