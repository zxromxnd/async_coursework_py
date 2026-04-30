from async_map import async_map, AbortController
import asyncio

async def test_abort():
    controller = AbortController()
    
    async def transform(x):
        if x > 3:
            controller.abort()
        await asyncio.sleep(0.1)
        return x * 2
    
    try:
        result = await async_map([1, 2, 3, 4, 5], transform, controller)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Aborted: {e}")

asyncio.run(test_abort())