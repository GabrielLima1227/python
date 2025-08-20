# Inheritance
# Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that involves creating new classes (subclasses or derived classes) based on existing classes (superclasses or base classes).

class Vehicle:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def start(self) -> None:
        print("Vehicle is starting.")

    def stop(self) -> None:
        print("Vehicle is stoping.")

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doord, number_of_wheels) -> None:
        super().__init__(brand, model, year)
        self.number_of_doord = number_of_doord
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

car01 = Car("Foed", "Focus", "2008", 5, 4)
bike01 = Bike("Honda", "Scoopy", 2018, 2)

print(car01.__dict__)
print("-=" * 45)
print(bike01.__dict__)