# Lab 5: Async Array Functions

Asynchronous versions of array map function with multiple implementation variants.

## Task

Expand standard array map function into asynchronous versions with different approaches.

## Implementations

### Callback-based version
Traditional callback approach for asynchronous operations.

**Usage:**
```python
from async_map import async_map_callback

def transform(x):
    return x * 2

def callback(error, result):
    if error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result}")

async_map_callback([1, 2, 3], transform, callback)
```

### Promise-based version
Returns a Future object for chaining.

**Usage:**
```python
from async_map import async_map_promise

future = async_map_promise([1, 2, 3], transform)
result = future.result()
```

### Async/await version
Modern async/await syntax support.

**Usage:**
```python
from async_map import async_map
import asyncio

async def async_transform(x):
    await asyncio.sleep(0.1)
    return x * 2

result = await async_map([1, 2, 3], async_transform)
```

### AbortController support
All versions support cancellation via AbortController.

**Usage:**
```python
from async_map import async_map, AbortController

controller = AbortController()

# Can abort anytime
controller.abort()

result = await async_map([1, 2, 3], transform, controller)
```

## Files

- `async_map.py` - Core implementations
- `examples.py` - Usage examples
- `test_abort.py` - Abort functionality test

## Running examples
```bash
python lab5/examples.py
python lab5/test_abort.py
```

## Requirements

- Python >= 3.8