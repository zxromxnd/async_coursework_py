from src.task_system import Task, TaskProcessor
from src.cache import memoize


processor = TaskProcessor()


@memoize(max_size=10, strategy='lru')
def expensive_calculation(number):
    """Simulate expensive operation."""
    result = number ** 2
    print(f"  Computing {number}^2 = {result}")
    return result


def handle_with_cache(task_data):
    number = task_data.get("number", 0)
    return expensive_calculation(number)


def on_finished(task):
    print(f"Task {task.task_id} finished: {task.name}, result={task.result}")


processor.events.on("task_finished", on_finished)


print("Example: Task processing with cache\n")

task1 = Task(1, "calculate square", priority=5, data={"number": 10})
task2 = Task(2, "calculate square again", priority=5, data={"number": 10})
task3 = Task(3, "calculate different", priority=5, data={"number": 20})

print("Processing task 1 (cache miss - will compute):")
processor.process(task1, lambda t: handle_with_cache(t))
print()

print("Processing task 2 (cache hit - from cache):")
processor.process(task2, lambda t: handle_with_cache(t))
print()

print("Processing task 3 (cache miss - will compute):")
processor.process(task3, lambda t: handle_with_cache(t))