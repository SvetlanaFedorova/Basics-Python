# Lesson 5 Task 3

avarage = 0
i = 0
with open('my_file3.txt', 'r', encoding='utf-8') as f:
    print('Определить перечень сотрудников с доходом менее 20000:')
    while True:
        content = f.readline()
        if not content:
            break
        salary = float(content.split()[1])
        avarage = round((avarage + salary), 1)
        if salary < 20000:
            print(content.split()[0])
        i += 1
print(f'Средняя величина дохода всех сотрудников {avarage / i}')

