# Lesson 6 Task 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        my_calc = (self._length * self._width * 25 * 5)/1000
        print(f'При длине дороги: {self._length} м. '
              f'и ширине дороги: {self._width} м. '
              f' Получаемая масса асфальта: {my_calc} т.')
my_road = Road(5000, 20)
my_road.calc()

