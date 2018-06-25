class Animal:
    height = 'средний'
    coating = 'шерсть'
    food = 'трава'
    color = []
    voice = ''
    product = []
    average_speed = 3  # км/ч

    def presentation(self, name):
        self.name = name
        print('Я', name, '— домашнее животное')

    def make_some_noise(self, voice):
        self.voice = voice
        print(voice)

    def speed(self, average_speed):
        self.average_speed = average_speed
        print('Я пробегу за час', average_speed, 'километра')


class Bird(Animal):
    height = 'маленький'
    fly_speed = 0
    coating = 'перья'
    food = 'зерно'
    product = ['мясо', 'яйца']
    legs = ''
    def can_i_fly(self, fly_speed):
        if fly_speed > 0:
            self.fly_speed = fly_speed
            print('А еще я могу летать со скоростью', fly_speed, 'км/ч')
        else:
            print('Я не умею летать')


cow = Animal()
cow.height = 'высокий'
cow.product = ['молоко', 'мясо']
cow.color = ['черный', 'пятнистый', 'коричневый']
cow.presentation('корова')
cow.make_some_noise('Муууууууу')
cow.speed(3)

goat = Animal()
goat.height = 'средний'
goat.product = ['молоко']
goat.color = ['белый', 'черный']
goat.presentation('коза')
goat.make_some_noise('Меееее')
goat.speed(4)

sheep = Animal()
sheep.height = 'средний'
sheep.product = ['шерсть', 'молоко']
sheep.color = ['белый', 'черный']
sheep.presentation('овца')
sheep.make_some_noise('Бееее')
sheep.speed(5)

pig = Animal()
pig.height = 'средний'
pig.product = ['мясо']
pig.color = ['белый', 'черный']
pig.food = 'все, что можно съесть'
pig.presentation('свинья')
pig.make_some_noise('Хрю-хрю')
pig.speed(2)

duck = Bird()
duck.presentation('утка')
duck.color = ['серый', 'черный', 'коричневый']
duck.legs = 'с перепонками'
duck.make_some_noise('Кря-кря')
duck.speed(2)
duck.can_i_fly(6)

chicken = Bird()
chicken.presentation('курица')
chicken.color = ['белый', 'черный', 'коричневый']
chicken.legs = 'без перепонок'
chicken.make_some_noise('куд-ку-да')
chicken.speed(3)
chicken.can_i_fly(0)

goose = Bird()
goose.presentation('Гусь')
goose.product = ['мясо']
goose.color = ['белый', 'черный', 'коричневый']
goose.legs = 'без перепонок'
goose.make_some_noise('Гагагагага')
goose.speed(2)
goose.can_i_fly(7)
