from memoization import memoize

def test_lfu_basic():
    call_count = 0

    @memoize(max_size=3, strategy='lfu')
    def expensive_func(x):
        nonlocal call_count
        call_count += 1
        return x * 2
    
    expensive_func(1)
    expensive_func(2)
    expensive_func(3)
    assert call_count == 3

    expensive_func(1)
    expensive_func(1)
    expensive_func(3)
    assert call_count == 3

    expensive_func(4)
    assert call_count == 4

    expensive_func(2)
    assert call_count == 5

    print("LFU test passed.")

if __name__ == "__main__":
    test_lfu_basic()