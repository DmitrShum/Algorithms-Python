'''
Задание №1.
Вариант 3-й
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

for i in array:
    if i % 2 == 0:
        array_2.append(i)
for k in array_2:
    for n in range(len(array)):
        if array[n] == k:
            array[n] = None
array_2 = []
for t in range(len(array)):
    if array[t] == None:
        array_2.append(t)



print(array)
print(array_2)

s = '''
array = func_ar(size)
array_2 = []

for i in array:
    if i % 2 == 0:
        array_2.append(i)
for k in array_2:
    for n in range(len(array)):
        if array[n] == k:
            array[n] = None
array_2 = []
for t in range(len(array)):
    if array[t] == None:
        array_2.append(t)
'''
size = 10
print(timeit.timeit(s, number=100, globals=globals())) #0.0034137000000000056

size = 100
print(timeit.timeit(s, number=100, globals=globals())) #0.07529150000000001

size = 1000
print(timeit.timeit(s, number=100, globals=globals())) #5.7468817
cProfile.run(s)
'''   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.105    0.105    0.109    0.109 <string>:2(<module>)
        1    0.000    0.000    0.003    0.003 <string>:3(func_ar)
        1    0.001    0.001    0.003    0.003 <string>:6(<listcomp>)
     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
     1000    0.001    0.000    0.003    0.000 random.py:244(randint)
     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.109    0.109 {built-in method builtins.exec}
      493    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      984    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1266    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}'''