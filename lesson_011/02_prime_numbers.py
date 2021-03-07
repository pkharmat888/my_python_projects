# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#
#     def __init__(self, n):
#         self.i = 0
#         self.n = n
#         self.prime_numbers = []
#
#     def __iter__(self):
#         self.i = 1
#         return self
#
#     def __next__(self):
#         while True:
#             self.i += 1
#             for prime in self.prime_numbers:
#                 if self.i % prime == 0:
#                     break
#             else:
#                 self.prime_numbers.append(self.i)
#                 return self.i
#             if self.i > self.n:
#                 raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     prime_numbers = []
#     counter = 1
#     while counter < n:
#         counter += 1
#         for prime in prime_numbers:
#             if counter % prime == 0:
#                 break
#         else:
#             prime_numbers.append(counter)
#             yield counter
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


# def mersenne_numbers_generator(number):
#     counter = 1
#     while counter < number:
#         mersenne_number = (2**counter) - 1
#         yield mersenne_number
#         counter += 1


def lucky_numbers(number):
    number = str(number)
    number_len = len(number)
    if number_len > 1:
        first_part = number[0:number_len // 2]
        first_part_list = map(int, first_part)
        first_part = sum(list(first_part_list))

        if number_len % 2 == 0:
            second_part = number[number_len // 2:]
        else:
            second_part = number[(number_len // 2) + 1:]

        second_part_list = map(int, second_part)
        second_part = sum(list(second_part_list))

        if first_part == second_part:
            return True
        else:
            return False
    else:
        return False


def palindrome_numbers(number):
    number = str(number)
    if number == number[::-1] and len(number) > 1:
        return True
    else:
        return False


#   Числа Мерсенна
def mersenne_numbers(number):
    mersenne_numbers_list = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191]
    if number in mersenne_numbers_list:
        return True
    else:
        return False


def prime_numbers_generator_with_func(n, func):
    prime_numbers = []
    counter = 1
    while counter < n:
        counter += 1
        for prime in prime_numbers:
            if counter % prime == 0:
                break
        else:
            prime_numbers.append(counter)
            if func(counter):       # В это условие можем передавать функцию фильтр и генерировать только те числа,
                yield counter       # которые соответствуют условию
                                    # Это первый способ применения фильтров


# for number in prime_numbers_generator_with_func(n=10000, func=lucky_numbers):
#     print(number)
#


def prime_numbers_generator(n):
    prime_numbers = []
    counter = 1
    while counter < n:
        counter += 1
        for prime in prime_numbers:
            if counter % prime == 0:
                break
        else:
            prime_numbers.append(counter)
            yield counter


#   Второй способ фильтрации
# res = filter(lucky_numbers, prime_numbers_generator(n=10000))
# print(list(res))
# res = filter(palindrome_numbers, prime_numbers_generator(n=10000))
# print(list(res))
# res = filter(mersenne_numbers, prime_numbers_generator(n=10000))
# print(list(res))

#   Третий способ фильтрации
res = [x for x in prime_numbers_generator(n=10000) if lucky_numbers(x)]
print(res)
res = [x for x in prime_numbers_generator(n=10000) if palindrome_numbers(x)]
print(res)
res = [x for x in prime_numbers_generator(n=10000) if mersenne_numbers(x)]
print(res)
