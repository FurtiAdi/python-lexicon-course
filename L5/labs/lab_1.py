#Section 1
#1
class Square:
  def __init__(self, side):
    self.side = side
  
  @property
  def area(self):
    return self.side ** 2
  
  @property
  def side_value(self):
    return self.side
  
  @side_value.setter
  def side_value(self, newValue):
    self.side = newValue

s1 = Square(5)
print("Side value is: ", s1.side_value)
print("Area before changing the side is: ", s1.area)

s1.side_value = 10
print("New side value is: ", s1.side_value)
print("Area After changing the side is: ", s1.area)
