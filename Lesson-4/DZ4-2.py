'''
Задание 2:
Представлен список чисел. Необходимо вывести элементы исходного списка, значения
которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
формирования списка использовать генератор.
'''

from random import randint

# input_list = [int(i) for i in input('Enter a sequence of numbers by a space - ').split()] # 1 вариант формирования
random_list = [randint(-10, 10) for i in range(10)]                                         # 2 вариант формирования

new_list = [random_list[i] for i in range(1, len(random_list)) if random_list[i] > random_list[i-1]]
print(random_list)
print(new_list)
