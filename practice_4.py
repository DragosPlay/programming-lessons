class SpaceShip:
    def __init__(self,
                 fuel:float = 100,
                 health:float = 100,
                 speed:float = 0):
        self.fuel = fuel
        self.health = health
        self.speed = speed

    def gaz(self,
            znach:float = '5'):
        if self.fuel > 0:
            self.speed += znach
            self.fuel -= 4
            print(f'Текущая скорость {self.speed}, топлива осталось {self.fuel}')
        else:
            print(f'Нет топлива для газа(')

class CrewMember:
    def __init__(self,
                 name:str = 'None',
                 health:int = 100,
                 skills:list = [],
                 role:str = 'None'):
        self.name = name
        self.health = health
        self.skills = skills
        self.role = role

class Mission:
    def __init__(self,
                 goal:list = [],
                 resources:dict = {},
                 events:list = []):
        self.goal = goal
        self.resources = resources

