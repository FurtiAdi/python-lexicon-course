#inheritance
class A:
  def __init__(self, value):
    print(f'In A value = {value}')
    self.value = value

class B(A):
  def __init__(self, value):
    print(f'In B value  = {value}')
    super().__init__(value)
    self.value += 10    

class C(A):
  def __init__(self, value):
    print(f'In C value  = {value}')
    super().__init__(value)
    self.value *= 4  

class D(C, B):
  def __init__(self, value):
    print(f'In D value  = {value}')
    super().__init__(value) 

# b = B(10)
# print(b.value)

d = D(10)
print(d.value)
print(D.mro())

# Base class
class Animal:
  def __init__(self):
    print('Animal Created!')
  def whoAmI(self):
    print('Animal')
  def eat(self):
    print('Eating.. nom nom ..')

# Derived class
class Dog(Animal):
  def __init__(self):
    super().__init__()
    print('DOg created!')
  def whoAmI(self):
    print('Dog')
  def bark(self):
    print('Woof!')

d = Dog()
d.whoAmI()
d.eat()

class Employee:
    increase = 1.04
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def increaseSalary(self):
        self.salary *= self.increase
    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'

class Developer(Employee):
    increase = 1.10
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang
    def __str__(self):
        return f'{super().__str__()} and fav prog lang is {self.prog_lang}'


emp1 = Employee('Alice', 'Ason', 45000)
emp2 = Employee('Bob', 'Bson', 42000)
dev1 = Developer('Carl', 'Cson', 50000, 'Pyhton')

print('Before increase: ')
print(emp1)
print(emp2)
print(dev1)

print('After the increase ')
emp1.increaseSalary()
emp2.increaseSalary()
dev1.increaseSalary()

print(emp1)
print(emp2)
print(dev1)


# Private classes in Python
#  private value with two __ cannot be accessed but with 1 _ can be accessed but not changed
class MyClass:
  def __init__(self):
    self.__private_value = 42

obj = MyClass()
print(obj.__private_value)
print(obj._MyClass__private_value)