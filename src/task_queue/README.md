# Lab 4: Bi-Directional Priority Queue

Implementation of a priority queue that supports both priority-based and insertion order-based operations.

## Task

Create a priority queue that allows retrieving elements based on:
- Priority order (highest/lowest)
- Insertion order (oldest/newest - FIFO/LIFO)

## Features

- Enqueue elements with priority
- Peek operations (view without removing)
- Dequeue operations (remove from queue)
- Four retrieval modes: highest, lowest, oldest, newest

## Implementation

### Operations

**enqueue(item, priority)**
Add an element with associated priority.

**peek(highest, lowest, oldest, newest)**
View element without removing:
- `highest=True` - element with highest priority
- `lowest=True` - element with lowest priority
- `oldest=True` - oldest element (FIFO)
- `newest=True` - newest element (LIFO)

**dequeue(highest, lowest, oldest, newest)**
Remove and return element using same modes as peek.

## Files

- `priority_queue.py` - main queue implementation
- `test_queue.py` - tests for all operations 
- `examples.py` - usage examples

## Usage

Basic usage:
```python
from lab4 import BiDirectionalPriorityQueue

queue = BiDicretionalPriorityQueue()

queue.enqueue("task1", priority=5)
queue.enqueue("task2", priority=3)

item = queue.dequeue(highest=True)
```
Run examples:
```bash
python lab4/examples.py
```

Run tests:
```bash
python lab4/test_queue.py
```

## Requirements

- Python >= 3.8