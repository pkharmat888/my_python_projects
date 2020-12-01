# -*- coding: utf-8 -*-


import simple_draw as sd


def head(point, color=sd.COLOR_YELLOW):
    radius = 70
    sd.circle(center_position=point, radius=radius, color=color, width=3)


def eye(point, color=sd.COLOR_YELLOW, width=3):
    radius = 8
    sd.circle(center_position=point, radius=radius, color=color, width=width)


def smile(points, color=sd.COLOR_YELLOW):
    sd.lines(points, color=color, width=3)


def smile_draw(x, y):
    point_for_head = sd.get_point(x, y)
    point_for_right_eye = sd.get_point(x + 30, y + 20)
    point_for_left_eye = sd.get_point(x - 30, y + 20)
    points_for_smile = [sd.get_point(x + 40, y - 20), sd.get_point(x + 20, y - 40), sd.get_point(x - 20, y - 40),
                        sd.get_point(x - 40, y - 20)]
    head(point_for_head)
    eye(point_for_right_eye)
    eye(point_for_left_eye)
    smile(points_for_smile)


def one_eye_smile_draw(x, y, color=sd.COLOR_YELLOW):
    point_for_head = sd.get_point(x, y)
    point_for_right_eye = sd.get_point(x + 30, y + 20)
    points_for_smile = [sd.get_point(x + 40, y - 20), sd.get_point(x + 20, y - 40), sd.get_point(x - 20, y - 40),
                        sd.get_point(x - 40, y - 20)]
    head(point_for_head, color=color)
    eye(point_for_right_eye, color=color)
    smile(points_for_smile, color=color)


def eye_blinking(x, y, color=sd.COLOR_YELLOW):
    for width in range(0, 10):
        eye(sd.get_point(x, y), color=color, width=width)
