# Lab 3: Memoization Function

Implementation of memoization decorator with configurable cache eviction strategies.

## Task

Create a memoization function that wraps pure functions, caching results to avoid redundant calculations. Support multiple eviction strategies to manage cache size.

## Features

- Basic memoization with unlimited cache
- Least Recently Used (LRU) eviction strategy
- Least Frequently Used (LFU) eviction strategy
- Time-Based cache expiry
- Configurable cache size and TTL

## Implementation

### Eviction Strategies

**Least Recently Used (LRU)**
- Removes oldest unused entries when cache is full
- Usage: `@memoize(max_size=100, strategy='lru')`

**Least Frequently Used (LFU)**
- Removes least accessed entries
- Usage: `@memoize(max_size=100, strategy='lfu')`

**Time-Based Expiry**
- Expires cache entries after specified time
- Usage: `@memoize(strategy='time', ttl=60)`

## Files

- `memoization.py` - core decorator implementation
- `test_lru.py` - tests for LRU strategy
- `test_lfu.py` - tests for LFU strategy
- `examples.py` - usage examples for all strategies

## Usage

Basic usage:
```python
from lab3 import memoize

@memoize(max_size=100)
def expensive_function(x):
    return x * 2
```

Run examples:
```bash
python lab3/examples.py
```

Run tests:
```bash
python lab3/test_lru.py
python lab3/test_lfu.py
```

## Requirements

- python >= 3.8