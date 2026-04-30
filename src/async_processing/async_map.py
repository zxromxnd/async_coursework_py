import time
import asyncio
from typing import Callable, List, Any
from concurrent.futures import ThreadPoolExecutor


class AbortController:
    """Simple abort controller for cancellation."""
    def __init__(self):
        self.aborted = False
    
    def abort(self):
        self.aborted = True
    
    def is_aborted(self):
        return self.aborted


def async_map_callback(arr: List[Any], transform: Callable, callback: Callable, controller=None):
    """Callback-based async map with abort support."""
    results = []
    
    try:
        for item in arr:
            if controller and controller.is_aborted():
                callback(Exception("Aborted"), None)
                return
            
            result = transform(item)
            results.append(result)
        
        callback(None, results)
    except Exception as e:
        callback(e, None)


def async_map_promise(arr: List[Any], transform: Callable, controller=None):
    """Promise-based async map with abort support."""
    executor = ThreadPoolExecutor()
    
    def run():
        results = []
        for item in arr:
            if controller and controller.is_aborted():
                raise Exception("Aborted")
            results.append(transform(item))
        return results
    
    return executor.submit(run)


async def async_map(arr: List[Any], transform: Callable, controller=None):
    """Async/await version with abort support."""
    results = []
    
    for item in arr:
        if controller and controller.is_aborted():
            raise Exception("Aborted")
        
        if asyncio.iscoroutinefunction(transform):
            result = await transform(item)
        else:
            result = transform(item)
        results.append(result)
    
    return results