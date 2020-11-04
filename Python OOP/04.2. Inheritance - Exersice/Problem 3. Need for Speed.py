class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        needed_final = kilometers * self.fuel_consumption
        if self.fuel >= needed_final:
            self.fuel -= needed_final


class Motorcycle (Vehicle):
    pass


class Car (Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    pass


class RaceMotorcycle (Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    pass


class CrossMotorcycle (Motorcycle):
    pass


class FamilyCar (Car):
    pass


class SportCar (Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    pass
