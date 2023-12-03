from project.computer_types import Product


class Food(Product):
    def __init__(self, name: str, quantity=15):
        super().__init__(name, quantity)
