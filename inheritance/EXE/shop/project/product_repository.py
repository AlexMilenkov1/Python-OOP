from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        searched_item = self.find(product_name)
        if searched_item is not None:
            self.products.remove(searched_item)

    def __repr__(self):
        result = []
        for product in self.products:
            result.append(f'{product.name}: {product.quantity}')
        return '\n'.join(result)
