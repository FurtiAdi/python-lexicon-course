# SECTION 4 — Combined OOP + Scope + Pythonic Techniques
# 20
class Product:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs
    @property
    def item_price(self):
        return self.__dict__.get('price')
    @item_price.setter
    def item_price(self, newPrice):
        self.__dict__['price'] = newPrice
    @property
    def calculateNewPrice(self):
        if(self.__dict__.__contains__('dicount')):
          return self.__dict__.get('price') * self.__dict__.get('dicount')
        else:
            return self.item_price
    def __str__(self):
        return ', '.join(f'{key} = {value}' for key, value in self.__dict__.items())

p1 = Product(name='onion', price=50, quantity=10, dicount=0.8)
print(p1)
print("Orginal Price : ", p1.item_price)
p1.item_price = 60
print("Price changed to: ", p1.item_price)
print("Price after dicount is: ", p1.calculateNewPrice)

p2 = Product(name='tomato', price=10, quantity=10)
print(p2)
print("Orginal Price : ", p2.item_price)
p2.item_price = 12
print("Price changed to: ", p2.item_price)
print("Price is still the same: ", p2.calculateNewPrice)
