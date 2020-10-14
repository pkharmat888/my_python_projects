# -*- coding: utf-8 -*-

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
# TODO У вас два решения совмещены
# TODO попробуйте просто проверить, есть ли month среди ключей словаря
# TODO и если да - вывести print(months[month], 'Дней')
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(months[month], 'Дней')
elif month in [4, 6, 9, 11]:
    print(months[month], 'Дней')
elif month == 2:
    print(months[month], 'Дней')
else:
    print('Вы ввели неверный номер месяца')
