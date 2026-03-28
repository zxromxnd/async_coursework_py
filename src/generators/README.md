# Lab 1: Generators and Iterators

Implementation of Python generators and timeout-based iterators.

## Task

Create a generator that produces an infinite sequence of values and an iterator that processes values for a limited time.

## Implementation

### Generator
- **Type:** Incremental counter
- **Output:** 1, 2, 3, 4, 5...
- **Feature:** Infinite sequence

### Iterator
- **Feature:** Timeout-based processing
- **Statistics:** Running sum and average
- **Display:** Real-time value output

## Files

- `generators.py` - core configuration
- `main.py` - demo script
- `__init__.py` - package initialization

## Usage

Run the demo:
```bash
python lab1/main.py
```

Import in your code:
```bash
from lab1 import incremental_counter, timeout-iterator

gen = incremental_counter(1)
timeout_iterator(gen, 5)
```

## Requirements

- Python >= 3.8