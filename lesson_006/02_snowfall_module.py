# -*- coding: utf-8 -*-

import simple_draw as sd
from snow_engine import snowflakes_creating, snowflake_draw, snowflakes_step, snowflakes_end_numbers, delete_snowflakes

sd.resolution = (1800, 1000)

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

snowflakes_creating(count_of_snowflakes=10)
while True:
    sd.start_drawing()
    snowflake_draw(color=sd.background_color)
    snowflakes_step()
    snowflake_draw(color=sd.COLOR_WHITE)
    if snowflakes_end_numbers():
        snowflakes_need_create = delete_snowflakes()
        snowflakes_creating(count_of_snowflakes=snowflakes_need_create)
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break

sd.pause()
#зачёт!