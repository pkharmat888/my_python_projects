# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(300, 300)


# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position = point, radius = radius, width=2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=sd.random_color(), width=2)


# point = sd.get_point(300, 300)
# bubble(point, 5)


# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 300)
#     bubble(point, 5)


# for y in range(100, 301, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point, step)

sd.pause()
