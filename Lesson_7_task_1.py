# Lesson 7 Task 1

class Matrix:
    def __init__(self, a):
        my_list = []
        for i in a:
            my_list.append([j for j in i])
        self.a = my_list

    def __str__(self):
        return '\n'.join([' '.join([str(el) for el in line]) for line in self.a]) + '\n'

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                summa = other.a[i][j] + self.a[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

m1 = Matrix([[11, 22, 33], [33, 44, 22], [33, 44, 11]])
m2 = Matrix([[22, 33, 11], [44, 55, 33], [33, 44, 22]])
m3 = Matrix([[22, 33, 11], [44, 55, 33], [33, 44, 22]])
print(m1)
print(m2)
print(m3)
print(m1 + m2 + m3)



