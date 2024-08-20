from turtle import Turtle
from car import Car
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        new_car = Car(self.speed)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def increment_speed(self):
        self.speed += MOVE_INCREMENT
        for car in self.cars:
            car.increment_speed(MOVE_INCREMENT)

    def remove_off_screen_cars(self):
        for car in self.cars[:]:
            if car.head.xcor() < -350:  # Assuming -350 is off-screen on the left side
                for part in car.car_parts:
                    part.clear()
                    part.hideturtle()
                self.cars.remove(car)
