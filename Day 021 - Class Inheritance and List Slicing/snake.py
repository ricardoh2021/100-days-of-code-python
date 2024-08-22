from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_links = []
        self.create_snake()
        self.head = self.snake_links[0]


    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(position=pos)
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
    def extend(self):
        self.add_segment(self.snake_links[-1].position())

    def add_segment(self, position):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(position)
        self.snake_links.append(s)

    def reset(self):
        for snake in self.snake_links:
            snake.goto(1000, 1000)
        self.snake_links.clear()
        self.create_snake()
        self.head = self.snake_links[0]