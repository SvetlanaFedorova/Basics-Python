# Lesson 5 Task 6

with open('my_file6.txt', encoding='utf-8') as f:
    my_dict = dict()
    for line in f:
        name, other = line.split(": ")
        for i in other.split():
            if i != "-":
                my_dict[name] = my_dict.get(name, 0) + int(i.split("(")[0])

    print(my_dict)


