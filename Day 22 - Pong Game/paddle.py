from turtle import Turtle

STARTING_POSITIONS = [(480, 0), (480, -20), (480, -40)]
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, playerNumber):
        super().__init__()
        self.playerNumber = playerNumber
        self.paddle_segments = []
        self.create_paddle()
        self.is_moving_up = False
        self.is_moving_down = False

    def create_paddle(self):
        for pos in STARTING_POSITIONS:
            if self.playerNumber == 1:
                self.add_segment(position=(pos[0] * -1, pos[1]))
                self.setheading(180)
            else:
                self.add_segment(position=pos)

    def add_segment(self, position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(position)
        self.paddle_segments.append(s)

    def move_up(self):
        if self.paddle_segments[0].ycor() < 280:
            for index in range(len(self.paddle_segments)):
                segment = self.paddle_segments[index]
                self.paddle_segments[index].goto(segment.xcor(), segment.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.paddle_segments[-1].ycor() > -280:
            for index in range(len(self.paddle_segments)):
                segment = self.paddle_segments[index]
                self.paddle_segments[index].goto(segment.xcor(), segment.ycor() - MOVE_DISTANCE)

    def set_is_moving_up(self, moving):
        self.is_moving_up = moving

    def set_is_moving_down(self, moving):
        self.is_moving_down = moving