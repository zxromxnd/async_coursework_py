# Async Coursework Py

Asynchronous Task Processing and Monitoring System.

Coursework project in Python. The system demonstrates how different programming components can work together in a small task processing application.

## About

The project is based on laboratory works from chapter 2.

Main idea:

1. Create tasks.
2. Put tasks into a priority queue.
3. Process tasks.
4. Send events about task status.
5. Cache repeated results.
6. Process data asynchronously.
7. Read tasks from streams.
8. Use authentication proxy for API-like requests.
9. Log task processing.

The project is intentionally simple and educational. It is made to show how separate components can be connected into one system.

## Main Components

### Generators

Location: `src/generators/`

Used for creating incremental task ids.

### Cache

Location: `src/cache/`

Memoization decorator with configurable cache strategies:

- LRU
- LFU
- Time-based expiry

In the coursework demo it is used to cache repeated calculations.

### Task Queue

Location: `src/task_queue/`

Bi-directional priority queue.

It supports:

- highest priority
- lowest priority
- oldest item
- newest item

In the coursework demo it is used to process important tasks first.

### Async Processing

Location: `src/async_processing/`

Asynchronous map implementations:

- callback-based version
- future-based version
- async/await version
- abort controller support

In the coursework demo it is used to process a list of values asynchronously.

### Streams

Location: `src/streams/`

Async iterators for memory-efficient file processing.

Supports:

- chunk-based file reading
- line-by-line reading
- CSV streaming
- JSON Lines streaming

In the coursework demo it is used to create tasks from a file.

### Events

Location: `src/events/`

Simple EventEmitter implementation.

Supports:

- subscribe
- unsubscribe
- multiple listeners
- safe listener execution

In the coursework demo it is used through `TaskProcessor` events.

### Auth Proxy

Location: `src/auth/`

Authentication proxy for API-like requests.

Includes:

- base HTTP client
- auth proxy
- API key strategy
- bearer token strategy
- JWT strategy

In the coursework demo it shows how auth headers can be added before a request.

### Logging Tools

Location: `src/logging_tools/`

Logging decorator with:

- INFO level
- DEBUG level
- ERROR level
- sync function support
- async function support
- console logging
- file logging
- text formatter
- JSON formatter

In the coursework demo it is used by `TaskProcessor`.

### Task System

Location: `src/task_system/`

Main coursework layer.

Includes:

- `Task`
- `TaskProcessor`
- examples that connect queue, cache, streams, auth, events and logging

This module connects laboratory components into one task processing system.

## Project Structure

```text
async_coursework_py/
|-- examples/
|   |-- main_demo.py
|
|-- src/
|   |-- async_processing/
|   |-- auth/
|   |-- cache/
|   |-- events/
|   |-- generators/
|   |-- logging_tools/
|   |-- streams/
|   |-- task_queue/
|   |-- task_system/
|
|-- docs/
|-- tests/
|-- README.md
|-- pyproject.toml
|-- LICENSE
```

## Running Main Demo

Run from project root:

```bash
python -m examples.main_demo
```

The demo shows:

- task creation
- priority-based processing
- event monitoring
- cached calculation
- async processing
- stream-created tasks
- auth proxy usage
- logging

## Running Separate Examples

Task system:

```bash
python -m src.task_system.examples
python -m src.task_system.queue_example
python -m src.task_system.cached_example
python -m src.task_system.stream_example
python -m src.task_system.auth_example
python -m src.task_system.logging_example
```

Component examples:

```bash
python src/cache/examples.py
python src/task_queue/examples.py
python src/async_processing/examples.py
python src/streams/examples.py
python src/events/examples.py
python -m src.auth.examples
python -m src.logging_tools.examples
```

## Requirements

- Python >= 3.8

## Author

Eugene Briukhovetskyi  
Group IM-51

## License

MIT