# Task 1: Execution-time decorator
import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Time starts!')
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'The result is: {result}')
        stop_time = time.time()
        print('Time stops!')
        print(f'Execution time is: {stop_time - start_time}')
    return wrapper


@my_decorator
def my_lists(nums):
    total = 0
    for n in nums:
        total += n
    return total


my_lists([1, 2, 3, 4, 5, 6])
