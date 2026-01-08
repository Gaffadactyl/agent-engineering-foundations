# Session #: 02

## Objective: Make safe decisions in code using explicit guardrails

## Artifacts:
- src/classify_task.py
- tests/test_classify_task.py

## Prerequisites (Declared & Satisfied)
You already know:

- Strings
- Functions
- Dictionaries
- Input → output

## New concepts introduced and defined today:

- Boolean values
- if / else
- Guardrails
- Tests (as checks, not magic)

### Core idea (Theory)
- Agents must not treat all inputs the same.

- Before an agent:
    - acts
    - plans
    - calls tools
- it must decide whether something is simple, risky, incomplete, or invalid.
- In code, decisions are expressed with control flow.

### New Definitions (Plain Language)
- Boolean
A boolean is a value that is either:

    True
    False

Booleans answer yes/no questions.

Example:

len("hi") > 10
This is either True or False.

- if / else
An if statement says:

<If this condition is true, do this. Otherwise, do something else.>

Only one branch runs.

- Guardrails
A guardrail is a check that prevents unsafe or invalid behavior.

Agents rely on guardrails to:

    avoid acting on bad input
    choose safe defaults
    stop early when needed

#### See One (Complete, Explained Example)

def classify_length(text):
    if len(text) < 10:
        return "short"
    else:
        return "long"

##### Line-by-line explanation

def classify_length(text):
Defines a function that receives text.

if len(text) < 10:
Asks a yes/no question:

“Is the text shorter than 10 characters?”

return "short"
Runs only if the condition is true.

else:
    return "long"

Runs only if the condition is false.

This ensures every input produces exactly one outcome.

###### See One (Tests — Explained)

def test_short_text():
    result = classify_length("hi")
    assert result == "short"

-   Plain English:
        Run the function
        Check the result
        Fail loudly if it’s wrong
        Tests are proof, not decoration.

##### Do One

Do One (Session Task)

Write classify_task(task) that:

accepts a string
returns a dictionary with:
    "task"
    "category" → "simple" or "complex"

rule:

"simple" if len(task) < 20
"complex" otherwise

Final Correct Implementation

def classify_task(task):
    if len(task) < 20:
        category = "simple"
    else:
        category = "complex"

    return {
        "task": task,
        "category": category
    }

Tests (as checks, not magic)

def test_simple_task():
    result = classify_task("read")
    assert result["category"] == "simple"


Tests ensure:

decisions behave as expected
changes do not silently break behavior

Debugging Note (Important Learning)

Issue encountered:
    Tests failed due to import errors

Root cause:
    Python runs files, not projects
    imports depend on execution context

Fix:
    Explicitly add src/ to sys.path

Instructor Note:
Understanding imports is critical for agent systems that load tools dynamically.

You just learned that:

- Python does not run “projects” — it runs files.

That distinction is foundational for:

- test runners
- agent execution loops
- tool loading
- multi-module systems

##### Teach One
- Why is it important that every input goes through a decision (if/else) before returning data? 
"The if/else statement acts as decision stage gates. They control the flow of decisions."

<Decisions force the system to make assumptions explicit. Without a decision point, all inputs are treated as equivalent, which leads to unsafe or incorrect behavior.>

- What problem do guardrails prevent in agents or programs? 
"They set safe defaults and avoid an AI acting on bad inputs."

<They set safe defaults and avoid an AI acting on bad inputs.>

- Why do tests matter even when the function seems simple? 
"Tests perform checks and validate outputs. Even simple functions will have exponential effects from poor decisions and bad data if/when they are added to larger models."

<Even simple functions will have exponential effects from poor decisions and bad data if/when they are added to larger models.>

Outcome

Status: Pass
Time spent: 56 mins
Biggest confusion: Python imports and execution context
Key unlock: Decisions + tests prevent silent failure