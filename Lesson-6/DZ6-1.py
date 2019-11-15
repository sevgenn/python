'''
Задание 1:
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
'''
#            Два вопроса, если можно:
#  1) Почему недостаточно импортировать TIME, а нужно отдельно импортировать SLEEP из TIME?
#  2) Почему в методе с FOR не видит переменную __COLOR, а с WHILE видит?

from time import sleep
import time

class TrafficLight_while:
    __color = 'Red'
    def running(self):
        time_end = time.time() + 60
        while time.time() < time_end:
            __color = 'Red'
            print(__color)
            sleep(7)
            __color = 'Yellow'
            print(__color)
            sleep(2)
            __color = 'Green'
            print(__color)
            sleep(7)
            __color = 'Yellow'
            print(__color)
            sleep(2)

class TrafficLight_for:
    __color = 'Red'
    def running(self):
        for t in range(1, 100):
            if __color == 'Red':
                print(__color)
                sleep(7)
                __color = 'Yellow'
            elif __color == 'Green':
                print(__color)
                sleep(7)
                __color = 'Yellow'
            elif __color == 'Yellow':
                print(__color)
                sleep(2)
                if t % 4 == 0:
                    __color = 'Red'
                else:
                    __color = 'Green'


light_1 = TrafficLight_while()
print(TrafficLight_while._TrafficLight_while__color)

light_1.running()

# light_2 = TrafficLight_for()
# print(TrafficLight_for._TrafficLight_for__color)
#
# light_2.running()
