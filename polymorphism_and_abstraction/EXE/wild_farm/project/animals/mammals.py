from project.animals.animal import Mammal


class Mouse(Mammal):
    allowed_food = ['Fruit', 'Vegetable']
    gained_weight = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    allowed_food = ['Meat']
    gained_weight = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    allowed_food = ['Vegetable', 'Meat']
    gained_weight = 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    allowed_food = ['Meat']
    gained_weight = 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"
