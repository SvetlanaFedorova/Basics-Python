# Lesson 5 Task 2

with open("my_file2.txt", 'r', encoding='utf-8') as f:
    i = 1
    while True:
        content = f.readline()
        my_list = content.split()
        if not content:
            break
        print(f'Длина {i} строки {len(my_list)} слов(а)')
        i += 1
print(f'Всего в файле оказалось {i-1} строк(и)')


