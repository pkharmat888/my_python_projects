# -*- coding: utf-8 -*-

educational_grant, expenses = 10000, 12000
total_grant = 0
total_expenses = 0
months = 1
total_grant += educational_grant  # TODO эта строка лишняя получается
while months <= 9:  # TODO а тут нужен +1 месяц добавить
    total_grant += educational_grant
    total_expenses += expenses
    expenses *= 1.03
    months += 1

print('Студенту надо попросить', int(total_expenses - total_grant), 'рублей')
