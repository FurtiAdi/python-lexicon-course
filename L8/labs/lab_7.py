#Task 7: Preserving function metadata 

import functools
def my_decorator(func):
  @functools.wraps(func)
  def wrapper(*args):
    print(f'Meta data before calling func: {func.__name__} and {func.__doc__}')
    result = func(*args)
    print(f'Meta data After calling func:  {func.__name__} and {func.__doc__}')
    print(f'The sum of two numbers is: {result}')
  return wrapper

@my_decorator
def sum(a, b):
  """Return the sum of two numbers"""
  return a + b

sum(1,2)