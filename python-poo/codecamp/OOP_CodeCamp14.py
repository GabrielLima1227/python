# With Polymorphism
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
    def __init__(self, brand, model, year, number_of_doord) -> None:
        super().__init__(brand, model, year)
        self.number_of_doord = number_of_doord

    def start(self) -> None:
        print("Car is starting.")

    def stop(self) -> None:
        print("Car is stoping.")

class Motocycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self) -> None:
        print("Motocycle is starting.")

    def stop(self) -> None:
        print("Motocycle is stoping.")

class Plane(Vehicle):
    def __init__(self, brand, model, year, number_of_doord) -> None:
        super().__init__(brand, model, year)
        self.number_of_doord = number_of_doord

    def start(self) -> None:
        print("Plane is starting.")

    def stop(self) -> None:
        print("Plane is stoping.")



vehicles02: list[Vehicle]= [
    Car("Fod", "Focus", "2008", 5),
    Motocycle("Honda", "Scoopy", 2018),
    Plane("Boeing", "747", 2015, 16)
]

# Loop Through list of vehicles and inspect them (With Polymorphism)
# for vehicle in vehicles02:
#     if isinstance(vehicle, Vehicle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     else:
#         raise Exception(f"Object is not a valid vehicle")

for vehicle in vehicles02:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()