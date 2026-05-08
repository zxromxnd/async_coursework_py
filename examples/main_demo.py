"""
Example that connects the main coursework modules in one small scenario.
"""

import asyncio
import os

from src.async_processing import async_map
from src.auth import AuthProxy, HttpClient, ApiKeyStrategy
from src.cache import memoize
from src.generators import incremental_counter
from src.streams import AsyncLineIterator
from src.task_queue import BiDirectionalPriorityQueue
from src.task_system import Task, TaskProcessor


print("Asynchronous Task Processing and Monitoring System")
print()


task_ids = incremental_counter(1)
processor = TaskProcessor()
queue = BiDirectionalPriorityQueue()


def on_started(task):
    print(f"Started task: {task.name}")


def on_finished(task):
    print(f"Finished task: {task.name}, result={task.result}")


def on_failed(task):
    print(f"Failed task: {task.name}")


processor.events.on("task_started", on_started)
processor.events.on("task_finished", on_finished)
processor.events.on("task_failed", on_failed)


@memoize(max_size=5, strategy="lru")
def calculate_square(number):
    print(f"  Calculating square for {number}")
    return number * number


def calculation_handler(data):
    number = data.get("value", 0)
    return calculate_square(number)


def add_task(name, priority, data):
    task = Task(
        task_id=next(task_ids),
        name=name,
        priority=priority,
        data=data
    )
    queue.enqueue(task, priority=priority)


print("Demo 1: priority queue + task processor + events + cache")
print()

add_task("low priority calculation", 1, {"value": 3})
add_task("high priority calculation", 10, {"value": 5})
add_task("medium priority calculation", 5, {"value": 4})
add_task("cached calculation", 3, {"value": 5})

while not queue.is_empty():
    task = queue.dequeue(highest=True)
    processor.process(task, calculation_handler)
    print()


print("Demo 2: async processing")
print()


async def async_double(number):
    await asyncio.sleep(0.05)
    return number * 2


async def run_async_demo():
    numbers = [1, 2, 3, 4]
    result = await async_map(numbers, async_double)
    print(f"Input numbers: {numbers}")
    print(f"Async result: {result}")


asyncio.run(run_async_demo())
print()


print("Demo 3: stream-created tasks")
print()

sample_file = "demo_tasks.txt"

try:
    with open(sample_file, "w", encoding="utf-8") as file:
        file.write("first stream task\n")
        file.write("second stream task\n")

    async def run_stream_demo():
        iterator = AsyncLineIterator(sample_file)

        async for line in iterator:
            task = Task(
                task_id=next(task_ids),
                name="stream task",
                priority=2,
                data={"text": line}
            )

            processor.process(task, lambda data: data["text"].upper())

    asyncio.run(run_stream_demo())

finally:
    if os.path.exists(sample_file):
        os.remove(sample_file)

print()


print("Demo 4: authentication proxy")
print()

base_client = HttpClient()
auth_strategy = ApiKeyStrategy("demo-api-key")
auth_client = AuthProxy(base_client, auth_strategy)

headers = auth_client.auth_strategy.add_auth({"Accept": "application/json"})

print("Auth proxy prepared request headers:")
print(headers)
print()


print("Demo completed.")