from project.computer_types import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender=None)
        self.gender = 'Male'

    def make_sound(self):
        return 'Hiss'
