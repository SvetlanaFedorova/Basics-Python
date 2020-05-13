# Lesson 3 Task 4

# ---------------вариант 1. Через именную функцию
def my_func(x, y):
    res = x ** y
    return res

avarage = my_func(float(input('Enter real positive number: ')), int(input('Enter negative integer: ')))
print(avarage)

# ---------------вариант 2. Через анонимную ф-цию
res = lambda x, y: x ** y
print(res(float(input('Enter real positive number: ')), int(input('Enter negative integer: '))))


# --------------- вариант 3 Без использования **

def my_func(x, y):
    res = x
    for i in range(abs(y)-1):
        res *= x
    return f"{1/res:.2f}"

avarage = my_func(float(input('Enter real positive number: ')), int(input('Enter negative integer: ')))
print(avarage)


