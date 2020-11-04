import timeit
import cProfile

ser_num = int(input('Введите порядковый номер простого числа: '))

def func_sieve(ser_num):
    n = 2
    sieve = []
    while True:
        krat = 0
        for i in range(2, n + 1):
            if n % i == 0:
                krat += 1
            if krat > 1:
                continue
        if krat == 1:
            sieve.append(n)
        if len(sieve) == ser_num:
            break
        n += 1
    return sieve[ser_num - 1]

siev = func_sieve(ser_num)
print(f'Простое число с порядковым номером {ser_num} равно {siev}')

s = '''
siev = func_sieve(ser_num)'''
ser_num = 10
print(timeit.timeit(s, number=100, globals=globals())) #0.008775899999999837

ser_num = 20
print(timeit.timeit(s, number=100, globals=globals())) # 0.03851130000000014

ser_num = 40
print(timeit.timeit(s, number=100, globals=globals())) # 0.20031799999999977

ser_num = 80
print(timeit.timeit(s, number=100, globals=globals()))  # 1.0742017000000001
cProfile.run(s)
'''   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:2(<module>)
        1    0.011    0.011    0.011    0.011 <string>:2(func_sieve)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
      408    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''