from project.animals.animal import Bird


class Owl(Bird):
    allowed_food = ['Meat']
    gained_weight = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    allowed_food = ['Fruit', 'Vegetable', 'Meat', 'Seed']
    gained_weight = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
