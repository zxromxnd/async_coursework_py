from src.task_system import Task, TaskProcessor


processor = TaskProcessor()


def on_started(task):
    print(f"Started: {task}")


def on_finished(task):
    print(f"Finished: {task}, result={task.result}")


def handle_data(data):
    return data["value"] * 2


processor.events.on("task_started", on_started)
processor.events.on("task_finished", on_finished)

task = Task(1, "double value", priority=5, data={"value": 10})
processor.process(task, handle_data)