#5
class Person:
  def __init__(self, name, age):
    self.name  = name
    self. age = age
  
  def getInfo(self):
    return f'Person name is {self.name} and age is {self.age}'
  
class Student(Person):
  def __init__(self, name, age, stage):
    super().__init__(name, age)
    self.stage = stage
  
  def getInfo(self):
    return f'{super().getInfo()} and stage is {self.stage}'

p = Person('Fortuna', 27)
print(p.getInfo())

s = Student('Fortuna', 27, 'Junior')
print(s.getInfo())