from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reached_finished_line(self):
        #Function that returns a boolean if turtle is at finish line or not
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def check_collision(self, car):
        for part in car.car_parts:
            if self.distance(part) < 15:  # Adjust the threshold value as needed
                return True
        return False
