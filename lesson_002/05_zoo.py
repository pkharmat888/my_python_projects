#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(str(zoo))
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)
#  и выведите список на консоль
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)
# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')

print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print('Лев сидит в клетке номер: ' + str(zoo.index('lion') + 1),
      'Жайворонок сидит в клетке номер: ' + str(zoo.index('lark') + 1))
