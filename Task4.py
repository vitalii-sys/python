class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


subaru = SportCar(100, 'Blue', 'Subaru', False)
suzuki = TownCar(30, 'White', 'Suzuki', False)
hyundai = WorkCar(70, 'Gray', 'Hyundai', True)
lada = PoliceCar(110, 'Pink',  'Lada', True)
print(hyundai.turn_left())
print(f'When {suzuki.turn_right()}, then {subaru.stop()}')
print(f'{hyundai.go()} with speed exactly {hyundai.show_speed()}')
print(f'{hyundai.name} is {hyundai.color}')
print(f'Is {subaru.name} a police car? {subaru.is_police}')
print(f'Is {hyundai.name}  a police car? {hyundai.is_police}')
print(subaru.show_speed())
print(suzuki.show_speed())
print(lada.police())
print(lada.show_speed())
