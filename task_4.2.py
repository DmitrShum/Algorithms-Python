import timeit
import cProfile

ser_num = int(input('Введите порядковый номер простого числа: '))

def func_sieve(ser_num):
    if ser_num < 200:
        n = 1250
    else:
        n = ser_num * 5 * (ser_num // 100)    # Примитивно рассчитываю переменную n в зависимости от входной переменной ser_num
    nums = [i for i in range(n)]
    sieve = []
    k = 2
    while True:
        if nums[k] != 0:
            sieve.append(nums[k])
            if len(sieve) == ser_num:  # Ограничиваю вычисление векторна натуральных чисел до заданного значения
                break
            j = k + k
            while j < n:
                nums[j] = 0
                j += k
        k += 1
    return sieve[ser_num - 1]

siev = func_sieve(ser_num)
print(f'простое число с порядковым номером {ser_num} равно {siev}')

s = '''
siev = func_sieve(ser_num)
'''
ser_num = 10
print(timeit.timeit(s, number=100, globals=globals())) # 0.04044049999999988

ser_num = 20
print(timeit.timeit(s, number=100, globals=globals())) # 0.04552239999999985

ser_num = 40
print(timeit.timeit(s, number=100, globals=globals())) # 0.05146150000000027

ser_num = 80
print(timeit.timeit(s, number=100, globals=globals())) # 0.05809370000000014
cProfile.run(s)
'''  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:2(<module>)
        1    0.001    0.001    0.001    0.001 <string>:2(func_sieve)
        1    0.000    0.000    0.000    0.000 <string>:7(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
       80    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       80    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''