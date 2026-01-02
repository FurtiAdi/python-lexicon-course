#2
class Base:
  def __init__(self, value):
    print('Base value is: ', value)
    self.value = value

class FirstSubClass(Base):
  def __init__(self, value):
    print('FirstSubClass value is: ', value)
    super().__init__(value)
    self.value /= 2

class SecondSubClass(FirstSubClass):
  def __init__(self, value):
    print('SecondSubClass value is: ', value)
    super().__init__(value)
    self.value += 10

s = SecondSubClass(50)
print('Final value is: ', s.value)

