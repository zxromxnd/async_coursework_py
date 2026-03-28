from memoization import memoize
import time

print("Example 1: LRU strategy")
print("Cache size: 3\n")

call_count = 0

@memoize(max_size=3, strategy='lru')
def compute_lru(x):
    global call_count
    call_count += 1
    return x * 2

compute_lru(1)
compute_lru(2)
compute_lru(3)
compute_lru(1)
compute_lru(4)
compute_lru(2)

print(f"Function called {call_count} times")
print()

print("Example 2: LFU strategy")
print("Cache size: 3\n")

call_count = 0

@memoize(max_size=3, strategy='lfu')
def compute_lfu(x):
    global call_count
    call_count += 1
    return x * 3

compute_lfu(1)
compute_lfu(2)
compute_lfu(3)
compute_lfu(1)
compute_lfu(1)
compute_lfu(4)
compute_lfu(2)

print(f"Function called {call_count} times")
print()

print("Example 3: Time-based expiry")
print("TTL: 2 seconds\n")

call_count = 0

@memoize(strategy='time', ttl=2)
def compute_time(x):
    global call_count
    call_count += 1
    print(f"Computing {x}..")
    return x * 5

compute_time(10)
compute_time(10)
time.sleep(3)
compute_time(10)
print(f"\nFunction called {call_count} times")