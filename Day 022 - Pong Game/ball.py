from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.direction = 1
        self.x_direction = 1
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("white")
        self.speed("fastest")
        y = random.randint(-280, 280)
        self.goto(0, y)
        self.initial()
        print(self.heading())
    def initial(self):
        random_int = random.randint(0,1)
        if random_int == 1:
#             move left
            self.setheading(180)
    def move(self):
        self.forward(10 * self.x_direction)
        self.goto(self.xcor(), self.ycor() + (10 * self.direction))
        if self.ycor() > 280:
            self.change_vertical_direction()
        if self.ycor() < -280:
            self.change_vertical_direction()

    def change_vertical_direction(self):
        self.direction *= -1

    def change_direction(self):
        self.x_direction *= -1
    def refresh(self):
        y = random.randint(-280, 280)
        self.goto(0, y)





