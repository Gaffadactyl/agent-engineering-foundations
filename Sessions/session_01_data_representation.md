# Session 01 — Data Representation

## Objective
Learn how to represent information in a structured, deterministic way using Python.

## Concepts
- Strings
- Functions
- Dictionaries
- Input → Output
- Determinism

## Artifact
- src/summarize_task.py

## Teach One

### Why is a dictionary useful here instead of returning just a string?
<From my perspective a dictionary takes unstructured data and makes it structured and usable.>
<A dictionary makes implicit meaning explicit by labeling parts of the data, which allows other code (or agents) to reason over it without guessing.>

### Why is it important that this function describes data instead of doing actions?
<I believe describing data is a prerequisite to use data for functions.>
<Separating description from action allows reasoning, validation, and planning to happen before execution.>

### How does this pattern help when building agents later?
<The agent will later use this dictionary to process strings into usable data>
<Agents operate on structured representations so they can plan, evaluate, and choose actions without executing prematurely.>

## Outcome
- Status: Pass
- Notes: First official session captured in the foundations repo.