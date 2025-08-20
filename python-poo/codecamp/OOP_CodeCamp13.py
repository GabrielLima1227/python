# Polymorphism 
# The word Polymorphism  is derived from Greek, and means "Having multiple forms":
# Poly = Many
# Morphism = Forms

# No Polymorphism
class Car:
    def __init__(self, brand, model, year, number_of_doord) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doord = number_of_doord

    def start(self) -> None:
        print("Car is starting.")

    def stop(self) -> None:
        print("Car is stoping.")

class Motocycle:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def start_bike(self) -> None:
        print("Motocycle is starting.")

    def stop_bike(self) -> None:
        print("Motocycle is stoping.")

# Create list of vehicles to inspect
vehicles01 = [
    Car("Fod", "Focus", "2008", 5),
    Motocycle("Honda", "Scoopy", 2018)
]

# Loop Through list of vehicles and inspect them
for vehicle in vehicles01:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, Motocycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception(f"Object is not a valid vehicle")