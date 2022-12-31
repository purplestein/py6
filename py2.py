from timeit import timeit
import time
from memory_profiler import profile

"""Переделал задачу из первого семинара, 
где заменил все расчеты на встроенную функцию."""

n = 10001
time_format = time.strftime("%H:%M:%S", time.gmtime(n))

print(timeit('time_format = time.strftime("%H:%M:%S", time.gmtime(10001))',
             number=1000))
"""Получил результат: 0.007956599991302937"""

"""Вариант с расчетом вручную оказался быстрее"""
print(timeit("""
seconds = 10001 % 3600
minutes = seconds // 60
hours = 10001 // 3600
seconds %= 60""", number=1000))
"""Получил результат: 0.00014869996812194586"""
