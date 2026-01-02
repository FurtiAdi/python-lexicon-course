#1
class Animal:
  def __init__(self, name, age, weight):
    print("Animal Created \n")
    self.name = name
    self.age = age
    self.weight = weight

class Cat(Animal):
  def __init__(self, name, age, weight):
    print('Cat created!')
    super().__init__(name, age, weight)
  
class Kitten(Cat):
  def __init__(self, name, age, weight):
    print('Kitten created!')
    super().__init__(name, age, weight)


c1 = Cat('Cali', 3, 15)
k1 = Kitten('Smalan', 1, 5)