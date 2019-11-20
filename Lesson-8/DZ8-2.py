'''
Задание 2:
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
'''

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

a, b = input('Enter divisor and dividend by space - ').split()

try:
    if int(b) == 0:
        raise OwnError('It\'s impossible to divide by zero.')
    res = int(a) / int(b)
except ValueError:
    print('You should enter numbers not strings!')
except OwnError as err:
    print(err)
else:
    print(f'The result of division is {res}.')

