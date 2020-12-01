# -*- coding: utf-8 -*-

import simple_draw as sd


def wall_draw(x_start_point, x_endpoint, y_start_point, y_endpoint, color_of_wall):
    for row, y in enumerate(range(y_start_point, y_endpoint+1, 25)):
        x = (x_start_point-25) if row % 2 else x_start_point
        for x in range(x, x_endpoint, 50):
            point1 = sd.get_point(x - 50, y - 25)
            point2 = sd.get_point(x, y)
            sd.rectangle(left_bottom=point1, right_top=point2, color=color_of_wall, width=2)
