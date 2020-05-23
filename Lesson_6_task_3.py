# Lesson 6 Task 3

class Worker:
    def __init__(self, name, surname, position, num_wage, num_bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': num_wage, 'bonus': num_bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'

staff = Position('Ivanov', 'Alex', 'It-manager', 1000, 10000)
print(staff.get_full_name())
print(staff.position)
print(staff.get_full_profit())









