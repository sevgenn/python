'''
Задание 7:
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
'''

class ComplexNumber:
    def __init__(self, c):
        self.compl = c

    def __add__(self, other):
        return ComplexNumber(self.compl + other.compl)

    def __mul__(self, other):
        return ComplexNumber(self.compl * other.compl)

    def __str__(self):
        return f'Result of operation is {self.compl}.'

c_1 = ComplexNumber(complex(1, -1))
c_2 = ComplexNumber(complex(3, 6))
print(c_1 + c_2)
print(c_1 * c_2)