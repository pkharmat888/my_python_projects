# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

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

print('Студенту надо попросить',int(expenses - educational_grant),'рублей')






