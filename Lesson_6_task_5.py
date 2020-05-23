# Lesson 6 Task 5

class Stationery:
    def __init__(self, title='Канцелярские принадлежности'):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать тем, что у нас есть: {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Если нужно написать текст, возъмем {self.title} ручку')

class Pensil(Stationery):
    def draw(self):
        print(f'Если понадобится накидать контуры, воспользуемся {self.title} карандашом')

class Handle(Stationery):
    def draw(self):
        print(f'Если хоти выделить детали берем {self.title} маркер')

write = Stationery()
write.draw()
pen = Pen('Шариковую')
pen.draw()
pensil = Pensil('Простым')
pensil.draw()
handle = Handle('Черный')
handle.draw()


