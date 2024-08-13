from turtle import Turtle, Screen
import random

# Function to generate a random color
def get_random_color():
    r = random.random()  # Random value between 0 and 1 for red
    g = random.random()  # Random value between 0 and 1 for green
    b = random.random()  # Random value between 0 and 1 for blue
    return (r, g, b)


# Function to get a random direction
def get_random_direction():
    return random.choice(directions)


directions = [0, 90, 180, 270]  # Right, Up, Left, Down


tim = Turtle()

tim.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(get_random_color())  # Set turtle color to a random color
        tim.circle(radius=100)
        tim.setheading(tim.heading() + size_of_gap)



draw_spirograph(3)

screen = Screen()