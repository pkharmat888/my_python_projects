# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1000)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# x_coordinates = []
# y_coordinates = []
# random_length = []
#
# for number in range(N):
#     x_coordinates.append(sd.random_number(0, 1200))
#     y_coordinates.append(sd.random_number(900, 1000))
#     random_length.append(sd.random_number(10, 100))
#
# while True:
#     sd.clear_screen()
#     for index, x in enumerate(x_coordinates):
#         y = y_coordinates[index]
#         y_coordinates[index] -= 10
#         point = sd.get_point(x, y)
#         sd.snowflake(center=point, length=random_length[index])
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# sd.pause()


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# x_coordinates = []
# y_coordinates = []
# random_length = []
#
# step = 10
#
# for number in range(N):
#     x_coordinates.append(sd.random_number(0, 1200))
#     y_coordinates.append(sd.random_number(900, 1000))
#     random_length.append(sd.random_number(10, 100))

# while True:
#     sd.start_drawing()
#     for index, x in enumerate(x_coordinates):
#         y = y_coordinates[index]
#         point = sd.get_point(x, y + step)
#         sd.snowflake(center=point, length=random_length[index], color=sd.background_color)
#         y_coordinates[index] -= step
#         new_point = sd.get_point(x, y)
#         sd.snowflake(center=new_point, length=random_length[index], color=sd.COLOR_WHITE)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# sd.pause()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


# Создаю пустые списки для координат, размеров снежинки и "старых" индексов
x_coordinates = []
y_coordinates = []
random_length = []
old_index_list = []

# Генерирование координат и размеров снежинок и добавление их в списки
for number in range(N):
    x_coordinates.append(sd.random_number(0, 1200))
    y_coordinates.append(sd.random_number(1000, 1100))
    random_length.append(sd.random_number(10, 100))

while True:
    sd.start_drawing()
    for index, x in enumerate(x_coordinates):
        # Назначаю рандомное значение падения и отклонения на каждом шагу
        random_step_x = sd.random_number(-30, 30)
        random_step_y = sd.random_number(5, 15)
        # Создаю точку и рисую снежинку цветом фона
        point = sd.get_point(x_coordinates[index], y_coordinates[index])
        sd.snowflake(center=point, length=random_length[index], color=sd.background_color)
        # Изменяю координаты
        x_coordinates[index] += random_step_x
        y_coordinates[index] -= random_step_y
        # Создаю точку и рисую снежинку белым цветом
        point = sd.get_point(x_coordinates[index], y_coordinates[index])
        sd.snowflake(center=point, length=random_length[index], color=sd.COLOR_WHITE)
        # Добавляю индекс снежинки, которая по игреку меньше пятидесяти в список "старых" индексов
        if y_coordinates[index] < 50:
            old_index_list.append(index)
            # Сортирую список со "старыми" индексами
            sorted(old_index_list, reverse=True)
            # TODO 1) sorted() не меняет сам список, он возвращает результат - отсортированную копию списка
            # TODO результат надо куда-то записывать
            # TODO Вот наглядный пример
            # s = [1,2,3]
            # print(s)
            # sorted(s, reverse=True)
            # print(s)  TODO Изменится ли список?
            # s = [1,2,3]
            # print(s)
            # s = sorted(s, reverse=True)
            # print(s)  TODO А так?
            # TODO 2) сортировку надо реализовать один раз, а не после каждого добавленного индекса
            # TODO Нужно это, т.к. сортировка - трудозатратная операция
            # TODO и каждое её выполнение будет замедлять наш алгоритм
    # TODO Но если выполнить сортировку один раз, после цикла, то результат будет таким же,
    # TODO а операций мы выполним гораздо меньше!
    # Если в списке "старых" индексов, находится хотя бы одно значение, то захожу в цикл и
    # удаляю старые и сразу же добавляю новые значения, в списки координат и размеров снежинки,
    # по индексу из списка "старых" индексов,
    if any(old_index_list):
        for old_index in old_index_list:
            x_coordinates.pop(old_index)
            x_coordinates.insert(old_index, sd.random_number(0, 1200))
            y_coordinates.pop(old_index)
            y_coordinates.insert(old_index, sd.random_number(1000, 1100))
            random_length.pop(old_index)
            random_length.insert(old_index, sd.random_number(10, 100))
        # Очищаю список "старых" индексов
        if any(old_index_list):  # TODO Повторно вызывать это условие не стоит
            # TODO оно уже выполнено, раз код зашёл в этот if
            old_index_list.clear()

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
