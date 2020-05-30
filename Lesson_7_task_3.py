# Lesson 7 Task 3

class Cell:
    def __init__(self, amount_cell):
        self.amount_cell = amount_cell

    def __str__(self):
        return str(self.amount_cell)

    def __add__(self, other):
        return 'Результат сложения клеток: ' + str(self.amount_cell + other.amount_cell)

    def __sub__(self, other):
        return 'Результат вычитания клеток: ' + str(self.amount_cell - other.amount_cell)

    def __mul__(self, other):
        return 'Результат умножения клеток: ' + str(self.amount_cell * other.amount_cell)

    def __truediv__(self, other):
        return 'Результат деления клеток: ' + str(round(self.amount_cell / other.amount_cell, 0))

    def make_order(self, num):
        a = '\n' + '*' * (self.amount_cell % num)
        b = '\n'.join(['*' * num for i in range (self.amount_cell // num)])
        c = b + a
        return c

my_cell1 = Cell(34)
my_cell2 = Cell(12)
print(my_cell1)
print(my_cell2)
print(my_cell1 + my_cell2)
print(my_cell1 - my_cell2)
print(my_cell1 * my_cell2)
print(my_cell1 / my_cell2)
print(my_cell1.make_order(5))
