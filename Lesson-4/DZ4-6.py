'''
Задание 6:
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import count
from itertools import cycle

start = int(input('Enter start value - '))
stop = int(input('Enter end value - '))
some_list = input('Enter some phrase - ').split()

for num in count(start):
    if num > stop:
        break
    else:
        print(num)
print()

for word in cycle(some_list):
    if start <= stop:
        print(word)
        start += 1
    else:
        break