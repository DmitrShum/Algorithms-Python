'''Задание № 2. Закодируйте любую строку по алгоритму Хаффмана.'''

def sorted_dict(t_dict):
    '''Ф-ция сортировки словаря'''
    sort_val = sorted(t_dict.values())
    sort_dict = {}
    for i in range(len(sort_val)):
        for k in t_dict.keys():
            if t_dict[k] == sort_val[i]:
                sort_dict[k] = t_dict[k]
    return sort_dict

bit_dict = {}
text = 'beep boop!' # Строка, которрая будет кодироваться
text_set = set(text)
text_count = {i: text.count(i) for i in set(text)} # Формирую словарь - символ: кол-во
#print(text_count)

sort_text_count = sorted_dict(text_count)

'''Цикл для создания словаря - символ: код символа'''
while len(sort_text_count) > 1:
    sort_text_count = sorted_dict(sort_text_count)
    print(f'{sort_text_count=}')
    list_keys = list(sort_text_count.keys())
    sort_text_count[list_keys[0] + list_keys[1]] = sort_text_count[list_keys[0]] + sort_text_count[list_keys[1]]
    
    if len(list_keys[0]) > 1:
        for i in list_keys[0]:
            bit_dict[i] = '0' + bit_dict[i]
    else:
        bit_dict[list_keys[0]] = '0'

    if len(list_keys[1]) > 1:
        for i in list_keys[1]:
            bit_dict[i] = '1' + bit_dict[i]
    else:
        bit_dict[list_keys[1]] = '1'

    del sort_text_count[list_keys[0]]
    del sort_text_count[list_keys[1]]
    print(f'{bit_dict=}')


code_text = ''
for i in text:
    code_text += f'{bit_dict[i]} '

print(f'Текст "{text}" в кодировке Хаффмана: {code_text}')