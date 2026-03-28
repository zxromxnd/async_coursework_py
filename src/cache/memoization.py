from collections import OrderedDict
import time


def memoize(func=None, max_size=None, strategy='lru', ttl=None):
    def decorator(f):
        cache = OrderedDict()
        frequency = {}
        timestamps = {}
        
        def wrapper(*args):
            current_time = time.time()
            
            if args in cache and strategy == 'time' and ttl:
                if current_time - timestamps[args] > ttl:
                    del cache[args]
                    del timestamps[args]
            
            if args in cache:
                if strategy == 'lru':
                    cache.move_to_end(args)
                elif strategy == 'lfu':
                    frequency[args] += 1
                return cache[args]
            
            result = f(*args)
            cache[args] = result
            
            if strategy == 'lfu':
                frequency[args] = 1
            
            if strategy == 'time':
                timestamps[args] = current_time
            
            if max_size and len(cache) > max_size:
                if strategy == 'lru':
                    cache.popitem(last=False)
                elif strategy == 'lfu':
                    lfu_key = min(frequency, key=frequency.get)
                    del cache[lfu_key]
                    del frequency[lfu_key]
            
            return result
        
        return wrapper
    
    if func is None:
        return decorator
    else:
        return decorator(func)