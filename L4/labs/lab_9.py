class Calculator:
  def __init__(self, value):
    self.value = value
  
  def calculateArea(self):
      area = self.value * self.value
      return area

c1 = Calculator(10)
print("Area before changing attribute is: ", c1.calculateArea())
c1.value = 20
print("Area aftetr changing attribute is: ", c1.calculateArea())

