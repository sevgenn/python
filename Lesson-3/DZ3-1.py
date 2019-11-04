'''
Задание 1:
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
'''

def division(var_1, var_2):
    try:
        print(f'{var_1} : {var_2} = {(var_1 / var_2):.2f}')
    except ZeroDivisionError:
        print('Division by zero!')

user_answer = 'Answer of an user'
while user_answer != 'n':
    num1 = float(input('Enter the first number - '))
    num2 = float(input('Enter the second number - '))
    division(num1, num2)
    user_answer = input('Try again or not? y/n - ').lower()
