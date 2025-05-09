import json
import os
import tempfile

import pytest
from mycliapp.core import TaskManager, Task

@pytest.fixture
def tmp_tasks_file(monkeypatch):
    # Create a temporary file for tasks.json
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    # Write initial empty list
    with open(path, "w") as f:
        f.write("[]")
    # Monkeypatch DATA_FILE in the module
    from mycliapp import core
    monkeypatch.setattr(core, "DATA_FILE", path)
    return path

def test_add_and_list(tmp_tasks_file):
    tm = TaskManager()
    assert tm.list() == []
    t = tm.add("Test Task")
    assert isinstance(t, Task)
    # Reload from file to check persistence
    tm2 = TaskManager()
    assert len(tm2.list()) == 1
    assert tm2.list()[0].title == "Test Task"
    assert not tm2.list()[0].completed

def test_complete(tmp_tasks_file):
    tm = TaskManager()
    tm.add("Another Task")
    completed = tm.complete(0)
    assert completed.completed
    # Reload and verify
    tm2 = TaskManager()
    assert tm2.list()[0].completed
