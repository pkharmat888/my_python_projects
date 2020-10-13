# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1600, 900)


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def head(point):
    radius = 70
    color = sd.random_color()
    sd.circle(center_position=point, radius=radius, color=color, width=1)


def eye(point):
    radius = 8
    color = sd.random_color()
    sd.circle(center_position=point, radius=radius, color=color, width=1)


def smile(points):
    color = sd.random_color()
    sd.lines(points, color=color)


def smile_drawing(x, y):
    point_for_head = sd.get_point(x, y)
    point_for_right_eye = sd.get_point(x + 30, y + 20)
    point_for_left_eye = sd.get_point(x - 30, y + 20)
    points_for_smile = [sd.get_point(x + 40, y - 20), sd.get_point(x + 20, y - 40), sd.get_point(x - 20, y - 40),
                        sd.get_point(x - 40, y - 20)]
    head(point_for_head)
    eye(point_for_right_eye)
    eye(point_for_left_eye)
    smile(points_for_smile)


for _ in range(100):
    point = sd.random_point()
    x = point.x
    y = point.y
    smile_drawing(x, y)

sd.pause()
