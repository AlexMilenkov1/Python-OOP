from project.computer_types import Person
from project.computer_types import Employee


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
