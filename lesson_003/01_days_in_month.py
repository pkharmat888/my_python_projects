# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
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

if month == 1:
    print(months[1], 'Дней')
elif month == 2:
    print(months[2], 'Дней')
elif month == 3:
    print(months[3], 'Дней')
elif month == 4:
    print(months[4], 'Дней')
elif month == 5:
    print(months[5], 'Дней')
elif month == 6:
    print(months[6], 'Дней')
elif month == 7:
    print(months[7], 'Дней')
elif month == 8:
    print(months[8], 'Дней')
elif month == 9:
    print(months[9], 'Дней')
elif month == 10:
    print(months[10], 'Дней')
elif month == 11:
    print(months[11], 'Дней')
elif month == 12:
    print(months[12], 'Дней')
else:
    print('Вы ввели неверный номер месяца')

