import random
from turtle import Turtle, Screen

color_list = [
    (215, 85, 48), (190, 187, 71), (73, 160, 220), (220, 122, 167),
    (64, 143, 76), (181, 38, 106), (41, 34, 123), (248, 253, 251),
    (151, 30, 29), (149, 29, 33), (60, 136, 203), (240, 193, 70),
    (252, 243, 249), (240, 246, 252), (189, 75, 52), (64, 117, 170),
    (143, 184, 68), (35, 28, 85), (136, 175, 146), (181, 95, 123),
    (223, 172, 193), (230, 174, 164), (89, 147, 101), (182, 185, 214),
    (75, 143, 176), (170, 205, 179), (99, 20, 27), (158, 203, 220),
    (98, 25, 20), (33, 85, 44), (32, 68, 37)
]

def get_random_color():
    return random.choice(color_list)

def draw_circle(turtle, radius=20):
    color = get_random_color()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Setup turtle and screen
t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed(0)
t.penup()
t.hideturtle()  # Hide the turtle (arrow)
t.setpos(-300, -300)

x = t.xcor()
y = t.ycor()

# Draw grid of circles
for _ in range(10):
    for _ in range(10):
        t.pendown()
        draw_circle(t)
        t.penup()
        t.forward(70)
    y += 70
    t.setpos(x, y)

# Exit on click
screen.exitonclick()