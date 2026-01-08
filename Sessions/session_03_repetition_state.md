# Session #: 03

## Objective: Process multiple inputs predictably using repetition and accumulated state

## Artifacts:
- src/process_tasks.py
- tests/test_process_tasks.py

## Prerequisites (Declared & Satisfied)
You already know:
- Strings
- Functions
- Dictionaries
- Input → output
- if / else
- Tests (basic asserts)
- Import mechanics (sys.path fix)

## New concepts introduced and defined today:
- Lists
- for loops
- Accumulation (state over time)
- (Important Python nuance) Indentation controls logic

---

### Core idea (Theory)
- Agents do not reason once — they reason in cycles.
- A loop is a cycle:
  - take one item
  - apply the same decision rules
  - store the result
- Accumulation is state:
  - you start empty
  - you build results over time
  - you return the whole batch

This is the shape of an “agent-like” reasoning loop without any LLMs.

---

### New Definitions (Plain Language)

#### List
A list is an ordered collection of items.

Example:
["read", "write", "analyze data"]

#### for loop
A for loop repeats the same work for every item in a list.

Example:
for task in tasks:
    ...

#### Accumulation (State)
State is information that builds up over time.
Common pattern:
- create empty list
- append results inside the loop
- return the list

#### Indentation (Python-specific truth)
Indentation is not just formatting.
Indentation IS the logic (what belongs “inside” the loop/if).

---

### See One (Complete, Explained Example)

def summarize_tasks(tasks):
    summaries = []

    for task in tasks:
        summaries.append({
            "task": task,
            "length": len(task)
        })

    return summaries

- summaries starts empty (state)
- for loops over tasks
- each iteration appends one dictionary
- return after the loop finishes

---

### Do One

Task:
Write process_tasks(tasks) that:
- input: list of strings
- output: list of dictionaries
- each dictionary includes:
  - "task": task
  - "category": "simple" or "complex"
- rule:
  - "simple" if len(task) < 20
  - "complex" otherwise

✅ Correct final code pattern:

def process_tasks(tasks):
    results = []

    for task in tasks:
        if len(task) < 20:
            category = "simple"
        else:
            category = "complex"

        results.append({
            "task": task,
            "category": category
        })

    return results

---

### Debugging Note (Important learning)
Initial bug encountered:
- else lined up with for loop → Python interpreted it as for/else (rare feature)
- results.append was outside the loop → only one item appended at the end

Fix:
- else must line up with if
- append must be inside the for loop

This directly explains why output originally only contained the last task.

---

### Tests (as checks, not magic)

Create tests/test_process_tasks.py

We use the same sys.path pattern to ensure imports work when running the test file directly:

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

Run from repo root:
python tests/test_process_tasks.py

If it prints nothing and exits cleanly → tests pass.

---

### Teach One

- Why does results.append(...) need to be inside the loop?
results.append need to be in the loop so the result of each loop is added to the list (state)

<append must be inside the loop so each iteration contributes to accumulated state. If it’s outside, only the final iteration is captured.>

- What went wrong when the else lined up with the for loop?
Without the correct indentation the program is confused when to execute i.e. else and for are to be executed at the same time.

<In Python, else aligned with for becomes a for/else construct, which executes only after the loop completes. This caused the decision to run once instead of per task.>

- How does “loop + state + guardrails” resemble an agent reasoning cycle?
This is the structure for the logic to follow. Loop is work to be done. State is the result set. Guardrails is the testing and results.

<An agent repeatedly processes inputs (loop), accumulates memory or intermediate results (state), and applies decision rules to avoid unsafe or invalid actions (guardrails).>

## Outcome
- Status: Pass
- Time spent: 55 mins
- Biggest confusion: Indentation ownership and `for/else`
- Key unlock: Indentation defines execution flow in Python