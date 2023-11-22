from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_INCREMENT = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        burned_fuel = distance * (self.fuel_consumption + Car.AC_INCREMENT)

        if self.fuel_quantity >= burned_fuel:
            self.fuel_quantity -= burned_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_INCREMENT = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        burned_fuel = distance * (self.fuel_consumption + Truck.AC_INCREMENT)

        if self.fuel_quantity >= burned_fuel:
            self.fuel_quantity -= burned_fuel

    def refuel(self, fuel):
        current_fuel = 0.95 * fuel

        self.fuel_quantity += current_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
