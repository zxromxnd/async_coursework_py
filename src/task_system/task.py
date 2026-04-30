class Task:
    def __init__(self, task_id, name, priority, data):
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.data = data
        self.status = "created"
        self.result = None

    def mark_running(self):
        self.status = "running"

    def mark_done(self, result):
        self.status = "done"
        self.result = result

    def mark_failed(self):
        self.status = "failed"

    def __repr__(self):
        return f"Task(id={self.task_id}, name={self.name}, priority={self.priority}, status={self.status})"