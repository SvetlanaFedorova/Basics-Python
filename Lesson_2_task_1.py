# LESSON 2 TASK 1

my_dict = dict(k_1='box_1', k_2='box_2')
my_list = list("lesson2")
my_tuple = tuple("invar")
my_set = set("abcd")
my_sp = [1, "2", my_dict, my_list, my_tuple, my_set]
for i, item in enumerate(my_sp):
    print(f'{i}) {item} - {type(item)}')
