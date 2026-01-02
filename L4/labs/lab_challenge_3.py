#Enroll class
class Enroll:
  def __init__(self, data:dict):
    self.__dict__ = data

  def getEnrolledStudent(self):
    return self.__dict__
  
  def addStudent(self, key, value):
    self.__dict__[key] = value

#Student class
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __repr__(self):
    return f'{{ name : {self.name} age: {self.age}}}'

student1 = Student('Fortuna', 27)
e = Enroll({})
e.addStudent('student1', student1)
print("Before changing attribute: ", e.getEnrolledStudent())

student1.name = 'Fortuna Eyob'
student1.age = 28
print("After changing attribute: ",e.getEnrolledStudent())