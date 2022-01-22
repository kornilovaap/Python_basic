"""
Реализуйте базовый класс Car.

 - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
   А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
 - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
 - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
 - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

"""


class Car:
    speed: int
    color: str
    name: str
    is_police = bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула ", direction)

    def show_speed(self):
        print("Текущая скорость атомобиля: ", self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Для TownCar превышение скорости")
        else:
            print("Для TownCar скорость в пределах нормы")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Для WorkCar превышение скорости")
        else:
            print("Для WorkCar скорость в пределах нормы")


class PoliceCar(Car):
    def __init__(self, color, name, is_police):
        self.is_police = is_police
        super().__init__(color, name, float('inf'), True)


my_car = Car(51, "black", "Ford")
print(my_car.go(), my_car.stop(), my_car.turn("куда-то"), my_car.show_speed())
my_town_car = TownCar(51, "black", "Ford")
my_town_car.show_speed()
my_work_car = WorkCar(51, "black", "Ford")
my_work_car.show_speed()
_______________________________
Машина поехала
Машина остановилась
Машина повернула  куда-то
Текущая скорость атомобиля:  51
None None None None
Для TownCar скорость в пределах нормы
Для WorkCar превышение скорости
                  
