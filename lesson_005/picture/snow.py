# -*- coding: utf-8 -*-

import simple_draw as sd


# Функция для создания и наполнения изначальных списков


def snowfall_lists(x_start_point, x_endpoint, y_start_point, y_endpoint, count_of_snowflakes):
    # Создаю пустые списки для координат, размеров снежинки и "старых" индексов
    x_coordinates = []
    y_coordinates = []
    random_length = []
    list_of_start_end_points = [x_start_point, x_endpoint, y_start_point, y_endpoint]
    # Генерирование координат и размеров снежинок и добавление их в списки
    for number in range(count_of_snowflakes):
        x_coordinates.append(sd.random_number(list_of_start_end_points[0], list_of_start_end_points[1]))
        y_coordinates.append(sd.random_number(list_of_start_end_points[2], list_of_start_end_points[3]))
        random_length.append(sd.random_number(10, 50))

    return [x_coordinates, y_coordinates, random_length, list_of_start_end_points]


# Функция для отрисовки снежинок


def snowfall_draw(x_coordinates, y_coordinates, random_length, list_of_start_end_points, endpoint_of_snowfall):
    sd.start_drawing()
    old_index_list = []
    for index, x in enumerate(x_coordinates):
        # Назначаю рандомное значение падения и отклонения на каждом шагу
        random_step_x = sd.random_number(-30, 30)
        random_step_y = sd.random_number(5, 15)
        # Создаю точку и рисую снежинку цветом фона
        point = sd.get_point(x_coordinates[index], y_coordinates[index])
        sd.snowflake(center=point, length=random_length[index], color=sd.background_color)
        # Изменяю координаты
        x_coordinates[index] += random_step_x
        y_coordinates[index] -= random_step_y
        # Создаю точку и рисую снежинку белым цветом
        point = sd.get_point(x_coordinates[index], y_coordinates[index])
        sd.snowflake(center=point, length=random_length[index], color=sd.COLOR_DARK_BLUE)
        # Добавляю индекс снежинки, которая по игреку меньше пятидесяти в список "старых" индексов
        if y_coordinates[index] < endpoint_of_snowfall:
            old_index_list.append(index)
    # Сортирую список со "старыми" индексами
    old_index_list.sort(reverse=True)
    # Если в списке "старых" индексов, находится хотя бы одно значение, то захожу в цикл и
    # удаляю старые и сразу же добавляю новые значения, в списки координат и размеров снежинки,
    # по индексу из списка "старых" индексов,
    if any(old_index_list):
        for old_index in old_index_list:
            x_coordinates.pop(old_index)
            x_coordinates.insert(old_index, sd.random_number(list_of_start_end_points[0], list_of_start_end_points[1]))
            y_coordinates.pop(old_index)
            y_coordinates.insert(old_index, sd.random_number(list_of_start_end_points[2], list_of_start_end_points[3]))
            random_length.pop(old_index)
            random_length.insert(old_index, sd.random_number(10, 50))
        # Очищаю список "старых" индексов
        old_index_list.clear()

    sd.finish_drawing()
