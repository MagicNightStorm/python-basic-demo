"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


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
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(is_odd, numbers_list))
    if filter_type == EVEN:
        return list(filter(is_even, numbers_list))
    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list))

if __name__ == "__main__":
    # pow_numbers = power_numbers(1, 7, 19, -15, 25, 2, -1)
    # print(pow_numbers)
    #
    # odd_numbers = filter_numbers([1, 2, 100, 25, 199], ODD)
    # print(odd_numbers)
    #
    # even_numbers = filter_numbers([1, 2, 100, 25, 199], EVEN)
    # print(even_numbers)

    prime_numbers = filter_numbers([0,1,2,3,4,5,6,7,8,9,10,11], PRIME)
    print(prime_numbers)
