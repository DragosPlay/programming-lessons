class Product:
    def __init__(self,
                price:float = 0.0,
                availability:int = 0,
                product_name:str = 'None',
                category:str = 'None'
                ):
        self.price = price
        self.availability = availability
        self.product_name = product_name
        self.category = category

class Order:
    def __init__(self,
                 discount:int = 0,
                 tax:int = 10
                 ):
        self.discount = discount
        self.tax = tax

    def total_price(self):
        total = 0
        for product, quantity in self.items.items():
            total += quantity * product.price

        total -= total * self.discount
        total += self.tax * self.discount

        return total

class Customer:
    def __init__(self,
                 ID:str = 'None'):
        self.ID = ID
        self.order_history = []

        def add_order(self,
                      order):
            self.order_history.append(order)

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self,
                 product:str = 'None',
                 quantity:int = 0):
        self.items[product] = quantity

    def remove_item(self,
                    product:str = 'None',
                    quantity:int = 0):
        if self.items[product] - quantity > 0:
            self.items[product] = self.items[product] - quantity
        else:
            self.items[product] = 0
        def update_quantity(self,
                            product:str = 'None',
                            quantity:int = 0):
            self.items[product] = quantity