# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def figures(point, angle, length, step):
        # TODO внутри этой функции надо использовать 'n' для расчёта step
        # TODO тогда мы сможем просто убрать функции обертки (это будет замена им)
        start_point = point
        step = step
        for tilt_angle in range(0, 360 - step, step):
            v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
            v.draw()
            start_point = v.end_point
        sd.line(start_point=v.end_point, end_point=point)

    if n == 3:
        def triangle(point, angle=0, length=200):
            step = 120
            figures(point, angle, length, step)

        return triangle

    if n == 4:
        def square(point, angle=0, length=200):
            step = 90
            figures(point, angle, length, step)

        return square

    if n == 5:
        def pentagon(point, angle=0, length=175):
            step = 72
            figures(point, angle, length, step)

        return pentagon

    if n == 6:
        def hexagon(point, angle=0, length=150):
            step = 60
            figures(point, angle, length, step)

        return hexagon


sd.resolution = (1200, 1000)

point_triangle = sd.get_point(250, 100)
point_square = sd.get_point(750, 100)
point_pentagon = sd.get_point(250, 550)
point_hexagon = sd.get_point(750, 550)

draw_triangle = get_polygon(n=3)
draw_square = get_polygon(n=4)
draw_pentagon = get_polygon(n=5)
draw_hexagon = get_polygon(n=6)

draw_triangle(point=point_triangle, angle=13, length=200)
draw_square(point=point_square, angle=13, length=200)
draw_pentagon(point=point_pentagon, angle=13, length=175)
draw_hexagon(point=point_hexagon, angle=13, length=150)


sd.pause()
