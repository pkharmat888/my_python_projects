# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):

    def __str__(self):
        return 'поле имени содержит НЕ только буквы'


class NotEmailError(Exception):

    def __str__(self):
        return 'поле емейл НЕ содержит @ и .(точку)'


def registration_controller(line):
    try:
        # TODO Проверка на наличие всех 3 полей
        #  Сразу разделять список, полученный при помощи split на 3 переменные нельзя.
        #  т.к. если элемента не хватает, то в списке пустого элемента тоже не будет,
        #  просто будет список из меньшего количества объектов.
        #  И распаковка в данном случае вызовет сама по себе ошибку.
        #  А раз мы хотим управлять вызовом ошибок, то нам нужно перехватить эту проблему.
        #  Сделать это можно узнав длину получившегося списка.
        #  т.е. если длина разделенной строки не равна 3 - то вызываем ошибку вручную (через raise)
        #  если же равна 3 - то разделяем на три элемента.
        name, email, age = line.split(' ')
    except ValueError:
        raise ValueError('НЕ присутсвуют все три поля')
    age = int(age)
    # TODO Проверку возраста хорошо будет разделить на 2 этапа.
    #  1-проверка, что строка состоит из чисел (поможет isdigit())
    #  2-проверка, что строка принадлежит нужному нам отрезку
    #  (тут подойдут либо операторы сравнения "<" ">", либо тот же range,
    #  только в этом случае надо будет проверять не каждый элемент отдельно
    #  а просто использовать условие - "age in полученный_диапазон")
    if not name.isalpha():
        raise NotNameError
    if '@' and '.' not in email:
        # TODO такое условие не сработает
        # TODO важно понимать порядок действий, с которым пайтон выполняет его
        # TODO пайтон проверит '.' in word - получит True/False
        # TODO затем сравнит '@' and True/False
        # TODO проверять @ in email он не будет
        raise NotEmailError
    if not (10 <= age <= 99):
        raise ValueError('Возраст НЕ является числом от 10 до 99')
    return line


registrations_good = open(file='registrations_good.log.txt', mode='w', encoding='utf8')

registrations_bad = open(file='registrations_bad.log.txt', mode='w', encoding='utf8')

file = open(file='registrations.txt', mode='r', encoding='utf8')
for line in file:
    try:
        # TODO В конце каждой строки из файла стоит знак \n который означает переход на новую строку
        # TODO (если конечно в файле данные разделены на строки)
        # TODO Поэтому стоит работать не с полной строкой, а со срезом до последнего элемента
        # TODO Либо можно использовать метод строки rstrip
        # https://docs.python.org/3/library/stdtypes.html#str.rstrip
        good_data = registration_controller(line)
        registrations_good.write(good_data)
    except NotNameError as exc:
        registrations_bad.write(f'{line[:-1]} - {exc}\n')
    except NotEmailError as exc:
        registrations_bad.write(f'{line[:-1]} - {exc}\n')
    except ValueError as exc:
        registrations_bad.write(f'{line[:-1]} - {exc}\n')
registrations_good.close()
registrations_bad.close()
file.close()

