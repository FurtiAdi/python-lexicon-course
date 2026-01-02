from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
# Attempt to create a subclass that does not implement the method
class Cat(Animal):
    def __init__(self):
        pass
#c = Cat('Cali')
#print(c.name)
"""
I got an error saying: Can't instantiate abstract class Cat 
without an implementation for abstract method 'speak'
"""
# Valid subclasses
class Dog(Animal):
    def __init__(self):
        pass
    def speak(self):
        print('Woof!!')
class Duck(Animal):
    def __init__(self):
        pass
    def speak(self):
        print('Quack!!')
d = Dog()
d.speak()
k = Duck()
k.speak()

# function
def my_func(Animal):
    Animal.speak()
my_func(Dog())
my_func(Duck())
