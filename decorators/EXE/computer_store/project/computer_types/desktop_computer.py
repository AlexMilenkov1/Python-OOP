from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    @staticmethod
    def available_processors():
        return {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}

    @staticmethod
    def max_ram():
        return 128

    def __str__(self):
        return 'desktop computer'
