'''
Задание 5:
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

def multi_func(elem, next_elem):
    return elem * next_elem

rand_list = [n for n in range(100, 1001) if n % 2 == 0]

print(reduce(multi_func, rand_list))

##################### 2 Вариант вывода ######################

# Не смог отформатировать вывод в экспоненциальной форме
result = str(reduce(multi_func, rand_list))
divider = 10 ** (len(result) - 1)
res = round(int(result) / divider, 10)

print(f'{res}e+{len(result) - 1}')

