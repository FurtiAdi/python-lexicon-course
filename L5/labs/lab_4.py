#Section 1
#4
class Student:
  def __init__(self, **kwargs):
    self.__dict__ = kwargs

  def __str__(self):
    s = ''
    for key, value in self.__dict__.items():
      s += f'{key} = {value}, '
    return s

s1 = Student(name='Fortuna', age=27)
s2 = Student(name='Robel', age=26, email='robeleyob@email.com')

print(s1)
print(s2)