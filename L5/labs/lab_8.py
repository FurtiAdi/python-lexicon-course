# Section 2
# 8
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name = {self.name}, age = {self.age}'

    def __add__(self, other):
        return Student(self.name + other.name, self.age + other.age)


s1 = Student('Fortuna', 27)
s2 = Student('Eyob', 0)

print(s1 + s2)
