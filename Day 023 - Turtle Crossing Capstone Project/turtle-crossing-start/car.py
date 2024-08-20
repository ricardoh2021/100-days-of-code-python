from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.car_parts = []
        self.move_distance = speed
        self.create_car()
        self.head = self.car_parts[0]
        self.hideturtle()

    def create_car(self):
        # Create random car color at random position.
        color = random.choice(COLORS)
        # Get a random y coordinate position to start out and then just add to the right
        y_axis = random.randint(-260, 260)
        x_axis = 300
        for _ in range(3):
            pos = (x_axis, y_axis)
            x_axis += 20
            self.add_car_segment(color, position=pos)
        self.setheading(270)

    def add_car_segment(self, color, position):
        c = Turtle("square")
        c.color(color)
        c.penup()
        c.goto(position)
        self.car_parts.append(c)

    def move(self):
        for part in self.car_parts:
            # Change the position of each
            part.goto(part.xcor() - self.move_distance, part.ycor())

    def increment_speed(self, increment):
        self.move_distance += increment
