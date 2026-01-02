# Section 2
# 9
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name = {self.name}, age = {self.age}'

    def __len__(self):
        return len(self.name)

s1 = Student('Fortuna', 27)

print(len(s1))
