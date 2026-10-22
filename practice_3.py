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

class Customer:
    shopping_list = {}
    def add_item(self,
                  item:Product):
        self.item = item
    def remove_item(self,
                    item:Product):
        self.item = item
    def change_quantity(self,
                    item:Product):
class ShoppingCart: