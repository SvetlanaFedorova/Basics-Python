# Lesson 2 task 5

el = int(input('Enter a positive integer: '))
my_list = [7, 5, 3, 3, 2]
i = 0
for n in my_list:
    if el <= n:
        i += 1
my_list.insert(i, el)
print(my_list)
