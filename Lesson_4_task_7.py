# Lesson 4 Task 7

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

g = fibo_gen()
z = 0
for i in g:
    if z == 15:
        break
    else:
        z += 1
        print(f'Факториал {z} = {i}')
