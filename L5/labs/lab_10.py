# Section 2
# 10
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name = {self.name}, age = {self.age}'

    def __contains__(self, value):
        return value in self.name

s1 = Student('Fortuna', 27)

print('o' in s1)