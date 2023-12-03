from project.computer_types.computer import Computer


class Laptop(Computer):
    @staticmethod
    def available_processors():
        return {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}

    @staticmethod
    def max_ram():
        return 64

    def __str__(self):
        return 'laptop'
