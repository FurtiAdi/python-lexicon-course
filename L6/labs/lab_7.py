#7
class Base:
  def __init__(self):
    self._protected_value = 3.14

class DerivedClass(Base):
  def __init__(self):
    super().__init__()
    self._protected_value = 4.14

class NotDerivedClass():
  def __init__(self):
    pass

d = DerivedClass()
print("Modified value: ", d._protected_value) #Demonstartes it can be accessed and modified

"""
protected attribute can be accessed in subclass because Pyhton doesn't
force any restriction. However, it is dicouraged to access it outside the 
class to prevent misuse. As adult, Pyhton expects us to understand the single 
underscore indicates that the attribute is intended for internal use only.
"""