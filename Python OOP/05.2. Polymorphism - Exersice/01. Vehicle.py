from abc import ABC, abstractmethod


class Vehicle (ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    #def __init__(self, fuel_quantity, fuel_consumption):
        #super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + 0.90) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + 1.6) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (0.95 * fuel)


# Test Code:

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

# Expected output:

# 2.299999999999997
# 12.299999999999997


# Test Code:

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

# Expected output:

# 17.0
# 64.5