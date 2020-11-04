# Задание № 3
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой — не больше медианы.

import random

def random_array(size, min_item, max_item):
    if size % 2 == 0:
        size += 1
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array

# Функция поиска мединаны
def mediana(arr):
    while len(arr) != 1:
        arr.remove(min(arr))
        arr.remove(max(arr))
    med = arr[0]
    return med

# Сортировка для удобства проверки полученной медианы
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

# Выполнение кода
array = random_array(11, 0, 10)
print(f'Исходный массив: \n{array}')
print(f'Отсортированный массив: \n{bubble(array)}') # Сортировка для удобства проверки полученной медианы
print(f'Медиана {mediana(array)}')