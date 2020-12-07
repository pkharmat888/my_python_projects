# -*- coding: utf-8 -*-

import simple_draw as sd

_count_of_snowflakes = 0
_index = 0
_old_index_list = []
_x_coordinates = []
_y_coordinates = []
_random_length = []


def snowflakes_creating(count_of_snowflakes):
    global _count_of_snowflakes, _x_coordinates, _y_coordinates, _random_length
    _count_of_snowflakes = count_of_snowflakes
    for number in range(count_of_snowflakes):
        _x_coordinates.append(sd.random_number(0, 1800))
        _y_coordinates.append(sd.random_number(800, 900))
        _random_length.append(sd.random_number(10, 50))
    return [_x_coordinates, _y_coordinates, _random_length]


def snowflake_draw(color=sd.COLOR_DARK_BLUE):
    global _index
    for _index, x in enumerate(_x_coordinates):
        point = sd.get_point(_x_coordinates[_index], _y_coordinates[_index])
        sd.snowflake(center=point, length=_random_length[_index], color=color)


def snowflakes_step():
    global _index
    for _index, x in enumerate(_x_coordinates):
        random_step_x = sd.random_number(-30, 30)
        random_step_y = sd.random_number(5, 15)
        _x_coordinates[_index] += random_step_x
        _y_coordinates[_index] -= random_step_y


def snowflakes_end_numbers():
    global _index
    # TODO очищать список индексов лучше тут
    for _index, y in enumerate(_y_coordinates):
        if _y_coordinates[_index] < 25:
            _old_index_list.append(_index)
    _old_index_list.sort(reverse=True)
    return _old_index_list


def delete_snowflakes():
    # TODO удалять надо не все координаты, а только те, индексы которых попали в _old_index_list
    # TODO (т.е. нужен цикл по _old_index_list с удалением этих снежинок из всех списков
    _x_coordinates.clear()
    _y_coordinates.clear()
    _random_length.clear()
    _old_index_list.clear()  # TODO а не тут
