#5
#Version 1 — before redesign
def myFunc(obj):
  if  isinstance(obj, str):
    return len(obj) 
  elif isinstance(obj, list):
    return obj[0]
  elif isinstance(obj, MyClass): #modified after adding the class
    return len(obj.text)
  else:
    return f'{obj} is not an instance of str or list'

class MyClass:
  def __init__(self, text):
    self.text = text



## Version 2 – Redesign using polymorphism
# Adding this class, won't change existing functions 
class MyClass_Version2():
  def __init__(self, text):
    self.text = text
  def __len__(self): #created a method to make the class do its own job
    return len(self.text)
  
print(myFunc(MyClass('Fortuna')))
print(MyClass_Version2('Fortuna').__len__())