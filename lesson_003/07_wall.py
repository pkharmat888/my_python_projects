# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1600, 900)

color = sd.COLOR_DARK_ORANGE


def create_brick(point1, point2, color):
    sd.rectangle(left_bottom=point1, right_top=point2, color=color, width=2)


y1 = -50
y2 = 0

for y in range(0, 18, 1):
    if y % 2 == 0:
        x1 = -50
        x2 = 50
    if y % 2 != 0:
        x1 = 0
        x2 = 100
    y1 += 50
    y2 += 50
    for x in range(0, 18, 1):
        point1 = sd.get_point(x1, y1)
        point2 = sd.get_point(x2, y2)
        x1 += 100
        x2 += 100
        create_brick(point1, point2, color)

sd.pause()
