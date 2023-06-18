class Transport:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


class Car(Transport):
    def __init__(self, brand, color, fuel_type):
        super().__init__(brand, color)
        self.fuel_type = fuel_type


class Airplane(Transport):
    def __init__(self, brand, color, airline):
        super().__init__(brand, color)
        self.airline = airline


class Ship(Transport):
    def __init__(self, brand, color, cargo_capacity):
        super().__init__(brand, color)
        self.cargo_capacity = cargo_capacity


# Creating objects to test the classes
car = Car("KIA", "Black", "Petrol")
airplane = Airplane("Boeing", "White", "UIA")
ship = Ship("Queen of the sea", "Black", "10000 tons")

print(car.brand)  # Outputs: KIA
print(car.color)  # Outputs: Black
print(car.fuel_type)  # Outputs: Petrol


print(airplane.brand)  # Outputs: Boeing
print(airplane.color)  # Outputs: White
print(airplane.airline)  # Outputs: UIA

print(ship.brand)  # Outputs: Queen of the sea
print(ship.color)  # Outputs: Black
print(ship.cargo_capacity)  # Outputs: 10000 tons
