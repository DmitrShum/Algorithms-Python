#4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 5
num = 0
max_num = 0
item_max = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

for _1 in array:
    num = 0
    for _2 in array:
        if _1 == _2:
            num += 1
    if num > max_num:
        max_num = num
        item_max = _1

print(array)
print(f'чаще всех в массиве встречается число: {item_max}')
