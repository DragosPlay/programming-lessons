class SpaceShip:
    def __init__(self,
                 fuel:float = 100,
                 health:float = 100,
                 speed:float = 0):
        self.fuel = fuel
        self.health = health
        self.speed = speed

    def gaz(self, znach):
        if self.fuel > 0:
            self.speed += znach
            self.fuel -= 4
            print(f'Текущая скорость {self.speed}, топлива осталось {self.fuel}')
        else:
            print(f'Нет топлива для газа(')

class CrewMember:

class Mision:

