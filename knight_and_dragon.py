'''
Разработать консольную игру игру Рыцарь и Дракон

Нужно применить все 4 принципа ООП

Нужно создать минимум 3 класса
в каждом классе минимум 4 свойства и 4 метода
Нужно чтобы в игре было минимум 4 сюжетные концовки
Soft Deadline: 16: 00 - нужно показать прогресс за два часа/
Hard Deadline: 1 неделя - сдача итоговой работы
'''

import random

class Player:
    def __init__(self,
                 nickname:str = 'BestPlayer',
                 money_balance:int = 0,
                 star_balance:int = 0,
                 power:int = 20,
                 health:int = 100,
                 stamina:int = 100,
                 inventory:list = []):
        self.nickname = nickname
        self.money_balance = money_balance
        self.star_balance = star_balance
        self.power = power
        self.health = health
        self.stamina = stamina
        self.inventory = inventory

    def training(self):
        stamina_error, health_error = False, False
        if self.power == 100:
            print('Ваша сила достагла максимального уровня, тренировка не требуется')
        elif self.stamina >= 20 and self.health >= 40:
            if self.power + 5 < 100:
                self.power += 5
                self.stamina -= 10
                print(f'Успешная тренировка, Ваша сила повышена до {self.power}')
            else:
                diff = (100 - self.power) * 2
                self.stamina -= diff
                self.power = 100
                print(f'Успешная лёгкая тренировка, Ваша сила повышена до максимального уровня, расход выносливости составил {diff}')
        else:
            if self.stamina < 20:
                stamina_error = True
            if self.health < 40:
                health_error = True
            if stamina_error:
                if health_error:
                    print('Для тренировки недостаточно здоровья и выносливости')
                else:
                    print('Для тренировки недостаточно выносливости')
            else:
                print('Для тренировки недостаточно здоровья')

    def treatment(self, points):
        st_pt = points // 2  # расход стамины на запрашиваемое игроком лечение
        if self.health == 100:
            print('Лечение не требуется, ваше здоровье максимально')
        elif self.stamina >= st_pt + 5:
            if self.health + points < 100:
                self.health += points
                self.stamina -= st_pt
                print(f'Успешное лечение принесло {points} здоровья! Текущее значение: {self.health}')
            else:
                st_pt = int((100 - self.health) / 2)
                self.stamina -= st_pt
                self.health = 100
                print(f'Здоровье повышено до максимум, расход выносливости составил {st_pt}')
        else:
            print(f'Для лечения недостаточно выносливости, отдохните. Текущий показатель: {self.health}')

    def chill(self):
        if self.stamina == 100:
            print('Уровень вашей выносливости максимальный, отдых не требуется')
        else:
            if self.stamina + 31 < 100:
                self.stamina += 30
                print(f'Выносливость восстановлена до {self.stamina}')
            else:
                self.stamina = 100
                print(f'Выносливость восстановлена до максимального уровня')

    def rebirth(self):
        if self.health == 100 and self.power == 100 and self.stamina == 100:
            self.star_balance += 1
            self.health = 40
            self.power = 20
            self.stamina = 0

    def attack(self, dragon):
        if self.stamina >= 10:
            if bool(random.getrandbits(1)):
                dragon.health -= self.power * (self.star_balance / 10 + 1)
                print(f'Критический удар! Здоровье дракона = {dragon.health}')
                self.stamina -= 10
            else:
                dragon.health -= self.power
                print(f'Удар! Здоровье дракона = {dragon.health}')
                self.stamina -= 4

class Dragon:
    def __init__(self,
                 name:str = 'None',
                 power:int = 20,
                 health:int = 100,
                 stamina:int = 100,
                 star_balance:int = 0):
        self.name = name
        self.star_balance = star_balance
        self.power = power
        self.health = health
        self.stamina = stamina

    def attack(self, player):
        if self.stamina >= 10:
            if self.health <= 30:
               player.health -= self.power * 3
               self.stamina -= 10
            else:
                if bool(random.getrandbits(1)):
                    player.health -= self.power * (self.star_balance / 10 + 1)
                    print(f'Критический удар! Здоровье игрока = {player.health}')
                    self.stamina -= 10
                else:
                    player.health -= self.power
                    print(f'Удар! Здоровье игрока = {player.health}')
                    self.stamina -= 5


class Item:
    def __init__(self,
                 name:str = 'None',
                 star_rating:int = 0,
                 damage:int = 0,
                 durability:int = 100,
                 armor:int = 0,
                 ):
        self.name = name
        self.star_rating = star_rating
        self.damage = damage
        self.durability = durability
        self.armor = armor

    def upgrade(self, player):
        if player.star_balance > self.star_rating:
            upgrade_price = (self.star_rating + 1) * 100
            if player.money_balance >= upgrade_price:
                player.money_balance -= upgrade_price
                if bool(random.getrandbits(1)):
                    self.star_rating += 1
                    self.durability += int(self.durability * 1.3)
                    self.armor = int(self.armor * 1.15)
                    self.damage = int(self.damage * 1.2)
                    print(f'Успешное улучшение!')
                else:
                    print(f'Предмет не улудшен :C')
            else:
                print(f'Недостаточно денег для улучшения. Ваш баланс: {player.money_balance}, стоимость улучшения: {upgrade_price}')
        else:
            print('Ваш престиж не превышает престиж предмета, улучшение невозможно')

    def repair(self, player, new_durability):
        repair_pt = new_durability - self.durability
        repair_price = (self.star_rating / 10 + 1) * repair_pt * 100
        if player.money_balance >= repair_price:
            self.durability = new_durability  # нет ограничения по максимальной прочности
            print(f'Успешеный ремонт! Стоимость составила {repair_price}')
        else:
            print(f'Денег недостаточно для ремонта, его стоимость {repair_price}, ваш баланс {player.money_balance}')

    def rename(self):
        new_name = input('Введите новое имя предмета: ')
        self.name = new_name

class Shop:
    def __init__(self,
                 shop_item: Item = None,
                 price:int = 0,
                 amount:int = 0,
                 min_player_lvl:int = 0
                 ):
        self.shop_item = shop_item
        self.price = price
        self.amount = amount
        self.min_player_lvl = min_player_lvl

    def buy_item(self, player):
        if self.amount == 0:
            print('Предмета нет в наличии :C')
            return
        if self.min_player_lvl > player.star_balance:
            print('Уровень вашего персонажа слишком мал для покупки этого преддмета')
            return
        if self.price <= player.money_balance:
            player.inventory.append(self.shop_item)
            player.money_balance -= self.price
            self.amount -= 1
            print(f"Предмет {self.shop_item.name} успешно куплен!")
        else:
            print(f'Для покупки недостаточно {self.price - player.money_balance} монет')

    def sell_item(self, player):
        if self.shop_item in player.inventory:
            player.inventory.remove(self.shop_item)
            player.money_balance += int(self.price * 0.7)
            print('Предмет успешно продан!')
        else:
            print(f'В вашем инвентаре нет такого предмета :C')

    def apply_discount(self, percent:int = 0):
        self.price = int(self.price - self.price * percent / 100)

class Ending:
    def __init__(self,
                 title:str = 'None',
                 description:str = 'None',
                 is_secret:bool = False,
                 required_stars:int = 0):
        self.title = title
        self.description = description
        self.is_secret = is_secret
        self.required_stars = required_stars

    def show_title(self):
        print(f'Приключение окончено: {self.title}')
        print(f'{self.description}')

class SecretEnding(Ending):
    def __init__(self,
                 title:str = 'None',
                 description:str = 'None',
                 required_stars:int = 0):
        super().__init__(title, description)
        self.is_secret = True
        self.required_stars = required_stars

    def show_title(self):
        print(f'Секретная концовка!')
        super().show_title()



if __name__ == '__main__':
    player = Player('Jora', 4500)

    Toothless = Dragon('Беззубик', 35, 120, 120)
    Stormfly = Dragon('Громгильда', 22, 110, 100)
    Hookfang = Dragon('Кривоклык', 28, 115, 80)
    Meatlug = Dragon('Сарделька', 15, 180, 90)
    Barf_Belch = Dragon('Барс и Вепрь', 25, 130, 100)
    Cloudjumper = Dragon('Облацепр', 26, 140, 110)
    Skullcrusher = Dragon('Шлемолом', 30, 160, 80)
    Grump = Dragon('Ворчун', 12, 200, 60)
    Light_Fury = Dragon('Дневная Фурия',30, 100, 150)

    Hauberk = Shop(
        shop_item=Item(name='Хауберк', star_rating=0, damage=0, durability=100, armor=15),
        price=120, amount=1, min_player_lvl=0
    )
    Gambeson = Shop(
        shop_item=Item(name='Гамбезон', star_rating=0, damage=0, durability=80, armor=10),
        price=80, amount=1, min_player_lvl=0
    )
    Aketon = Shop(
        shop_item=Item(name='Акетон', star_rating=0, damage=0, durability=85, armor=12),
        price=90, amount=1, min_player_lvl=0
    )
    Brigandine = Shop(
        shop_item=Item(name='Бригантина', star_rating=1, damage=0, durability=150, armor=32),
        price=300, amount=1, min_player_lvl=1
    )
    Cuirass = Shop(
        shop_item=Item(name='Кираса', star_rating=2, damage=0, durability=220, armor=55),
        price=550, amount=1, min_player_lvl=2
    )
    Coif = Shop(
        shop_item=Item(name='Кольчужный капюшон', star_rating=0, damage=0, durability=70, armor=6),
        price=50, amount=1, min_player_lvl=0
    )
    Sallet = Shop(
        shop_item=Item(name='Салад', star_rating=1, damage=0, durability=110, armor=16),
        price=160, amount=1, min_player_lvl=1
    )
    Barbuta = Shop(
        shop_item=Item(name='Барбют', star_rating=1, damage=0, durability=120, armor=20),
        price=200, amount=1, min_player_lvl=1
    )
    Bascinet = Shop(
        shop_item=Item(name='Бацинет', star_rating=1, damage=0, durability=130, armor=24),
        price=240, amount=1, min_player_lvl=1
    )
    Great_helm = Shop(
        shop_item=Item(name='Топфхельм', star_rating=2, damage=0, durability=180, armor=42),
        price=420, amount=1, min_player_lvl=2
    )
    Armet = Shop(
        shop_item=Item(name='Армэ', star_rating=2, damage=0, durability=200, armor=48),
        price=480, amount=1, min_player_lvl=2
    )
    Bevor = Shop(
        shop_item=Item(name='Бувигер', star_rating=1, damage=0, durability=90, armor=10),
        price=100, amount=1, min_player_lvl=1
    )
    Pauldrons = Shop(
        shop_item=Item(name='Наплечники', star_rating=1, damage=0, durability=100, armor=14),
        price=140, amount=1, min_player_lvl=1
    )
    Vambrace = Shop(
        shop_item=Item(name='Наручи', star_rating=0, damage=0, durability=90, armor=8),
        price=90, amount=1, min_player_lvl=0
    )
    Gauntlets = Shop(
        shop_item=Item(name='Латные рукавицы', star_rating=1, damage=0, durability=95, armor=12),
        price=130, amount=1, min_player_lvl=1
    )
    Cuisses = Shop(
        shop_item=Item(name='Набедренники', star_rating=1, damage=0, durability=110, armor=15),
        price=150, amount=1, min_player_lvl=1
    )
    Greaves = Shop(
        shop_item=Item(name='Поножи', star_rating=0, damage=0, durability=100, armor=10),
        price=110, amount=1, min_player_lvl=0
    )
    Sabatons = Shop(
        shop_item=Item(name='Сабатоны', star_rating=1, damage=0, durability=80, armor=8),
        price=95, amount=1, min_player_lvl=1
    )
