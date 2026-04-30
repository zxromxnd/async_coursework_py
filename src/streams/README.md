# Lab 6: Large Data Processing with Streams

Memory-efficient processing of large datasets using async iterators and streaming.

## Task

Implement a system for processing large data sets that do not fit in memory using incremental, chunk-based processing.

## Features

- **AsyncFileIterator** - read files in chunks
- **AsyncLineIterator** - read files line by line
- **CSV streaming** - process CSV files without loading into memory
- **JSON Lines streaming** - process JSON objects one by one
- Memory-efficient processing for large datasets

## Components

### AsyncFileIterator

Reads files in configurable chunk sizes.

**Usage:**
```python
from stream_processor import AsyncFileIterator

iterator = AsyncFileIterator('large_file.txt', chunk_size=1024)

async for chunk in iterator:
    process(chunk)
```

### AsyncLineIterator

Reads files line by line.

**Usage:**
```python
from stream_processor import AsyncLineIterator

iterator = AsyncLineIterator('data.txt')

async for line in iterator:
    process(line)
```

### CSV Streaming

Process CSV files row by row.

**Usage:**
```python
from stream_processor import process_csv_stream

async def process_row(row):
    print(row)

await process_csv_stream('data.csv', process_row, skip_header=True)
```

### JSON Lines Streaming

Process JSON Lines files (one JSON object per line).

**Usage:**
```python
from stream_processor import process_json_stream

async def process_object(obj):
    print(obj)

await process_json_stream('data.jsonl', process_object)
```

## Files

- `stream_processor.py` - Core streaming implementations
- `examples.py` - Usage examples

## Running examples

```bash
python lab6/examples.py
```

## Why Streaming?

Traditional approach (loads entire file):
```python
with open('huge_file.csv') as f:
    data = f.read()
```

Streaming approach (memory-efficient):
```python
async for line in AsyncLineIterator('huge_file.csv'):
    process(line)
```

## Requirements

- Python >= 3.8