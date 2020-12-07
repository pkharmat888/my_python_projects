import random as rd


_number_to_guess = '0'
_bulls_and_cows = {'bulls': 0, 'cows': 0}
dict_to_show = {}


def guessing_the_number():
    global _number_to_guess
    _number_to_guess = str(rd.randint(1111, 9999))
    set_number_to_guess = set(_number_to_guess)
    if len(_number_to_guess) != len(set_number_to_guess):
        return guessing_the_number()
    elif _number_to_guess[0] == '0':
        return guessing_the_number()
    elif len(_number_to_guess) != 4:
        return guessing_the_number()
    else:
        return print(_number_to_guess)


def check_number(user_input):
    global _bulls_and_cows, dict_to_show
    for index, number in enumerate(user_input):
        if _number_to_guess[index] == number:
            _bulls_and_cows['bulls'] += 1
        elif number in _number_to_guess:
            _bulls_and_cows['cows'] += 1
    dict_to_show = _bulls_and_cows.copy()
    _bulls_and_cows['bulls'] = 0
    _bulls_and_cows['cows'] = 0
    return dict_to_show


def end_of_game():
    return dict_to_show['bulls'] == 4
