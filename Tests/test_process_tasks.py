import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from process_tasks import process_tasks

def test_process_tasks_returns_two_results():
    tasks = ["read", "write something long long"]
    result = process_tasks(tasks)
    
    assert len(result) == 2

def test_process_tasks_categories_are_correct():
    tasks = ["read", "write something long long"]
    result = process_tasks(tasks)

    assert result[0]["category"] == "simple"
    assert result[1]["category"] == "complex"