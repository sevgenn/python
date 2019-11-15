'''
Задание 2:
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''

############## 1 Вариант ###################
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self, thikness_cm):
        self.thikness_cm = thikness_cm
        weight = self._length * self._width * 0.025 * thikness_cm
        print(f'Weight of asphalt is {weight} tonn.')

mkad = Road(5000, 20)
mkad.asphalt(5)

################ 2 Вариант ####################
class Road_2:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        thikness_cm = int(input('Enter a thikness of the layer in cm - '))
        weight = self._length * self._width * 0.025 * thikness_cm
        print(f'Weight of asphalt is {weight} tonn.')

mkad = Road_2(5000, 20)
mkad.asphalt()