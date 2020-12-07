# -*- coding: utf-8 -*-


# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from mastermind_engine import guessing_the_number, check_number, end_of_game
from termcolor import cprint, colored


user_input = 0
move_counter = 0
guessing_the_number()
cprint('Компютер загадал число', color='cyan')
while True:
    user_input = input(colored('Отгадайте число. Напишите ваш вариант: ', color='green'))
    if user_input.isnumeric():
        set_user_input = set(user_input)
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
        result = check_number(user_input=user_input)
        cprint('Колличество быков: {}, Колличество коров: {}'.format(result['bulls'], result['cows']), color='magenta')
        move_counter += 1
    else:
        print('Вы должны ввести числа')
        continue
    if end_of_game():
        cprint('Колличество ходов сделанных игроком: {}'.format(move_counter), color='blue')
        while True:
            answer = input(colored('Хотите еще партию ?  y/n  ', color='yellow'))
            if answer == 'y':
                move_counter = 0
                cprint('Начало новой партии', color='yellow')
                cprint('Компютер загадал число', color='cyan')
                guessing_the_number()
                continue
            elif answer == 'n':
                break
        if answer == 'n':
            cprint('Игра оконченна', color='red')
            break

