# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
item_max = 0
p_max = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

for _ in range(SIZE):
    if array[_] < 0:
        if item_max == 0:
            item_max = array[_]
            p_max = _
        if item_max < array[_]:
            item_max = array[_]
            p_max = _

print(array)
print(f'Максимальное отрицательное число {item_max}, c индексом {p_max}')