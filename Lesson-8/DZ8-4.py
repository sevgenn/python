'''
Задание 4-6:
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
    Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
    Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''

class Warehouse:
    def __init__(self):
        self.goods = {}
    def in_storage(self, model, quantity):
        product = [model, quantity]
        if product[0] in self.goods:
            self.goods[product[0]] += product[1]
        else:
            self.goods[product[0]] = product[1]
        return self.goods
    def out_storage(self, model, quantity):
        product = [model, quantity]
        if product[0] in self.goods and self.goods[product[0]] >= product[1]:
            self.goods[product[0]] -= product[1]
        else:
            print('Lack of goods.')
        return self.goods
    def __str__(self):
        return f'Goods remaining in the warehouse: {self.goods}'

class Equipment:
    def __init__(self, quantity):
        self.quantity = quantity
    def print_method(self):
        return self.quantity

class Printer(Equipment):
    def __init__(self, quantity):
        self.quantity = quantity
    def __str__(self):
        return f'{self.quantity}'

class Scaner(Equipment):
    def __init__(self, quantity):
        self.quantity = quantity
    def __str__(self):
        return f'{self.quantity}'

class Copier(Equipment):
    def __init__(self, quantity):
        self.quantity = quantity
    def __str__(self):
        return f'{self.quantity}'

samsung_555 = Printer(50)
print(samsung_555)
storage = Warehouse()

name = input('Enter name of product: ')
num = input('Enter the quantity of incoming product: ')
while True:
    try:
        if num.isdigit():
            num = int(num)
            break
    except ValueError:
        print('Not a number.')
    num = input('Enter the quantity of incoming product (number): ')
storage.in_storage(name, num)

name = input('Enter name of product: ')
num = int(input('Enter the quantity of incoming product: '))
storage.in_storage(name, num)
print(storage)

name = input('Enter name of product: ')
num = int(input('Enter the quantity of outgoing product: '))
storage.out_storage(name, num)
print(storage)

name = input('Enter name of product: ')
num = int(input('Enter the quantity of outgoing product: '))
storage.out_storage(name, num)
print(storage)



