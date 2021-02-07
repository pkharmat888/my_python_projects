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
    if len(line.split()) == 3:
        name, email, age = line.split()
        if not name.isalpha():
            raise NotNameError
        if age.isdigit():
            if int(age) not in range(10, 100):
                raise ValueError('поле возраст НЕ является числом от 10 до 99')
        else:
            raise ValueError('поле возраст НЕ является числом от 10 до 99')
        if not (('@' in email) and ('.' in email)):
            raise NotEmailError
    else:
        raise ValueError('НЕ присутсвуют все три поля')
    return line


registrations_good = open(file='registrations_good.log.txt', mode='w', encoding='utf8')

registrations_bad = open(file='registrations_bad.log.txt', mode='w', encoding='utf8')

file = open(file='registrations.txt', mode='r', encoding='utf8')
for line in file:
    line = line.rstrip()
    try:
        good_data = registration_controller(line)
        registrations_good.write(f'{good_data}\n')
    except NotNameError as exc:
        registrations_bad.write(f'{line} - {exc}\n')
    except NotEmailError as exc:
        registrations_bad.write(f'{line} - {exc}\n')
    except ValueError as exc:
        registrations_bad.write(f'{line} - {exc}\n')
registrations_good.close()
registrations_bad.close()
file.close()
#зачёт!