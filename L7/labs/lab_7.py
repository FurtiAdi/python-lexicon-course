# 7 Duck typing
from abc import ABC, abstractmethod
def call_contains(obj):
    return obj.__contains__('o')
class DuckClass:
    def __init__(self, text):
        self.text = text
    def __contains__(self, char):
        return char in self.text

class NotDuckClass():
    def __init__(self, text):
        self.text = text
print(call_contains("hello"))          # Works
print(call_contains(DuckClass("hello")))  # Works
# print(call_contains(NotDuckClass('Hi'))) #Error
"""
Error Timing -> runtime error
Error Message
- AttributeError: 'NotDuckClass' object has no attribute '__contains__'"
"""
# Abstract
class AbsClass(ABC):
    @abstractmethod
    def __contains__(self, char):
        pass
class DerivedClass(AbsClass):
    def __init__(self, text):
        self.text = text
    def __contains__(self, char):
        return char in self.text
class BrokenAbsClass(AbsClass):
    def __init__(self, text):
        self.text = text
def my_func(abs: AbsClass):
    return abs.__contains__('o')
print(my_func(DerivedClass('hello')))  # Works
#print(my_func(BrokenAbsClass('hello')))  # Error
"""
Error Timing -> instantiation error
Error Message
- TypeError: Can't instantiate abstract class BrokenAbsClass 
without an implementation for abstract method '__contains__'
Developer exprience:
- Duck class is easy to write and flexible
- Abs class is not fast to write but safer
"""
