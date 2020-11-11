# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1000)


# 1) Написать функцию draw_branches

# root_point = sd.get_point(300, 30)
#
# v = sd.get_vector(start_point=root_point, angle=90, length=100)
# v.draw()
#
# start_point = v.end_point
#
#
# def draw_branches(point, angle, length):
#     delta = 30
#     branch1 = sd.get_vector(start_point=point, angle=angle - delta, length=length)
#     branch2 = sd.get_vector(start_point=point, angle=angle + delta, length=length)
#     branch1.draw()
#     branch2.draw()
#
#
# draw_branches(point=start_point, angle=90, length=100)
# sd.pause()

# 2) Сделать draw_branches рекурсивной

# 3) Запустить вашу рекурсивную функцию

# def draw_branches(point, angle, length):
#     delta = 30
#     if length < 2:
#         return
#     next_angle1 = angle + delta
#     next_angle2 = angle - delta
#     branch1 = sd.get_vector(start_point=point, angle=next_angle1, length=length)
#     branch2 = sd.get_vector(start_point=point, angle=next_angle2, length=length)
#     next_length = length * .75
#     branch1.draw()
#     branch2.draw()
#     draw_branches(point=branch1.end_point, angle=next_angle1, length=next_length)
#     draw_branches(point=branch2.end_point, angle=next_angle2, length=next_length)
#
#
# root_point = sd.get_point(600, 30)
#
# v = sd.get_vector(start_point=root_point, angle=90, length=100)
# v.draw()
#
# start_point = v.end_point
#
# draw_branches(point=start_point, angle=90, length=100)
#
# sd.pause()

# 4) Усложненное задание (делать по желанию)

def draw_branches(point, angle, length):
    delta_angle1 = sd.random_number(18, 42)
    delta_angle2 = sd.random_number(18, 42)
    delta_length1 = (sd.random_number(60, 90)) * 0.01
    delta_length2 = (sd.random_number(60, 90)) * 0.01
    if length < 2:
        return
    next_angle1 = angle + delta_angle1
    next_angle2 = angle - delta_angle2
    # TODO Для того, чтобы у дерева был ствол - можно тут убрать один из векторов
    # TODO Чтобы по итогу функция рисовала один вектор и вызывала себя дважды
    # TODO Получится вот такая последовательность ветвей (1-2-4-8...)
    branch1 = sd.get_vector(start_point=point, angle=next_angle1, length=length)
    branch2 = sd.get_vector(start_point=point, angle=next_angle2, length=length)
    next_length1 = length * delta_length1
    next_length2 = length * delta_length2
    branch1.draw()
    branch2.draw()
    draw_branches(point=branch1.end_point, angle=next_angle1, length=next_length1)
    draw_branches(point=branch2.end_point, angle=next_angle2, length=next_length2)


root_point = sd.get_point(600, 30)

v = sd.get_vector(start_point=root_point, angle=90, length=100)
v.draw()

start_point = v.end_point

draw_branches(point=start_point, angle=90, length=100)


sd.pause()
