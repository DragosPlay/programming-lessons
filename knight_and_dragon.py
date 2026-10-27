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

    def training(self):
        if self.power == 100:
            print('Ваша сила достагла максимального уровня, тренировка не требуется')
        elif self.stamina >= 20 and self.health >= 40:
            if self.power + 6 <= 100:
                self.power += 5
                self.stamina -= 10
                print(f'Успешная тренировка, Ваша сила повышена до {self.power}')
            else:
                self.power = 100
                self.stamina -= (100 - self.power) * 2
                print(f'Успешная лёгкая тренировка, Ваша сила повышена до максимального уровня, расход выносливости составил {(100 - self.power) * 2}')
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
        st_pt = points / 2  # расход стамины на запрашиваемое игроком лечение
        if self.health == 100:
            print('Лечение не требуется, ваше здоровье максимально')
        elif self.stamine >= st_pt + 5:
            if self.health + (st_pt + 1) <= 100:
                self.health += points
                self.stamina -= st_pt
                print(f'Успешное лечение принесло {points} здоровья! Текущее значение: {self.health}')
            else:
                self.health = 100
                st_pt = int((100 - self.health) / 2)
                self.stamina -= st_pt
                print(f'Здоровье повышено до максимум, расход выносливости составил {st_pt}')
        else:
            print(f'Для лечения недостаточно выносливости, отдохните. Текущий показатель: {self.health}')

    def chill(self):
        if self.stamina == 100:
            print('Уровень вашей выносливости максимальный, отдых не требуется')
        else:
            if self.stamina + 31 <= 100:
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

