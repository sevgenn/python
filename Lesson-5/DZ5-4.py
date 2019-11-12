'''
Задание 4:
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

my_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('text_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lst = line.split()
        for key in my_dict:
            if key == int(lst[2]):
                lst[0] = my_dict[key]
        print(' '.join(lst))
