import random as rd
from termcolor import cprint, colored

_number_to_guess = '0'
_bulls_and_cows = {'bulls': 0, 'cows': 0}
dict_to_show = {}


def guessing_the_number():
    global _number_to_guess
    while True:
        _number_to_guess = str(rd.randint(1000, 9999))
        set_number_to_guess = set(_number_to_guess)
        if len(_number_to_guess) != len(set_number_to_guess):
            continue
        elif len(_number_to_guess) != 4:
            continue
        else:
            return _number_to_guess


def check_number(user_input):
    global _bulls_and_cows, dict_to_show
    _bulls_and_cows['bulls'] = 0
    _bulls_and_cows['cows'] = 0
    for index, number in enumerate(user_input):
        if _number_to_guess[index] == number:
            _bulls_and_cows['bulls'] += 1
        elif number in _number_to_guess:
            _bulls_and_cows['cows'] += 1
    return _bulls_and_cows


def input_check():
    while True:
        user_input = input(colored('Отгадайте число. Напишите ваш вариант: ', color='green'))
        if user_input.isnumeric():
            set_user_input = set(user_input)
        else:
            cprint('Вы должны ввести числа', color='red')
            continue
        if len(user_input) != len(set_user_input):
            cprint('Вы ввели неверное число. Все цифры в числе должны быть уникальны',
                   color='red')
            continue
        elif user_input[0] == '0':
            cprint('Вы ввели неверное число. Число не может начинатся с нуля', color='red')
            continue
        elif len(user_input) != 4:
            cprint('Вы ввели неверное число. Длинна числа должна равнятся четырем числам',
                   color='red')
            continue
        else:
            return user_input


def end_of_game():
    return _bulls_and_cows['bulls'] == 4



