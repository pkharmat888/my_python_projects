# -*- coding: utf-8 -*-


educational_grant, expenses = 10000, 12000
months = 0
percents_increase = 0.03
while months < 10:
    months += 1
    if months < 10:
        expenses += 12000
        educational_grant += 10000
    if months >= 2:
        percents = 12000 * percents_increase
        percents_increase = (percents_increase + 0.03)
        expenses = expenses + percents

print('Студенту надо попросить', int(expenses - educational_grant), 'рублей')
