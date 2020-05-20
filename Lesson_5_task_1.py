# Lesson 5 Task 1

with open("my_file.txt", 'w', encoding='utf-8') as f:
    while True:
        content = f.write(input('Введите данные для файла: '))
        if not content:
            break
        f.write('\n')



