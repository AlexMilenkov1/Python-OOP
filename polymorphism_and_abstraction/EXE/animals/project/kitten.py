from project.computer_types import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender=None)
        self.gender = 'Female'

    def make_sound(self):
        return 'Meow'
