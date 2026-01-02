# SECTION 4 — Combined OOP + Scope + Pythonic Techniques
# 19

class Students:
  def __init__(self, **kwargs):
    self.__dict__ = kwargs
  
  def __str__(self):
    return ", ".join(f'{key} = {value}' for key, value in self.__dict__.items())
  
s1 = Students(firstname='Fortuna', lastname='Fessehaye', age=27, email='furti@gmail.com')
print(s1)
print(s1.firstname)
print(s1.lastname)
print(s1.age)
print(s1.email)