from src.events import EventEmitter
from src.logging_tools import log


class TaskProcessor:
    def __init__(self):
        self.events = EventEmitter()

    @log(level="INFO")
    def process(self, task, handler):
        """Process task with logging."""
        self.events.emit("task_started", task)

        try:
            task.mark_running()
            result = handler(task.data)
            task.mark_done(result)
            self.events.emit("task_finished", task)
            return result
        except Exception:
            task.mark_failed()
            self.events.emit("task_failed", task)
            raise