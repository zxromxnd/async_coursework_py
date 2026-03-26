from priority_queue import BiDirectionalPriorityQueue

print("Example 1: Basic usage.\n")

queue = BiDirectionalPriorityQueue()

queue.enqueue("Low priority task", priority=1)
queue.enqueue("Medium priority task", priority=5)
queue.enqueue("High priority task", priority=10)

print(f"Queue size: {queue.size()}")
print(f"Highest priority: {queue.peek(highest=True)}")
print(f"Lowest priority: {queue.peek(lowest=True)}")
print()

print("Example 2: Priority-based dequeue\n")

queue = BiDirectionalPriorityQueue()

queue.enqueue("Email", priority=3)
queue.enqueue("Call client", priority=9)
queue.enqueue("Meeting", priority=7)

print("Processing by priority:")
print(f"  {queue.dequeue(highest=True)}")
print(f"  {queue.dequeue(highest=True)}")
print(f"  {queue.dequeue(highest=True)}")
print()

print("Example 3: FIFO and LIFO\n")

queue = BiDirectionalPriorityQueue()

queue.enqueue("First", priority=5)
queue.enqueue("Second", priority=5)
queue.enqueue("Third", priority=5)

print(f"FIFO (oldest): {queue.dequeue(oldest=True)}")
print(f"LIFO (newest): {queue.dequeue(newest=True)}")
print(f"Remaining: {queue.dequeue(oldest=True)}")