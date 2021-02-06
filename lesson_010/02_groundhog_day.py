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
        exc = random.choice(list_of_errors)
        file = open(file='log_of_groundhog_day.txt', mode='a', encoding='utf8')
        try:  # TODO try/except тут не нужен, только raise случайной ошибки
            raise exc
        except:
            file.write(f'Ошибка типа - {exc}\n')
        finally:
            file.close()

    return carma


total_carma = 0
while True:
    # TODO а вот тут уже try/except
    total_carma += one_day()
    print(total_carma)
    if total_carma >= ENLIGHTENMENT_CARMA_LEVEL:  # TODO это условие надо в while добавить, вместо True
        break

# TODO Открытие/закрытие файлов (оператор with именно это и делает)
# TODO это довольно трудоёмкое занятие. Поэтому его нужно стараться выносить из цикла.
# TODO Открывать файл один раз до цикла и закрывать один раз, уже после цикла.