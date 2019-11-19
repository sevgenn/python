'''
Задание 1:
Реализовать класс​Matrix​(матрица). Обеспечить перегрузку конструктора класса (метод __init__()​),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — ​система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода ​__str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода ​__add__() для реализации операции сложения двух объектов класса​Matrix​(двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, col, *args):
        num = [n for n in args]
        matrix = [num[i * len(num) // col : (i+1) * len(num) // col] for i in range(col)]
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(str(i) for i in row) for row in self.matrix)

    def __add__(self, other):
        s = 0
        result = []
        for i in range(len(self.matrix)):
            res = []
            for j in range(len(self.matrix[i])):
                s = self.matrix[i][j] + other.matrix[i][j]
                res.append(s)
            result.append(res)
        print(result)
        return '\n'.join('\t'.join(str(i) for i in row) for row in result)

m_1 = Matrix(2, 1, 2, 3, 1, 2, 3)
m_2 = Matrix(2, 2, 3, 4, 2, 3, 4)
print(m_1.matrix)
print(m_1)
print(m_2.matrix)
print(m_2)
print(m_1 + m_2)