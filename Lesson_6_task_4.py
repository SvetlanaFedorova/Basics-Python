# Lesson 6 Task 4

class Car:
    auto1 = 'Автомобиль'

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Это машина: {self.name} (цвет {self.color}) машина относится к Полиции - {self.is_police}')

    def go(self):
        print(f'{self.name}: машина поехала')

    def stop(self):
        print(f'{self.name}: машина остановилась')

    def turn(self, traffic):
        print(f'{self.name}: машина повернула {"налево" if traffic == 0 else "направо"}')

    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed}'

class TownCar(Car):
    auto2 = 'Городской автомобиль'

    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость машины: {self.speed}"

class WorkCar(Car):
    auto3 = 'Служебный автомобиль'

    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость машины: {self.speed}"

class SportCar(Car):
    auto4 = 'Спортивный автомобиль'

    def show_speed(self):
        return f'{self.name}: скорость машины: {self.speed}. Начинаем взлет!' \
            if self.speed > 180 else f" {self.name}: Скорость машины: {self.speed}"

class PoliceCar(Car):
    auto5 = 'Полицейский автомобиль'

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

police_car = PoliceCar('Полицейская', 'желтый', 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('пикап', 'оранжевый', 50)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('Ламбарджини', 'желтый', 180)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('Lada Granta', 'голубой', 60)
town_car.go()
town_car.turn(1)
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')



