from car import Car
import random

class Lanes:
    def __init__(self):
        self.cars = []

    def setup(self):
        for _ in range(20):
            self.incoming()
            for _ in range(8):
                self.traffic()

    def traffic(self):
        if self.cars:
            for car in self.cars:
                car.drive()

    def incoming(self):
        num = random.randint(0, 3)
        for _ in range(num):
            new_car = Car(((random.randint(0, 24) * 20) - 230))
            self.cars.append(new_car)