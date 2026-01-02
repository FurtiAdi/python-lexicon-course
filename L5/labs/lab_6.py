# Section 2
# 6
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


s1 = Student('Fortuna', 27)
s2 = Student('Robel', 26)
s3 = Student('Robel', 26)

print(s1 == s2)
print(s3 == s2)
