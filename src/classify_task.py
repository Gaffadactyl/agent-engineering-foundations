def classify_task(task):
    if len(task) < 20:
        category = "simple"
    else:
        category = "complex"
    
    return {
        "task": task,
        "category": category
    }