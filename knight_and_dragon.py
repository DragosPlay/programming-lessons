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

    Dagger = Shop(
        shop_item=Item(name='Кинжал', star_rating=0, damage=12, durability=60, armor=0),
        price=40, amount=1, min_player_lvl=0
    )
    Rondel = Shop(
        shop_item=Item(name='Рондель', star_rating=0, damage=14, durability=70, armor=0),
        price=55, amount=1, min_player_lvl=0
    )
    Misericorde = Shop(
        shop_item=Item(name='Мизерикордия', star_rating=1, damage=18, durability=80, armor=0),
        price=90, amount=1, min_player_lvl=1
    )
    Falchion = Shop(
        shop_item=Item(name='Фальшион', star_rating=0, damage=22, durability=90, armor=0),
        price=110, amount=1, min_player_lvl=0
    )
    Arming_sword = Shop(
        shop_item=Item(name='Рыцарский меч', star_rating=1, damage=26, durability=100, armor=0),
        price=160, amount=1, min_player_lvl=1
    )
    Broadsword = Shop(
        shop_item=Item(name='Широкий меч', star_rating=1, damage=28, durability=110, armor=0),
        price=180, amount=1, min_player_lvl=1
    )
    Longsword = Shop(
        shop_item=Item(name='Длинный меч', star_rating=1, damage=35, durability=120, armor=0),
        price=250, amount=1, min_player_lvl=1
    )
    Zweihander = Shop(
        shop_item=Item(name='Цвайхендер', star_rating=2, damage=55, durability=150, armor=0),
        price=500, amount=1, min_player_lvl=2
    )
    Spear = Shop(
        shop_item=Item(name='Копье', star_rating=0, damage=20, durability=80, armor=0),
        price=80, amount=1, min_player_lvl=0
    )
    Pike = Shop(
        shop_item=Item(name='Пика', star_rating=1, damage=25, durability=95, armor=0),
        price=120, amount=1, min_player_lvl=1
    )
    Glaive = Shop(
        shop_item=Item(name='Глефа', star_rating=1, damage=32, durability=110, armor=0),
        price=210, amount=1, min_player_lvl=1
    )
    Billhook = Shop(
        shop_item=Item(name='Биллгук', star_rating=1, damage=30, durability=105, armor=0),
        price=190, amount=1, min_player_lvl=1
    )
    Halberd = Shop(
        shop_item=Item(name='Алебарда', star_rating=2, damage=45, durability=130, armor=0),
        price=380, amount=1, min_player_lvl=2
    )
    Poleaxe = Shop(
        shop_item=Item(name='Полэкс', star_rating=2, damage=48, durability=140, armor=0),
        price=410, amount=1, min_player_lvl=2
    )
    Mace = Shop(
        shop_item=Item(name='Шестопёр', star_rating=1, damage=30, durability=140, armor=0),
        price=220, amount=1, min_player_lvl=1
    )
    Battle_axe = Shop(
        shop_item=Item(name='Боевой топор', star_rating=1, damage=34, durability=110, armor=0),
        price=240, amount=1, min_player_lvl=1
    )
    Flail = Shop(
        shop_item=Item(name='Цепной кистень', star_rating=1, damage=36, durability=100, armor=0),
        price=260, amount=1, min_player_lvl=1
    )
    Morningstar = Shop(
        shop_item=Item(name='Моргенштерн', star_rating=2, damage=42, durability=130, armor=0),
        price=350, amount=1, min_player_lvl=2
    )
    War_hammer = Shop(
        shop_item=Item(name='Боевой молот', star_rating=2, damage=46, durability=150, armor=0),
        price=390, amount=1, min_player_lvl=2
    )
    Longbow = Shop(
        shop_item=Item(name='Длинный лук', star_rating=1, damage=24, durability=90, armor=0),
        price=150, amount=1, min_player_lvl=1
    )
    Crossbow = Shop(
        shop_item=Item(name='Арбалет', star_rating=2, damage=40, durability=100, armor=0),
        price=320, amount=1, min_player_lvl=2
    )

    e1 = Ending("Смерть героя", "Вы погибли в бою. Дракон оказался сильнее.", False, 0)
    e2 = Ending("Победа", "Дракон повержен. Вы спасли королевство.", False, 0)
    e3 = Ending("Трус", "Вы сбежали из королевства и стали фермером.", False, 0)
    e4 = Ending("Измождение", "Вы упали без сил посреди тренировки и не проснулись.", False, 0)
    e5 = SecretEnding("Божество", "Ваш престиж абсолютен. Драконы преклонили колени без боя.", 3)
    e6 = SecretEnding("Банкрот", "У вас отрицательный баланс из-за баганного ремонта. Вас посадили в тюрьму.", 0)
    e7 = SecretEnding("Пацифист",
                      "Вы зашли в магазин, скупили всё оружие и доспехи, но так ни разу и не ударили дракона. Наступил мир.",
                      0)
    e8 = SecretEnding("Истинный Повелитель", "Вы одолели Беззубика, имея 5 звезд престижа. Вы — новый Король Драконов.",
                      5)

    import os
    import time

    e9 = Ending("Гроза Архипелага",
                "Вы поочередно сокрушили всех 9 великих драконов! Ваше имя навсегда вписано в легенды.", False, 0)
    e10 = Ending("Мастер-Оружейник",
                 "Вы выковали легендарное именное снаряжение в кузнице и основали собственную гильдию.", False, 0)
    e11 = SecretEnding("Всадник Ночной Фурии",
                       "Вместо последнего удара вы протянули Беззубику рыбу и приручили его. Теперь вы летаете вместе!",
                       2)
    e12 = SecretEnding("Золотой Магнат", "Вы накопили более 10 000 монет на боях и торговле, выкупив королевский трон!",
                       1)

    # Цветовая палитра консоли
    C_RESET = '\033[0m'
    C_BOLD = '\033[1m'
    C_RED = '\033[91m'
    C_GREEN = '\033[92m'
    C_YELLOW = '\033[93m'
    C_BLUE = '\033[94m'
    C_MAGENTA = '\033[95m'
    C_CYAN = '\033[96m'
    C_GRAY = '\033[90m'

    all_dragons = [
        Grump, Meatlug, Stormfly, Barf_Belch, Hookfang,
        Cloudjumper, Skullcrusher, Light_Fury, Toothless
    ]
    dragon_lore = {
        'Ворчун': 'Старый кузнечный дракон класса Камнеед. Медленный, но с толстой шкурой.',
        'Сарделька': 'Панцирная Громмель, чья чешуя крепче чугунных щитов.',
        'Громгильда': 'Стремительный Злобный Змеевик с ядовитыми шипами на хвосте.',
        'Барс и Вепрь': 'Двухголовый Кошмарный Пристеголов: одна голова пускает газ, другая — искру!',
        'Кривоклык': 'Свирепое Ужасное Чудовище, объятое жидким пламенем.',
        'Облацепр': 'Четырехкрылый Шторморез, рассекающий грозовые тучи.',
        'Шлемолом': 'Неудержимый Костолом, таранящий скалы своим костяным лбом.',
        'Дневная Фурия': 'Ослепительная молния небес, способная растворяться в воздухе.',
        'Беззубик': 'Альфа-дракон. Король Ночных Фурий и повелитель архипелага.'
    }

    armor_shops = [
        Hauberk, Gambeson, Aketon, Brigandine, Cuirass, Coif, Sallet, Barbuta,
        Bascinet, Great_helm, Armet, Bevor, Pauldrons, Vambrace, Gauntlets,
        Cuisses, Greaves, Sabatons
    ]
    weapon_shops = [
        Dagger, Rondel, Misericorde, Falchion, Arming_sword, Broadsword, Longsword,
        Zweihander, Spear, Pike, Glaive, Billhook, Halberd, Poleaxe, Mace,
        Battle_axe, Flail, Morningstar, War_hammer, Longbow, Crossbow
    ]
    all_shops = armor_shops + weapon_shops

    # Игровые флаги для сюжета и секретных концовок
    has_attacked_any_dragon = False
    discount_used = False
    exhaustion_counter = 0
    forged_custom_weapon = False


    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    def draw_bar(val, max_val, length=15, color=C_GREEN):
        val_clamped = max(0, min(val, max_val))
        filled = int(length * val_clamped / max_val) if max_val > 0 else 0
        return f"{color}{'█' * filled}{C_GRAY}{'░' * (length - filled)}{C_RESET} {int(val)}/{max_val}"


    def get_bonus_damage():
        weapons = [i for i in player.inventory if i.damage > 0 and i.durability > 0]
        return max((w.damage for w in weapons), default=0)


    def get_bonus_armor():
        armors = [i for i in player.inventory if i.armor > 0 and i.durability > 0]
        return min(75, sum(a.armor for a in armors))


    def show_hud():
        stars = "★" * player.star_balance if player.star_balance > 0 else "☆ (0)"
        alive_dragons = sum(1 for d in all_dragons if d.health > 0)
        print(f"{C_CYAN}╔{'═' * 72}╗{C_RESET}")
        print(
            f"{C_CYAN}║{C_RESET} 🛡 Рыцарь: {C_BOLD}{player.nickname:<12}{C_RESET} │ Золото: {C_YELLOW}{player.money_balance:>6} 🪙{C_RESET} │ Престиж: {C_MAGENTA}{stars:<10}{C_RESET} {C_CYAN}║{C_RESET}")
        print(f"{C_CYAN}╠{'═' * 72}╣{C_RESET}")
        print(
            f"{C_CYAN}║{C_RESET} ❤️ HP:   {draw_bar(player.health, 100, 14, C_RED):<32} │ 🗡 Доп. урон оружия: +{get_bonus_damage():<4} {C_CYAN}║{C_RESET}")
        print(
            f"{C_CYAN}║{C_RESET} ⚡ Вын.: {draw_bar(player.stamina, 100, 14, C_CYAN):<32} │ 🛡 Защита доспехов:  {get_bonus_armor():>2}%   {C_CYAN}║{C_RESET}")
        print(
            f"{C_CYAN}║{C_RESET} 💪 Сила: {draw_bar(player.power, 100, 14, C_GREEN):<32} │ 🐉 Осталось драконов: {alive_dragons}/9  {C_CYAN}║{C_RESET}")
        print(f"{C_CYAN}╚{'═' * 72}╝{C_RESET}")


    def trigger_ending(ending_obj):
        clear_screen()
        color = C_MAGENTA if ending_obj.is_secret else C_YELLOW
        print(f"\n{color}╔{'═' * 72}╗")
        print(f"║{'ФИНАЛ ИСТОРИИ'.center(72)}║")
        print(f"╚{'═' * 72}╝{C_RESET}\n")
        ending_obj.show_title()
        print(f"\n{C_GRAY}{'─' * 74}{C_RESET}")
        print(f"Итоговая статистика рыцаря {C_BOLD}{player.nickname}{C_RESET}:")
        print(f" • Звезды престижа: ★ {player.star_balance}")
        print(f" • Баланс золота:   {player.money_balance} монет")
        print(f" • Предметов:       {len(player.inventory)} шт.")
        print(f" • Побеждено боссов: {sum(1 for d in all_dragons if d.health <= 0)} из 9")
        print(f"{C_GRAY}{'─' * 74}{C_RESET}")
        input(f"\n{C_CYAN}[Нажмите Enter, чтобы завершить игру...]{C_RESET}")
        raise SystemExit


    # --- ПРОЛОГ И ВЫБОР ИМЕНИ ---
    clear_screen()
    print(f"""{C_YELLOW}
                     ___====-_  _-====___
               _--^^^#####//      \\\\#####^^^--_
            _-^##########// (    ) \\\\##########^-_
           -############//  |\\^^/|  \\\\############-
         _/############//   (@::@)   \\\\############\\_
        /#############((     \\\\//     ))#############\\
       -###############\\\\    (oo)    //###############-
        {C_RESET}""")
    print(f"{C_BOLD}{C_CYAN}      ⚔️  ЛЕГЕНДЫ ЭЛЬДОРИИ: РЫЦАРЬ И ДРАКОН  ⚔️{C_RESET}\n")
    print("Над королевством сгустились тучи. Девять легендарных драконов во главе")
    print("с неуловимым Беззубиком заняли горные пики. Король выдал вам 4500 золотых")
    print("из казны на снаряжение и подготовку. Ваша судьба — в ваших руках!\n")
    custom_name = input(f"Как величать вас, сэр рыцарь? (Enter — оставить '{player.nickname}'): ").strip()
    if custom_name:
        player.nickname = custom_name

    # --- ГЛАВНЫЙ СЮЖЕТНЫЙ ЦИКЛ ---
    while True:
        # Проверка автоматических секретных концовок
        if player.money_balance < 0:
            trigger_ending(e6)  # Банкрот

        if not has_attacked_any_dragon and all(s.amount == 0 for s in all_shops):
            trigger_ending(e7)  # Пацифист (скупил все 39 товаров и ни разу не ударил дракона)

        if all(d.health <= 0 for d in all_dragons):
            trigger_ending(e9)  # Все 9 драконов побеждены

        clear_screen()
        show_hud()
        print(f"\n{C_BOLD}🏰 ГЛАВНАЯ ПЛОЩАДЬ КОРОЛЕВСТВА:{C_RESET}")
        print(f"  {C_YELLOW}[1]{C_RESET} ⛺ Лагерь Рыцаря     (Тренировка, Лечение, Отдых, Перерождение ★)")
        print(f"  {C_YELLOW}[2]{C_RESET} 🛒 Королевский Рынок (Покупка/Продажа 39 видов оружия и брони, Скидки)")
        print(f"  {C_YELLOW}[3]{C_RESET} ⚒️  Кузница и Инвентарь (Улучшение ★, Ремонт, Переименование)")
        print(f"  {C_YELLOW}[4]{C_RESET} 🌋 Пик Драконов      (Сюжетные битвы с 9 драконами)")
        print(f"  {C_YELLOW}[5]{C_RESET} 📜 Зал Судьбы        (Завершить путь / Проверить доступные концовки)")
        print(f"  {C_YELLOW}[0]{C_RESET} 🚜 Сбежать из королевства на ферму")

        choice = input(f"\n{C_CYAN}Ваш выбор > {C_RESET}").strip()

        # ==================== 0. ПОБЕГ (КОНЦОВКА ТРУС) ====================
        if choice == '0':
            trigger_ending(e3)

        # ==================== 1. ЛАГЕРЬ РЫЦАРЯ ====================
        elif choice == '1':
            while True:
                clear_screen()
                show_hud()
                print(f"\n{C_BOLD}⛺ ЛАГЕРЬ РЫЦАРЯ:{C_RESET}")
                print("Здесь вы можете закалить тело, залечить раны или пройти ритуал Перерождения.")
                print(f"  {C_GREEN}[1]{C_RESET} 🏋️ Тренироваться (Повысить силу, нужно HP >= 40 и Вын. >= 20)")
                print(f"  {C_GREEN}[2]{C_RESET} 🧪 Вылечиться    (Восстановить здоровье за счет выносливости)")
                print(f"  {C_GREEN}[3]{C_RESET} 🔥 Отдохнуть     (Восстановить +30 выносливости у костра)")
                print(
                    f"  {C_MAGENTA}[4]{C_RESET} 🌟 Алтарь Перерождения (Нужно 100 HP, 100 Силы, 100 Вын. -> +1 ★ Престижа)")
                print(f"  {C_YELLOW}[0]{C_RESET} 🔙 Вернуться на площадь")

                c_act = input(f"\n{C_CYAN}Действие в лагере > {C_RESET}").strip()
                if c_act == '0':
                    break
                elif c_act == '1':
                    prev_power = player.power
                    player.training()
                    if player.stamina < 20 and player.power == prev_power and player.power < 100:
                        exhaustion_counter += 1
                        print(
                            f"{C_RED}⚠️ Осторожно! Вы тренируетесь на пределе сил ({exhaustion_counter}/3 до обморока)!{C_RESET}")
                        if exhaustion_counter >= 3:
                            time.sleep(1.5)
                            trigger_ending(e4)  # Концовка: Измождение
                    else:
                        exhaustion_counter = 0
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif c_act == '2':
                    pts_str = input("Сколько единиц здоровья восстановить? (например, 30): ").strip()
                    if pts_str.isdigit():
                        player.treatment(int(pts_str))
                    else:
                        print("Введите корректное число!")
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif c_act == '3':
                    player.chill()
                    exhaustion_counter = 0
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif c_act == '4':
                    old_stars = player.star_balance
                    player.rebirth()
                    if player.star_balance > old_stars:
                        print(
                            f"{C_MAGENTA}✨ Небесный свет озарил лагерь! Ваш престиж вырос до ★ {player.star_balance}!{C_RESET}")
                    else:
                        print(
                            f"{C_RED}Требования ритуала не выполнены: доведите HP, Силу и Выносливость ровно до 100!{C_RESET}")
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")

        # ==================== 2. КОРОЛЕВСКИЙ РЫНОК ====================
        elif choice == '2':
            while True:
                clear_screen()
                show_hud()
                left_count = sum(s.amount for s in all_shops)
                total_cost_left = sum(s.price for s in all_shops if s.amount > 0)
                print(
                    f"\n{C_BOLD}🛒 КОРОЛЕВСКИЙ РЫНОК (Осталось товаров: {left_count}/39 на сумму {total_cost_left} 🪙):{C_RESET}")
                print(f"  {C_YELLOW}[1]{C_RESET} 🛡 Купить Доспехи и Шлемы (18 видов)")
                print(f"  {C_YELLOW}[2]{C_RESET} 🗡 Купить Оружие          (21 вид)")
                print(f"  {C_YELLOW}[3]{C_RESET} 💰 Продать предмет из инвентаря (за 70% цены)")
                print(
                    f"  {C_MAGENTA}[4]{C_RESET} 👑 Королевский указ о скидке (Применить apply_discount ко всем товарам)")
                print(f"  {C_GREEN}[5]{C_RESET} 📦 Скупить вообще ВСЁ доступное на рынке (Путь Пацифиста)")
                print(f"  {C_YELLOW}[0]{C_RESET} 🔙 Вернуться на площадь")

                s_act = input(f"\n{C_CYAN}Выбор в магазине > {C_RESET}").strip()
                if s_act == '0':
                    break
                elif s_act in ('1', '2'):
                    cat_list = armor_shops if s_act == '1' else weapon_shops
                    cat_title = "ДОСПЕХИ" if s_act == '1' else "ОРУЖИЕ"
                    clear_screen()
                    print(
                        f"{C_BOLD}=== {cat_title} (Ваш баланс: {player.money_balance} 🪙 | Ваш престиж: ★{player.star_balance}) ==={C_RESET}")
                    for idx, sh in enumerate(cat_list, 1):
                        it = sh.shop_item
                        stat = f"Броня: +{it.armor}" if it.armor > 0 else f"Урон: +{it.damage}"
                        status = f"{C_GREEN}{sh.price} 🪙{C_RESET}" if sh.amount > 0 else f"{C_RED}ПРОДАНО{C_RESET}"
                        print(
                            f"  [{idx:>2}] {it.name:<20} │ {stat:<12} │ Прочн.: {it.durability:<3} │ Мин.★: {sh.min_player_lvl} │ {status}")
                    num_s = input("\nВведите номер товара для покупки (0 - отмена): ").strip()
                    if num_s.isdigit() and 1 <= int(num_s) <= len(cat_list):
                        cat_list[int(num_s) - 1].buy_item(player)
                        input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif s_act == '3':
                    if not player.inventory:
                        print("Ваш инвентарь пуст!")
                    else:
                        print("\nВаши предметы:")
                        for idx, it in enumerate(player.inventory, 1):
                            print(f"  [{idx}] {it.name} (★{it.star_rating}, Прочность: {it.durability})")
                        num_s = input("Номер предмета для продажи (0 - отмена): ").strip()
                        if num_s.isdigit() and 1 <= int(num_s) <= len(player.inventory):
                            target_item = player.inventory[int(num_s) - 1]
                            shop_match = next((s for s in all_shops if s.shop_item == target_item), None)
                            if shop_match:
                                shop_match.sell_item(player)
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif s_act == '4':
                    if not discount_used:
                        disc = 50 if player.star_balance >= 2 else 35
                        for s in all_shops:
                            s.apply_discount(disc)
                        discount_used = True
                        print(
                            f"{C_GREEN}📜 Вы предъявили королевскую грамоту! Все цены в магазине снижены на {disc}%!{C_RESET}")
                    else:
                        print(f"{C_YELLOW}Торговец уже предоставил вам максимальную королевскую скидку!{C_RESET}")
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif s_act == '5':
                    for s in all_shops:
                        if s.amount > 0:
                            s.buy_item(player)
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")

        # ==================== 3. КУЗНИЦА И ИНВЕНТАРЬ ====================
        elif choice == '3':
            while True:
                clear_screen()
                show_hud()
                print(f"\n{C_BOLD}⚒️  КУЗНИЦА И ИНВЕНТАРЬ ({len(player.inventory)} предм.):{C_RESET}")
                if not player.inventory:
                    print(f"  {C_GRAY}У вас пока нет снаряжения. Загляните на Королевский Рынок!{C_RESET}")
                else:
                    for idx, it in enumerate(player.inventory, 1):
                        stat = f"🗡 Урон: {it.damage}" if it.damage > 0 else f"🛡 Броня: {it.armor}"
                        print(
                            f"  [{idx:>2}] {C_BOLD}{it.name:<20}{C_RESET} │ ★{it.star_rating} │ {stat:<12} │ 🔧 Прочность: {it.durability}")

                print(f"\n  {C_YELLOW}[1]{C_RESET} ✨ Улучшить предмет (upgrade — нужен престиж игрока > ★ предмета)")
                print(f"  {C_YELLOW}[2]{C_RESET} 🔧 Отремонтировать предмет (repair — задать новую прочность)")
                print(f"  {C_YELLOW}[3]{C_RESET} 🏷  Переименовать предмет (rename — дать легендарное имя)")
                print(f"  {C_YELLOW}[0]{C_RESET} 🔙 Вернуться на площадь")

                f_act = input(f"\n{C_CYAN}Выбор в кузнице > {C_RESET}").strip()
                if f_act == '0':
                    break
                if not player.inventory:
                    input(f"\n{C_RED}Сначала купите хотя бы один предмет! [Enter]{C_RESET}")
                    continue

                idx_s = input("Введите номер предмета из списка: ").strip()
                if not (idx_s.isdigit() and 1 <= int(idx_s) <= len(player.inventory)):
                    continue
                selected_item = player.inventory[int(idx_s) - 1]

                if f_act == '1':
                    selected_item.upgrade(player)
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif f_act == '2':
                    print(f"Текущая прочность '{selected_item.name}': {selected_item.durability}")
                    print(
                        f"{C_GRAY}(Подсказка: если ввести отрицательную прочность и согласиться на списание пошлины, сработает баг ремонта для секретной концовки Банкрот){C_RESET}")
                    dur_s = input("Введите желаемую новую прочность (например, 150 или -100): ").strip()
                    try:
                        new_dur = int(dur_s)
                        old_dur = selected_item.durability
                        selected_item.repair(player, new_dur)
                        # Если ремонт прошел, списываем пошлину кузнеца (или загоняем в долг при баганном ремонте)
                        if selected_item.durability == new_dur:
                            cost = int((selected_item.star_rating / 10 + 1) * abs(new_dur - old_dur) * 100)
                            player.money_balance -= cost
                            print(f"Кузнец списал со счета {cost} монет. Текущий баланс: {player.money_balance} 🪙")
                    except ValueError:
                        print("Некорректное число!")
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")
                elif f_act == '3':
                    selected_item.rename()
                    forged_custom_weapon = True
                    input(f"\n{C_GRAY}[Enter]{C_RESET}")

        # ==================== 4. ПИК ДРАКОНОВ (СЮЖЕТНЫЕ БИТВЫ) ====================
        elif choice == '4':
            clear_screen()
            show_hud()
            # Проверка секретной концовки Божество (e5)
            if player.star_balance >= e5.required_stars:
                print(f"\n{C_MAGENTA}⚡ ВАША АУРА ПРЕСТИЖА (★{player.star_balance}) СОТРЯСАЕТ ГОРЫ!{C_RESET}")
                print("Драконы чувствуют вашу божественную мощь и готовы склонить головы без боя.")
                god_choice = input(
                    "Принять поклонение драконов и вознестись? (1 - Да [Секретный финал], 2 - Нет, я хочу сражаться!): ").strip()
                if god_choice == '1':
                    trigger_ending(e5)

            print(f"\n{C_BOLD}🌋 ЛОГОВО ДРАКОНОВ — ВЫБЕРИТЕ ПРОТИВНИКА:{C_RESET}")
            for idx, d in enumerate(all_dragons, 1):
                status = f"{C_RED}❤️ HP: {int(d.health):<4} │ ⚡ Вын.: {d.stamina:<3} │ 🔥 Сила: {d.power}{C_RESET}" if d.health > 0 else f"{C_GREEN}ПОВЕРЖЕН ✅{C_RESET}"
                print(f"  [{idx}] {C_BOLD}{d.name:<15}{C_RESET} │ {status}")
                print(f"      {C_GRAY}└─ {dragon_lore.get(d.name, '')}{C_RESET}")
            print(f"  [0] 🔙 Отступить в город")

            d_choice = input(f"\n{C_CYAN}С кем вступить в бой? > {C_RESET}").strip()
            if d_choice.isdigit() and 1 <= int(d_choice) <= len(all_dragons):
                target_dragon = all_dragons[int(d_choice) - 1]
                if target_dragon.health <= 0:
                    input(f"\n{C_GREEN}Этот дракон уже повержен! [Enter]{C_RESET}")
                    continue

                # --- БОЕВОЙ РЕЖИМ ---
                while target_dragon.health > 0 and player.health > 0:
                    clear_screen()
                    show_hud()
                    print(f"\n{C_RED}╔{'═' * 72}╗{C_RESET}")
                    print(
                        f"{C_RED}║{C_RESET} 🐉 ПРОТИВНИК: {C_BOLD}{target_dragon.name:<18}{C_RESET}                                       {C_RED}║{C_RESET}")
                    print(
                        f"{C_RED}║{C_RESET} ❤️ Здоровье:  {draw_bar(target_dragon.health, 200, 20, C_RED):<38} │ 🔥 Урон: {target_dragon.power:<4} {C_RED}║{C_RESET}")
                    print(
                        f"{C_RED}║{C_RESET} ⚡ Вынослив.: {draw_bar(target_dragon.stamina, 150, 20, C_YELLOW):<38} │ ★ Ранг: {target_dragon.star_balance:<4} {C_RED}║{C_RESET}")
                    print(f"{C_RED}╚{'═' * 72}╝{C_RESET}")

                    print(f"\n{C_BOLD}ВАШ ХОД В БОЮ:{C_RESET}")
                    print(
                        f"  {C_RED}[1]{C_RESET} ⚔️ Атаковать дракона   (player.attack + бонус оружия +{get_bonus_damage()})")
                    print(f"  {C_GREEN}[2]{C_RESET} 🧪 Перевязать раны     (player.treatment)")
                    print(f"  {C_CYAN}[3]{C_RESET} 🛡 Перевести дух       (player.chill — +30 выносливости)")
                    if target_dragon == Toothless and target_dragon.health <= 50 and player.star_balance >= 2:
                        print(f"  {C_MAGENTA}[4]{C_RESET} 🐟 Протянуть Беззубику рыбу и приручить (Секретное действие!)")
                    print(f"  {C_YELLOW}[0]{C_RESET} 🏃 Сбежать с поля боя")

                    b_act = input(f"\n{C_CYAN}Боевая команда > {C_RESET}").strip()
                    if b_act == '0':
                        print("Вы отступили с поля боя в город!")
                        time.sleep(1)
                        break
                    elif b_act == '4' and target_dragon == Toothless and target_dragon.health <= 50 and player.star_balance >= 2:
                        trigger_ending(e11)  # Секретная концовка: Всадник Ночной Фурии
                    elif b_act == '1':
                        if player.stamina < 10:
                            print(
                                f"{C_RED}У вас недостаточно выносливости для удара (<10)! Переведите дух [3]!{C_RESET}")
                            input(f"{C_GRAY}[Enter]{C_RESET}")
                            continue
                        has_attacked_any_dragon = True
                        hp_before = target_dragon.health
                        player.attack(target_dragon)
                        # Применяем бонус от оружия из инвентаря
                        w_bonus = get_bonus_damage()
                        if target_dragon.health < hp_before and w_bonus > 0:
                            target_dragon.health -= w_bonus
                            for it in player.inventory:
                                if it.damage > 0 and it.durability > 0:
                                    it.durability = max(0, it.durability - 2)
                                    break
                            print(
                                f"{C_CYAN}🗡 Ваше оружие наносит дополнительно {w_bonus} урона! (HP дракона: {int(target_dragon.health)}){C_RESET}")
                    elif b_act == '2':
                        player.treatment(30)
                    elif b_act == '3':
                        player.chill()
                    else:
                        continue

                    # Проверка победы над драконом
                    if target_dragon.health <= 0:
                        reward = target_dragon.power * 35
                        player.money_balance += reward
                        print(
                            f"\n{C_GREEN}🎉 ПОБЕДА! Дракон {target_dragon.name} повержен! Вы получили награду {reward} 🪙!{C_RESET}")
                        input(f"\n{C_GRAY}[Нажмите Enter...]{C_RESET}")
                        if target_dragon == Toothless:
                            if player.star_balance >= e8.required_stars:
                                trigger_ending(e8)  # Истинный Повелитель (5 звезд + победа над Беззубиком)
                            else:
                                ans = input(
                                    "Альфа-дракон повержен! Завершить игру триумфом? (1 - Да, 2 - Продолжить зачистку пещер): ").strip()
                                if ans == '1':
                                    trigger_ending(e2)
                        break

                    # Ответный ход дракона
                    print(f"\n{C_RED}--- Ход дракона {target_dragon.name} ---{C_RESET}")
                    if target_dragon.stamina < 10:
                        target_dragon.stamina += 25
                        print(
                            f"{C_YELLOW}🐉 {target_dragon.name} тяжело дышит и восстанавливает силы (+25 выносливости).{C_RESET}")
                    else:
                        p_hp_before = player.health
                        target_dragon.attack(player)
                        dmg_taken = p_hp_before - player.health
                        armor_pct = get_bonus_armor()
                        if dmg_taken > 0 and armor_pct > 0:
                            blocked = int(dmg_taken * (armor_pct / 100))
                            player.health += blocked
                            for it in player.inventory:
                                if it.armor > 0 and it.durability > 0:
                                    it.durability = max(0, it.durability - 2)
                            print(
                                f"{C_BLUE}🛡 Ваша броня поглотила {blocked} ед. урона! Текущее здоровье: {int(player.health)}{C_RESET}")

                    if player.health <= 0:
                        input(f"\n{C_RED}Вы пали в бою... [Enter]{C_RESET}")
                        trigger_ending(e1)  # Смерть героя

                    input(f"\n{C_GRAY}[Следующий раунд — Enter]{C_RESET}")

        # ==================== 5. ЗАЛ СУДЬБЫ (КОНЦОВКИ) ====================
        elif choice == '5':
            clear_screen()
            show_hud()
            print(f"\n{C_BOLD}📜 ЗАЛ СУДЬБЫ (Выберите или проверьте условия 12 концовок):{C_RESET}")
            print("  • [e1] Смерть героя         — Погибнуть в бою с драконом")
            print("  • [e2] Победа               — Победить дракона и спасти королевство")
            print("  • [e3] Трус                 — Выбрать побег на ферму [0] в главном меню")
            print("  • [e4] Измождение           — 3 раза подряд пытаться тренироваться без выносливости")
            print("  • [e5] ★ Божество           — Достичь 3 ★ престижа и войти на Пик Драконов")
            print("  • [e6] ★ Банкрот            — Уйти в отрицательный баланс при ремонте в кузнице")
            print("  • [e7] ★ Пацифист           — Скупить все 39 предметов в магазине, ни разу не ударив дракона")
            print("  • [e8] ★ Истинный Повелитель— Одолеть Беззубика, имея 5 ★ престижа")
            print("  • [e9] Гроза Архипелага     — Одолеть всех 9 драконов")
            print("  • [e10] Мастер-Оружейник    — Переименовать и улучшить оружие в кузнице")
            print("  • [e11] ★ Всадник Фурии     — Приручить раненого Беззубика в бою (при 2+ ★ престижа)")
            print("  • [e12] ★ Золотой Магнат    — Накопить 10 000+ монет и 1+ ★ престижа\n")

            if player.money_balance >= 10000 and player.star_balance >= 1:
                if input(
                        f"{C_YELLOW}Доступен финал 'Золотой Магнат'! Завершить игру? (1 - Да, 0 - Нет): {C_RESET}").strip() == '1':
                    trigger_ending(e12)
            if forged_custom_weapon and any(i.star_rating >= 1 for i in player.inventory):
                if input(
                        f"{C_YELLOW}Доступен финал 'Мастер-Оружейник'! Завершить игру? (1 - Да, 0 - Нет): {C_RESET}").strip() == '1':
                    trigger_ending(e10)
            if any(d.health <= 0 for d in all_dragons):
                if input(
                        f"{C_GREEN}Вы уже победили дракона! Завершить игру концовкой 'Победа'? (1 - Да, 0 - Нет): {C_RESET}").strip() == '1':
                    trigger_ending(e2)

            input(f"\n{C_GRAY}[Нажмите Enter, чтобы вернуться в город...]{C_RESET}")