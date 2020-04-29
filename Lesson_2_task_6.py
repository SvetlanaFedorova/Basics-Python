# Lesson 2 task 6

how_many = int(input('How many products do you want to enter? '))
n = 1
my_tuple = tuple()
my_list = list()
list_name = list()
list_price = list()
list_amount = list()
list_unit = list()
while n <= how_many:
    name = input('Enter the product name: ')
    list_name.append(name)
    price = input('Price of goods: ')
    list_price.append(price)
    amount = input('Amount of goods: ')
    list_amount.append(amount)
    unit = input('Unit of measurement: ')
    list_unit.append(unit)
    my_dict = {'name': name, 'price': price, 'amount': amount, 'unit': unit}
    my_tuple = n, my_dict
    my_list.append(my_tuple)
    n += 1
for el in my_list:
    print(el)
main_dict = ({'Name': list_name, 'Price': list_price, "Amount": list_amount, "Unit": list_unit})
for el in main_dict.items():
    print(el)






