from memory_profiler import memory_usage
import math

"""Задача из первого примера, но теперь подсчитаем память"""
def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper

@memory
def my_func(x, y):
    x = x ** y
    return x
"""Выполнение заняло 0.0078125 Mib"""

@memory
def my_func2(x, y):
    math.pow(x, y)
"""Выполнение заняло 0.0 Mib"""

my_func(2, 5)
my_func2(2, 5)

