from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    #Move each segment
    screen.update()
    time.sleep(0.1)
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        score.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # Detect collision with tail
    for link in snake.snake_links[1:]:
        if snake.head.distance(link) < 10:
            score.reset()
            snake.reset()

    snake.move()


screen.exitonclick()
