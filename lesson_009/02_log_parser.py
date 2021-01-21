# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import os
import time
import io


class LogParser:
    nok_log = {}

    def __init__(self, file_name):
        self.file_name = file_name
        self.out_file_name = 'NOK logs by minutes'

    def file_open(self):
        with open(self.file_name, mode='r') as file:
            self._file_parse(file=file)

    def _file_parse(self, file):
        for line in file:
            if 'NOK' in line:
                date = time.strptime(line, '[%Y-%m-%d %H:%M:%S.%f] NOK ')
                new_date = time.strftime('[%Y-%m-%d %H:%M]', date)
                if new_date not in self.nok_log:
                    self.nok_log[new_date] = 1
                else:
                    self.nok_log[new_date] += 1

    def file_writing(self):
        with open(self.out_file_name, mode='w', encoding='utf8') as out_file:
            for time, counts in self.nok_log.items():
                out_file.write(f'{time} {counts}\n')

    def get_logs(self):
        self.file_open()
        self.file_writing()


file_name = 'events.txt'
file = LogParser(file_name=file_name)
file.get_logs()


# nok_log = {}
#
# file_name = 'events.txt'
# out_file_name = 'NOK logs by minutes'

# with open(file_name, mode='r') as file:
#     for line in file:
#         if 'NOK' in line:
#             date = time.strptime(line, '[%Y-%m-%d %H:%M:%S.%f] NOK ')
#             new_date = time.strftime('[%Y-%m-%d %H:%M]', date)
#             if new_date not in nok_log:
#                 nok_log[new_date] = 1
#             else:
#                 nok_log[new_date] += 1

# with open(out_file_name, mode='w', encoding='utf8') as out_file:
#     for time, counts in nok_log.items():
#         out_file.write(f'{time} {counts}\n')

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
