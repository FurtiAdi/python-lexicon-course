class Grocery:
  def __init__(self, item):
    self.item = item
  
  def setItem(self, newItem):
    self.item = newItem
  
  def getPrice(self):
    if self.item.lower() == 'onion':
      print("Onion price is: ", 20)
    elif self.item.lower()  == 'tomato':
      print("Tomato price is: ", 50)
    elif self.item.lower()  == 'potato':
      print("Potato price is: ", 10)
    else:
      print("Enjoy your free grocery!")

g1 = Grocery('onion')
g1.getPrice()
g1.setItem('Potato')
g1.getPrice()