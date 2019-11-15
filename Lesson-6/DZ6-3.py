'''
Задание 3:
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
surname , position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
дохода с учетом премии ( get_total_income ). Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
'''

class Worker():
    def __init__(self, worker_name, worker_surname, worker_position, vage, bonus):
        self.worker_name = worker_name
        self.worker_surname = worker_surname
        self.worker_position = worker_position
        self.vage = vage
        self.bonus = bonus
        self._worker_income = {'vage': self.vage, 'bonus': self.bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.worker_surname} {self.worker_name}'
    def get_full_income(self):
        self.full_income = self._worker_income['vage'] + self._worker_income['bonus']
        return f'Full income of {self.worker_surname} {self.worker_name} is {self.full_income}'


name, surname = input("Enter the worker's name and surname - ").title().split()
position = input("Enter the worker's position - ")
vage = int(input('Enter the vage - '))
bonus = int(input('Enter the bonus - '))

person_1 = Position(name, surname, position, vage, bonus)
print(person_1.get_full_name())
print(person_1.worker_position)
print(person_1._worker_income)
print(person_1.get_full_income())
