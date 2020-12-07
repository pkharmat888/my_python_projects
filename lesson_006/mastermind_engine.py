import random as rd


_number_to_guess = '0'
_bulls_and_cows = {'bulls': 0, 'cows': 0}
dict_to_show = {}


def guessing_the_number():
    global _number_to_guess
    _number_to_guess = str(rd.randint(1111, 9999))  # TODO почему от 1111 а не от 1000? 1023 например рабочий вариант
    set_number_to_guess = set(_number_to_guess)
    if len(_number_to_guess) != len(set_number_to_guess):
        return guessing_the_number()
    # TODO от рекурсии стоит отказаться
    # TODO где можно использовать цикл - используйте
    # TODO в большинстве случаев цикл будет эффективнее, в частности тут
    # TODO (каждый вызов функции тратит ресурсы, рекурсия создает сразу много вызовов)
    elif _number_to_guess[0] == '0':  # TODO 0 не может быть первым, если генерируются числа от 1000
        return guessing_the_number()
    elif len(_number_to_guess) != 4:
        return guessing_the_number()
    else:
        return print(_number_to_guess)  # TODO возвращать надо число, а не функцию принт
    # TODO принт сам по себе ничего не возвращает в результате своей работы
    # TODO (только выводит данные в консоль, если написать x = print(), то x будет равен None всегда)


def check_number(user_input):
    global _bulls_and_cows, dict_to_show
    # TODO обнулять быков и коров стоит тут
    for index, number in enumerate(user_input):
        if _number_to_guess[index] == number:
            _bulls_and_cows['bulls'] += 1
        elif number in _number_to_guess:
            _bulls_and_cows['cows'] += 1
    dict_to_show = _bulls_and_cows.copy()  # TODO тогда не нужны будут копии
    _bulls_and_cows['bulls'] = 0
    _bulls_and_cows['cows'] = 0
    return dict_to_show


def end_of_game():
    return dict_to_show['bulls'] == 4
