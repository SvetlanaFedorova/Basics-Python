# Lesson 4 Task 2

my_list = [5, 8, 1, 22, 2, 0, 55, 66]
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el-1]]
print(new_list)
