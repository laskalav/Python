class Car(object):
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!!")
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!!")
        return self.speed


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    town_car = TownCar(speed=70,
                       color="Green",
                       name="Nissan",
                       is_police= False,
                       direction="Повернула направо"
                       )
    print()
    sport_car = SportCar(speed=240,
                         color="Red",
                         name="lamborghini",
                         is_police=False,
                         direction="Едет прямо"
                         )

    work_car = WorkCar(speed=30,
                       color="Gray",
                       name="Ford",
                       is_police=False,
                       direction="Повернула налево"
                       )
    police_car = PoliceCar(speed=100,
                           color="Blue",
                           name="Hyundai",
                           is_police=True,
                           direction="Развернулась"
                           )
    print(f"{town_car.show_speed()},{town_car.color},{town_car.name},{town_car.is_police}, {town_car.direction}")
    print(f"{sport_car.show_speed()},{sport_car.color},{sport_car.name},{sport_car.is_police}, {sport_car.direction}")
    print(f"{work_car.show_speed()},{work_car.color},{work_car.name},{work_car.is_police}, {work_car.direction}")
    print(f"{police_car.show_speed()},{police_car.color},{police_car.name},{police_car.is_police}, {police_car.direction}")