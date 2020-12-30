# -*- coding: utf-8 -*-
import random as rd
import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    __list_of_flakes = []
    __list_of_fallen_flakes = []

    def __init__(self):
        self.x = rd.randint(0, 1800)
        self.y = rd.randint(800, 900)
        self.length = rd.randint(10, 50)

    def snowflakes_creating(self):
        self.x = self.x
        self.y = self.y
        self.length = self.length

    def clear_previous_picture(self):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=sd.background_color)

    def move(self):
        self.x += rd.randint(-30, 30)
        self.y -= rd.randint(5, 15)

    def draw(self):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        if self.y > 30:
            return self.y

    def get_flakes(self, count):
        for flake in range(count):
            self.__list_of_flakes.append(Snowflake())
        return self.__list_of_flakes

    def get_fallen_flakes(self):
        if not self.can_fall():
            for flake in self.__list_of_flakes:
                self.__list_of_fallen_flakes.append(flake)
        return len(self.__list_of_fallen_flakes)

    def append_flakes(self, count):
        self.__list_of_flakes.clear()
        self.__list_of_fallen_flakes.clear()
        for i in range(count):
            self.__list_of_flakes.append(Snowflake())
        return self.__list_of_flakes


sd.resolution = (1800, 1000)

# flake = Snowflake()

# while True:
#     flake.snowflakes_creating()
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = Snowflake.get_flakes(count=20)  # создать список снежинок

flakes = Snowflake().get_flakes(count=10)


while True:
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = flake.get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        flake.append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break

sd.pause()
