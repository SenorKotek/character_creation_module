"""Программа для вычисления квадратного корня."""
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    """Сообщает о результате или невозможности вычисления."""
    if your_number <= 0:
        return 'Корень из 0 или отрицательного числа извлечь нельзя'

    sqrt_num = calculate_square_root(your_number)

    return ('Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {sqrt_num}')


print(message)
print(calc(25.5))
