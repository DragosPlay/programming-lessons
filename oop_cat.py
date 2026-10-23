class Cats:
    def __init__(
            self,
            attractiveness:bool = True,
            degree_of_fluffiness:int = 10,
            low_maintenance:int = 10,
            color:str = 'black',
            meowing:bool = True,
            breed:str = 'classic cat',
            whiskers:int = 10,
            ear_shape:int = 10,
    ):
        self.attractiveness = attractiveness
        self.degree_of_fluffiness = degree_of_fluffiness
        self.low_maintenance = low_maintenance
        self.color = color
        self.meowing = meowing
        self.breed = breed
        self.whiskers = whiskers
        self.ear_shape = ear_shape

    def info(self):
        print(f'attractiveness: {self.attractiveness}')
        print(f'degree_of_fluffiness: {self.degree_of_fluffiness}')
        print(f'low_maintenance: {self.low_maintenance}')
        print(f'color: {self.color}')
        print(f'meowing: {self.meowing}')
        print(f'breed: {self.breed}')
        print(f'whiskers: {self.whiskers}')
        print(f'ear_shape: {self.ear_shape}')

main_coon = Cats(
    attractiveness = True,
    degree_of_fluffiness = 9,
    low_maintenance = 9,
    color = 'red-naired',
    meowing = True,
    breed = 'main_coon',
    whiskers = 9,
    ear_shape = 9
)

main_coon.info(S)