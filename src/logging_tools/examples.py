from src.logging_tools import log, FileLogger, TextFormatter, JsonFormatter
import asyncio


print("Example 1: INFO logging")

@log(level="INFO")
def add(a, b):
    return a + b

print(add(2, 3))
print()


print("Example 2: DEBUG logging")

@log(level="DEBUG")
def multiply(a, b):
    return a * b

print(multiply(4, 5))
print()


print("Example 3: ERROR logging")

@log(level="ERROR")
def broken():
    raise ValueError("Something went wrong")

try:
    broken()
except ValueError:
    print("Error was handled in example")
print()


print("Example 4: Async function logging")

@log(level="INFO")
async def async_task(name):
    await asyncio.sleep(0.1)
    return f"Task {name} finished"

print(asyncio.run(async_task("demo")))
print()


print("Example 5: File logger")

file_logger = FileLogger("example.log")

@log(level="INFO", logger=file_logger, formatter=TextFormatter())
def save_result():
    return "saved to file"

save_result()
print("Log was written to example.log")
print()


print("Example 6: JSON formatter")

@log(level="INFO", formatter=JsonFormatter())
def json_example():
    return {"status": "ok"}

print(json_example())