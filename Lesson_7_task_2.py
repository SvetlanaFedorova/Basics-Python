# Lesson 7 Task 2

from abc import ABC, abstractmethod

class Clothes():
    def __init__(self, dress, shirt, skirt):
        self.dress = dress
        self.shirt = shirt
        self.skirt = skirt
        self._volume_production = self.dress + self.shirt + self.skirt

    @property
    def volume_production(self):
        if self._volume_production < 100:
            return f'Производство {self._volume_production} шт. НЕ рентабельно! (не менее 100 ед)'
        else:
            return f'Запуск производства в количестве: {self._volume_production} ед.!'

    @abstractmethod
    def consumption(self):
        print('Расчет расхода ткани:')

class Coat(Clothes):
    def __init__(self, v, n):
        self.size = v
        self.n = n

    def consumption(self):
        self.t_cons_coat = round(((self.size / 6.5 + 0.5) * self.n), 1)
        return self.t_cons_coat

class Costume(Clothes):
    def __init__(self, h, m):
        self.height = h
        self.m = m

    def consumption(self):
        self.t_cons_costume = round(((2 * self.height + 0.3) * self.m), 1)
        return self.t_cons_costume

clothes = Clothes(10, 10, 10)
print(clothes.volume_production)
clothes.consumption()

coat = Coat(44, 10)
print(f'Расход ткани на производство пальто: {coat.consumption()}')

costume = Costume(44, 10)
print(f'Расход ткани на производство костюмов: {costume.consumption()}')

print(f'Общий расход ткани: {coat.consumption() + costume.consumption()}')
