# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

x1 = 50
x2 = 350

for color in rainbow_colors:
    start_point = sd.get_point(x1, 50)
    end_point = sd.get_point(x2, 450)
    x1 += 5
    x2 += 5
    sd.line(start_point, end_point, color)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

sd.resolution = (1200, 600)


def bubble(point, step):
    radius = 500
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for color in rainbow_colors:
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=5)


point = sd.get_point(600, -200)
bubble(point, 5)

sd.pause()
