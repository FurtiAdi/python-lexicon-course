#Challenge Task 10: Decorators + recursion interaction 

def my_decorator(func):
    def wrapper(*args):
        print(f'Decorator Calling {func.__name__}')
        return func(*args)
    return wrapper

@my_decorator
def power(base, exponent):
    print('Orginal Called')
    if exponent == 0:  # Base case
        return 1
    else:
        return base * power(base, exponent - 1)


print("Result: ", power(2,3))

"""
The output shows that the decorator message prints everytime and 
the orginal function body also runs per recursive call.

This happens because the function name is replaced by the wrapper and
every call to the function goes through the decorator first. 
That means that the decorator runs first and then the orginal function body.
"""