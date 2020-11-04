# Задание № 1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

def random_array(size, min_item, max_item):
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array

def bubble(arr):
    n = 1
    while n < len(arr):
        takt = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                takt += 1
        if takt == 0:    # Сортировка завершается, если все элементы уже отсортированы
            break
    return arr

array = random_array(10, -100, 100)
print(f'Исходный массив: \n{array}')
array = bubble(array)
print(f'Отсортированный массив: \n{merge(array)}')