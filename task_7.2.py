# Задание № 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def random_array(size, min_item, max_item):
    array = [round(random.uniform(min_item, max_item), 2) for _ in range(size)]
    return array

def merge(arr):
    if len(arr) > 2:
        result = []
        portion_1 = merge(arr[:len(arr) // 2])
        portion_2 = merge(arr[len(arr) // 2:])

        while portion_1 and portion_2:
            if portion_1[0] <= portion_2[0]:
                result.append(portion_1[0])
                del portion_1[0]
            else:
                result.append(portion_2[0])
                del portion_2[0]

        if portion_1: result.extend(portion_1)
        if portion_2: result.extend(portion_2)

        arr = result


    elif len(arr) > 1 and arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]

    return arr

array = random_array(10, 0, 50)

print(f'Исходный массив: \n{array}')
print(f'Отсортированный массив: \n{merge(array)}')
