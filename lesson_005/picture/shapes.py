# -*- coding: utf-8 -*-

import simple_draw as sd


def figures(point, figure_color, angle, length, step, width):
    start_point = point
    step = step
    for tilt_angle in range(0, 360 - step, step):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length, width=width)
        v.draw(color=figure_color)
        start_point = v.end_point
    sd.line(start_point=v.end_point, end_point=point, color=figure_color, width=width)


def triangle(point, figure_color, angle=0, length=200, width=1):
    step = 120
    figures(point, figure_color, angle, length, step, width)


def square(point, figure_color, angle=0, length=200, width=1):
    step = 90
    figures(point, figure_color, angle, length, step, width)


def pentagon(point, figure_color, angle=0, length=175, width=1):
    step = 72
    figures(point, figure_color, angle, length, step, width)


def hexagon(point, figure_color, angle=0, length=150, width=1):
    step = 60
    figures(point, figure_color, angle, length, step, width)


