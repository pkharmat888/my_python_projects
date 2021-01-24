# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


import os


class CharStatistics:
    statistics = {}
    sorted_statistics = {}
    total_chars = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.path = 'C:/python_base/lesson_009/python_snippets/'
        self.path_normalized = os.path.normpath(self.path)
        self.path_to_our_file = os.path.join(self.path_normalized, file_name)
        self.file = None
        self.statistics_sorted_keys = None

    def file_open(self):
        with open(self.path_to_our_file, mode='r', encoding='cp1251') as file:
            self._get_statistics(file=file)

    def _get_statistics(self, file):
        self.file = file
        for line in self.file:
            for char in line:
                if char.isalpha():
                    self.total_chars += 1
                    if char not in self.statistics:
                        self.statistics[char] = 1
                    else:
                        self.statistics[char] += 1

    def sorting(self):
        self.statistics_sorted_keys = sorted(self.statistics)

    def make_new_sorted_statistics(self):
        for char in self.statistics_sorted_keys:
            self.sorted_statistics[char] = self.statistics[char]

    def visualise_data(self):
        print(f'+{"+":-^21}+')
        print(f'|{"Буква":^10}|{"Частота":^10}|')
        print(f'+{"+":-^21}+')
        for char, number in self.sorted_statistics.items():
            print(f'|{char:^10}|{number:^10}|')
        print(f'+{"+":-^21}+')
        print(f'|{"Итого":^10}|{self.total_chars:^10}|')
        print(f'+{"+":-^21}+')

    def get_statistics(self):
        self.file_open()
        self.sorting()
        self.make_new_sorted_statistics()
        self.visualise_data()


# file_name = 'voyna-i-mir.txt'
# file = CharStatistics(file_name=file_name)
# file.get_statistics()


# file_name = 'voyna-i-mir.txt'
# path = 'C:/python_base/lesson_009/python_snippets/'
# path_normalized = os.path.normpath(path)
# path_to_our_file = os.path.join(path_normalized, file_name)
#
# statistics = {}
# sorted_statistics = {}
# total_chars = 0
#
# with open(path_to_our_file, mode='r', encoding='cp1251') as file:
#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 total_chars += 1
#                 if char not in statistics:
#                     statistics[char] = 1
#                 else:
#                     statistics[char] += 1
#     statistics_sorted_keys = sorted(statistics, key=statistics.get, reverse=True)
#     for char in statistics_sorted_keys:
#         sorted_statistics[char] = statistics[char]
#
#
# print(f'+{"+":-^21}+')
# print(f'|{"Буква":^10}|{"Частота":^10}|')
# print(f'+{"+":-^21}+')
# for char, number in sorted_statistics.items():
#     print(f'|{char:^10}|{number:^10}|')
# print(f'+{"+":-^21}+')
# print(f'|{"Итого":^10}|{total_chars:^10}|')
# print(f'+{"+":-^21}+')


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

class CharStatisticsDescending(CharStatistics):

    def sorting(self):
        self.statistics_sorted_keys = sorted(self.statistics, key=self.statistics.get, reverse=True)


class CharStatisticsAscending(CharStatistics):

    def sorting(self):
        self.statistics_sorted_keys = sorted(self.statistics, key=self.statistics.get)


class CharStatisticsAlphabetAscending(CharStatistics):

    def sorting(self):
        self.statistics_sorted_keys = sorted(self.statistics)


class CharStatisticsAlphabetDescending(CharStatistics):

    def sorting(self):
        self.statistics_sorted_keys = sorted(self.statistics, reverse=True)


file_name = 'voyna-i-mir.txt'
file = CharStatisticsAlphabetDescending(file_name=file_name)
file.get_statistics()
#зачёт!