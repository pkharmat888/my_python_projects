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


class Man:
    total_food_eaten = 0
    total_pets = []
    total_pets_died = []

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.pet = None

    # def __str__(self):
    #     return 'Я {}, моя сытость {}, моя радость {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.house_food > 10:
            Man.total_food_eaten += 30
            self.fullness += 30
            self.house.house_food -= 30
            # cprint('{} покушал(-а)'.format(self.name), color='yellow')

    def get_home(self, house):
        self.house = house
        self.house.list_of_inhabitants.append(self)
        # print('{}, заселился(-ась) в дом'.format(self.name))

    def get_the_cat(self, pet):
        self.pet = pet
        self.pet.house = self.house
        self.total_pets.append(self.pet.name)
        # cprint('{} подобрал(-а) кота {}'.format(self.name, self.pet.name), color='cyan')

    def buy_cat_food(self):
        if self.house.house_money > 10:
            self.house.cat_food += 10
            self.house.house_money -= 10
            self.fullness -= 10
            # cprint('{} купил(-а) кошачьей еды'.format(self.name), color='green')

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        # cprint('{} погладил(-а) кота'.format(self.name), color='green')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер(ла)'.format(self.name), color='red')
            if isinstance(self, (Husband, Wife, Child)):
                for number, obj in enumerate(self.house.list_of_inhabitants):
                    if self == obj:
                        del self.house.list_of_inhabitants[number]
            return False
        elif self.happiness <= 10:
            cprint('{} умер(ла) от депрессии'.format(self.name), color='red')
            if isinstance(self, (Husband, Wife, Child)):
                for number, obj in enumerate(self.house.list_of_inhabitants):
                    if self == obj:
                        del self.house.list_of_inhabitants[number]
            return False
        elif self.fullness <= 10:
            self.eat()
            return False
        elif self.happiness <= 15:
            self.pet_the_cat()
            # cprint('{} погладил(-а) кота {}'.format(self.name, self.pet.name))
            return False
        elif self.house.house_dirt >= 90:
            self.happiness -= 10
        return True


class House:

    def __init__(self):
        self.house_money = 100
        self.house_food = 50
        self.cat_food = 30
        self.house_dirt = 0
        self.peoples = None
        self.list_of_inhabitants = []

    # def __str__(self):
    #     # return 'В доме осталось {} денег, {} еды. Дома есть грязь в колличестве {}. В доме живут {}\nКошачьей еды {}' \
    #         .format(
    #         self.house_money, self.house_food, self.house_dirt, self.list_of_inhabitants, self.cat_food
    #     )


class Husband(Man):
    total_money_earned = 0

    def __init__(self, name):
        super().__init__(name=name)
        self.salary = 0

    def __str__(self):
        return super().__str__()

    def get_salary(self, salary):
        self.salary = salary

    def act(self):
        res = super().act()
        if res:
            if self.happiness <= 20:
                self.gaming()
            elif self.house.house_money < 1500:
                self.work()
            elif self.house.cat_food <= 10:
                self.buy_cat_food()

    def eat(self):
        super().eat()

    def work(self):
        self.house.house_money += self.salary
        Husband.total_money_earned += self.salary
        self.fullness -= 10
        # cprint('{} сходил на работу'.format(self.name), color='magenta')

    def gaming(self):
        if self.happiness <= 30:
            self.happiness += 20
            self.fullness -= 10
            # cprint('{} поиграл в WOT'.format(self.name), color='green')


class Wife(Man):
    total_coats_bought = 0

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        res = super().act()
        if res:
            if self.happiness <= 20:
                self.buy_fur_coat()
            elif self.house.house_food <= 50:
                self.shopping()
            elif self.house.house_dirt >= 50:
                self.clean_house()

    def eat(self):
        super().eat()

    def shopping(self):
        if self.house.house_money > 10:
            self.house.house_food += 30
            self.house.house_money -= 30
            self.fullness -= 10
            # cprint('{} сходила в магазин и купила еды'.format(self.name), color='green')

    def buy_fur_coat(self):
        if self.house.house_money >= 350:
            Wife.total_coats_bought += 1
            self.happiness += 60
            self.house.house_money -= 350
            self.fullness -= 10
            # cprint('{} купила новую шубу'.format(self.name), color='blue')

    def clean_house(self):
        self.house.house_dirt -= 100
        self.fullness -= 10
        # cprint('{} убралась в доме'.format(self.name), color='green')


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    # def __str__(self):
    #     return 'Я - {}. Моя сытость {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            if len(Man.total_pets) != 0:
                cprint('Кот {} умер'.format(self.name), color='red')
                Man.total_pets_died.append(self.name)
                for name in Man.total_pets:
                    if name == self.name:
                        Man.total_pets.remove(name)
                return
        dice = randint(0, 8)
        if self.fullness <= 10:
            self.eat()
        elif dice == 3:
            self.soil()
        elif self.fullness >= 50:
            self.sleep()

    def eat(self):
        if self.house.cat_food >= 10:
            # cprint('Кот {} покушал(-а)'.format(self.name), color='blue')
            self.fullness += 20
            self.house.cat_food -= 10

    def sleep(self):
        self.fullness -= 10
        # cprint('Кот/Кошка {} поспала'.format(self.name), color='blue')

    def soil(self):
        self.fullness -= 10
        self.house.house_dirt += 5
        # cprint('{} подрал(-а) обои'.format(self.name), color='blue')


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        res = super().act()
        if res:
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
        # cprint('Ребенок {} поспал(-а)'.format(self.name), color='blue')


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# murka = Cat(name='Мурка')
#
# serge.get_home(house=home)
# masha.get_home(house=home)
#
# serge.get_the_cat(pet=murka)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.house_dirt += 5
#     serge.act()
#     masha.act()
#     murka.act()
#     cprint('================== В конце дня ==================', color='yellow')
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(murka, color='cyan')
#     cprint(home, color='cyan')
#
# cprint('================== В конце года ==================', color='magenta')
# cprint('Всего было заработано денег {}'.format(Husband.total_money_earned), color='blue')
# cprint('Всего было съедено {} едениц еды'.format(Peoples.total_food_eaten), color='magenta')
# cprint('Всего было шуб куплено {} едениц'.format(Wife.total_coats_bought), color='yellow')


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


class Simulation:
    counter_of_money_incidents = 0
    counter_of_food_incidents = 0
    cat_names = ['Мурка', 'Маруся', 'Гарфилд', 'Сайлем', 'Кот Василий', 'Барсик']
    cats = []

    def __init__(self, money_incidents, food_incidents):
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents
        self.home = None
        self.salary = 0

    def experiment(self, salary):
        self.salary = salary
        home = House()
        self.home = home

        self.serge = Husband(name='Сережа')
        self.masha = Wife(name='Маша')
        self.sasha = Child(name='Саша')
        self.serge.get_salary(salary=self.salary)
        self.serge.get_home(house=self.home)
        self.masha.get_home(house=self.home)
        self.sasha.get_home(house=self.home)

        for name in Simulation.cat_names:
            Simulation.cats.append(Cat(name=name))

        for cat in Simulation.cats:
            self.serge.get_the_cat(pet=cat)

        self.set_of_inhabitants = set(self.home.list_of_inhabitants)

        cprint('================== Начало ==================', color='red')
        # cprint(home, color='cyan')
        for day in range(365):
            # cprint('================== День {} =================='.format(day + 1), color='red')
            self.money_incident(day=day)
            self.food_incident(day=day)
            home.house_dirt += 5
            if len(self.home.list_of_inhabitants) != len(self.set_of_inhabitants):
                print('Кто-то из людей умер, прокормить котов нельзя')
                break
            if len(Man.total_pets) == 0:
                print('Все коты умерли')
                break
            self.serge.act()
            self.masha.act()
            self.sasha.act()
            for self.cat in Simulation.cats:
                self.cat.act()

            # cprint('================== В конце дня ==================', color='yellow')
            # cprint(self.serge, color='cyan')
            # cprint(self.masha, color='cyan')
            # cprint(self.sasha, color='cyan')
            # for self.cat in Simulation.cats:
            #     cprint(self.cat, color='cyan')
            # cprint(home, color='cyan')
        if len(self.home.list_of_inhabitants) == len(self.set_of_inhabitants):
            cprint('================== В конце года ==================', color='magenta')
            cprint('Всего было заработано денег {}'.format(Husband.total_money_earned), color='blue')
            cprint('Всего было съедено {} едениц еды'.format(Man.total_food_eaten), color='magenta')
            cprint('Всего было шуб куплено {} едениц'.format(Wife.total_coats_bought), color='yellow')
            cprint('Всего котов в семье {}'.format(len(Man.total_pets)), color='magenta')
            cprint('Всего котов умерло {}'.format(len(Man.total_pets_died)), color='magenta')
            how_mutch_cats = (len(Man.total_pets))
            return how_mutch_cats

    def money_incident(self, day):
        if self.counter_of_money_incidents < self.money_incidents:
            random_money_incident_day = randint(day, 365)
            if random_money_incident_day == day:
                if self.home.house_money >= 1:
                    self.counter_of_money_incidents += 1
                    self.home.house_money /= 2
                    cprint('Пропало денег {} едениц'.format(int(self.home.house_money)), color='red')
                    cprint('Из тумбочки пропала половина денег', color='red')

    def food_incident(self, day):
        if self.counter_of_food_incidents < self.food_incidents:
            random_food_incident_day = randint(day, 365)
            if random_food_incident_day == day:
                if self.home.house_food >= 1:
                    self.counter_of_food_incidents += 1
                    self.home.house_food /= 2
                    cprint('Пропало еды {} едениц'.format(int(self.home.house_food)), color='red')
                    cprint('Из холодильника исчезло половина еды', color='red')


food_incidents = 0
money_incidents = 0

for salary in range(50, 401, 50):
    life = Simulation(money_incidents=money_incidents, food_incidents=food_incidents)
    food_incidents += 1
    money_incidents += 1
    max_cats = life.experiment(salary=salary)
    print('Случайных пропаж денег было - {}\nСлучайных пропаж еды было - {}'.format(money_incidents, food_incidents))
    print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
    Simulation.cats.clear()
    Man.total_pets.clear()
Man.total_food_eaten = 0
Husband.total_money_earned = 0
Wife.total_coats_bought = 0

# food_incidents = 6
# money_incidents = 6
# salary = 150
# life = Simulation(money_incidents=money_incidents, food_incidents=food_incidents)
# max_cats = life.experiment(salary=salary)
# print('Случайных пропаж денег было - {}\nСлучайных пропаж еды было - {}'.format(money_incidents, food_incidents))
# print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачёт!