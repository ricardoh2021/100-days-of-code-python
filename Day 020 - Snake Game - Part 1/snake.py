from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_links = []
        self.create_snake()
        self.head = self.snake_links[0]


    def create_snake(self):
        for pos in STARTING_POSITIONS:
            s = Turtle("square")
            s.color("white")
            s.penup()
            s.goto(pos)
            self.snake_links.append(s)
    def move(self):
        for seg_num in range(len(self.snake_links) - 1, 0, -1):
            newX = self.snake_links[seg_num - 1].xcor()
            newY = self.snake_links[seg_num - 1].ycor()
            self.snake_links[seg_num].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)