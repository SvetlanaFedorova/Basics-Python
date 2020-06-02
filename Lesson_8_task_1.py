# Lesson 8 Task 1

class Data():

    @classmethod
    def my_metod_1(cls, data_str):
        my_list = []
        for el in data_str.split('-'):
            my_list.append(int(el))
        return print(my_list)

    @staticmethod
    def my_metod_2(data_str):
        try:
            if data_str[6:] != int(data_str[6:]):
                pass
        except ValueError:
            print('Ошибка ввода года')
        if int(data_str[3:5]) <= 0 or int(data_str[3:5]) > 12:
            print('Ошибка ввода месяца')
        if data_str[2] != '-' or data_str[5] != '-':
            print('Ошибка ввода формата даты')
        return print(data_str)

Data.my_metod_1('17-06-1977')
Data.my_metod_2('17-06-1977')



