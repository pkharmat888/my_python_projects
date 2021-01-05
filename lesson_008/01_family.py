# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class Peoples:

    total_food_eaten = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return 'Я {}, моя сытость {}, моя радость {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.house_food > 10:
            Peoples.total_food_eaten += 10
            self.fullness += 10
            self.house.house_food -= 10
            cprint('{} покушал(-а)'.format(self.name), color='yellow')

    def get_home(self, house):
        self.house = house
        self.house.list_of_inhabitants.append(self.name)
        print('{}, заселился(-ась) в дом'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер(ла)'.format(self.name), color='red')
            return False
        elif self.happiness <= 10:
            cprint('{} умер(ла) от депрессии'.format(self.name), color='red')
            return False
        elif self.fullness <= 20:
            self.eat()
            return False
        elif self.house.house_dirt > 90:
            self.happiness -= 10
        return True


class House:

    def __init__(self):
        self.house_money = 100
        self.house_food = 50
        self.house_dirt = 0
        self.peoples = None
        self.list_of_inhabitants = []

    def __str__(self):
        return 'В доме осталось {} денег, {} еды. Дома есть грязь в колличестве {}. В доме живут {}'.format(
            self.house_money, self.house_food, self.house_dirt, self.list_of_inhabitants
        )


class Husband(Peoples):

    total_money_earned = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        res = super().act()
        if res:
            if self.happiness < 20:
                self.gaming()
            elif self.house.house_money < 360:
                self.work()

    def eat(self):
        super().eat()

    def work(self):
        self.house.house_money += 150
        Husband.total_money_earned += 150
        self.fullness -= 10
        cprint('{} сходил на работу'.format(self.name), color='magenta')

    def gaming(self):
        if self.happiness <= 30:
            self.happiness += 20
            self.fullness -= 10
            cprint('{} поиграл в WOT'.format(self.name), color='green')


class Wife(Peoples):

    total_coats_bought = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        res = super().act()
        if res:
            if self.house.house_food < 50:
                self.shopping()
            elif self.house.house_dirt >= 100:
                self.clean_house()
            else:
                self.buy_fur_coat()

    def eat(self):
        super().eat()

    def shopping(self):
        if self.house.house_money > 10:
            self.house.house_food += 30
            self.house.house_money -= 30
            self.fullness -= 10
            cprint('{} сходила в магазин и купила еды'.format(self.name), color='green')

    def buy_fur_coat(self):
        if self.house.house_money > 400:
            Wife.total_coats_bought += 1
            self.happiness += 60
            self.house.house_money -= 350
            self.fullness -= 10
            cprint('{} купила новую шубу'.format(self.name), color='blue')

    def clean_house(self):
        self.house.house_dirt -= 100
        self.fullness -= 10
        cprint('{} убралась в доме'.format(self.name), color='green')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

serge.get_home(house=home)
masha.get_home(house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.house_dirt += 5
    serge.act()
    masha.act()
    cprint('================== В конце дня ==================', color='yellow')
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')


cprint('================== В конце года ==================', color='magenta')
cprint('Всего было заработано денег {}'.format(Husband.total_money_earned), color='blue')
cprint('Всего было съедено {} едениц еды'.format(Peoples.total_food_eaten), color='magenta')
cprint('Всего было шуб куплено {} едениц'.format(Wife.total_coats_bought), color='yellow')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Peoples):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()  # TODO а почему тут не проверяется результат супер акта? (как у родителей например)
        if self.fullness < 30:
            self.eat()
        elif self.house.house_dirt > 90:
            self.happiness = 100
        else:
            self.sleep()

    def eat(self):
        super().eat()

    def sleep(self):
        self.fullness -= 10


# после реализации второй части - отдать на проверку учителем две ветки
# TODO Тут должен быть код с запуском жизни с ребенком

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
