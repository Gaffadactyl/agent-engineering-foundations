def process_tasks(tasks):
    results: list[dict] = []

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