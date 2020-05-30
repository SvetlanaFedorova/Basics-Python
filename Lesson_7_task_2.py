# Lesson 7 Task 2

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, v, n):
        self.size = v
        self.n = n    # Количество единиц

    @property
    def consumption(self):
        return round(((self.size / 6.5 + 0.5) * self.n), 1)

class Costume(Clothes):
    def __init__(self, h, m):
        self.height = h
        self.m = m    # Количество единиц

    @property
    def consumption(self):
        return round(((2 * self.height + 0.3) * self.m), 1)

coat = Coat(50, 20)
print(f'Расход ткани на производство пальто: {coat.consumption}')

costume = Costume(50, 10)
print(f'Расход ткани на производство костюмов: {costume.consumption}')
