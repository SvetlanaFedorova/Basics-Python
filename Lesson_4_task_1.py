# Lesson 4 Task 1

from sys import argv

def salary():
      try:
            hour, rate, prize = map(int, argv[1:])
            salary = hour * rate + prize
            print(f'Выработка в часах: {hour},\n '
                  f'Ставка в час: {rate} руб.,\n '
                  f'Премия: {prize} руб.,\n '
                  f'Заработная плата: {salary} руб.')
      except ValueError:
            print('Некорректный ввод. Введите три числа.')

salary()
