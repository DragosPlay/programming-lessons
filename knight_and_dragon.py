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


class item:
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

class shop:
    def __init__(self,
                 shop_item: item = None,
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
