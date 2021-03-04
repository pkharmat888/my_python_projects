# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


import time


def log_parser(file_name):
    counter = 0
    old_date = None
    with open(file_name, mode='r') as file:
        for line in file:
            if 'NOK' in line:
                date = time.strptime(line, '[%Y-%m-%d %H:%M:%S.%f] NOK ')
                new_date = time.strftime('%Y-%m-%d %H:%M', date)
                counter += 1
                if old_date != new_date:
                    if old_date is not None:
                        yield old_date, counter
                    counter = 0
                old_date = new_date
        yield old_date, counter + 1  # last yield for flushing buffered data once finished reading file


grouped_events = log_parser(file_name='events.txt')

for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
