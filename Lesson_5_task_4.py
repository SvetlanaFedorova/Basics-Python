# Lesson 5 Task 4

with open('my_file4.txt', encoding='utf-8') as f:
    with open('my_file4new.txt', 'w', encoding='utf-8') as f_new:
        while True:
            content = f.readline()
            if not content:
                break
            if content.split()[0] == 'One':
                print((content.replace('One', 'Один')).strip(), file=f_new)
            elif content.split()[0] == 'Two':
                print((content.replace('Two', 'Два')).strip(), file=f_new)
            elif content.split()[0] == 'Three':
                print((content.replace('Three', 'Три')).strip(), file=f_new)
            elif content.split()[0] == 'Four':
                print((content.replace('Four', 'Четыре')).strip(), file=f_new)





