#Section 1
#3
class Person:
  def __init__(self, name, age, email ):
    self.name = name
    self.age = age
    self.email = email
  
  def __repr__(self):
    return f"Person(name = '{self.name}', age = {self.age}, email = '{self.email}')"
  
p = Person('Fortuna', 27, 'furtiadi@gmail.com')
print(p)