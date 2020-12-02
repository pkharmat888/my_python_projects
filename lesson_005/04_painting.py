# -*- coding: utf-8 -*-

import simple_draw as sd
# TODO импорты нужно указывать относительно рабочей директории в которой находится запускаемый файл
# TODO т.е. например: не import rainbow, а from picture import rainbow
import rainbow
import house
import snow
import smile
import tree
import grass
import sun

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

sd.resolution = (1900, 1000)

sd.background_color = sd.COLOR_BLACK

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# Создаю списки для снегопада
sd.start_drawing()
list_x = snow.snowfall_lists(x_start_point=0, x_endpoint=700, y_start_point=1000, y_endpoint=1100,
                             count_of_snowflakes=20)
# Создаю список цветов радуги
rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

# Создаю список для углов лучей солнца
sun_list = sun.sun_list()

# Рисую траву
grass.grass_draw(start_point=sd.get_point(0, 0), x_end_point=1900, length=80)

# Рисую дом
house.house_draw(house_point=sd.get_point(600, 200), house_color=sd.COLOR_DARK_RED)

# Рисую деревья
start_list = []
list_of_endpoints_final = tree.tree_with_leaves_draw(point=sd.get_point(1600, 200), angle=90, length=40, width=2,
                                                     list_of_endpoints=start_list)
tree.tree_draw(point=sd.get_point(1425, 400), angle=90, length=80, width=2)

# Рисую смайлик
smile.one_eye_smile_draw(x=900, y=380, color=sd.COLOR_DARK_GREEN)

l_lists = tree.leaves_lists(list_of_endpoints=list_of_endpoints_final)
sd.finish_drawing()
# Запускаю бесконечный цикл для анимирования и там выполняю функции отрисовки радуги, снегопада и падения листьев
while True:
    sd.start_drawing()
    sd.draw_background()
    sd.take_background()
    snow.snowfall_draw(x_coordinates=list_x[0], y_coordinates=list_x[1], random_length=list_x[2],
                       list_of_start_end_points=list_x[3], endpoint_of_snowfall=150)

    sun_list = sun.sun_draw(point=sd.get_point(1750, 850), angle_list=sun_list)

    rainbow.rainbow_draw(point=sd.get_point(950, 0), step=5, colors_list=rainbow_colors)

    tree.leaves_fall(x_coordinates=l_lists[0], y_coordinates=l_lists[1], endpoint_of_laves_fall=100)

    smile.eye_blinking(x=870, y=400, color=sd.COLOR_DARK_GREEN)
    if sd.user_want_exit():
        break
    sd.sleep(0.01)
    sd.finish_drawing()
sd.pause()
