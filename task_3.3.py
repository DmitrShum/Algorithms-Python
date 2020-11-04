#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
it_max = MIN_ITEM
p_max = 0
it_min = MAX_ITEM
p_min = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
for _ in range(SIZE):
    if array[_] > it_max:
        it_max = array[_]
        p_max = _
    if array[_] < it_min:
        it_min = array[_]
        p_min = _

array[p_max], array[p_min] = array[p_min], array[p_max]


print(array)
print(f'{it_max=} {p_max=}')
print(f'{it_min=} {p_min=}')