# 📝 Amir Kasili — Task Manager CLI

A lightweight, terminal-based **Task Manager** built in Python with a focus on clean architecture and **SOLID principles**.

---

## ✨ Features

- ➕ **Add tasks** — create tasks with a title, description, and due date
- ✏️ **Edit tasks** — update the status of any existing task
- ❌ **Delete tasks** — remove tasks by ID
- 🔍 **Filter tasks** — view tasks by status (`done` / `pending`) or see all
- 🎨 **Color-coded CLI** — intuitive, readable output powered by `colorama`
- 💾 **Persistent storage** — tasks are saved to a local `tasks.json` file
- ✅ **Input validation** — dates, IDs, strings, and statuses are all validated before use

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Install dependencies:

```bash
pip install colorama python-dotenv
```

### Running the App

```bash
python main.py
```

---

## 🖥️ Example Usage

### Adding a Task

```
===== Task Manager =====
1. Add Task
2. Edit Task
3. Delete Task
4. Filter Tasks
5. Exit
Choose an option: 1

Enter title: Fix login bug
Enter description: Users are unable to log in on mobile
Enter due date or 'ENTER' for today's date (YYYY-MM-DD): 2024-12-01

✅ Task added successfully!
```

### Viewing / Filtering Tasks

```
Choose an option: 4

Filter by status ('P' or 'PENDING' / 'D' or 'DONE'), leave blank for all): [ENTER]

ID: 100, Title: Fix login bug, Due Date: 2024-12-01, Status: pending
Description: Users are unable to log in on mobile

ID: 200, Title: Write unit tests, Due Date: 2024-11-28, Status: done
Description: Cover the task service with pytest
```

### Editing a Task

```
Choose an option: 2

Enter task ID to edit: 100
Enter new status ('P' or 'PENDING' / 'D' or 'DONE'): D

✅ Task updated successfully!
```

### Deleting a Task

```
Choose an option: 3

Enter task ID to delete: 100

✅ Task deleted successfully!
```

---

## 🏗️ Design Patterns & Principles

### SOLID Principles

| Principle | How It's Applied |
|---|---|
| **Single Responsibility** | `FileService` handles only I/O; `TaskService` handles only business logic; `CLI` handles only presentation |
| **Open/Closed** | New task fields or storage backends can be added without modifying existing classes |
| **Dependency Inversion** | `TaskService` depends on the `FileService` abstraction injected at runtime, not a concrete import |

### Separation of Concerns

The project is split into three distinct layers:

```
main.py                     ← Entry point / wiring
├── user_interface/         ← Presentation layer (CLI, input helpers, error display)
├── core/
│   ├── models/             ← Data model (Task)
│   ├── services/           ← Business logic (TaskService, FileService)
│   └── utils/              ← Shared helpers (ID generation)
```

### Dependency Injection

Services are instantiated in `main.py` and injected into dependent classes, making them independently testable and swappable.

```python
file_service = FileService()
task_service = TaskService(file_service)  # injected
cli = CLI(task_service)                   # injected
```

---

## 📁 Project Structure

```
.
├── main.py
├── config.py
├── .env
├── tasks.json
├── core/
│   ├── models/
│   │   └── task.py
│   ├── services/
│   │   ├── file_service.py
│   │   └── task_service.py
│   └── utils/
│       └── helpers.py
└── user_interface/
    ├── cli.py
    ├── get_input.py
    └── erorrs.py
```

---

## ⚙️ Configuration

The path to the task storage file can be configured via the `.env` file:

```env
TASKS_FILE_PATH=./tasks.json
```

---

## 📄 License

MIT — feel free to use, modify, and distribute.
