# -*- coding: utf-8 -*-


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for name_of_good, number_of_good in goods.items():

    total_goods = 0
    total_price = 0

    store_number = store[number_of_good]

    if number_of_good in store:
        for things in store_number:
            total_goods += things['quantity']
            total_price += things['price']
        print(name_of_good, '-', total_goods, 'шт, стоимость', total_price, 'руб')
