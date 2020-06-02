# Lesson 8 Task 2

class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = int(input("Введите положительное не нулевое число в знаменатель деления: "))

try:
    if inp_data == 0:
        raise MyOwnError("Вы ввели ноль, делить на ноль нельзя")
except MyOwnError as err:
    print(err)
else:
    print(f"Все хорошо. Результат деления: {1000 / inp_data}")

