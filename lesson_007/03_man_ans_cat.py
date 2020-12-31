# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.pet = None
        self.pets = []

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def get_the_cat(self, pet):
        self.pet = pet
        self.pet.house = self.house
        self.pets.append(self.pet)
        cprint('{} подобрал кота'.format(self.name), color='cyan')

    def buy_cat_food(self):
        self.house.cat_food += 40
        self.house.money -= 50
        cprint('{} купил кошачей еды'.format(self.name), color='cyan')

    def clean_in_the_house(self):
        if self.house.dirt > 100:
            self.house.dirt -= 100
            self.fullness -= 20
            cprint('{} убрался в доме'.format(self.name), color='cyan')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 15:
            self.buy_cat_food()
        elif self.house.dirt > 100:
            self.clean_in_the_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}\nВ доме осталось {} кошачей еды\nВ доме {} грязи'.format(
            self.food, self.money, self.cat_food, self.dirt
        )


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}. Моя сытость {}'.format(self.name, self.fullness)

    def cat_eat(self):
        if self.house.cat_food > 10:
            self.fullness += 20
            self.house.cat_food -= 10
            cprint('{} покушал'.format(self.name), color='cyan')

    def cat_sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='magenta')

    def cat_scratching_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('{} подрал обои'.format(self.name), color='blue')

    def cat_play(self):
        self.fullness -= 15
        self.house.dirt += 15
        cprint('{} поигрался'.format(self.name), color='green')

    def cat_walk(self):
        self.fullness -= 10
        cprint('{} погулял'.format(self.name), color='yellow')

    def cat_act(self):
        if self.fullness <= 0:
            cprint('Кот умер...', color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.cat_eat()
        elif dice == 1:
            self.cat_walk()
        elif dice == 2:
            self.cat_play()
        elif dice == 3:
            self.cat_sleep()
        else:
            self.cat_scratching_wallpaper()


citizen = Man(name='Вася')

my_sweet_home = House()

cats = [
    Cat(name='Мурка'),
    Cat(name='Барсик'),
    Cat(name='Маруся')
]

citizen.go_to_the_house(house=my_sweet_home)

for cat in cats:
    citizen.get_the_cat(pet=cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    citizen.act()
    for cat in cats:
        cat.cat_act()
    print('--- в конце дня ---')
    print(citizen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
#зачёт!