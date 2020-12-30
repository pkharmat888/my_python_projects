# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        # TODO Такая проверка - антипаттерн,
        # TODO В таких случаях стоит использовать проверку isinstance(other, Class)
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Mud()
        elif other.name == 'Пар':
            return RainFall()
        else:
            return None

    def __str__(self):
        return ''.join(self.name)


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Вода':
            return Storm()
        elif other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Земля':
            return Dust()
        else:
            return None

    def __str__(self):
        return ''.join(self.name)


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Вода':
            return Steam()
        elif other.name == 'Земля':
            return Lava()
        elif other.name == 'Воздух':
            return Lightning()
        else:
            return None

    def __str__(self):
        return ''.join(self.name)


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if other.name == 'Вода':
            return Mud()
        elif other.name == 'Воздух':
            return Dust()
        elif other.name == 'Огонь':
            return Lava()
        else:
            return None

    def __str__(self):
        return ''.join(self.name)


class Storm:

    def __init__(self):
        self.name = 'Гроза'

    def __str__(self):
        return ''.join(self.name)


class Steam:

    def __init__(self):
        self.name = 'Пар'

    def __add__(self, other):
        if other.name == 'Вода':
            return RainFall()

    def __str__(self):
        return ''.join(self.name)


class Mud:

    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return ''.join(self.name)


class Lightning:

    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return ''.join(self.name)


class Dust:

    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return ''.join(self.name)


class Lava:

    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return ''.join(self.name)


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())


class RainFall:

    def __init__(self):
        self.name = 'Ливень'

    def __str__(self):
        return ''.join(self.name)


print(Steam(), '+', Water(), '=', Steam() + Water())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
