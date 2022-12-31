import math
from timeit import timeit

"""Переделал функцию возведения в квадрат 
с помощью встроенного math.pow"""

"""До: 0.0016959999920800328"""


def my_func(x, y):
    x = x ** y
    return x


"""После: 0.000507500022649765"""


def my_func2(x, y):
    math.pow(x, y)


my_func(2, 5)
my_func2(2, 5)

print(timeit('my_func(2, 5)', globals=globals(), number=1))
print(timeit('my_func2(2, 5)', globals=globals(), number=1))
