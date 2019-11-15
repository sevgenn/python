'''
Задание 4:
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed ,
color , name , is_police (булево). А также методы: go, stop, turn (direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed . При значении скорости свыше 60
( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The car {self.name} is moving.')
    def stop(self):
        print(f'The car {self.name} stopped.')
    def turn(self, direction):
        self.direction = direction
        print(f'The car {self.name} turns {self.direction}.')
    def show_speed(self):
        print(f'The car speed is {self.speed}.')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police)
    def speed_limit(self, limit = 60):
        self.limit = limit
        if self.speed > limit:
            print(f'{self.name}, your speed is {self.speed} km/h. Reduce your speed!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police)
    def speed_limit(self, limit = 40):
        self.limit = limit
        if self.speed > self.limit:
            print(f'{self.name}, your speed is {self.speed} km/h. Reduce your speed!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name, is_police)

car_1 = TownCar(90, 'red', 'Mazda')
car_2 = WorkCar(60, 'white', 'Ford')

print(car_1.name)
car_1.go()
car_1.turn('right')
car_1.speed_limit()
car_1.speed = 40
car_1.show_speed()
car_1.stop()
print(car_2.is_police)

