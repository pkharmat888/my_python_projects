# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1000)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# Если приблизить итоговую фигуру, нарисованную векторами, будет заметен разрыв между последней стороной
# и начальной точкой.
# Этот разрыв надо убрать.
# Происходит это потому, что вектор рисуется из одной точки, а координаты второй рассчитываются
# Расчёты округляются до целых чисел (тк нельзя нарисовать пол пикселя)
# Из-за этого появляются неточности, которые копятся с каждой стороной и в итоге происходит разрыв.
# В нашем случае решить это можно с помощью sd.line() вместо последнего вектора.


# #  ПРИМЕР:
# #  Первый вариант с расчётом всех 3 углов для треугольника
# start_angle = 20
# step = 120
# print('start 1')
# for cur_angle in range(0, 360, step):  #  Тут будет 3 итерации
#     print(cur_angle, start_angle, cur_angle + start_angle)
# print('end 1')
# print('start 2')
# for cur_angle in range(0, 360 - step, step):  #  Тут 1 итерация убирается (за счёт уменьшения 360 на один шаг)
#     print(cur_angle, start_angle, cur_angle + start_angle)
# print('end 2')


#  Таким образом мы можем 1) Рассчитывать углы при помощи цикла
#  2) Управлять количеством итераций цикла. Это нужно чтобы последнюю сторону нарисовать линией.

#  Попробуйте использовать эти приёмы и реализовать
#  1) Расчёт угла в цикле
#  2) Передачу начального угла (который задан параметром) и угла из цикла в вектор
#  3) Нарисовать последнюю линию при помощи sd.line
#  (или хотя бы для начала не рисовать последнюю сторону вообще)


# def triangle(point, angle=0, length=200):
#     start_point = point
#     step = 120
#     for tilt_angle in range(0, 360 - step, step):
#         v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
#         v.draw()
#         start_point = v.end_point
#     sd.line(start_point=v.end_point, end_point=point)
#
#
# def square(point, angle=0, length=200):
#     start_point = point
#     step = 90
#     for tilt_angle in range(0, 360 - step, step):
#         v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
#         v.draw()
#         start_point = v.end_point
#     sd.line(start_point=v.end_point, end_point=point)
#
#
# def pentagon(point, angle=0, length=175):
#     start_point = point
#     step = 72
#     for tilt_angle in range(0, 360 - step, step):
#         v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
#         v.draw()
#         start_point = v.end_point
#     sd.line(start_point=v.end_point, end_point=point)
#
#
# def hexagon(point, angle=0, length=150):
#     start_point = point
#     step = 60
#     for tilt_angle in range(0, 360 - step, step):
#         v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
#         v.draw()
#         start_point = v.end_point
#     sd.line(start_point=v.end_point, end_point=point)
#
#
# point_triangle = sd.get_point(250, 100)
# point_square = sd.get_point(750, 100)
# point_pentagon = sd.get_point(250, 550)
# point_hexagon = sd.get_point(750, 550)
#
# triangle(point=point_triangle, angle=30, length=200)
#
# square(point=point_square, angle=30, length=200)
#
# pentagon(point=point_pentagon, angle=30, length=175)
#
# hexagon(point=point_hexagon, angle=45, length=150)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def figures(point, angle, length, step):
    start_point = point
    step = step
    for tilt_angle in range(0, 360 - step, step):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw()
        start_point = v.end_point
    sd.line(start_point=v.end_point, end_point=point)


def triangle(point, angle=0, length=200):
    step = 120
    figures(point, angle, length, step)


def square(point, angle=0, length=200):
    step = 90
    figures(point, angle, length, step)


def pentagon(point, angle=0, length=175):
    step = 72
    figures(point, angle, length, step)


def hexagon(point, angle=0, length=150):
    step = 60
    figures(point, angle, length, step)


point_triangle = sd.get_point(250, 100)
point_square = sd.get_point(750, 100)
point_pentagon = sd.get_point(250, 550)
point_hexagon = sd.get_point(750, 550)

triangle(point=point_triangle, angle=30, length=200)

square(point=point_square, angle=30, length=200)

pentagon(point=point_pentagon, angle=30, length=175)

hexagon(point=point_hexagon, angle=45, length=150)


sd.pause()
#зачёт!