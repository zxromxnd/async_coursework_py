# Lab 9: Logging Decorator

Decorator-based logging system with configurable log levels, output targets and formatters.

## Task

Create a decorator-based logging system that can wrap sync and async functions while logging input, output and errors.

## Features

- Configurable log levels: INFO, DEBUG, ERROR
- Logs function calls and returned values
- DEBUG level logs function arguments
- ERROR level logs only exceptions
- Supports sync and async functions
- ISO timestamp for every log entry
- Console logging
- File logging
- Text formatter
- JSON formatter

## Implementation

### Logging Decorator

Main decorator for wrapping functions.

**Usage:**

```python
from logger import log

@log(level="INFO")
def add(a, b):
    return a + b
```

### Log Levels

**INFO:**
- Logs function call
- Logs returned value

**DEBUG:**
- Logs function call
- Logs args and kwargs
- Logs returned value

**ERROR:**
- Logs only exceptions
- Does not log successful calls

### Logger Outputs

**ConsoleLogger:**

Writes log messages to console.

```python
@log(level="INFO")
def example():
    return "ok"
```

**FileLogger:**

Writes log messages to file.

```python
from logger import log, FileLogger, TextFormatter

file_logger = FileLogger("app.log")

@log(level="INFO", logger=file_logger, formatter=TextFormatter())
def save_data():
    return "saved"
```

### Formatters

**TextFormatter:**

Creates readable text log messages.

**JsonFormatter:**

Creates structured JSON log messages.

```python
from logger import log, JsonFormatter

@log(level="INFO", formatter=JsonFormatter())
def get_status():
    return {"status": "ok"}
```

### Async Support

The decorator checks if a function is asynchronous and awaits it inside the wrapper.

```python
import asyncio
from logger import log

@log(level="INFO")
async def async_task():
    await asyncio.sleep(0.1)
    return "done"
```

## Files

- `logger.py` - logging decorator, loggers and formatters
- `examples.py` - usage examples
- `__init__.py` - module exports

## Running examples

```bash
python lab9/examples.py
```

## Requirements

- Python >= 3.8