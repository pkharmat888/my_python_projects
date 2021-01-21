# -*- coding: utf-8 -*-

# Форматирование вывода на консоль

# Старый стиль: %. Аналог С-форматирования функции printf()
print('Мы — те %s, что говорят "%s!"' % ('рыцари', 'Ха'))
print('Вывод числа %d' % 34)
# Плюсы: программистам на С проще :)
# Минусы: негибкий, мало возможностей.

# Более продвинутый способ - через метод строки .format()
print('Мы — те {}, что говорят "{}!"'.format('рыцари', 'Ха'))

# Можно указывать номер выводимого параметра
a = 'рыцари'
b = 'Ого'
print('Мы — те {0}, что говорят "{1}!"'.format(a, b))
# и менять местами
print('Мы — те {1}, что говорят "{0}!"'.format(a, b))

# вывод целых чисел
a = 27
print('Вывод числа {0}'.format(a))
print('Вывод числа {0:d}'.format(a))
# сколько символов выводить - указываем после двоеточия (дополняется пробелами сначала)
print('Вывод числа "{0:3d}" '.format(a))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d} '.format(x, x ** 2, x ** 3))

# вывод дробного числа с заданной точностью
# :8.4f - 8 знаков всего, 4 знака после запятой, дробное число
import math

print('Вывод числа "{0:5f}" '.format(math.pi))
print('Вывод числа "{0:5.2f}" '.format(math.pi))
print('Вывод числа "{0:8.2f}" '.format(math.pi))

# именованные аргументы
print('Этот {food} — {adjective}.'.format(
    food='фарш', adjective='непередаваемо ужасен',
))

# можно совмещать
print('История о {0}е, {1}е, и {other}е.'.format('Билл', 'Манфред', other='Георг'))

# форматирование вывода строк - минимальная ширина поля {xxx:10}
phones = {'Bill': 4127, 'Jameson': 4098, 'Abraham': 7678}
for name, phone in phones.items():
    print('{name:10} ==> {phone:10d}'.format(name=name, phone=phone))

# выравнивания строк
print('|{txt:<30}|'.format(txt='left aligned'))
# 'left aligned                  '
print('|{txt:>30}|'.format(txt='right aligned'))
# '                 right aligned'
print('|{txt:^30}|'.format(txt='centered'))
# '           centered           '
print('|{txt:*^30}|'.format(txt='centered'))  # use '*' as a fill char
# '***********centered***********'

# полное описание мини-языка форматирования тут - https://docs.python.org/3/library/string.html#formatspec

# В версии 3.6 ввели f-строки - такие строки, в которых можно указывать переменные пайтона или даже пайтон выражения
# https://docs.python.org/3.6/reference/lexical_analysis.html#formatted-string-literals

txt = 'строка'
print(f'{txt:*^30}')
# очень похож на .format() но только сначала вычисляется пайтон выражение, а потом применяется форматирование
# тут txt - это имя переменной
# можно так: писать код внутри строки :( получается ужасно, на мой вкус
var_1 = 34
print(f'Удвоенное значение переменной - {var_1 * 2:10d}')
# можно даже делать операции индексирования
my_list = [1, 2, 3, 4]
print(f'Третий элемент списка - {my_list[2]:10d}')
my_dict = {'a': 1, 'b': 2}
print(f"Значение словаря - {my_dict['a']:10d}")
# или вызывать функции... но лучше так не делать :)

# Один из постулатов пайтона - чем проще тем лучше. и поэтому вместо
print('Значение переменной var_1 - {}'.format(var_1))
# проще использовать
print(f'Значение переменной var_1 - {var_1}')


# не надо усложнять и заставлять читающего код читать сложные перл-подобные выражение при выводе


# для разрешения имен используются стандартный алгоритм поиска по области видимости
def f1():
    print(f'{var_2:*^30}')


var_2 = 'строка'
f1()

# # # # # # # # # #
# Форматирование вывода в файл ничем не отличается от форматирования вывода на консоль
# Мы так же формируем строку удобным способом и пишем её в файл

file_name = 'out.txt'
var_1 = 42
with open(file_name, mode='w') as file:
    file.write('Вывод числа %d' % (34,))
    file.write('\n')
    file.write('Мы — те {}, что говорят "{}!"'.format('рыцари', 'Ха'))
    file.write('\n')
    file.write(f'Значение переменной var_1 - {var_1:10}')
    file.write('\n')
