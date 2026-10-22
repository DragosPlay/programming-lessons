class Product:
    def __init__(self,
                price:float = 0.0,
                availability:int = 0,
                category:str = 'None'
                ):
        self.price = price
        self.availability = availability
        self.category = category

class Order(Product):
    def __init__(self,
                 discount: int = 0,
                 tax:int = 10
                 ):
        self.discount = discount
        self.tax = tax

class Customer:

class ShoppingCart: