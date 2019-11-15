'''
Задание 5:
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.
'''

class Stationery:
    title = 'stationery'
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    title = 'pen'
    def draw(self):
        print('Запуск отрисовки ручкой.')

class Pencil(Stationery):
    title = 'pencil'
    def draw(self):
        print('Запуск отрисовки карандашом.')

class Handle(Stationery):
    title = 'handle'
    def draw(self):
        print('Запуск отрисовки маркером.')

pen_blue = Pen()
pencil_lead = Pencil()
handle_green = Handle()

print(pen_blue.title)
pen_blue.draw()
pencil_lead.draw()
handle_green.draw()

Stationery.draw('something') # ??????????