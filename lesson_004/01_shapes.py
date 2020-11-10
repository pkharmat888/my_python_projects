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

point_triangle = sd.get_point(250, 100)
point_square = sd.get_point(750, 100)
point_pentagon = sd.get_point(250, 550)
point_hexagon = sd.get_point(750, 550)


# Triangle

def triangle(point, angle=0, length=200):
    start_point = point
    for tilt_angle in range(0, 360, 120):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw()
        start_point = v.end_point


triangle(point=point_triangle, angle=30, length=200)


# Square

def square(point, angle=0, length=200):
    start_point = point
    for tilt_angle in range(0, 360, 90):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw()
        start_point = v.end_point


square(point=point_square, angle=30, length=200)


# Pentagon

def pentagon(point, angle=0, length=175):
    start_point = point
    for tilt_angle in range(0, 360, 72):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw()
        start_point = v.end_point


pentagon(point=point_pentagon, angle=30, length=175)


# Hexagon

def hexagon(point, angle=0, length=150):
    start_point = point
    for tilt_angle in range(0, 360, 60):
        v = sd.get_vector(start_point=start_point, angle=angle + tilt_angle, length=length)
        v.draw()
        start_point = v.end_point


hexagon(point=point_hexagon, angle=45, length=150)

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


sd.pause()
