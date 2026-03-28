import time

def incremental_counter(start=1):
    current = start
    while True:
        yield current
        current += 1

def timeout_iterator(iterator, timeout):
    start_time = time.time()
    total_sum = 0
    count = 0

    while time.time() - start_time < timeout:
        value = next(iterator)
        total_sum += value
        count += 1
        average = total_sum / count
        print(f"Value: {value}, Sum: {total_sum}, Average: {average}")