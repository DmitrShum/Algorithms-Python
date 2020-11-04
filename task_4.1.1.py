'''
Задание №1.
Вариант 1-й
При анализе изменялась длина вектора: 10, 100 и 1000
Вывод: вариант 1-й и 2-й имеют наилучшие характеристики, поскольку имеют линейную зависимость,
однако 2-й вариант требует наименьшего времени для выполнения задачи.
3-й вариан имеет зависимость близкую к Оn**2
'''

import random
import timeit
import cProfile

def func_ar(size):
    MIN_ITEM = 1
    MAX_ITEM = 100
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

array = func_ar(100)
array_2 = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        array_2 += [i]

print(array)
print(array_2)


s = '''
array_2 = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        array_2 += [i]
'''
array = func_ar(10)
print(timeit.timeit(s, number=100, globals=globals())) #0.002103799999999996

array = func_ar(100)
print(timeit.timeit(s, number=100, globals=globals())) #0.018514899999999994

array = func_ar(1000)
print(timeit.timeit(s, number=100, globals=globals())) #0.1854333
cProfile.run(s)
'''  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:2(<module>)
        1    0.000    0.000    0.003    0.003 <string>:3(func_ar)
        1    0.001    0.001    0.003    0.003 <string>:6(<listcomp>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.001    0.000    0.003    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1282    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}'''