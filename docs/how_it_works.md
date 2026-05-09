# How It Works

This file explains how the coursework project works.

## Main Idea

The project is a simple asynchronous task processing and monitoring system.

The main flow is:

1. A task is created.
2. The task is added to a priority queue.
3. The task processor processes the task.
4. Events show when the task starts and finishes.
5. Logging records processing steps.
6. Cache can save repeated results.
7. Async processing and streams show additional ways to process data.
8. Auth proxy shows how API authentication can be added.

## Main Demo

The main demo is located in:

```text
examples/main_demo.py
```

Run it from the project root:

```bash
python -m examples.main_demo
```

This demo connects the main parts of the project in one scenario.

## What Happens In The Demo

First, the project creates task ids with a generator.

Then several tasks are added to the priority queue:

- low priority task
- medium priority task
- high priority task
- cached task

The queue returns tasks by highest priority first.

Each task is processed by `TaskProcessor`.

During processing:

- task status changes
- events are emitted
- log messages are printed
- result is saved inside the task

The cached task uses the same value as one previous task, so the result is taken from cache.

Then the demo shows async processing with `async_map`.

After that, it creates tasks from file lines using stream processing.

At the end, it shows how auth proxy adds an API key header.

## Main Modules

### `src/task_system`

This is the main coursework module.

It contains:

- `Task`
- `TaskProcessor`
- examples that connect other modules

`Task` stores:

- task id
- name
- priority
- input data
- status
- result

`TaskProcessor` processes a task and changes its status.

### `src/task_queue`

Priority queue from lab 4.

It is used to process important tasks first.

### `src/cache`

Memoization from lab 3.

It is used to avoid repeated calculations.

### `src/events`

EventEmitter from lab 7.

It is used by `TaskProcessor` to react to task events.

### `src/async_processing`

Async map from lab 5.

It is used to show async processing of several values.

### `src/streams`

Async iterators from lab 6.

They are used to read file lines and create tasks from them.

### `src/auth`

Authentication proxy from lab 8.

It is used to add authentication headers to API-like requests.

### `src/logging_tools`

Logging decorator from lab 9.

It is used to log task processing.

### `src/generators`

Generator from lab 1.

It is used to create task ids.

## Why The Project Is Split Into Modules

Each laboratory work was about a separate programming topic.

In the coursework, these topics are connected into one small system.

This makes the project simple, but each module has its own role.