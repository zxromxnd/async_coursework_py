from priority_queue import BiDirectionalPriorityQueue

def test_enqueue_and_size():
    queue = BiDirectionalPriorityQueue()

    assert queue.is_empty() == True
    assert queue.size() == 0

    queue.enqueue("task1", 5)
    queue.enqueue("task2", 3)
    queue.enqueue("task2", 8)

    assert queue.size() == 3
    assert queue.is_empty() == False

    print("Enqueue and size tests passed.")

def test_peek_operations():
    queue = BiDirectionalPriorityQueue()

    queue.enqueue("task1", 5)
    queue.enqueue("task2", 3)
    queue.enqueue("task3", 8)

    assert queue.peek(highest=True) == "task3"
    assert queue.peek(lowest=True) == "task2"
    assert queue.peek(oldest=True) == "task1"
    assert queue.peek(newest=True) == "task3"

    assert queue.size() == 3

    print("Peek operations tests passed.")

def test_dequeue_operations():
    queue = BiDirectionalPriorityQueue()

    queue.enqueue("task1", 5)
    queue.enqueue("task2", 3)
    queue.enqueue("task3", 8)

    item = queue.dequeue(highest=True)
    assert item == "task3"
    assert queue.size() == 2

    item = queue.dequeue(lowest=True)
    assert item == "task2"
    assert queue.size() == 1

    item = queue.dequeue(oldest=True)
    assert item == "task1"
    assert queue.size() == 0

    print("Dequeue operations tests passed.")

def test_empty_queue():
    queue = BiDirectionalPriorityQueue()

    assert queue.peek(highest=True) == None
    assert queue.dequeue(lowest=True) == None

    print("Empty queue tests passed.")

if __name__ == "__main__":
    test_enqueue_and_size()
    test_peek_operations()
    test_dequeue_operations()
    test_empty_queue()

    print("All tests passed.")