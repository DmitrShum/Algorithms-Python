# Задание к Уроку №6
# Задание №1 с урока №3: В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9.

# Второй вариант решения Задачи
# ОС моего ПК 64-х разрядное, интерпретатор 32-х разрядный.

# Результат решения: Общий объём занимаемой памяти равен 1630
# 2. Данное решение занимает наименьший объём памяти, так как все вычисленные данные сразу выводятся пользователю

# Вариант №1 решения задачи из разбора
import sys

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

for i in range(START_DIV, END_DIV + 1):
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    #print(f'Числу {i} кратно {frequency} чисел')

# Вычисляю общий объём памяти, который занимают используемые объекты
def show(var):                                                    # Функция для вычисления объёма занимаемой памяти каждой переменной
    sum_var = sys.getsizeof(var)                                  # Объём памяти всего объекта
    #print(f'{type(var)=}, {sys.getsizeof(var)=}, {var=}')
    if hasattr(var, '__iter__') and not isinstance(var, str):
        for i in var:
            sum_var += show(i)                                    # Суммируем объём занимаемой памяти в каждой переменной в списке
    elif isinstance(var, str):
        sum_var += len(var)                                       # Суммируем объём занимаемой памяти каждого элемента в строке
        #print(len(var))
    #print(f'{sum_var=}')
    return sum_var

def show_all(*vars):                                              # Функция для вычисления объёма занимаемой памяти всех перечисленных переменных
    sum_all = 0
    for k in vars:
        sum_all += show(k)
    print(f'Общий объём занимаемой памяти равен {sum_all}')

show_all(START_NUM, START_DIV, END_NUM, END_DIV, frequency, i, j,
         range(START_DIV, END_DIV + 1), range(START_NUM, END_NUM + 1))