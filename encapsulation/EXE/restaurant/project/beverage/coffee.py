from project.computer_types import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, price, milliliters, caffeine):
        super().__init__(name, price, milliliters)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
