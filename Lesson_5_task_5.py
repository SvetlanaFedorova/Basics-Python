# Lesson 5 Task 5

from functools import reduce
def my_func(prev_el, el):
    return prev_el + el

num_list = []
i = 0
import random
while i < 11:
    i += 1
    num_list.append(random.randint(0, 10))

with open("my_file5.txt", 'w', encoding='utf-8') as f:
    print(num_list, file=f)
    print(f'Сумма чисел в файле: {reduce(my_func, (num_list))}')

