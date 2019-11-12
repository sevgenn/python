'''
Задание 5:
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint

n = int(input('Enter quantity of numbers: '))
with open('text_5.txt', 'w', encoding='utf-8') as f:
    number_list = [str(randint(0, 100)) for i in range(n)]
    f.write(' '.join(number_list))

with open('text_5.txt', 'r', encoding='utf-8') as f:
    content = f.read().split()

result = [int(i) for i in content]
print(f'Sum of numbers in the file: {sum(result)}')