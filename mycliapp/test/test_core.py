import pytest
from mycliapp.core import Task

def test_complete():
    t = Task("Test")
    t.complete()
    assert t.completed is True
