# Lesson 4 Task 4

from random import randint

my_list = [randint(-5, 5) for i in range(15)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Первоначальный список: {my_list} \n'
      f'Обработанный список: {new_list}')



