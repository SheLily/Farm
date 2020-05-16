class animal(object):
    def __init__(self, name, weight, voice, type_animal):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.starv = True
        self.type_animal = type_animal

    def get_voice(self):
        print(self.voice)

    def eat(self):
        if self.starv:
            print(f'{self.type_animal} {self.name} покушало и довольно')
            self.startv = False
        else:
            print(f'{self.type_animal} {self.name} уже сыто')


class mammals(animal):
    def __init__(self, name, weight, voice):
        super(mammals, self).__init__(name, weight, voice, 'Зверь')
        self.milk = 10

    # Переопределение метода eat
    def eat(self):
        if self.starv:
            print(f'{self.type_animal} {self.name} покушал и доволен')
            self.startv = False
        else:
            print(f'{self.type_animal} {self.name} нагулял молока')
            self.milk += 10

    # Дойка
    def milking(self):
        if self.milk > 0:
            print(f'{self.type_animal} {self.name} подоен')
            self.milk = 0
        else:
            print(f'{self.type_animal} {self.name} уже был подоен')

        # птицы


class avifauna(animal):
    def __init__(self, name, weight, voice):
        super(avifauna, self).__init__(name, weight, voice, 'Птица')
        self.eggs = 1

    def eat(self):
        if self.starv:
            print(f'{self.type_animal} {self.name} покушала и довольна')
            self.startv = False
        else:
            print(f'{self.type_animal} {self.name} снесла яйцо')
            self.eggs += 1

    def collect(self):
        if self.eggs > 0:
            print(f'У {self.type_animal} {self.name} собрали яйца')
            self.eggs = 0
        else:
            print(f'У {self.type_animal} {self.name} нет яиц')


class goose(avifauna):
    def __init__(self, name, weight):
        super(goose, self).__init__(name, weight, 'Го-го-го')
        self.type_animal = 'Гусь'


class hen(avifauna):
    def __init__(self, name, weight):
        super(hen, self).__init__(name, weight, 'Куд-кудах')
        self.type_animal = 'Курица'


class duck(avifauna):
    def __init__(self, name, weight):
        super(duck, self).__init__(name, weight, 'Кря-кря')
        self.type_animal = 'Утка'


class cow(mammals):
    def __init__(self, name, weight):
        super(cow, self).__init__(name, weight, 'Му-му')
        self.type_animal = 'Корова'


class sheep(mammals):
    def __init__(self, name, weight):
        super(sheep, self).__init__(name, weight, 'Беееее')
        self.type_animal = 'Овца'
        self.wool = 10

    def shearing(self):
        if self.wool > 0:
            print(f'{self.type_animal} {self.name} подстрижена')
            self.wool = 0
        else:
            print(f'{self.type_animal} {self.name} была подстрижена ранее')


class goat(mammals):
    def __init__(self, name, weight):
        super(goat, self).__init__(name, weight, 'Меее')
        self.type_animal = 'Коза'


a = [
    goose('Серый', 10),
    goose('Белый', 11),
    cow('Манька', 450),
    sheep('Барашек', 150),
    sheep('Кудрявый', 145),
    hen('Ко-ко', 8),
    hen('Кукареку', 9),
    goat('Рога', 160),
    goat('Копыта', 163),
    duck('Кряква', 8),

]

for i in a:
    i.eat()
    if isinstance(i, mammals):
        i.milking()
    if isinstance(i, sheep):
        i.shearing()
    if isinstance(i, avifauna):
        i.collect()

weight = 0
for i in a:
    weight += i.weight

# weight = sum([i.weight for i in a])

print(f'Суммарный вес всех животных: {weight}')

max_weight = max(a, key=lambda x: x.weight)
print(f'Самый большой вес имеет {max_weight.type_animal} {max_weight.name} с весом {max_weight.weight}')