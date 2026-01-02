# 9
class Shapes:
    def __init__(self, base, height):
      print('\nShape created!')
      self.base = base
      self.height = height
    def __str__(self):
       return f'The base is {self.base} \nthe height is {self.height}'


class Triangle(Shapes):
  def __init__(self, base, height):
    super().__init__(base, height)
    print("The Shape is Triangle!")
  def area(self):
    return (self.base * self.height) / 2
  def __str__(self):
    return f'{super().__str__()} \nthe area is {self.area()}'
    
s = Shapes(5, 10)
print(s)
t = Triangle(5, 10)
print(t)

