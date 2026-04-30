import asyncio
import json
from typing import AsyncIterator, Callable


class AsyncFileIterator:
    """
    Async iterator for reading large files in chunks.
    
    Args:
        filepath: Path to file
        chunk_size: Size of each chunk in bytes
    """
    
    def __init__(self, filepath: str, chunk_size: int = 1024):
        self.filepath = filepath
        self.chunk_size = chunk_size
        self.file = None
    
    def __aiter__(self):
        """Return async iterator."""
        self.file = open(self.filepath, 'r', encoding='utf-8')
        return self
    
    async def __anext__(self):
        """Read next chunk."""
        if self.file is None:
            raise StopAsyncIteration
        
        chunk = self.file.read(self.chunk_size)
        
        if not chunk:
            self.file.close()
            raise StopAsyncIteration
        
        await asyncio.sleep(0)
        return chunk


class AsyncLineIterator:
    """
    Async iterator for reading files line by line.
    Memory-efficient for large files.
    """
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None
    
    def __aiter__(self):
        """Return async iterator."""
        self.file = open(self.filepath, 'r', encoding='utf-8')
        return self
    
    async def __anext__(self):
        """Read next line."""
        if self.file is None:
            raise StopAsyncIteration
        
        line = self.file.readline()
        
        if not line:
            self.file.close()
            raise StopAsyncIteration
        
        await asyncio.sleep(0)
        return line.strip()


async def process_stream(iterator: AsyncIterator, processor: Callable):
    """
    Process data from async iterator.
    
    Args:
        iterator: Async iterator
        processor: Function to process each chunk
    """
    async for chunk in iterator:
        processor(chunk)


async def process_csv_stream(filepath: str, processor: Callable, skip_header: bool = True):
    """
    Process CSV file line by line.
    
    Args:
        filepath: Path to CSV file
        processor: Function to process each row
        skip_header: Skip first line if True
    """
    iterator = AsyncLineIterator(filepath)
    first_line = True
    
    async for line in iterator:
        if first_line and skip_header:
            first_line = False
            continue
        
        if line:
            values = line.split(',')
            processor(values)


async def process_json_stream(filepath: str, processor: Callable):
    """
    Process JSON Lines file (one JSON object per line).
    
    Args:
        filepath: Path to JSON Lines file
        processor: Function to process each JSON object
    """
    iterator = AsyncLineIterator(filepath)
    
    async for line in iterator:
        if line:
            try:
                obj = json.loads(line)
                processor(obj)
            except json.JSONDecodeError:
                pass