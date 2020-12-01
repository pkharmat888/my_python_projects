# -*- coding: utf-8 -*-

import simple_draw as sd


# Функция для отрисовки обычного дерева


def tree_draw(point, angle, length, width):
    color = sd.COLOR_DARK_ORANGE
    delta_angle1 = sd.random_number(18, 42)
    delta_angle2 = sd.random_number(18, 42)
    delta_length1 = (sd.random_number(60, 90)) * 0.01
    delta_length2 = (sd.random_number(60, 90)) * 0.01
    if length < 2:
        return
    if length < 8:
        color = sd.COLOR_DARK_GREEN
    branch1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    next_angle1 = angle + delta_angle1
    next_angle2 = angle - delta_angle2
    next_length1 = length * delta_length1
    next_length2 = length * delta_length2
    branch1.draw(color=color)
    tree_draw(point=branch1.end_point, angle=next_angle1, length=next_length1, width=int(width))
    tree_draw(point=branch1.end_point, angle=next_angle2, length=next_length2, width=int(width))


# Функция для отрисовки дерева с листьями


def tree_with_leaves_draw(point, angle, length, width, list_of_endpoints):
    color = sd.COLOR_DARK_ORANGE
    delta_angle1 = sd.random_number(18, 42)
    delta_angle2 = sd.random_number(18, 42)
    delta_length1 = (sd.random_number(60, 90)) * 0.01
    delta_length2 = (sd.random_number(60, 90)) * 0.01
    if length < 2:
        list_of_endpoints.append([point.x, point.y])
        return
    if length < 8:
        color = sd.COLOR_DARK_GREEN
    branch1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    next_angle1 = angle + delta_angle1
    next_angle2 = angle - delta_angle2
    next_length1 = length * delta_length1
    next_length2 = length * delta_length2
    branch1.draw(color=color)
    tree_with_leaves_draw(point=branch1.end_point, angle=next_angle1, length=next_length1, width=int(width),
                          list_of_endpoints=list_of_endpoints)
    tree_with_leaves_draw(point=branch1.end_point, angle=next_angle2, length=next_length2, width=int(width),
                          list_of_endpoints=list_of_endpoints)
    return list_of_endpoints


# Функция для создания и наполнения изначальных списков для листьев


def leaves_lists(list_of_endpoints):
    # Создаю пустые списки для координат, размеров листка и "старых" индексов
    x_coordinates = []
    y_coordinates = []
    # Генерирование координат и размеров снежинок и добавление их в списки
    for index, coordinates_of_leaves in enumerate(list_of_endpoints):
        x_coordinates.append(list_of_endpoints[index][0])
        y_coordinates.append(list_of_endpoints[index][1])

    return [x_coordinates, y_coordinates]


# Функция для отрисовки листьев


def leaves_fall(x_coordinates, y_coordinates, endpoint_of_laves_fall):
    sd.start_drawing()
    for index, x in enumerate(x_coordinates):
        if y_coordinates[index] > endpoint_of_laves_fall:
            # Назначаю рандомное значение падения и отклонения на каждом шагу
            random_step_x = sd.random_number(-30, 30)
            random_step_y = sd.random_number(5, 15)
            # Создаю точку и рисую снежинку цветом фона
            left_bottom_point = sd.get_point(x_coordinates[index], y_coordinates[index])
            right_top_point = sd.get_point(x_coordinates[index] + 3, y_coordinates[index] + 3)
            sd.ellipse(left_bottom=left_bottom_point, right_top=right_top_point, color=sd.background_color)
            # Изменяю координаты
            x_coordinates[index] += random_step_x
            y_coordinates[index] -= random_step_y
            # Создаю точку и рисую лист
            left_bottom_point = sd.get_point(x_coordinates[index], y_coordinates[index])
            right_top_point = sd.get_point(x_coordinates[index] + 3, y_coordinates[index] + 3)
            sd.ellipse(left_bottom=left_bottom_point, right_top=right_top_point, color=sd.COLOR_DARK_RED)
    sd.finish_drawing()
