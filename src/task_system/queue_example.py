from src.task_system import Task, TaskProcessor
from src.task_queue import BiDirectionalPriorityQueue


queue = BiDirectionalPriorityQueue()
processor = TaskProcessor()


def handle_data(data):
    return data["value"] * 2


def on_finished(task):
    print(f"Done: {task.name}, priority={task.priority}, result={task.result}")


processor.events.on("task_finished", on_finished)

queue.enqueue(Task(1, "low priority task", 1, {"value": 5}), priority=1)
queue.enqueue(Task(2, "high priority task", 10, {"value": 7}), priority=10)
queue.enqueue(Task(3, "medium priority task", 5, {"value": 3}), priority=5)

while not queue.is_empty():
    task = queue.dequeue(highest=True)
    processor.process(task, handle_data)