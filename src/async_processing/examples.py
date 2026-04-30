from async_map import async_map_callback, async_map_promise, async_map, AbortController
import asyncio

print("Example 1: Callback version\n")

def transform(x):
    return x * 2

def callback(error, result):
    if error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result}")

async_map_callback([1, 2, 3, 4, 5], transform, callback)
print()

print("Example 2: Promise version\n")

future = async_map_promise([1, 2, 3, 4, 5], transform)
print(f"Result: {future.result()}")
print()

print("Example 3: Async/await version\n")

async def async_transform(x):
    await asyncio.sleep(0.05)
    return x * 3

async def test_async():
    result = await async_map([1, 2, 3, 4, 5], async_transform)
    print(f"Result: {result}")

asyncio.run(test_async())
print()

print("Example 4: AbortController\n")

controller = AbortController()

def slow_transform(x):
    if x > 2:
        controller.abort()
    return x * 2

async_map_callback([1, 2, 3, 4, 5], slow_transform, callback, controller)