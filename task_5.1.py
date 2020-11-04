from collections import namedtuple
from collections import deque

num = int(input('Введите количество предприятий: '))
Company = namedtuple('Company', 'name, quarter_1, quarter_2, quarter_3, quarter_4, year')
companies = deque()                             #Очередь для записи данных о предприятиях
years = 0
average_low = deque()

for i in range(1, num + 1):
    print(f'Ввод данных предприяия № {i}')
    name = input('Введите название преприятия: ')
    quarter_1 = int(input('Введите прибыль за первый квартал: '))
    quarter_2 = int(input('Введите прибыль за второй квартал: '))
    quarter_3 = int(input('Введите прибыль за третий квартал: '))
    quarter_4 = int(input('Введите прибыль за четвёртый квартал: '))
    year = quarter_1 + quarter_2 + quarter_3 + quarter_4
    companies.append((Company(name, quarter_1, quarter_2, quarter_3, quarter_4, year)))
    years += year

average = years / num
print(f'Средняя прибыль за год: {average}')
print('Предприятия с доходом выше среднего:')

for n in companies:
    if n.year > average:
        print(n.name)
    else:
        average_low.append(n.name)

print('Предприятия с доходом ниже среднего:')
for k in average_low:
    print(k)


