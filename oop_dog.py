class Dogs:
    def __init__(
            self,
            breed:str = 'basic dog',
            degree_of_barking:int = 10,
            coat_length:int = 10,
            prettiness:int = 10,
            affectionate:int = 10,
            is_this_a_taxi:bool = False  # такса или нет
    ):
        self.breed = breed
        self.degree_of_barking = degree_of_barking
        self.coat_length = coat_length
        self.prettiness = prettiness
        self.affectionate = affectionate
        self.is_this_a_taxi = is_this_a_taxi

    def info(self):
        print('breed:', self.breed)
        print('degree_of_barking:', self.degree_of_barking)
        print('coat_length:', self.coat_length)
        print('prettiness:', self.prettiness)
        print('affectionate:', self.affectionate)
        print('is_this_a_taxi:', self.is_this_a_taxi)

    def taxi(self):
        if self.is_this_a_taxi:
            print('Да, это представитель редкого класса немецкого такси!!!')
        else:
            print('О нет, эта собака не является таксой')

    def pet(self):
        if self.affectionate >= 6:
            print('Вы успешно погладили собаку, она довальна')
        elif self.affectionate >= 3:
            print('Собака косилась на вас, пока вы её гладили')
        else:
            print('Рука осталась косточкой для собаки')

        if self.coat_length >= 6:
            print('На руке осталась шерстянная перчатка')


german_shepherd = Dogs(
    breed = 'German shepherd',
    degree_of_barking = 7,
    coat_length = 6,
    prettiness = 10,
    affectionate = 2,  # так то 10, а для примеру пусть будет 2 🙂‍↕️
    is_this_a_taxi = False
)

taxi = Dogs(
    breed = 'Dachshund',
    degree_of_barking = 4,
    coat_length = 1,
    prettiness = 10,
    affectionate = 10,
    is_this_a_taxi = True
)

german_shepherd.pet()
print(' ')
taxi.taxi()