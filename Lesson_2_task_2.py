# Lesson 2 task 22

us_list = list(input("Enter some numbers: "))
n, i = 0, 1
new_list = list()
while i <= (len(us_list)//2):
    us_list[n], us_list[n + 1] = us_list[n + 1], us_list[n]
    new_list.extend([us_list[n], us_list[n + 1]])
    n, i = n + 2, i + 1
if len(us_list) % 2 != 0:
    new_list.extend([us_list[-1]])
print(new_list)

