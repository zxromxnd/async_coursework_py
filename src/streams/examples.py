import asyncio
from stream_processor import (
    AsyncFileIterator,
    AsyncLineIterator,
    process_csv_stream,
    process_json_stream
)
import json


print("Example 1: Basic file streaming\n")


async def example1():
    with open('sample.txt', 'w') as f:
        for i in range(20):
            f.write(f"Line {i}: Some data here\n")

    def process_chunk(chunk):
        print(f"Processing chunk ({len(chunk)} chars): {chunk[:50]}...")
    
    iterator = AsyncFileIterator('sample.txt', chunk_size=100)
    
    async for chunk in iterator:
        process_chunk(chunk)


asyncio.run(example1())
print()


print("Example 2: CSV streaming\n")


async def example2():
    with open('sample.csv', 'w') as f:
        f.write('id,name,value\n')
        for i in range(10):
            f.write(f'{i},Item{i},{i*10}\n')

    total = 0
    
    def process_row(row):
        nonlocal total
        if len(row) >= 3:
            total += int(row[2])
            print(f"  {row[0]}: {row[1]} = {row[2]}")
    
    await process_csv_stream('sample.csv', process_row)
    print(f"\nTotal value: {total}")


asyncio.run(example2())
print()


print("Example 3: JSON Lines streaming\n")


async def example3():
    with open('sample.jsonl', 'w') as f:
        for i in range(10):
            obj = {'id': i, 'name': f'User{i}', 'active': i % 2 == 0}
            f.write(json.dumps(obj) + '\n')

    active_count = 0
    
    def process_object(obj):
        nonlocal active_count
        print(f"  {obj['id']}: {obj['name']} - {'Active' if obj['active'] else 'Inactive'}")
        if obj['active']:
            active_count += 1
    
    await process_json_stream('sample.jsonl', process_object)
    print(f"\nActive users: {active_count}")


asyncio.run(example3())
print()


print("Example 4: Line-by-line processing\n")


async def example4():
    with open('sample_lines.txt', 'w') as f:
        f.write("Python\n")
        f.write("JavaScript\n")
        f.write("Java\n")
        f.write("C++\n")
        f.write("Go\n")

    iterator = AsyncLineIterator('sample_lines.txt')
    
    async for line in iterator:
        print(f"  Language: {line}")


asyncio.run(example4())


import os
for file in ['sample.txt', 'sample.csv', 'sample.jsonl', 'sample_lines.txt']:
    if os.path.exists(file):
        os.remove(file)