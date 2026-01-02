class Circle:
  pi = 3.14

  def _init_(self, radius = 1):
    self.radius = radius

  @property
  def area(self): 
    return self.radius * self.radius * Circle.pi
  
  @property
  def radius_value(self):
    return self.radius

  @radius_value.setter
  def radius_value(self, value):
    self.radius = value
  
c = Circle()
c.radius_value = 2

print("Radius is: ", c.radius_value)
print("Area is: ", c.area) #area looks like a variable, but behave like a method.

class Person:

  def __init__ (self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    
  def __str__(self):
    return f'{self.name} is {self.age} years old and has email {self.email}'
  

p1 = Person('Fortuna', 'fortuna@email.com', 27)
p2 = Person('Robel', 'robel@email.com', 26)

print(p1)
print(p2)

p1.phone = '0728737064'
print(p1.phone) #objects stores in dictionary but attributes in array??
#print(p2.phone) #error: object has no attribute 'phone

class Person:
  def __init__(self, **kwargs):
    self.__dict__ = kwargs

  def __str__(self):
    return f'{self.name} is {self.age} years old'
  
p1 = Person(name='Alice', age = 23)
p2 = Person(name = 'Bob', age = 45)

print(p1)
print(p2)

#Tomake it flexible by not setting some attribute
class Something:
  def __init__(self, data:dict):
    self.__dict__ = data
  
  def __str__(self):
    #str_rep = ''
    # for key, value in self.__dict__.items():
    #   str_rep += f'{key} = {value}, '
    # return str_rep
    return ', '.join([f'{key} = {value}' for key , value in self.__dict__.items()])
   
data_dict1 = {
  'a' : 10,
  'b' : 20,
  'name' : 'One'
}

data_dict2 = {
  'a' : 15,
  'b' : 25,
  'name' : 'Two'
}
  
s1 = Something(data_dict1)
s2 = Something(data_dict2)


print(s1)
print(s2)

## Class Point
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  #String representation of the Object
  def __repr__(self): #usually used to create error methods 
    return f'Point(x= {self.x}, y={self.y})'
  
  def __str__(self): #it will override the __rep__
    return f'Point object with (x= {self.x}, y={self.y})'
  
point1 = Point(1,2)
point2 = Point(10,20)

print(point1)
print(repr(point2))

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

p1 = Point(10,20)
p2 = Point(10,20)

print (p1 == p2) #comparing the adress in memory without __eq__ and gives False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap_xy(self):
        self.x, self.y = self.y, self.x

p1 = Point(10, 20)
p1.swap_xy()
print(p1.x, p1.y)

