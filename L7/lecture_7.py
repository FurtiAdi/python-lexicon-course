#Poly = many
#morph = form
#in programming it means writing a code once and it can 
# behave differently based on the object
#with out polymorphism our code would be full of if, elif, isInstance
#with polymorphism code will be shorter, easier to extend, breaks less when we add new features
# Duck typing : means if it looks like a duck we treat it like a duck, the same python doesnt care about an object, it if looks like a string 
#it will be treated like a string
#polymophism will let you run the code with showing error  

def make_it_upper(s):
  return s.upper() #here we doesnt care about s but we assume that it has upper method

#Here the class is not String class but acts like it
class Shouty:
  def __init__(self, text):
    self.text = text

  def upper(self):
    return self.text.upper() + '!!!'

print(make_it_upper('hello'))
print(make_it_upper(Shouty('hello')))

# if isinstance(x, str):
#   print(x.upper())

def safe_upper(x):
  try:
    return x.upper() #save way to do incase int sends
  except AttributeError:
    return str(x).upper()

print(safe_upper('hi'))
print(safe_upper(123))
print(safe_upper(Shouty('hi')))

#we define a base class
#we define subclass
#subclass override methods

class Animal:
  def speak(self):
    raise NotImplementedError

class Dog(Animal):
  def speak(self):
    return 'Woof!'
  
class Cat(Animal):
  def speak(self):
    return 'Meow!'
class Dog(Animal):
  def speak(self):
    return 'Woof!'

print(Dog().speak())
print(Cat().speak())

from abc import ABC, abstractmethod
import json


class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass


# class BadSerilizer(Serializer):
#     pass


# b = BadSerilizer()

# raises error because it doesnt implement the method serilize.
# the good thing about abstract it raise error immidiately
# unlike pholy which lets u run the code


class JsonSerializer(Serializer):
    def serialize(self, obj):
        return json.dumps(obj)
js = JsonSerializer()
print(js.serialize({"name": "Haithem"}))


class SimpleSerializer(Serializer):
  def serialize(self, obj):
    keys = obj[0].keys()
    lines = [", ".join(keys)]
    for row in obj:
       lines.append(",".join(str(row[k]) for k in keys ))
    return "\n".join(lines)

csv = SimpleSerializer()
print(csv.serialize([
   {"name":"Alice", "age":30},
   {"name":"Ema", "age":28}
]))

