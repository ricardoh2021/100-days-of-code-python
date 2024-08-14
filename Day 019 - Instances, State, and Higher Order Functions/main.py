from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']

y_cord = -100
turtles = []  # Create an empty list to store the turtles

for turtle_color in colors:
    t = Turtle(shape="turtle")
    t.color(turtle_color)
    t.penup()
    t.goto(-240, y_cord)
    y_cord += 50
    turtles.append(t)  # Add each turtle to the list

# Now you can access the turtles individually using the turtles list
# For example, to access the first turtle:
first_turtle = turtles[0]


if user_bet:
    is_race_on = True

while is_race_on:
    ##Race will be on until a turtle gets to position 250
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()