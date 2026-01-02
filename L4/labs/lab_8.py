class Vehicle:
    antalVehicle = 0

    def __init__(self, name, model):
        self.name = name
        self.model = model
        Vehicle.antalVehicle += 1

    def show_count(self):
        print(f"{self.name} sees antalVehicle = {self.antalVehicle}")


car1 = Vehicle('Volvo', 2020)
car2 = Vehicle('Toyota', 2023)
car3 = Vehicle('Kia', 2023)

car1.show_count()
car2.show_count()
car3.show_count()

car1.antalVehicle = 10
car1.show_count()
car2.show_count()
car3.show_count()