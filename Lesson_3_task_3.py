# Lesson 3 Task 3
# -----------------------------первый вариант

def my_func(arg_1, arg_2, agr_3):
    my_list = [arg_1, arg_2, agr_3]
    my_list.remove(min(my_list))
    res = sum(my_list)
    return res

avarage = my_func(20, 30, 40)
print(avarage)

# ----------------------------второй вариант

def my_func(arg_1, arg_2, agr_3):
    return sum(sorted([arg_1, arg_2, agr_3])[1:])

avarage = my_func(20, 30, 40)
print(avarage)

