import asyncio
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
with open("tasks.txt", "w") as f:
    f.write("first task\n")
    f.write("second task\n")
    f.write("third task\n")

asyncio.run(process_tasks_from_file("tasks.txt"))

print("\nAll tasks from file processed!")