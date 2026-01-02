#Section 1
#2
class Person:
  def __init__(self, name, age, email ):
    self.name = name
    self.age = age
    self.email = email
  
  def __str__(self):
    return (
        f"My name is {self.name}, and I am {self.age} years old.\n"
        f"You can contact me via email at {self.email}."
    )

p = Person('Fortuna', 27, 'furtiadi@gmail.com')
print(p)