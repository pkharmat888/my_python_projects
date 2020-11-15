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

# Создаю пустые списки для координат и размеров снежинки

x_coordinates = []
y_coordinates = []
random_length = []

# Шаг падения "у"
step = 10

# Генерирование координат и размеров снежинок и добавление их в списки
for number in range(N):
    x_coordinates.append(sd.random_number(0, 1200))
    y_coordinates.append(sd.random_number(1000, 1100))
    random_length.append(sd.random_number(10, 100))

while True:
    sd.start_drawing()
    for index, x in enumerate(x_coordinates):
        random = sd.random_number(-30, 30)   #Создаю переменную 'random' и присваиваю ей значение отклонения снежинки
        x += random #Добавляю рандом к каждому иксу
        y = y_coordinates[index] #Присваиваю переменной игрек значения из списка игреков и индексирую по энумерейту
        point = sd.get_point(x - random, y + step)
        if y > 50:
            sd.snowflake(center=point, length=random_length[index], color=sd.background_color)
        y_coordinates[index] -= step
        x_coordinates[index] += random   #Меняю значения в списках
        new_point = sd.get_point(x, y)
        if y > 50:
            sd.snowflake(center=new_point, length=random_length[index], color=sd.COLOR_WHITE)
        if y in range(500, 503):    #Добавляю новые снежинки
            for i in range(sd.random_number(1, 8)):
                x_coordinates.append(sd.random_number(0, 1200))
                y_coordinates.append(sd.random_number(1000, 1100))
                random_length.append(sd.random_number(10, 100))

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()
