'''
Разработать консольную игру игру Рыцарь и Дракон

Нужно применить все 4 принципа ООП

Нужно создать минимум 3 класса
в каждом классе минимум 4 свойства и 4 метода
Нужно чтобы в игре было минимум 4 сюжетные концовки
Soft Deadline: 16: 00 - нужно показать прогресс за два часа/
Hard Deadline: 1 неделя - сдача итоговой работы
'''

class Player:
    def __init__(self,
                 nickname:str = 'BestPlayer',
                 money_balance:int = 0,
                 star_balance:int = 0,
                 power:int = 20,
                 health:int = 100,
                 stamina:int = 100):
        self.nickname = nickname
        self.money_balance = money_balance
        self.star_balance = star_balance
        self.power = power
        self.health = health
        self.stamina = stamina

class shop:
    def __init__(self,
                 item:str = 'None',
                 price:int = 0,
                 amount:int = 0):
        self.item = item
        self.price = price
        self.amount = amount

    def buy_item(self):

    def sell_item(self):

