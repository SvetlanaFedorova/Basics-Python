# Lesson 3 Task 1

def my_func(arg_1, arg_2):
    try:
        print(arg_1 / arg_2)
    except ZeroDivisionError:
        print('division by zero!')
    return


my_func(int(input('Enter 1 value: ')), int(input('Enter 2 value: ')))
