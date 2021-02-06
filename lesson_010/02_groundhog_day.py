# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777


def one_day():
    list_of_errors = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
    carma = random.randint(1, 8)
    probability = random.randint(1, 14)
    if probability == random.randint(1, 14):
        error = random.choice(list_of_errors)
        raise error(f'Ошибка типа - {error}')
    return carma


total_carma = 0

with open(file='log_of_groundhog_day.txt', mode='w', encoding='utf8') as file:
    while total_carma <= ENLIGHTENMENT_CARMA_LEVEL:
        print(total_carma)
        try:
            total_carma += one_day()
            print(total_carma)
        except Exception as exc:
            print(exc)
            file.write(f'Ошибка типа - {exc}\n')
