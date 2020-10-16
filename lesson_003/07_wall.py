# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1600, 900)

color = sd.COLOR_DARK_ORANGE

for row, y in enumerate(range(50, 950, 50)):
    x = -50 if row % 2 else 0
    for x in range(x, 1700, 100):
        point1 = sd.get_point(x - 100, y - 50)
        point2 = sd.get_point(x, y)
        sd.rectangle(left_bottom=point1, right_top=point2, color=color, width=2)

sd.pause()
#зачёт!