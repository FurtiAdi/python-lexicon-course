# from math import sqrt
import math

def sqrt(x):
    return 'hello'

print(sqrt(25)) #w ill be overrided
print(math.sqrt(25)) # better to use this

from math import sqrt as sq
print(sq(25))

from my_funcs import adder
print(adder(2,3))

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper


@my_decorator #= my_decorator(say_hello)
def say_hello():
    print('Hello!!')


# Call a decorated function
say_hello()

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed to the functio:n: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f'Function returned: {result}')
    return wrapper


@my_decorator
def add(a, b):
    return a + b


add(5, 10)

#Static Methods
class MathHelper:
  @staticmethod
  def add_numbers(x,y):
    return x + y

print(MathHelper.add_numbers(5,7))

#@staticmethod, @classmethod, @property
#@functools.wraps

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      print(f'Calling {func.__name__}')
      return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
   print(f'Hello, {name}')
      
greet('Fortuna')

#Higher order function

def apply_function(func, value):
   return func(value)

def square(c):
   return c*c
def cube(x):
  return x*x*x

print(apply_function(square, 3))
print(apply_function(cube, 3))

#lambda
def square(x):
    return x * x

def square_lamda(x): 
   return x * x

print(square(5))
print(square_lamda(5))


print(apply_function(lambda x:x+10, 5))

#Recursion and memoization

def factorial(n):
  if n==0:
    return 1
  return n * factorial(n-1)

print(factorial(5))



from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5)) #output 55
print(fibonacci.cache_info())