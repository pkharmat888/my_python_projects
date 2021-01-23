# -*- coding: utf-8 -*-

import os
import time
import shutil
import zipfile
import zipfile as zp


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class FileArranger:
    dict_of_last_change = {}

    def __init__(self, path_to_search_files, path_to_save_files):
        self.path_to_search_files = path_to_search_files
        self.path_to_search_files_normalized = os.path.normpath(path_to_search_files)
        self.path_to_save_files = path_to_save_files

    def searching_files(self):
        for dirpath, dirnames, filenames in os.walk(self.path_to_search_files_normalized):
            for name in filenames:
                file_to_search = os.path.join(dirpath, name)
                self._file_sort(file_to_search=file_to_search)

    def _file_sort(self, file_to_search):
        time_of_last_change = os.path.getmtime(filename=file_to_search)
        gmtime = time.gmtime(time_of_last_change)
        years_and_months = time.strftime('%Y/%m', gmtime)
        self.dict_of_last_change[file_to_search] = years_and_months

    def sort_and_make_new_dirs(self):
        for name, time in self.dict_of_last_change.items():
            file_to_save = os.path.join(path_to_save_files, time)
            path_to_save_files_normalized = os.path.normpath(file_to_save)
            os.makedirs(name=path_to_save_files_normalized, mode=0o777, exist_ok=True)
            shutil.copy2(src=name, dst=path_to_save_files_normalized)
            print(f'{name:<90} : {time:^10}')

    def arrange(self):
        self.searching_files()
        self.sort_and_make_new_dirs()


# path_to_search_files = 'C:/python_base/lesson_009/icons'
# path_to_search_files_normalized = os.path.normpath(path_to_search_files)
#
# path_to_save_files = 'C:/python_base/lesson_009/icons_by_year'
#
# dict_of_last_change = {}
#
# for dirpath, dirnames, filenames in os.walk(path_to_search_files_normalized):
#     for name in filenames:
#         file_to_search = os.path.join(dirpath, name)
#         time_of_last_change = os.path.getmtime(filename=file_to_search)
#         gmtime = time.gmtime(time_of_last_change)
#         years_and_months = time.strftime('%Y/%m', gmtime)
#         dict_of_last_change[file_to_search] = years_and_months
#
# for name, time in dict_of_last_change.items():
#     file_to_save = os.path.join(path_to_save_files, time)
#     path_to_save_files_normalized = os.path.normpath(file_to_save)
#     if os.path.exists(path_to_save_files_normalized):
#         shutil.copy2(src=name, dst=path_to_save_files_normalized)
#     else:
#         os.makedirs(name=path_to_save_files_normalized, mode=0o777)
#         shutil.copy2(src=name, dst=path_to_save_files_normalized)
#     print(f'{name:<90} : {time:^10}')

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html


class FileArrangerFromZipFile(FileArranger):

    def searching_files(self):
        with zipfile.ZipFile(file=path_to_search_files, mode='r') as arhcive:
            for name in arhcive.namelist():
                if os.path.isfile(name):
                    self._file_sort(file_to_search=name)


path_to_search_files = 'icons.zip'
path_to_save_files = 'icons_by_year'
file = FileArrangerFromZipFile(path_to_search_files=path_to_search_files, path_to_save_files=path_to_save_files)
file.arrange()
