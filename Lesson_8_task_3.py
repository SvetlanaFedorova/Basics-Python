# Lesson 8 Task 3

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

def my_list():
    res_line = []
    while True:
        num = input('Введите число, или stop для выхода: ')
        if 'stop' in num:
            break
        try:
            num = int(num)
        except ValueError:
            print('Вы ввели не число!')
        except OwnError as err:
            print(err)
        else:
            res_line.append(num)
    return print(res_line)

a = my_list()
