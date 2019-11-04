'''
Задание 4:
Программа принимает действительное положительное число x и целое отрицательное число
y. Необходимо выполнить возведение числа x в степень y . Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''


def my_func_1(x, y):
    return x ** y

def my_func_2(x, y):
    res = 1
    for i in range(-y):     # range(abs(y))
        res *= 1 / x
    return res

while True:
    try:
        x = float(input('Enter real number - '))

    except ValueError:
        continue
    while True:
        try:
            y = int(input('Enter negative integer - '))
        except ValueError:
            continue
        if  y >= 0:
            continue
        else:
            break
    break

print(my_func_1(x, y))
print(f'{my_func_2(x, y):.10f}')
