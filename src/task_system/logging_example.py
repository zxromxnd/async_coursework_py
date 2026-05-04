from src.task_system import Task, TaskProcessor


processor = TaskProcessor()


def simple_handler(data):
    value = data.get("value", 0)
    return value * 2


print("Example: Task processing with logging\n")

task1 = Task(1, "double value", priority=5, data={"value": 10})
task2 = Task(2, "double another", priority=3, data={"value": 25})

print("Processing tasks (watch for logs):\n")

result1 = processor.process(task1, simple_handler)
print(f"Result 1: {result1}\n")

result2 = processor.process(task2, simple_handler)
print(f"Result 2: {result2}\n")

print("Done! All tasks logged.")