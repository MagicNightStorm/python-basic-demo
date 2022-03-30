"""
Домашнее задание №1
Функции и структуры данных
"""

ODD = "odd"
EVEN = "even"
PRIME = "prime"


def power_numbers(*numbers):
    return [number ** 2 for number in numbers]


def is_odd(n):
    return n % 2


def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def filter_numbers(numbers_list, filter_type):
    if filter_type == ODD:
        return list(filter(is_odd, numbers_list))
    if filter_type == EVEN:
        return list(filter(is_even, numbers_list))
    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list))
