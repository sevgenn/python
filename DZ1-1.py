'''
Задание 1:
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
'''

var_int_or_str = 45
print(var_int_or_str)
var_float = 45.6
print(var_float)
var_int_or_str = 'It is a string now.'
print(var_int_or_str + ' ' + str(var_float))

n = int(input('Enter a natural number: '))
name = input('Enter your name: ')
print(f'This is a new number {n * 3}, {name}.')
