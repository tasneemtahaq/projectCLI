import json
from pathlib import Path
from typing import List
import os
from pathlib import Path



DEFAULT_DATA_FILE = Path(__file__).parent.parent / "tasks.json"
DATA_FILE = Path(os.environ.get("MYCLIAPP_DATA_FILE", DEFAULT_DATA_FILE))

class Task:
    def __init__(self, title: str, completed: bool = False):
        self.title = title
        self.completed = completed

    def complete(self):
        """Mark this task as completed."""
        self.completed = True

    def to_dict(self) -> dict:
        return {"title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        return Task(data["title"], data.get("completed", False))

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self._load()

    def _get_file_path(self) -> Path:
        # Ensure DATA_FILE is a Path
        return Path(DATA_FILE)

    def _load(self):
        file_path = self._get_file_path()
        if file_path.exists():
            try:
                data = json.loads(file_path.read_text())
                self.tasks = [Task.from_dict(item) for item in data]
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []

    def _save(self):
        file_path = self._get_file_path()
        file_path.write_text(json.dumps([t.to_dict() for t in self.tasks], indent=2))

    def add(self, title: str) -> Task:
        task = Task(title)
        self.tasks.append(task)
        self._save()
        return task

    def list(self) -> List[Task]:
        return self.tasks

    def complete(self, index: int) -> Task:
        task = self.tasks[index]
        task.complete()
        self._save()
        return task
