#Section 1
#5
class Student:
  def __init__(self, **kwargs):
    self.__dict__ = kwargs
  
  def __str__(self):
    return ', '.join(f'{key} = {value}'for key, value in self.__dict__.items())
  

s1 = Student(name='Fortuna', age=27)
s2 = Student(name='Robel', age=26, email='robeleyob@email.com')

print(s1)
print(s2)