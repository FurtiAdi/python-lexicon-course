#3
class Base:
    def __init__(self, antalAnimal):
        self.antalAnimal = antalAnimal


class Cat(Base):
    def __init__(self, antalAnimal):
        super().__init__(antalAnimal)
        self.antalAnimal += 1


class Dog(Base):
    def __init__(self, antalAnimal):
        super().__init__(antalAnimal)
        self.antalAnimal *= 2


class House(Cat, Dog):
    def __init__(self, antalAnimal):
        super().__init__(antalAnimal)

h = House(5)
print('Final value: ', h.antalAnimal)
print(House.mro())

"""
The final value 11 is produced because constructors are executed 
accroding to MRO (House->Cat->Dog->Base). The Base constructor will 
initialize the value to 5, then Dog doubles it to 10 and finally 
Cat will increment it by 1. 
"""