'''
Задание 4:
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

n = int(input('Введите целое положительное число: '))
while n <= 0:
    n = int(input('Введите целое положительное число: '))

rest = n
count = 0
maximum = 0
while rest != 0:
    rest = rest // 10
    count += 1          # Количество разрядов в числе
while count != 0:
    rest = n
    rest = rest % 10
    if rest >= maximum:
        maximum = rest
    n = n // 10
    count -= 1
print(maximum)
