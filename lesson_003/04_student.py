# -*- coding: utf-8 -*-


educational_grant, expenses = 10000, 12000
months = 0
percents_increase = 0.03
while months < 10:
    months += 1
    if months < 10:  # TODO попробуйте обойтись вовсе без if-ов
        expenses += 12000  # TODO вручную прописывать значения не нужно, используйте переменные
        educational_grant += 10000
    if months >= 2:
        percents = 12000 * percents_increase
        percents_increase = (percents_increase + 0.03)
        expenses = expenses + percents
    # TODO В этом цикле нужно выполнять последовательно 3 действия
    # TODO 1) Прибавлять расходы (expenses) в переменную с общими расходами
    # TODO 2) Увеличивать расходы на 3% (expenses *= 1.03 например)
    # TODO 3) Прибавлять +1 месяц

print('Студенту надо попросить', int(expenses - educational_grant), 'рублей')
