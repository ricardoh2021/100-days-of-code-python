from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()