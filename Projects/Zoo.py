# ---------------------------------------------------------------------
# Base class - Animal
# ---------------------------------------------------------------------
class Animal:
    def __init__(self, name, age, energy_level):
        self.name = name
        self.age = age
        self.energy_level = energy_level
        self.sleep_state = False

    @property
    def energy_level_value(self):
        return self.energy_level

    @energy_level_value.setter
    def energy_level_value(self, new_energy_level):
        if new_energy_level < 0:
            self.energy_level = 0
        elif new_energy_level > 100:
            self.energy_level = 100
        else:
            self.energy_level = new_energy_level

# -----------------------------------------------------------------

    def eat(self, food_type, allowed_food, tired_limit, full_limit, increase_factor):
        # Too tired to eat
        if self.energy_level <= tired_limit:
            print(f"{self.name} is too tired to eat and needs sleep.")
            return
        # Cannot eat while sleeping
        if self.sleep_state:
            print(f"{self.name} is sleeping and cannot eat.")
            return
        # Wrong food
        if food_type not in allowed_food:
            print(f"{self.name} can only eat {allowed_food}.")
            return
        # Too full
        if self.energy_level > full_limit:
            print(f"{self.name} is full and cannot eat.")
            return
        # Eating is allowed
        print(f"{self.name} is eating {food_type}!")
        self.energy_level_value = self.energy_level_value * increase_factor

# -----------------------------------------------------------------

    def sleep(self, tired_limit, wake_limit, increase_factor):
        # Enter sleep if too tired
        if self.energy_level <= tired_limit:
            print(f"{self.name} is tired and sleeping!")
            self.sleep_state = True
        # Recover energy while sleeping
        if self.sleep_state:
            self.energy_level_value = self.energy_level_value * increase_factor
        # Wake up if enough energy
        if self.energy_level >= wake_limit:
            print(f"{self.name} is awake now!")
            self.sleep_state = False
# -----------------------------------------------------------------

    def interact_base(self, min_energy, energy_loss_factor):
        if self.energy_level > min_energy and not self.sleep_state:
            print(f"{self.name} is interacting!")
            self.energy_level_value = self.energy_level_value * energy_loss_factor
        else:
            print(f"{self.name} cannot interact right now!")

# ----------------------------------------------------------------------
# Subclasses
# ----------------------------------------------------------------------
# Herbivore class
# ----------------------------------------------------------------------


class Herbivore(Animal):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def eats(self, food_type):
        self.eat(
            food_type=food_type,
            allowed_food=['plant'],
            tired_limit=40,
            full_limit=75,
            increase_factor=1.15
        )

    def sleeps(self):
        self.sleep(
            tired_limit=40,
            wake_limit=50,
            increase_factor=1.1
        )

    def interact(self):
        self.interact_base(
            min_energy=40,
            energy_loss_factor=0.95
        )
# ---------------------------------------------------------------------
# Carnivore class
# ---------------------------------------------------------------------


class Carnivore(Animal):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def eats(self, food_type):
        self.eat(
            food_type=food_type,
            allowed_food=['meat'],
            tired_limit=45,
            full_limit=50,
            increase_factor=1.3
        )

    def sleeps(self):
        self.sleep(
            tired_limit=45,
            wake_limit=65,
            increase_factor=1.25
        )

    def interact(self):
        self.interact_base(
            min_energy=45,
            energy_loss_factor=0.90
        )

    def hunt(self, animal: Animal):
        if isinstance(animal, Herbivore):
            if self.energy_level >= 50 and not self.sleep_state:
                print(f"{self.name} tries to hunt {animal.name_value}.")
                self.energy_level *= 0.85  # loses 15% during hunting
                animal.energy_level_value = animal.energy_level_value * 0.90  # lose 10%
                if (self.energy_level > animal.energy_level_value):
                    print("Hunting was succesfull!")
                    animal.energy_level_value *= 0.75  # loses again 25%
                    self.eats('meat')
                else:
                    print(
                        f"Hunting was not succesfull! {animal.name_value} escaped.")
            else:
                print(f"{self.name} is too tired to hunt.")
        else:
            print(f"{self.name} can not hunt {animal.name_value}")
# ---------------------------------------------------------------------
# Omnivore class
# ---------------------------------------------------------------------


class Omnivore(Animal):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level)

    def eats(self, food_type):
        self.eat(
            food_type=food_type,
            allowed_food=['plant', 'meat'],
            tired_limit=35,
            full_limit=65,
            increase_factor=1.2
        )

    def sleeps(self):
        self.sleep(
            tired_limit=35,
            wake_limit=55,
            increase_factor=1.15
        )

    def interact(self):
        self.interact_base(
            min_energy=35,
            energy_loss_factor=0.85
        )
# ---------------------------------------------------------------------
# Visitor class
# ---------------------------------------------------------------------


class Visitor:
    def __init__(self, name):
        self.name = name

    def feed(self, animal: Animal, food_type):
        print(f"{self.name} is trying to feed {animal.name_value} {food_type}")
        animal.eats(food_type)

    def interact(self, animal: Animal):
        print(f"{self.name} is trying to interact with {animal.name}.")
        animal.interact()
# ---------------------------------------------------------------------
# Simulation function for testing
# ---------------------------------------------------------------------


def simulate(days, animal: Animal, visitor: Visitor, food_type):
    for n in range(days):
        print(f'\nDay {n+1}')

        print(f'.....Morning Time....')
        animal.eats(food_type)
        print('Energy after eating:', animal.energy_level_value)

        print(f'\n.....Daytime interaction....')
        visitor.interact(animal)
        print('Energy after interacting:', animal.energy_level_value)

        print(f'\n.....Feeding time.....')
        visitor.feed(animal, food_type)
        print(f'Energy after eating {food_type}: {animal.energy_level_value}')

        visitor.interact(animal)
        visitor.interact(animal)
        visitor.interact(animal)
        visitor.interact(animal)
        visitor.interact(animal)
        print('Energy after interacting:', animal.energy_level_value)

        print(f'\n......Night Time.....')
        animal.sleeps()
        animal.sleeps()
        print(f'Energy after sleeping: {animal.energy_level_value} \n')


# ---------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------
visitor = Visitor('Fortuna')
# ---------------------------------------------------------------------
# Test1- Carnivore
# ---------------------------------------------------------------------

"""
Carnivore
Eats when energy is 45-50%
interacts when > 45%
sleeps when ≤ 45%
wakes up at ≥ 65%
# """
lion = Carnivore('Simba', 5, 49)
simulate(1, lion, visitor, 'meat')

# ---------------------------------------------------------------------
# Test2 – Herbivore
# ---------------------------------------------------------------------
"""
Herbivore
Eats when energy is 41–75%
interacts when > 40%
sleeps when ≤ 40%
wakes up at ≥ 50%
"""
sheep = Herbivore('Begiey', 3, 41)
simulate(1, sheep, visitor, 'plant')

# ---------------------------------------------------------------------
# Test3 – Omnivore
# ---------------------------------------------------------------------
"""
Omnivore
Eats when energy is 36–65%
interacts when > 35%
sleeps when ≤ 35%
wakes up at ≥ 55%
"""
bear = Omnivore('TeddyBear', 7, 60)
simulate(1, bear, visitor, 'plant')

# ---------------------------------------------------------------------
# Test4 – Carnivore hunts Hernivore
# ---------------------------------------------------------------------

lion = Carnivore('Simba', 5, 55)
sheep = Herbivore('Begiey', 3, 50)
print(f'{lion.name_value} energy level before hunting is: ',
      lion.energy_level_value)
print(f'{sheep.name_value} energy level before hunting is: ',
      sheep.energy_level_value)
lion.hunt(sheep)
print(f'{lion.name_value} energy level after hunting is: ',
      lion.energy_level_value)
print(f'{sheep.name_value} energy level after hunting is: ',
      sheep.energy_level_value)

# ---------------------------------------------------------------------

