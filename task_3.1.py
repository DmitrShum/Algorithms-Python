#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

num = [[0]*3 for _ in range(8)]
for i in range(2, 100):
    for n in range(2, 10):
        if i == 2:
            num[n - 2][0] = n
            num[n - 2][1] =  '- имеет кратных чисел в количестве:'
        if i % n == 0:
            num[n - 2][2] += 1

for line in num:
    for c in line:
        print(f'{c}', end='')
    print('')