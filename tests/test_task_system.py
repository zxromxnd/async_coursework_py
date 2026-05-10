import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.task_system import Task, TaskProcessor
from src.task_queue import BiDirectionalPriorityQueue
from src.cache import memoize


def test_task_processing():
    processor = TaskProcessor()
    task = Task(1, "test task", priority=5, data={"value": 10})

    def handler(data):
        return data["value"] * 2

    result = processor.process(task, handler)

    assert result == 20
    assert task.status == "done"
    assert task.result == 20


def test_priority_queue():
    queue = BiDirectionalPriorityQueue()

    low = Task(1, "low", priority=1, data={})
    high = Task(2, "high", priority=10, data={})
    medium = Task(3, "medium", priority=5, data={})

    queue.enqueue(low, priority=low.priority)
    queue.enqueue(high, priority=high.priority)
    queue.enqueue(medium, priority=medium.priority)

    first = queue.dequeue(highest=True)
    second = queue.dequeue(highest=True)
    third = queue.dequeue(highest=True)

    assert first.name == "high"
    assert second.name == "medium"
    assert third.name == "low"


def test_cache():
    calls = {"count": 0}

    @memoize(max_size=5, strategy="lru")
    def square(number):
        calls["count"] += 1
        return number * number

    first = square(5)
    second = square(5)

    assert first == 25
    assert second == 25
    assert calls["count"] == 1


if __name__ == "__main__":
    test_task_processing()
    test_priority_queue()
    test_cache()
    print("All tests passed.")