# Variable Scope
x = 15

def printer():
  x = 30
  return x

print(x)
print(printer())
print (x)

#1. Name assignment will create or change local names vy default
#2. Nmae references search (at most) four scopes, these are: (LEGB rule)
  #L : Local - Name assigned in anyway within a function and not declared global in that function
  #E : Enclosing functions - Name in the local scope of any and all enclosing func, inner or outer
  #G: Global - Name assigned at the top level of a  module file or declared globally in a def within a file
  #B: Build-in - Built-in names, range....(all that is built in)
#3. Names declared in global and nonlocal statement map assigned names to enclosing module and function scopes

#1 (Local) x is local : 
f = lambda x: x**2

name = 'This is some global name'

#Enclosing Function
def greet():
  name = 'Erik'

  def hello():
    name = 'Fortuna'
    print('Hello ' + name)
  
  hello()

greet()

#Global Scope
print(name)

# Built in
len(name)

#Example
x = 50
def func(x):
  print('x is ', x)
  x = 2
  print('Change local x to ', x)

func(x)
print('x is still ', x)

x = 50

def func():
  global x # not recommended
  print('This function is now using global x')
  print('Because of global x is: ', x)
  x=2
  print('Run func(), changed global x to ', x )

print('Before calling func() x is: ', x)
func()
print('After calling func() x is: ', x)

# OOP
# Class : a template for object instances
# Method : creates inside a class
class Sample():
  pass

x = Sample()

print(type(x))

class Dog():
  species = 'mammal'
  def __init__(self, breed, name): #used to initialize the attribute
    self.breed = breed
    self.name = name

milo = Dog('Larbrador','Milo')
frank = Dog(breed='Husikie', name = 'Frank')

print(milo.breed) 
print(milo.name) 
print(frank.breed)
print(milo.species)


class Circle:
  pi = 3.14

  #Circle get instaniated with a radius
  def __init__(self, radius = 1):
    self.radius = radius
  
  #Area method calculates the area. Note use of self!!
  def area(self):
    return self.radius * self.radius * Circle.pi
  
  #Method for resetting Radius
  def setRadius(self, radius):
    self.radius = radius
  
  #Method for getting Radius
  def getRadius(self):
    return self.radius

c = Circle()
print(c.getRadius())
c.setRadius(2)
print('Radius is: ', c.getRadius())
print('Area is: ', c.area())

  