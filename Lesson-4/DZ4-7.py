'''
Задание 7:
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

def fibo_gen(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        yield fact

num = int(input('Enter a number - '))
if num <= 15:
    func = fibo_gen(num)
else:
    func = fibo_gen(15)
    print(f'The first fifteen elements:\n(There are another {num - 15} elements.)')
for elem in func:
     print(elem)
