# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите целое число в диапазоне от 100 до 999: '))

if (a // 100) < 1 or (a // 100) > 9:
    print('Ввели неверное значение числа')
else:
    summa = (a // 100) + ((a % 100) // 10) + (a % 10)
    pr = (a // 100) * ((a % 100) // 10) * (a % 10)

    print('Сумма цифр трёхзначного числа равна', summa)
    print('Произведение цифр трёхзначного числа равна', pr)