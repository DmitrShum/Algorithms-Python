from collections import deque
from collections import Counter

hex_in_int = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
                      'c': 12, 'd': 13, 'e': 14, 'f': 15})
int_in_hex = Counter({0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                      12: 'c', 13: 'd', 14: 'e', 15: 'f'})
summ = deque()
transfer = 0

a = deque(input('Введите первое шестнадцатиричное число: '))
b = deque(input('Введите второе шестнадцатиричное число: '))

while len(a) != len(b):
    if len(a) < len(b):
        a.appendleft('0')
    else:
        b.appendleft('0')

# Cумма двух чисел
for i in range(len(a) - 1, -1, -1):
    result = hex_in_int[a[i]] + hex_in_int[b[i]] + transfer
    if result > 16:
        result -= 16
        transfer = 1
    else:
        transfer = 0
    summ.appendleft(int_in_hex[result])

if transfer == 1:
    summ.appendleft('1')
    transfer = 0


print(f'Первое число равно: {list(a)}')
print(f'Второе число равно: {list(b)}')
print(f'Сумма чисел равна: {list(summ)}')
