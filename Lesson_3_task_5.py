# Lesson 3 Task 5

sum = 0
try:
    while sum != 'q':
        for i in map(int, input("To exit, click: 'q'\nEnter numbers using the space bar: \n").split()):
            sum += i
        print(sum)
except ValueError:
    print(sum)



