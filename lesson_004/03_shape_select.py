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
    step = 120
    for tilt_angle in range(0, 360 - step, step):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw(color=figure_color)
        start_point = v.end_point
    sd.line(start_point=v.end_point, end_point=point, color=figure_color)


def square(point, figure_color, angle=0, length=200):
    start_point = point
    step = 90
    for tilt_angle in range(0, 360 - step, step):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw(color=figure_color)
        start_point = v.end_point
    sd.line(start_point=v.end_point, end_point=point, color=figure_color)


def pentagon(point, figure_color, angle=0, length=175):
    start_point = point
    step = 72
    for tilt_angle in range(0, 360 - step, step):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw(color=figure_color)
        start_point = v.end_point
    sd.line(start_point=v.end_point, end_point=point, color=figure_color)


def hexagon(point, figure_color, angle=0, length=150):
    start_point = point
    step = 60
    for tilt_angle in range(0, 360 - step, step):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw(color=figure_color)
        start_point = v.end_point
    sd.line(start_point=v.end_point, end_point=point, color=figure_color)


central_point = sd.get_point(600, 500)

colors = {
    '0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
    '1': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
    '2': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
    '3': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
    '4': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
    '5': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
    '6': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}
}

print('Возможные цвета: ')
for t, i in colors.items():
    print(t, ':', i['color_name'])

input_color = input('Введите желаемый цвет: ')

while input_color not in colors:
    print('Вы ввели некорректный номер !')
    input_color = input('Введите желаемый цвет: ')
else:
    number_of_color = input_color
    color = colors[input_color]

figures = {
    '0': {'figure_name': 'Треугольник', 'fg_name': triangle},
    '1': {'figure_name': 'Квадрат', 'fg_name': square},
    '2': {'figure_name': 'Пятиугольник', 'fg_name': pentagon},
    '3': {'figure_name': 'Шестиугольник', 'fg_name': hexagon}
}

print('Возможные фигуры: ')
for q, w in figures.items():
    print(q, ':', w['figure_name'])

input_figure = input('Введите желаемую фигуру: ')

while input_figure not in figures:
    print('Вы ввели некорректный номер !')
    input_figure = input('Введите желаемую фигуру: ')
else:
    number_of_figure = input_figure
    color = colors[input_color]['sd_name']
    figures[number_of_figure]['fg_name'](point=central_point, figure_color=color, angle=30, length=200)
sd.pause()
