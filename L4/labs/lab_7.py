class Vehicle:
  def __init__(self, name, model):
    self.name = name
    self.model = model
  
  def getVehicleInfo(self):
    print (f"The Vehicle name is {self.name} and is model {self.model}")


car1 = Vehicle('Volvo', 2020)
car2 = Vehicle('Toyota', 2023)

car1.getVehicleInfo()
car2.getVehicleInfo()