# Lesson 6 Task 5

class Matrix:
    def __init__(self, a):
        my_list = []
        for i in a:
           my_list.append([j for j in i])
        self.a = my_list

    def __str__(self):
        self.c = str(f'{self.a[0]},\n{self.a[1]}')
        return self.c

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

m1 = Matrix([[11, 22], [33, 44], [33, 44]])
m2 = Matrix([[22, 33], [44, 55], [33, 44]])
print(m1 + m2)



