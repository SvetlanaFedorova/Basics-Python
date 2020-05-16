# Lesson 4 Task 6

from itertools import count
for i in count(int(input("введите первое число, для выхода 'q': "))):
    print(i, end='')
    exit = input()
    if exit == 'q':
        break

n = 0
from itertools import cycle
my_list = input('введите список через пробел: ').split()
my_iter = cycle(my_list)
quit = None

while quit != 'q':
    print(next(my_iter), end='')
    quit = input()

