#4
class Employee:
  def __init__(self, name):
    self.name = name
  def getName(self):
    NotImplementedError

class Developer(Employee):
  def __init__(self, name):
    super().__init__(name)
  def getName(self):
    return self.name

class Manager(Employee):
  def __init__(self, name, antalTeam):
    super().__init__(name)
    self.anatalTeam = antalTeam
  def getName(self):
    return self.name
  
class Intern(Employee):
  def __init__(self, name, duration):
    super().__init__(name)
    self.duration = duration
  def getName(self):
    return self.name

def emp(e):
  return e.getName()
print(emp(Developer('Fortuna')))
print(emp(Manager('Robel', 10)))
print(emp(Intern('Maku', 6)))