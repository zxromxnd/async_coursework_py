import asyncio
import os
from src.streams import AsyncLineIterator
from src.task_system import Task, TaskProcessor


processor = TaskProcessor()


def process_line(data):
    """Process task data from file line."""
    text = data.get("text", "")
    return f"Processed: {text.upper()}"


def on_finished(task):
    print(f"Task {task.task_id} done: {task.result}")


processor.events.on("task_finished", on_finished)


async def process_tasks_from_file(filepath):
    """Create and process tasks from file."""
    print(f"Reading tasks from {filepath}\n")

    iterator = AsyncLineIterator(filepath)
    task_id = 1

    async for line in iterator:
        if line.strip():
            task = Task(
                task_id=task_id,
                name=f"process line {task_id}",
                priority=task_id,
                data={"text": line}
            )

            processor.process(task, lambda t: process_line(t))
            task_id += 1


print("Creating sample task file...\n")

sample_file = "tasks.txt"

try:
    with open(sample_file, "w", encoding="utf-8") as file:
        file.write("first task\n")
        file.write("second task\n")
        file.write("third task\n")

    asyncio.run(process_tasks_from_file(sample_file))

    print("\nAll tasks from file processed!")

finally:
    if os.path.exists(sample_file):
        os.remove(sample_file)