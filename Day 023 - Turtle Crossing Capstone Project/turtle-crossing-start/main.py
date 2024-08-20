import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True

# Initial maximum time range
max_time_interval = 0.10
time_until_next_car = random.uniform(0, max_time_interval)
time_elapsed = 0

while game_is_on:
    start_time = time.time()

    screen.update()
    car_manager.move_cars()
    car_manager.remove_off_screen_cars()  # Remove cars that are off-screen

    for car in car_manager.cars:
        if player.check_collision(car):
            print("Collision detected!")
            game_is_on = False  # End the game or handle collision
            score.game_over()

    # Check if it's time to create a new car
    if time_elapsed >= time_until_next_car:
        car_manager.create_cars()
        time_until_next_car = random.uniform(0, max_time_interval)
        time_elapsed = 0

    # If the player reaches the end, reset the position and increase the score
    if player.reached_finished_line():
        print("Restart game")
        player.reset_pos()
        score.increase_score()
        car_manager.increment_speed()

        # Decrease the maximum time interval by 25%
        max_time_interval *= 0.75

    # Calculate the time elapsed during this iteration
    end_time = time.time()
    time_elapsed += end_time - start_time

    # Small delay for smoother movement
    time.sleep(0.1)

screen.exitonclick()