# -*- coding: utf-8 -*-

# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11


envelop_x, envelop_y = 10, 7

if envelop_x >= paper_x and envelop_y >= paper_y:
    print('Да, письмо помещается в конверте')
elif envelop_x >= paper_y and envelop_y >= paper_x:
    print('Да, письмо поместится в конверте, если его перевернуть')
else:
    print('Нет, письмо не поместится в конверте')

# Усложненное задание, решать по желанию.

hole_x, hole_y = 8, 9

# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)
# TODO Для того, чтобы кирпич прошёл в отверстие - достаточно проверить 2 стороны, чтобы они были меньше отверстия
# TODO Тут всего может быть 6 различных вариантов (3 площади у кирпича это первые три варианта,
# TODO и если их перевернуть будет ещё 3)
# TODO Дам вам вот такую подсказочку:
# TODO h_x - b_x  h_y - b_y
# TODO h_x - b_y  h_y - b_x
# TODO h_x - b_x  h_y - b_z
# TODO h_x - b_z  h_y - b_x
# TODO h_x - b_y  h_y - b_z
# TODO h_x - b_z  h_y - b_y
if hole_x >= brick_x and hole_y >= brick_y:
    if hole_x >= brick_x and hole_y >= brick_z:
        if hole_x >= brick_z and hole_y >= brick_y:
            print('Войдет')
else:
    print('Не войдет')
