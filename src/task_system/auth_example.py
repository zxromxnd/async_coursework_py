from src.task_system import Task, TaskProcessor
from src.auth import HttpClient, AuthProxy, ApiKeyStrategy


processor = TaskProcessor()


def make_api_request(data):
    """Simulate API request with authentication."""
    url = data.get("url", "")
    
    base_client = HttpClient()
    strategy = ApiKeyStrategy(api_key="demo-key-123")
    auth_client = AuthProxy(base_client, strategy)

    headers = strategy.add_auth()
    
    print(f"  Making request to: {url}")
    print(f"  Auth headers: {headers}")
    
    return f"Response from {url}"


def on_finished(task):
    print(f"Task {task.task_id} finished: {task.result}\n")


processor.events.on("task_finished", on_finished)


print("Example: Task with API authentication\n")

task1 = Task(
    task_id=1,
    name="fetch user data",
    priority=5,
    data={"url": "https://api.example.com/users"}
)

task2 = Task(
    task_id=2,
    name="fetch products",
    priority=3,
    data={"url": "https://api.example.com/products"}
)

print("Processing API tasks with authentication:\n")
processor.process(task1, lambda t: make_api_request(t))
processor.process(task2, lambda t: make_api_request(t))

print("All API tasks completed!")