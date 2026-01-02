# Section 2
# 7
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return  self.age < other.age


s1 = Student('Fortuna', 27)
s2 = Student('Robel', 26)
s3 = Student('Robel', 26)

print(s1 < s2)
print(s3 < s2)
