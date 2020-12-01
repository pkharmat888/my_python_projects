# -*- coding: utf-8 -*-

import simple_draw as sd


# Функция для создания углов лучей


def sun_list():
    angles = []
    for angle in range(0, 360, 60):
        angles.append(angle)
    return angles

# Функция для отрисовки солнца


def sun_draw(point, angle_list):
    sd.start_drawing()

    def plus(number):
        return number + 5
    for index, angle in enumerate(angle_list):
        sd.vector(start=point, angle=angle, length=130, color=sd.background_color, width=3)
    angles = list(map(plus, angle_list))
    for index, angle in enumerate(angles):
        sd.vector(start=point, angle=angle, length=130, color=sd.COLOR_YELLOW, width=3)
    sd.circle(center_position=point, radius=70, color=sd.COLOR_YELLOW, width=0)
    sd.finish_drawing()
    return angles
