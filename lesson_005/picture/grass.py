# -*- coding: utf-8 -*-

import simple_draw as sd


def grass_draw(start_point, x_end_point, length=50):
    step = 1
    points = [start_point.x, start_point.y]
    while start_point.x < x_end_point:
        angle = 90
        angle += sd.random_number(-30, 30)
        grass_branch = sd.get_vector(start_point=start_point, angle=angle, length=length)
        points[0] += step
        start_point = sd.get_point(points[0], points[1])
        grass_branch.draw(color=sd.COLOR_DARK_GREEN)
