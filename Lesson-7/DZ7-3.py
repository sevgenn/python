'''
Задание 3:
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться​только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
'''

class Cell:
    def __init__(self, quant):
        self.quant = quant

    # def __del__(self):
    #     print(f'Object {self.quant} is deleted.')

    def __add__(self, other):
        return Cell(self.quant + other.quant)

    def __sub__(self, other):
        return (Cell(self.quant - other.quant) if self.quant >= other.quant else 'The result is negative.')

    def __mul__(self, other):
        return Cell(self.quant * other.quant)

    def __truediv__(self, other):
        return Cell(round(self.quant / other.quant))

    def __str__(self):
        return f'The result of operation is {self.quant}.'

    def make_order(self, num):
        for i in range(self.quant // num):
            print('*' * num)
        if (self.quant % num > 0):
            print('*' * (self.quant % num))


cell_1 = Cell(50)
cell_2 = Cell(60)
print(cell_1 + cell_2)
print(cell_1 - cell_2)

cell_3 = Cell(cell_1 * cell_2)
print(cell_1 * cell_2)
del cell_1
del cell_2
try:
    cell_3
except:
    print('cell_3 does not exist.')
else:
    print('cell_3 exists.')

cell_1 = Cell(80)
cell_2 = Cell(100)
cell_4 = Cell(cell_2 / cell_1)
print(cell_2 / cell_1)
del cell_1
del cell_2

cell_1 = Cell(35)
cell_1.make_order(12)