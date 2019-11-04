'''
Задание 3:
Реализовать функцию my_func() , которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
'''

def my_func(var_1, var_2, var_3):
    l = [var_1, var_2, var_3]
    s = 0
    for el in l:
        s += max(l)
        l.remove(max(l))
    return s

######################## Вариант 1 #########################

n1 = int(input('Enter the first number - '))
n2 = int(input('Enter the second number - '))
n3 = int(input('Enter the third number - '))
print(my_func(n1, n2, n3))

######################## Вариант 2 #########################

lst = [int(input('Enter 3 number - ')) for x in range(3)]
print(my_func(lst[0], lst[1], lst[2]))