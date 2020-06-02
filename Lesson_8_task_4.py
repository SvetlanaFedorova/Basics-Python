# Lesson 8 Task 4

from abc import ABC, abstractmethod
class OrgTc(ABC):

    def __init__(self, name, number, price, *args):
        self.name = {'Наименование': name}
        self.number = {'Количество': number}
        self.price = {'Цена': price}
        self.args = {'Характеристики': args}

    def __str__(self):
        return f'{self.name}\n {self.number}\n {self.price}\n {self.args}\n'

    @abstractmethod
    def my_list(self):
        pass

class Printer(OrgTc):
    def __init__(self, name, number, price):
        super().__init__(name, number, price)
        self.num_copy = {'кол-во копий: ': 1000}

    def my_list(self):
        num_printer = self.name, self.number, self.price, self.num_copy
        return num_printer

class Skaner(OrgTc):
    def __init__(self, name, number, price):
        super().__init__(name, number, price)
        self.num_quality = {'качество печати: ': 1000}

    def my_list(self):
        num_skaner = self.name, self.number, self.price, self.num_quality
        return num_skaner

class Xerox(OrgTc):
    def __init__(self, name, number, price):
        super().__init__(name, number, price)
        self.num_time = {'период службы в час.: ': 1000}

    def my_list(self):
        num_xerox = self.name, self.number, self.price, self.num_time
        return num_xerox

class OrgTcStore():
    def __init__(self):
        self.store_list = []

    def to_input(self, *nam):
        for el in nam:
            self.store_list.append(el)

class Department():
    def __init__(self, dep_name):
        self.dep_name = dep_name
        self.depart_list = []

    def to_take(self, nam):
        self.depart_list.append(nam)

while True:
    try:
        number = int(input('Введите количество принтеров: '))
        if number == int(number):
            break
    except ValueError:
        print('Вы ввели не число!')

printers = Printer('Принтеры', number, 100)
skaners = Skaner('Сканеры', input('Введите количество сканеров: '), 120)
xeroxs = Xerox('Ксероксы', input('Введите количество ксероксов: '), 130)
# Склад получает оборудование:
my_store = OrgTcStore()
my_store.to_input(printers.my_list(), skaners.my_list(), xeroxs.my_list())
print(f'На склад поступило: {my_store.store_list}\n')
# Склад перемещает оборудование в департаменты:
my_dep1 = Department('Отдел продаж')
my_dep2 = Department('Отдел закупок')
my_dep1.to_take(printers)
print(f'В {my_dep1.dep_name} поступило: {my_dep1.depart_list[0]}')
my_dep2.to_take(xeroxs)
print(f'В {my_dep2.dep_name} поступило: {my_dep2.depart_list[0]}')


