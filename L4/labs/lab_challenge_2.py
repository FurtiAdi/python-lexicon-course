class Enroll:
  antalStudent = 0
  def __init__(self, name):
    self.name = name
    Enroll.antalStudent += 1

  def getName(self):
    return self.name
  
  def getAntalStudent(self):
    return Enroll.antalStudent

  def resetAntalStudent(self):
    Enroll.antalStudent = 0

student1 = Enroll('Fortuna')
student2 = Enroll('Robel')
print("Before changing an instance attribute: ", student1.getName())
print("Before changing an instance attribute: ", student2.getName())

student1.name = 'Fortuna Eyob'
print("After changing student1 instance attribute: ", student1.getName())
print("After changing student1 instance attribute: ", student2.getName())

print("Before changing a class attribute: ", student1.getAntalStudent())
print("Before changing a class attribute: ",student2.getAntalStudent())

student1.resetAntalStudent()
print("After changing a class attribute: ",student1.getAntalStudent())
print("After changing a class attribute: ",student2.getAntalStudent())
  
