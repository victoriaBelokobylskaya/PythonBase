# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} go')

    def stop(self):
        print(f'Car {self.name} stop')

    def turn(self, direction):
        print(f'Car {self.name} turn {direction}')

    def show_speed(self):
        print(f'Car speed {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
                print(f'Speeding on {self.speed - self.speed_limit}')
        else:
            super(TownCar, self).show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def power(self, power):
        print(f'Power of car {self.name} - {power}л/c')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed_limit = 40

    def show_speed(self):
        if int(self.speed) > int(self.speed_limit):
            print(f'Speeding on {int(self.speed) - int(self.speed_limit)}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def for_police(self):
        print(f'Police car can use speed > 100 km/h')


w_car = WorkCar(100, 'red', 'bmw', False)
w_car.go()
w_car.turn('left')
w_car.stop()
w_car.show_speed()

s_car = SportCar(300, 'black', 'mazda', False)
s_car.power(200)
print(s_car.is_police)

p_car = PoliceCar(120, 'blue', 'opel', True)
p_car.for_police()
print(p_car.is_police)

t_car = TownCar(40, 'green', 'ford', False)
t_car.go()
t_car.turn('right')
t_car.stop()
t_car.show_speed()
