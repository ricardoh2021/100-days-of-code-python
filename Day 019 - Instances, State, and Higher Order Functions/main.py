from turtle import Turtle, Screen
import random

def setup_screen():
    screen = Screen()
    screen.setup(width=500, height=400)
    return screen

def get_user_bet(screen, colors):
    user_bet = None
    while not user_bet or user_bet.lower() not in colors:
        user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color ({', '.join(colors)}): ")
        if user_bet is None:  # Handle cancel/close input dialog
            return None
    return user_bet.lower()

def create_turtles(colors):
    turtles = []
    y_cord = -100
    for turtle_color in colors:
        t = Turtle(shape="turtle")
        t.color(turtle_color)
        t.penup()
        t.goto(-240, y_cord)
        y_cord += 50
        turtles.append(t)
    return turtles

def race_turtles(turtles):
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                return turtle.pencolor()
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

def main():
    colors = ['red', 'orange', 'yellow', 'blue', 'purple', 'green']
    screen = setup_screen()

    while True:
        user_bet = get_user_bet(screen, colors)

        if not user_bet:
            print("No bet was placed. Exiting the game.")
            break

        turtles = create_turtles(colors)
        winning_color = race_turtles(turtles)

        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You've lost! The {winning_color} turtle is the winner!")

        restart = screen.textinput(title="Play Again?", prompt="Do you want to play again? Type 'yes' to restart or 'no' to exit.")
        if not restart or restart.lower() != 'yes':
            print("Thanks for playing! Exiting the game.")
            break

        # Clear the turtles for the next race
        screen.clear()
        for turtle in turtles:
            turtle.reset()


    screen.bye()  # Close the screen window

if __name__ == "__main__":
    main()