from turtle import Turtle, Screen
from paddle import Paddle
from score import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# Draw the center line
line = Turtle()
line.speed(0)
line.hideturtle()
line.penup()
line.goto(x=0, y=280)
line.setheading(270)
line.color("white")
line.pensize(5)

while line.ycor() > -280:
    line.pendown()
    line.forward(15)
    line.penup()
    line.forward(15)

score = ScoreBoard()
ball = Ball()

# Create players
player_1 = Paddle(1)
player_2 = Paddle(2)

# Set up key bindings
screen.listen()
screen.onkeypress(fun=lambda: player_1.set_is_moving_up(True), key="w")
screen.onkeyrelease(fun=lambda: player_1.set_is_moving_up(False), key="w")
screen.onkeypress(fun=lambda: player_1.set_is_moving_down(True), key="s")
screen.onkeyrelease(fun=lambda: player_1.set_is_moving_down(False), key="s")

screen.onkeypress(fun=lambda: player_2.set_is_moving_up(True), key="Up")
screen.onkeyrelease(fun=lambda: player_2.set_is_moving_up(False), key="Up")
screen.onkeypress(fun=lambda: player_2.set_is_moving_down(True), key="Down")
screen.onkeyrelease(fun=lambda: player_2.set_is_moving_down(False), key="Down")

# Variables to control game state
game_is_on = True
game_over_state = False


# Functions for restarting or quitting the game
def restart_game():
    global game_is_on, game_over_state
    if game_over_state:
        game_over_state = False
        score.reset_score()
        ball.refresh()
        game_is_on = True


def quit_game():
    global game_is_on
    game_is_on = False
    screen.bye()


screen.onkeypress(fun=restart_game, key="r")
screen.onkeypress(fun=quit_game, key="q")

# Main game loop
while game_is_on:
    ball.move()

    if player_1.is_moving_up:
        player_1.move_up()
    if player_1.is_moving_down:
        player_1.move_down()

    if player_2.is_moving_up:
        player_2.move_up()
    if player_2.is_moving_down:
        player_2.move_down()

    # Check collision between ball and each segment of player 1's paddle
    for segment in player_1.paddle_segments:
        if ball.distance(segment) < 20:  # Adjust the distance threshold as needed
            ball.change_direction()
            break  # Exit the loop if a collision is detected

    # Check collision between ball and each segment of player 2's paddle
    for segment in player_2.paddle_segments:
        if ball.distance(segment) < 20:  # Adjust the distance threshold as needed
            ball.change_direction()
            break  # Exit the loop if a collision is detected

    # Calculate score
    if ball.xcor() > 480:
        score.increase_score(player=1)
        ball.refresh()

    if ball.xcor() < -480:
        score.increase_score(player=2)
        ball.refresh()

    # Check if game is over (when a player reaches 10 points)
    if score.p1_score >= 10 or score.p2_score >= 10:
        score.game_over()
        score.display_restart_quit()
        game_is_on = False
        game_over_state = True

    screen.update()
    time.sleep(0.05)  # Small delay for smoother movement

# Keep the screen open to allow restart or quit actions
while True:
    screen.update()
