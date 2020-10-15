# -*- coding: utf-8 -*-


a1, b1 = 179, 37
count = 0
a = a1
b = b1

while a >= b:
    a -= b
    count += 1
print('Целочисленное деление ', a1,' на ', b1,' дает', count)