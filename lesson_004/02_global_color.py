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


point_triangle = sd.get_point(250, 100)
point_square = sd.get_point(750, 100)
point_pentagon = sd.get_point(250, 550)
point_hexagon = sd.get_point(750, 550)
#  Названия цветов и значения цветов - 2 связанных элемента, которые необходимы нам для
#  работы этого алгоритма.
#  Поэтому в этом случае удобнее создать словарь следующей структуры
#  словарь = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},...}
#  Таким образом для каждого цвета у нас будет свой словарь. И у каждого словаря будут одинаковые ключи
#  'color_name' и 'sd_name'
#  Тогда можно будет легко проверить ввод (user_input in словарь)
#  А если среди ключей есть выбор пользователя - по этому ключу мы получим нужный вложенный словарь
#  А там все ключи одинаковые, можем получить как название цвета, так и sd_цвет
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

user_input = input('Введите желаемый цвет: ')

while user_input not in colors:
    print('Вы ввели некорректный номер !')
    user_input = input('Введите желаемый цвет: ')
else:
    number_of_color = int(user_input)
    color = colors[user_input]['sd_name']

    triangle(point=point_triangle, figure_color=color, angle=30, length=200)

    square(point=point_square, figure_color=color, angle=30, length=200)

    pentagon(point=point_pentagon, figure_color=color, angle=30, length=175)

    hexagon(point=point_hexagon, figure_color=color, angle=45, length=150)

sd.pause()
