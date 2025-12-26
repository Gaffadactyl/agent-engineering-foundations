import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from classify_task import classify_task

def test_simple_task():
    result = classify_task("read")
    assert result["category"] == "simple"

def test_complex_task():
    result =   classify_task("read write")
    assert result ["category"] == "complex"