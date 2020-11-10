# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 1000)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def triangle(point, figure_color, angle=0, length=200):
    start_point = point
    for tilt_angle in range(0, 360, 120):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length, width=2)
        v.draw(color=figure_color)
        start_point = v.end_point


def square(point, figure_color, angle=0, length=200):
    start_point = point
    for tilt_angle in range(0, 360, 90):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw(color=figure_color)
        start_point = v.end_point


def pentagon(point, figure_color, angle=0, length=175):
    start_point = point
    for tilt_angle in range(0, 360, 72):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw(color=figure_color)
        start_point = v.end_point


def hexagon(point, figure_color, angle=0, length=150):
    start_point = point
    for tilt_angle in range(0, 360, 60):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw(color=figure_color)
        start_point = v.end_point


point_triangle = sd.get_point(250, 100)
point_square = sd.get_point(750, 100)
point_pentagon = sd.get_point(250, 550)
point_hexagon = sd.get_point(750, 550)

colors = {
    0: sd.COLOR_RED,
    1: sd.COLOR_ORANGE,
    2: sd.COLOR_YELLOW,
    3: sd.COLOR_GREEN,
    4: sd.COLOR_CYAN,
    5: sd.COLOR_BLUE,
    6: sd.COLOR_PURPLE
}

print("""Возможные цвета:
            0 : red
            1 : orange
            2 : yellow
            3 : green
            4 : cyan
            5 : blue
            6 : purple""")

user_input = int(input('Введите желаемый цвет: '))

while user_input not in colors:
    print('Вы ввели некорректный номер !')
    user_input = int(input('Введите желаемый цвет: '))
else:
    number_of_color = int(user_input)
    color = colors[user_input]

    triangle(point=point_triangle, figure_color=color, angle=30, length=200)

    square(point=point_square, figure_color=color, angle=30, length=200)

    pentagon(point=point_pentagon, figure_color=color, angle=30, length=175)

    hexagon(point=point_hexagon, figure_color=color, angle=45, length=150)

sd.pause()
