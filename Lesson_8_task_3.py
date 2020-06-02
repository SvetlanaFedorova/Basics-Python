# Lesson 8 Task 3

class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

def my_list():
    ex = False
    res_line = []
    while ex == False:
        numbers = input('Введите число, или stop для выхода: ').split()
        for num in numbers:
            if 'stop' in num:
                ex = True
                break
            res_line.append(num)
    return print(res_line)


try:
    if type(num) == type(int) :
        raise MyOwnError("Вы ввели ноль, делить на ноль нельзя")
except MyOwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {1000 / inp_data}")

a = my_list()