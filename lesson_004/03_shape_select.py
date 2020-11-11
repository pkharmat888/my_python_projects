# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1000)


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


central_point = sd.get_point(600, 500)

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

input_color = int(input('Введите желаемый цвет: '))

while input_color not in colors:
    print('Вы ввели некорректный номер !')
    input_color = int(input('Введите желаемый цвет: '))
else:
    number_of_color = int(input_color)
    color = colors[input_color]

figures = {
    0: triangle,
    1: square,
    2: pentagon,
    3: hexagon
}

# TODO Здесь стоит использовать структуру, схожую с 02
# TODO чтобы в одном месте были и номера выбора, и названия функций, и сами функции
print("""Возможные фигуры:
            0 : Треугольник
            1 : Квадрат
            2 : Пятиугольник
            3 : Шестиугольник""")

input_figure = int(input('Введите желаемую фигуру: '))

while input_figure not in figures:
    print('Вы ввели некорректный номер !')
    input_figure = int(input('Введите желаемую фигуру: '))
else:
    number_of_figure = int(input_figure)
    figures[number_of_figure](point=central_point, figure_color=color, angle=30, length=200)
sd.pause()
