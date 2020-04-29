# Lesson 2 task 3
# вариант через dict

num = int(input("Enter integer from 1 to 12: "))
while num < 0 or num > 12:
    num = int(input("Error! Enter integer from 1 to 12: "))
season = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
          7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(season[num])


# вариант через list

num = int(input("Enter integer from 1 to 12: "))
while num < 0 or num > 12:
    num = int(input("Error! Enter integer from 1 to 12: "))
season = ('winter', 'winter', 'spring', 'spring', 'spring', 'summer',
          'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter')
print(season[num - 1])
