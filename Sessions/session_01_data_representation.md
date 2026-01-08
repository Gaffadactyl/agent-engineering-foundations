# Session #: 01

## Objective: Represent information in a structured, deterministic way

## Artifacts:
- src/summarize_task.py

---

## Prerequisites (Declared & Satisfied)

No prior Python knowledge assumed.
All concepts were introduced during this session.

---

## New concepts introduced and defined today:
- Strings
- Functions
- Dictionaries
- Input → Output
- Determinism

---

## Core idea (Theory)

Before an agent can reason or act, it must be able to **represent information clearly**.

This session focused on:
- separating description from action
- turning raw text into structured data
- ensuring deterministic output (same input → same result)

Agents reason over **structured representations**, not raw strings.

---

## New Definitions (Plain Language)

### String
A string is text.

Example:
"build an agent"

Strings hold information but have no structure by themselves.

Function
A function is a named set of steps that:

accepts input
returns output

Functions allow us to reason about behavior in isolation.

Dictionary
A dictionary is a labeled container for data.

Example:

{
    "task": "build an agent",
    "length": 15
}
Dictionaries make implicit meaning explicit by naming values.

See One (Complete, Explained Example)

def describe_task(task):
    return {
        "task": task,
        "note": "this function only describes data"
    }
Explanation:

the function receives text
the function returns structured data
no action is taken
nothing is executed
This establishes the separation between description and action.

Do One (Session Task)
Write a function summarize_task(task) that:

accepts a string
returns a dictionary with:
"original" → the input string
"length" → number of characters

Final Correct Implementation

def summarize_task(task):
    return {
        "original": task,
        "length": len(task)
    }

Teach One
Why is a dictionary useful here instead of returning just a string?
From my perspective a dictionary takes unstructured data and makes it structured and usable.
<A dictionary turns unstructured text into structured data, making the information explicit and usable by other parts of the system.>

Why is it important that this function describes data instead of doing actions?
I believe describing data is a prerequisite to use data for functions.
<Describing data is a prerequisite for reasoning. Acting before description removes flexibility and safety.>

How does this pattern help when building agents later?
The agent will later use this dictionary to process strings into usable data
<Agents rely on structured state to plan, evaluate, and decide actions. This pattern creates that state.>

Outcome
Status: Pass
Time spent: 50 mins
Biggest confusion: Understanding Python syntax for dictionaries
Key unlock: Structure enables reasoning
