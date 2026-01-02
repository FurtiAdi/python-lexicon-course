#8
class Base:
  def __init__(self):
    self.__private_value = 3.14

class DerivedClass(Base):
  def __init__(self):
    super().__init__()

class NotDerivedClass():
  def __init__(self):
    pass

d = DerivedClass()
print(d._Base__private_value)
print(d.__private_value) #Demonstartes it can not be accessed


"""
When an attribute is defined with two underscores, Python makes it harder to
access by using a feature called name mangling. The attribute name is internally 
changed to for example _Base__private_value, where the class name is added as a 
prefix.
"""