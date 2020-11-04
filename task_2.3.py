# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите число: '))
num_or = num
num_end = 0
step = 1
step_2 = 1

while num != 0:
    a = (num % (10**(step + 1)))/10**step
    num = num - (a*10**step)
    step += 1

num = num_or
while step != 0:
    a = (num_or % (10 ** step_2)) / 10 ** (step_2-1)
    num_or = num_or - (a * 10 ** (step_2-1))

    num_end = num_end + a*10**(step-1)

    step_2 += 1
    step -= 1

print("Введёное значение: ", num)
print('Полученное значение: ', int(num_end))